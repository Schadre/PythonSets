customer_ids = ["C001", "C002", "C003", "C002", "C001", "C004"]

def no_duplicates(customer_ids):
    update = set()
    print("\nHere is a list of updated customer ids:")
    for ids in customer_ids:
        if ids not in update:
            update.add(ids)
            print(f"- {ids}")
no_duplicates(customer_ids)