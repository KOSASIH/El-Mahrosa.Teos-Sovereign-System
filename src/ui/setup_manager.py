import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext
import os
import logging
from src.security.file_encryption import SovereignFileEncryptor  # Import modul enkripsi
from src.security.blockchain_audit import SovereignBlockchainAudit  # Import modul audit

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class SovereignSetupManager:
    """
    User-friendly GUI for Teos Sovereign System setup and management.
    Integrates encryption, audit, and system controls in a tabbed interface.
    """
    
    def __init__(self, root):
        self.root = root
        self.root.title("Teos Sovereign System Manager")
        self.root.geometry("600x500")
        
        # Initialize modules
        self.encryptor = SovereignFileEncryptor()
        self.audit = SovereignBlockchainAudit()
        
        # Create tabs
        self.tab_control = tk.ttk.Notebook(root)
        self.setup_tab = tk.ttk.Frame(self.tab_control)
        self.file_tab = tk.ttk.Frame(self.tab_control)
        self.audit_tab = tk.ttk.Frame(self.tab_control)
        
        self.tab_control.add(self.setup_tab, text="Setup")
        self.tab_control.add(self.file_tab, text="File Management")
        self.tab_control.add(self.audit_tab, text="Audit Trail")
        self.tab_control.pack(expand=1, fill="both")
        
        self.build_setup_tab()
        self.build_file_tab()
        self.build_audit_tab()
        
        logging.info("GUI initialized.")

    def build_setup_tab(self):
        """Build setup wizard tab."""
        tk.Label(self.setup_tab, text="Welcome to Teos Sovereign System Setup", font=("Arial", 14)).pack(pady=10)
        tk.Label(self.setup_tab, text="Step 1: Choose installation directory").pack()
        self.install_dir = tk.StringVar(value=os.getcwd())
        tk.Entry(self.setup_tab, textvariable=self.install_dir, width=50).pack()
        tk.Button(self.setup_tab, text="Browse", command=self.browse_dir).pack(pady=5)
        
        tk.Label(self.setup_tab, text="Step 2: Set passphrase for encryption (optional)").pack()
        self.passphrase = tk.StringVar()
        tk.Entry(self.setup_tab, textvariable=self.passphrase, show="*", width=30).pack()
        
        tk.Button(self.setup_tab, text="Install & Initialize", command=self.initialize_system).pack(pady=20)
        
        self.status_label = tk.Label(self.setup_tab, text="")
        self.status_label.pack()

    def build_file_tab(self):
        """Build file encryption/decryption tab."""
        tk.Label(self.file_tab, text="File Encryption/Decryption", font=("Arial", 14)).pack(pady=10)
        
        tk.Label(self.file_tab, text="Select file to encrypt:").pack()
        self.file_path = tk.StringVar()
        tk.Entry(self.file_tab, textvariable=self.file_path, width=50).pack()
        tk.Button(self.file_tab, text="Browse File", command=self.browse_file).pack(pady=5)
        
        tk.Button(self.file_tab, text="Encrypt File", command=self.encrypt_file_gui).pack(side=tk.LEFT, padx=10)
        tk.Button(self.file_tab, text="Decrypt File", command=self.decrypt_file_gui).pack(side=tk.LEFT, padx=10)
        
        self.file_status = tk.Label(self.file_tab, text="")
        self.file_status.pack(pady=10)

    def build_audit_tab(self):
        """Build audit trail viewer tab."""
        tk.Label(self.audit_tab, text="Blockchain Audit Trail", font=("Arial", 14)).pack(pady=10)
        tk.Button(self.audit_tab, text="View Chain Summary", command=self.view_audit).pack(pady=5)
        tk.Button(self.audit_tab, text="Verify Chain Integrity", command=self.verify_audit).pack(pady=5)
        
        self.audit_text = scrolledtext.ScrolledText(self.audit_tab, width=70, height=15)
        self.audit_text.pack(pady=10)
        
        self.audit_status = tk.Label(self.audit_tab, text="")
        self.audit_status.pack()

    def browse_dir(self):
        dir_path = filedialog.askdirectory()
        if dir_path:
            self.install_dir.set(dir_path)

    def browse_file(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            self.file_path.set(file_path)

    def initialize_system(self):
        """Initialize system with passphrase and log to audit."""
        passphrase = self.passphrase.get()
        if passphrase:
            self.encryptor = SovereignFileEncryptor(passphrase=passphrase)
        self.audit.log_action("System initialized with GUI setup.")
        self.status_label.config(text="System initialized successfully!", fg="green")
        logging.info("System setup completed via GUI.")

    def encrypt_file_gui(self):
        """Encrypt selected file and log action."""
        input_file = self.file_path.get()
        if not input_file or not os.path.exists(input_file):
            messagebox.showerror("Error", "Please select a valid file.")
            return
        output_file = input_file + ".enc"
        if self.encryptor.encrypt_file(input_file, output_file):
            self.audit.log_action(f"File encrypted: {os.path.basename(input_file)}")
            self.file_status.config(text=f"Encrypted to: {output_file}", fg="green")
        else:
            self.file_status.config(text="Encryption failed.", fg="red")

    def decrypt_file_gui(self):
        """Decrypt selected file."""
        input_file = self.file_path.get()
        if not input_file or not os.path.exists(input_file):
            messagebox.showerror("Error", "Please select a valid encrypted file.")
            return
        output_file = input_file.replace(".enc", "_decrypted")
        passphrase = self.passphrase.get() if self.passphrase.get() else None
        if self.encryptor.decrypt_file(input_file, output_file, passphrase):
            self.audit.log_action(f"File decrypted: {os.path.basename(input_file)}")
            self.file_status.config(text=f"Decrypted to: {output_file}", fg="green")
        else:
            self.file_status.config(text="Decryption failed (wrong passphrase or corrupted file).", fg="red")

    def view_audit(self):
        """Display audit chain summary."""
        summary = self.audit.get_chain_summary()
        self.audit_text.delete(1.0, tk.END)
        self.audit_text.insert(tk.END, summary)

    def verify_audit(self):
        """Verify audit chain and show result."""
        if self.audit.verify_chain():
            self.audit_status.config(text="Audit chain is valid.", fg="green")
        else:
            self.audit_status.config(text="Audit chain is invalid!", fg="red")

if __name__ == "__main__":
    root = tk.Tk()
    app = SovereignSetupManager(root)
    root.mainloop()
