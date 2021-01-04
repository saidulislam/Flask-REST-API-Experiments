from libs.openexchange import OpenExchangeClient
import time

# your app id from https://openexchangerates.org/
APP_ID = "<2346sdfhg3456sdgf>"

client = OpenExchangeClient(APP_ID)

amount = 1000
start = time.time()
gbp_amount = client.convert(amount, 'USD', 'GBP')
end = time.time()


print(f"USD: {amount}  =  GBP: {gbp_amount}")
print(f"Request completed in {end-start:.2f} sec.")