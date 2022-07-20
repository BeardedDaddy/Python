file = open(
    r'C:\Users\grevy\OneDrive\Desktop\Learning Python\BeardedDaddy\UdemyClasses\country_info.py')

    for row in file:
        data = row.split('|')
        print(data)