import re

url = 'https://serasaczx.com/exchange?currencyOrigin=real'
default_url = re.compile('(http(s)://)?(www.)serasaczx.com.(br)/exchange?currencyOrigin=real')
match = default_url.match('url')

if not match:
    raise ValueError('The URL is not valid.')

print("The URL is Validated")