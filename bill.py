bill = int(input("How much they need to pay?: "))
persons = 5
service_fee = ((bill / persons) * 10) / 100

per_person = bill / persons + service_fee
print(per_person)