"""
Push contract data to Salesforce using simple-salesforce.
"""

from simple_salesforce import Salesforce

def push_contract_to_salesforce(contract_id, status, sf_username, sf_password, sf_token):
    sf = Salesforce(username=sf_username, password=sf_password, security_token=sf_token)
    sf.Contract.create({
        "ContractNumber": contract_id,
        "Status": status
    })
    print(f"Contract {contract_id} pushed to Salesforce.")

# Usage: push_contract_to_salesforce("LA2025-001", "Awarded", "user", "pass", "token")
