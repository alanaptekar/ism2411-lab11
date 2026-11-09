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

user_profile = {"name": "Alice", "age": 25}  

email_status = user_profile.get("email", "no email on file")
print(email_status)  # Returns: no email on file

try:
    email_status = user_profile["email"]
except KeyError:
    print("Caught expected KeyError using bracket notation!")

# --- Exercise 3 ---

user_profile = {"name": "Alice", "age": 25, "role": "Admin"}

print("Iterating with .items():")
for key, value in user_profile.items(): 
    print(f"{key}: {value}")

print("Iterating without .items():")
for key in user_profile:
    print(f"{key}: {user_profile[key]}")
