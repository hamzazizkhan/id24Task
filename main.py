from crawler import login, search
sessionAndcustom_headers = login()
session = sessionAndcustom_headers[0]
custom_headers = sessionAndcustom_headers[1]
searchQuery = 'microsoft'


while True:
    searchQuery = input('\nplease input a company. enter q to quit: ')
    if searchQuery=='q':
        break
    
    print(searchQuery)

    code, data = search(session, custom_headers, searchQuery)
    print('\nstatus code:', code)
    for item in data:
        print(f"{item['item']}: {item['status']}")


