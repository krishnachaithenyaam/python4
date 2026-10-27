consultation = float(input("Consultation charges: "))
diagnostic = float(input("Diagnostic charges: "))
treatment = float(input("Treatment charges: "))
age = int(input("Patient age: "))
payment = float(input("Amount paid: "))

total = consultation + diagnostic + treatment

if age >= 60:
    concession = total * 0.10
else:
    concession = 0

final_bill = total - concession

print("\n--- Hospital Bill ---")
print("Total charges:", round(total, 2))
print("Concession:", round(concession, 2))
print("Final bill:", round(final_bill, 2))

if payment < 0:
    print("Invalid payment")
elif payment >= final_bill:
    print("Patient classification: Fully Paid")
    print("Change:", round(payment - final_bill, 2))
else:
    print("Patient classification: Payment Pending")
    print("Balance:", round(final_bill - payment, 2))