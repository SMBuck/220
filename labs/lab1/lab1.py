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
    average_daily_balance = step3 / billing_cycle
    monthly_conversion = annual_interest / 12
    percent_decimal = monthly_conversion / 100
    monthly_interest_charge = average_daily_balance * percent_decimal
    print("This is the monthly interest charge: $", monthly_interest_charge)
