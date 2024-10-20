calls = 0
def count_calls ():
    global callscalls
    callscalls =+ 1
def string (string):
    count_calls()
    return (len(string), string.upper(), string.lower())
def is_contains (string, list_to_seach):
    count_calls()
print (count_calls())