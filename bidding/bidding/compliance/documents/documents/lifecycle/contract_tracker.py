"""
Track contract phases and notify team when stage changes.
"""

import json

CONTRACTS_FILE = "contracts.json"

def load_contracts():
    try:
        with open(CONTRACTS_FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def save_contracts(contracts):
    with open(CONTRACTS_FILE, "w") as f:
        json.dump(contracts, f, indent=2)

def update_status(contract_id, new_status):
    contracts = load_contracts()
    contracts[contract_id] = new_status
    save_contracts(contracts)
    print(f"Contract {contract_id} updated to {new_status}")

if __name__ == "__main__":
    update_status("LA2025-001", "Awarded")
