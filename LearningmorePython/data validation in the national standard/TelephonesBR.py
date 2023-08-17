import re


class TelephonesBR:
    def __init__(self, telephone):
        if self.valida_telephone(telephone):
            self.number = telephone
        else:
            raise ValueError("Wrong number!")

    def __str__(self):
        return self.formart_number()

    def valida_telephone(self, telephone):
        default = "([0-9]{2,3})?([0-9]{2})([0-9]{4,5})([0-9]{4})"
        response = re.findall(default, telephone)
        if response:
            return True
        else:
            return False

    def formart_number(self):
        default = "([0-9]{2,3})?([0-9]{2})([0-9]{4,5})([0-9]{4})"
        response = re.search(default, self.number)
        formatted_number = "+{} ({}) {}-{}".format(
            response.group(1), response.group(2),
            response.group(3), response.group(3),
            response.group(4)
        )
        return formatted_number
