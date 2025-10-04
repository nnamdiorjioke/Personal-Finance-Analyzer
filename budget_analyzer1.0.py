import math
print("Personal Financial Analyzer")

name = input("Hello, welcome to our Personal Financial Analyzer! What is your name? ")
print(f"Hello {name}, let's track your finances and see how financially healthy you are.")
    
def monthly_income(income):
    return round(income/(12),2)

print("Avoid using commas while using the analyzer.")
salary_input = (input("What is your salary? "))
salary = float(salary_input.replace(",", "").strip())
while True:
    answer = input("Do you have any other sources of income? (Yes/No) ").lower()
    if answer == "yes":
        outside_input = (input("How much do you make outside of your salary? "))
        outside_income = float(outside_input.replace(",","").strip())
        denominator = float(salary + outside_income)
        monthly = monthly_income(denominator)
        print(f"Got it. So your yearly income is {denominator:,.2f}. Bringing your monthly income to {monthly}")
        break
    elif answer == "no":
        denominator = float(salary)
        monthly = monthly_income(denominator)
        print(f"Got it. So your yearly income is {denominator}. Bringing your monthly income to {monthly}")
        break
    else:
        print("Invalid Response. Please type yes or no.")

def monthly_expenses():
    h = float(input("How much do you spend on your home a month? (rent or mortgage) "))
    c = float(input("How much do you spend on your car a month? (gas, insurance, auto-loan included) "))
    u = float(input("How much do you spend on utilities a month? "))
    f = float(input("How much do you spend on food a month? (groceries & dining out?) "))
    d = float(input("How much does your debt cost you a month? (loans, credit, etc.) "))
    per_month = float(round(h + c + u + f + d))
    print(f"This brings your monthly necessities cost to {per_month}.")
    return float(round(per_month, 2))

def efficient_spending(earnings, spending):
    percent = float(round((spending / earnings)*100,2))
    if percent >= 70:
        print(f"That's {percent}% of your monthly income. This is too high and certain spending must be rearranged. ")
    elif percent >= 60:
        print(f"That's {percent}% of your monthly income. That's a fairly high amount.")
    elif percent >= 50:
        print(f"That's {percent}% of your monthly income. Just above the 50% threshold, but doable. {name}.")
    elif percent <= 50:
        print(f"That's {percent}% of your monthly income. Great job {name}! Below the 50% threshold. ")
    return percent

def monthly_wants():
    e = float(input("How much do you spend on entertainment a month? (subscriptions, games, movies, clubs, bars) "))
    cl = float(input("How much do you spend on clothes a month? "))
    wants_per_month = float(round(e + cl))
    print(f"This brings your monthly wants costs to {wants_per_month}.")
    return float(round(wants_per_month, 2))

def efficient_want_spending(earnings, spending):
    percent = float(round((spending / earnings)*100,2))
    if percent >= 30:
        print(f"That's spending {percent}% of your monthly income. That's a fairly high amount {name}.")
    elif percent <= 30:
        print(f"That's spending {percent}% of your monthly income. Great job {name}! Below the 30% threshold. Not too bad! ")
    return percent

def efficient_saving(earnings, saving):
    percent = float(round((saving / earnings)*100,2))
    if percent >= 20:
        print(f"Your saving {percent}% of your monthly income. Over the 20% standard. Great job {name}! ")
    elif percent <= 20:
        print(f"Your saving {percent}% of your monthly income. You need to save more. ")
    return percent

monthlyspending = monthly_expenses()
percentagespending = efficient_spending(monthly, monthlyspending)

monthlywantspending = monthly_wants()
percentagewantspending = efficient_want_spending(monthly, monthlywantspending)

savings = float(input("How much do you put into your savings a month? "))
percentagesaving = efficient_saving(monthly, savings)

if percentagespending <= 50 and percentagewantspending <= 30 and percentagesaving >= 20:
    print(f"Great job {name}, you are practicing the 50/30/20 rule to perfection. Keep doing what you're doing, you may even have extra money to spend.")
elif percentagespending >= 50 and percentagewantspending <= 30 and percentagesaving <= 20:
    print(f"Nice work {name}, you are pretty close to perfecting the 50/30/20, a little adjustment to spending and saving could bring you into perfect alignment.")
elif percentagespending >= 50 and percentagewantspending >= 30 and percentagesaving <= 20:
    print(f"We need to be careful {name}, over 80% of your income is being spent, while less than 20% is being saved. Try to cut back on non-essentials and prioritize building your savings.")
elif percentagespending <= 50 and percentagewantspending >= 30 and percentagesaving >= 20:
    print(f"{name}, You are doing a great job saving your money, but maybe consider we should consider cutting down on our non-essentials.")

