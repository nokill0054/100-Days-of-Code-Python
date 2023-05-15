#Life in Weeks#
#1 year 365 days
#1 year 52 week
#1 year 12 months

days=int(365)
weeks=int(52)
months=int(12)

age =int(input("What is your current age? \n"))
age_remaining = int(90) - int(age)      

days = int(age_remaining)*int(days)

weeks = int(age_remaining)*int(weeks)

months = int(age_remaining)*int(months)

print(f"You have {days} days,{weeks} weeks and {months} months left")
