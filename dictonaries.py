# customer = {
#     "name": "Sow",
#     "age": 20,
#     "is_verified": True
# }
#
# print(customer["name"])
# print(customer.get("name"))

print(input("Phone: "))
phone = {
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four"
}
output = ""
for ch in phone:
    output += phone.get(ch, "!") + " "
print(output)