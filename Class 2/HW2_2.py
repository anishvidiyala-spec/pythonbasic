amount = int(input("What was the purchase amount?"))

if amount > 100:
    newamount = 0.9*amount
    print("Final Amount: ", newamount)
    print("You saved ",amount-newamount )
else:
    print("Final Amount: ", amount )
    print("No discount applied")