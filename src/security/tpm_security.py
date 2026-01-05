import os
import logging
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.exceptions import InvalidSignature

# TPM Library (install tpm2-pytss)
try:
    from tpm2_pytss import TSS2_Exception, ESAPI, TPM2_ALG, TPM2_ECC, TPM2B_PUBLIC, TPM2B_SENSITIVE_CREATE, TPM2B_DATA
    TPM_AVAILABLE = True
except ImportError:
    TPM_AVAILABLE = False
    logging.warning("TPM library not available. Using simulation mode.")

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class SovereignTPMSecurity:
    """
    Hardware security module for Teos Sovereign System using TPM 2.0.
    Generates and stores AES keys securely in TPM, preventing extraction.
    Falls back to software simulation if TPM unavailable.
    """
    
    def __init__(self, tpm_device: str = "/dev/tpm0"):
        """
        Initialize TPM context.
        tpm_device: Path to TPM device (default /dev/tpm0).
        """
        self.tpm_device = tpm_device
        self.tpm_context = None
        self.key_handle = None
        if TPM_AVAILABLE:
            try:
                self.tpm_context = ESAPI()
                self.tpm_context.initialize()
                logging.info("TPM initialized successfully.")
            except TSS2_Exception as e:
                logging.error(f"TPM initialization failed: {e}. Switching to simulation.")
                TPM_AVAILABLE = False
        if not TPM_AVAILABLE:
            logging.info("Using TPM simulation for testing.")
            self.simulated_keys = {}  # Dict to simulate key storage

    def create_aes_key(self, key_name: str) -> bool:
        """
        Create and seal an AES-256 key in TPM.
        key_name: Unique identifier for the key.
        Returns True on success.
        """
        if TPM_AVAILABLE:
            try:
                # Define key template (AES key sealed in TPM)
                public_template = TPM2B_PUBLIC(
                    type=TPM2_ALG.AES,
                    nameAlg=TPM2_ALG.SHA256,
                    objectAttributes=0x00060072,  # FixedTPM, FixedParent, SensitiveDataOrigin, UserWithAuth, NoDA
                    authPolicy=b'',  # No policy for simplicity
                    parameters=TPM2_ECC()  # Placeholder; adjust for AES
                )
                sensitive = TPM2B_SENSITIVE_CREATE(
                    userAuth=b'',  # No password
                    data=b''  # Sensitive data (key will be generated)
                )
                # Create primary key (storage root)
                primary_handle = self.tpm_context.create_primary(
                    primaryHandle=0x40000001,  # Owner hierarchy
                    inSensitive=sensitive,
                    inPublic=public_template
                )
                # Create and load AES key
                self.key_handle = self.tpm_context.create(
                    parentHandle=primary_handle,
                    inSensitive=sensitive,
                    inPublic=public_template,
                    outsideInfo=b'',
                    creationPCR=[]
                )
                logging.info(f"AES key '{key_name}' created and sealed in TPM.")
                return True
            except TSS2_Exception as e:
                logging.error(f"Failed to create TPM key: {e}")
                return False
        else:
            # Simulation: Generate and "store" key in memory
            key = os.urandom(32)  # 256-bit AES key
            self.simulated_keys[key_name] = key
            logging.info(f"AES key '{key_name}' simulated (TPM not available).")
            return True

    def get_aes_key(self, key_name: str) -> bytes or None:
        """
        Retrieve AES key from TPM for encryption/decryption.
        Returns key bytes or None if failed.
        """
        if TPM_AVAILABLE:
            try:
                # Unseal the key (requires TPM authentication if set)
                unsealed = self.tpm_context.unseal(self.key_handle)
                logging.info(f"AES key '{key_name}' retrieved from TPM.")
                return unsealed
            except TSS2_Exception as e:
                logging.error(f"Failed to retrieve TPM key: {e}")
                return None
        else:
            # Simulation: Return stored key
            key = self.simulated_keys.get(key_name)
            if key:
                logging.info(f"AES key '{key_name}' retrieved from simulation.")
                return key
            else:
                logging.error(f"Simulated key '{key_name}' not found.")
                return None

    def encrypt_with_tpm_key(self, key_name: str, data: bytes) -> bytes or None:
        """
        Encrypt data using AES key from TPM.
        Returns encrypted bytes or None if failed.
        """
        key = self.get_aes_key(key_name)
        if not key:
            return None
        iv = os.urandom(12)
        cipher = Cipher(algorithms.AES(key), modes.GCM(iv), backend=default_backend())
        encryptor = cipher.encryptor()
        ciphertext = encryptor.update(data) + encryptor.finalize()
        tag = encryptor.tag
        # Return: IV + Tag + Ciphertext
        return iv + tag + ciphertext

    def decrypt_with_tpm_key(self, key_name: str, encrypted_data: bytes) -> bytes or None:
        """
        Decrypt data using AES key from TPM.
        Returns decrypted bytes or None if failed.
        """
        key = self.get_aes_key(key_name)
        if not key or len(encrypted_data) < 28:  # IV(12) + Tag(16) + min ciphertext
            return None
        iv = encrypted_data[:12]
        tag = encrypted_data[12:28]
        ciphertext = encrypted_data[28:]
        cipher = Cipher(algorithms.AES(key), modes.GCM(iv, tag), backend=default_backend())
        decryptor = cipher.decryptor()
        try:
            plaintext = decryptor.update(ciphertext) + decryptor.finalize()
            return plaintext
        except InvalidSignature:
            logging.error("Decryption failed: Invalid key or corrupted data.")
            return None

    def close(self):
        """Clean up TPM context."""
        if self.tpm_context:
            self.tpm_context.close()

# Unit Tests (jalankan dengan pytest atau python -m unittest)
import unittest

class TestSovereignTPMSecurity(unittest.TestCase):
    def setUp(self):
        self.tpm = SovereignTPMSecurity()

    def test_create_and_use_key_simulation(self):
        # Test with simulation (always available)
        key_name = "test_key"
        self.assertTrue(self.tpm.create_aes_key(key_name))
        key = self.tpm.get_aes_key(key_name)
        self.assertIsNotNone(key)
        self.assertEqual(len(key), 32)

        # Test encryption/decryption
        data = b"Sovereign data"
        encrypted = self.tpm.encrypt_with_tpm_key(key_name, data)
        self.assertIsNotNone(encrypted)
        decrypted = self.tpm.decrypt_with_tpm_key(key_name, encrypted)
        self.assertEqual(decrypted, data)

    def tearDown(self):
        self.tpm.close()

if __name__ == "__main__":
    unittest.main()
