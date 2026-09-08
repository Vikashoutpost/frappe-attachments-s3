import subprocess
import sys
import frappe

def execute():
    """Ensure cryptography and pyOpenSSL are aligned with compatible versions."""
    print("\n[frappe_s3_attachment] Running migration patch: downgrade_cryptography...")
    cmd = [
        sys.executable, "-m", "pip", "install",
        "cryptography~=46.0.3",
        "pyOpenSSL~=26.0.0"
    ]
    try:
        res = subprocess.run(cmd, capture_output=True, text=True, check=True)
        print("[frappe_s3_attachment] Successfully installed cryptography~=46.0.3 and pyOpenSSL~=26.0.0!")
        print(res.stdout)
    except subprocess.CalledProcessError as e:
        print("[frappe_s3_attachment] Failed to install packages:", e.stderr)
        frappe.log_error(title="Failed to fix cryptography", message=e.stderr)
