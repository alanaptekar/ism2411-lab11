customer = {
    "name": "Alex Smith",
    "email": "alex.smith@example.com",
    "tier": "gold",
    "ytd_spend": 1250.50
}

print(customer["name"])
print(customer["email"])
print(customer["tier"])
print(customer["ytd_spend"])

print(customer)

# --- Exercise 1 ---

customer = { "name": "Alex Smith",
    "email": "alex.smith@example.com",
    "tier": "gold",
    "ytd_spend": 1250.50
}

customer["phone"] = "555-0199"
print(customer)

customer["tier"] = "platinum"
print(customer)

del customer["email"]
print(customer)

# --- Exercise 2 ---

