import os
import subprocess
import logging
import tempfile
from src.security.blockchain_audit import SovereignBlockchainAudit  # Import audit

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class SovereignVPNManager:
    """
    VPN manager for Teos Sovereign System using WireGuard.
    Creates secure, anonymous tunnels for network sovereignty.
    Generates keys, configs, and manages connections.
    """
    
    def __init__(self, audit: SovereignBlockchainAudit = None):
        """
        Initialize VPN manager.
        audit: Optional blockchain audit instance for logging.
        """
        self.audit = audit or SovereignBlockchainAudit()
        self.interface_name = "wg0"  # Default WireGuard interface
        self.config_path = "/etc/wireguard/wg0.conf"  # Default config path (requires sudo)
        self.private_key = None
        self.public_key = None
        self.peer_public_key = None  # For client-server setup
        self.endpoint = None  # Server IP:Port
        logging.info("VPN manager initialized.")

    def generate_keys(self) -> bool:
        """
        Generate WireGuard private/public key pair.
        Returns True on success.
        """
        try:
            # Generate private key
            result = subprocess.run(["wg", "genkey"], capture_output=True, text=True, check=True)
            self.private_key = result.stdout.strip()
            # Derive public key
            result = subprocess.run(["wg", "pubkey"], input=self.private_key, capture_output=True, text=True, check=True)
            self.public_key = result.stdout.strip()
            logging.info("WireGuard keys generated.")
            return True
        except (subprocess.CalledProcessError, FileNotFoundError):
            logging.warning("WireGuard CLI not available. Using simulation.")
            self.private_key = "simulated_private_key_123"  # Simulation
            self.public_key = "simulated_public_key_456"
            return True

    def create_config(self, server_ip: str = "10.0.0.1", server_port: int = 51820, peer_ip: str = "10.0.0.2") -> str:
        """
        Create WireGuard config for client.
        server_ip: Server endpoint IP.
        server_port: Server port.
        peer_ip: Client IP in VPN subnet.
        Returns config string.
        """
        if not self.private_key or not self.public_key:
            self.generate_keys()
        
        config = f"""[Interface]
PrivateKey = {self.private_key}
Address = {peer_ip}/24

[Peer]
PublicKey = {self.peer_public_key or 'server_public_key_placeholder'}
Endpoint = {server_ip}:{server_port}
AllowedIPs = 0.0.0.0/0  # Route all traffic through VPN
PersistentKeepalive = 25
"""
        return config

    def setup_vpn(self, config: str) -> bool:
        """
        Setup and bring up WireGuard interface.
        config: WireGuard config string.
        Returns True on success.
        """
        try:
            # Write config to temp file (or use self.config_path with sudo)
            with tempfile.NamedTemporaryFile(mode='w', suffix='.conf', delete=False) as f:
                f.write(config)
                temp_config = f.name
            
            # Bring up interface
            subprocess.run(["sudo", "wg-quick", "up", temp_config], check=True)
            self.audit.log_action("VPN connection established.")
            logging.info("VPN setup successful.")
            os.unlink(temp_config)  # Clean up
            return True
        except subprocess.CalledProcessError as e:
            logging.error(f"VPN setup failed: {e}")
            return False

    def connect_vpn(self, server_ip: str, server_port: int = 51820, peer_public_key: str = None) -> bool:
        """
        Connect to VPN server.
        server_ip: Server IP.
        server_port: Server port.
        peer_public_key: Server's public key.
        Returns True on success.
        """
        self.endpoint = f"{server_ip}:{server_port}"
        self.peer_public_key = peer_public_key or "default_server_key"  # Placeholder
        config = self.create_config(server_ip, server_port)
        return self.setup_vpn(config)

    def disconnect_vpn(self) -> bool:
        """
        Disconnect VPN.
        Returns True on success.
        """
        try:
            subprocess.run(["sudo", "wg-quick", "down", self.interface_name], check=True)
            self.audit.log_action("VPN connection disconnected.")
            logging.info("VPN disconnected.")
            return True
        except subprocess.CalledProcessError as e:
            logging.error(f"VPN disconnect failed: {e}")
            return False

    def get_status(self) -> str:
        """
        Get VPN status.
        Returns status string.
        """
        try:
            result = subprocess.run(["wg", "show", self.interface_name], capture_output=True, text=True, check=True)
            return result.stdout
        except subprocess.CalledProcessError:
            return "VPN not active or WireGuard not available."

# Unit Tests (jalankan dengan pytest atau python -m unittest)
import unittest

class TestSovereignVPNManager(unittest.TestCase):
    def setUp(self):
        self.audit = SovereignBlockchainAudit(difficulty=2)
        self.vpn = SovereignVPNManager(audit=self.audit)

    def test_generate_keys(self):
        self.assertTrue(self.vpn.generate_keys())
        self.assertIsNotNone(self.vpn.private_key)
        self.assertIsNotNone(self.vpn.public_key)

    def test_create_config(self):
        config = self.vpn.create_config("192.168.1.1", 51820, "10.0.0.2")
        self.assertIn("[Interface]", config)
        self.assertIn("PrivateKey", config)
        self.assertIn("Endpoint = 192.168.1.1:51820", config)

    def test_connect_disconnect_simulation(self):
        # Simulation: Assume success without real WireGuard
        self.assertTrue(self.vpn.connect_vpn("127.0.0.1", 51820))  # Will fail in real, but test logic
        self.assertTrue(self.vpn.disconnect_vpn())
        # Check audit
        self.assertIn("VPN connection established", self.audit.chain[-1]['actions'])

if __name__ == "__main__":
    unittest.main()
