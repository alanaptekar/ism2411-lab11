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

# --- Exercise 4 ---

tier_discounts = {"bronze": 0, "silver": .05, "gold": .10, "platinum": .15}

customer_tier = "gold"
purchase_amount = 200

discount_rate = tier_discounts.get(customer_tier, 0)
discount_amount = purchase_amount * discount_rate
final_price = purchase_amount - discount_amount

print(f"Tier: {customer_tier.capitalize()}")
print(f"Discount: {discount_rate * 100:.0f}%")
print(f"Final Price: ${final_price:.2f}")

# --- Exercise 5 ---

tier_discounts = {
    "Bronze": 0.05,
    "Silver": 0.10,
    "Gold": 0.15
}

dict1 = {"name": "Luc", "tier": "Bronze"}
dict2 = {"name": "Rodrigo", "tier": "Silver"}
dict3 = {"name": "Krish", "tier": "Gold"}

customers = [dict1, dict2, dict3]

purchase_amount = 300

for customer in customers:
    customer_tier = customer["tier"]
    discount_rate = tier_discounts.get(customer_tier, 0)
    discount_amount = purchase_amount * discount_rate
    final_price = purchase_amount - discount_amount

    print(f"Customer: {customer['name']}")
    print(f"Tier: {customer_tier.capitalize()}")
    print(f"Discount: {discount_rate * 100:.0f}%")
    print(f"Final Price: ${final_price:.2f}")
    print()