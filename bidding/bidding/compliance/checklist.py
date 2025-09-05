"""
Compliance checklist tracker for contract requirements.
"""

CHECKLIST = [
    "Registered in county/vendor portal",
    "Submitted W-9",
    "Reviewed insurance requirements",
    "Uploaded bid bond",
    "Certified compliance with local ordinances",
    "Reviewed contract terms"
]

def check_progress(completed_items):
    return [item for item in CHECKLIST if item not in completed_items]

if __name__ == "__main__":
    completed = ["Registered in county/vendor portal", "Submitted W-9"]
    print("Pending items:", check_progress(completed))
