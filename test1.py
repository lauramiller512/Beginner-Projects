print("How many kilometers did you run today?")
kms = input()
miles = float(kms)/1.6093
miles = round(miles,1)
print(f"Woah, your {kms}km ride was {miles} miles.") #f turns the number into a string