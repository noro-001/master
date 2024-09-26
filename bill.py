bill = eval(input("How much you need to pay?: "))
persons = eval(input("how many people want to split?: "))
fee = eval(input("How much you want to give ass fee in percents?: "))

service_fee = ((bill / persons) * fee) / 100

per_person = bill / persons + service_fee
print(per_person)