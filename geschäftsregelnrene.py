import datetime

# Define the current date and time
current_date = input("input current date: ")
# Define the user's subscription end date 
subscription_end_date = input("input expirement date: ")

# Check if the subscription is due to expire soon
if (subscription_end_date - current_date).days <= 10:
    print("Your subscription will expire soon. Renew now!")

elif (subscription_end_date - current_date).days <= 5:
    print(f"Your subscription expires in {(subscription_end_date - current_date).days} days. Renew now and save 10%!")

elif (subscription_end_date - current_date).days == 1:
    print("Your subscription expires within a day! Renew now and save 20%!")

elif (subscription_end_date - current_date).days <= 0:
    print("Your subscription has expired.")

else: 
    print("Nothing to display.")