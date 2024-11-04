from datetime import datetime

price = 1234.56789
print(f"the price is ${price:.2f}")

now = datetime.now()
print(f"the time is {now:%I:%M %p}")
