"""
Auto-organize documents and tag by contract or bid.
"""

import os
import shutil

def organize_documents(src_folder, dest_folder, contract_id):
    for filename in os.listdir(src_folder):
        if filename.endswith(".pdf") or filename.endswith(".docx"):
            contract_folder = os.path.join(dest_folder, contract_id)
            os.makedirs(contract_folder, exist_ok=True)
            shutil.move(os.path.join(src_folder, filename), os.path.join(contract_folder, filename))
            print(f"Moved {filename} to {contract_folder}")

if __name__ == "__main__":
    organize_documents("incoming_docs", "contracts_archive", "LA2025-001")
