# url = "https://serasaczx.com/exchange?currencyOrigin=real"
# print(len(url))
# print(url)
url = " "

# sanitization url
url = url.strip()

# url validation
if url == "":
    raise ValueError("The url is empty")

# separates base and parameter
question_mark_index = url.find('?')
url_base = url[:question_mark_index]
url_parameters = url[question_mark_index+1:]
print(url_parameters)

# fetch the value of a parameter
search_parameter = 'amount'
index_parameter = url_parameters.find(search_parameter)
index_value = index_parameter + len(search_parameter) + 1
index_and_ampersand = url_parameters.find('&', index_value)
if index_and_ampersand == -1:
    value = url_parameters[index_value:]
else:
    value = url_parameters[index_value:index_and_ampersand]

print(value)
