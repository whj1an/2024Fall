def create_books_2Dlist(file_name):
    books_list = []

    with open(file_name, 'r') as file:
        for line in file:
            d = line.strip().split('\t')
            books_list.append(d)

    return books_list

def search_by_year(books,year1,year2):
    '''(str, int, int) -> list'''
    suit_list = []
    # books = create_books_2Dlist(file_name)
    for char in books:
        year = int(char[3][-4:])
        
        if year <= year2 and year >= year1:
            suit_list.append(char)
    return suit_list





#main
#file_name=input("Enter the name of the file: ")
#file_name=file_name.strip()
#book_list = create_books_2Dlist(file_name)
