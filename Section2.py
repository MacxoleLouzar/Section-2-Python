import re


def phone_number():
    x = input("Enter your phone number: ")  # input characters
    clean_number = re.sub('[^0-9]+', '', x)  # Accept number from 0 to 9
    x = re.sub("(\d)(?=(\d{3})+(?!\d))", r"\1-", "%d" %
               int(clean_number[:-1])) + clean_number[-1]  # remove non-numeric character
    x = x.removeprefix("+")
    x = x.removeprefix("27")     # remove leading +27
    x = re.sub("[ ()-]", '', x)  # remove space, (),-
    x[0] == "0"  # Initial Char 0
    assert (len(x) == 11)  # Accept 10 characters

    print('()-()-()'.format(x[:3], x[3:6], x[6:]))


phone_number()
