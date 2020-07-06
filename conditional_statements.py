is_hot = True
if is_hot:
    print("Drink water")
else:
    print("Cold")

no_pending_loan = False
enough_credit_score = True

if no_pending_loan and enough_credit_score:
    print("Eligible for 100 EGP loan")
elif (not no_pending_loan) and enough_credit_score:
    print("Eligible for 50 EGP loan")
else:
    print("Not eligible")