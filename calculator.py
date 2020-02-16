def conversion():
  '''
  This function takes in either GYD or USD and outputs the equivalent in the other currency according to RB VTM card conversion.
  '''

  toBeConverted = input("What would you like to convert? ").lower()
  amount = float(toBeConverted[:-3]) # gets all but the last 3 characters
  currency = str(toBeConverted[-3:]) # gets the last 3 characters
  converted = None
  
  # gyd to usd
  if currency == "gyd":
    converted = round((amount / 217 ) * 0.99, 2)
    print(f"\n{toBeConverted} = {str(converted)}usd\n")
    conversion()

  # usd to gyd
  elif currency == "usd":
    converted = round(amount * 1.01 * 217, 2)
    print(f"\n{toBeConverted} = {str(converted)}gyd\n")
    conversion()
  
  else:
    print("Your input was incorrect. Try again.\n")
    conversion()

conversion()