def monthly_interest():
    print("Monthly Interest Calculator")
    annual_interest = eval(input("Enter the annual interest rate: "))
    billing_cycle = eval(input("Enter number of days during billing cycle: "))
    net_balance = eval(input("Enter net balance: "))
    payment_amount = eval(input("Enter payment amount: "))
    payment_made = eval(input("Enter when payment was made: "))
    step1 = net_balance * billing_cycle
    step2 = payment_amount * payment_made
    step3 = step1 - step2
    step4 = step3 / billing_cycle
    step5 = annual_interest / 12
    step6 = step5 / 100
    step7 = step4 * step6
    print("This is the monthly interest charge: $", step7)
