import json
collection = []
def addBook():
    print("Adding a book...")
    book = {}
    title = input("Enter the title of the book: ")
    author = input("Enter the author name of the book: ")
    year = input("Enter the publication year of the book: ")
    genre = input("Enter the Genre of the book: ")

    #adding the book details
    book["title"] = title
    book["author"] = author
    book["year"] = year
    book["genre"] = genre

    if book not in collection:
        collection.append(book)
        print("Book successfully added to the collection.")
        print()
    else: 
        print("Book already exists. Please add another one...")
        print()
        addBook()
    print("----------------------------------------------------")


def viewCollection():
    if collection:
        print("[")
        for i in collection: 
            print(f"{i},")
        print("]")
        # print(collection)
        print()
    else: 
        print("Collection is empty.")
        print()
    print("----------------------------------------------------")


def savetoJSON():
    with open("collection.json","w+") as a:
        json.dump(collection,a,indent=4) 
    print("Successfully saved the collection in JSON format")
    print()
    print("----------------------------------------------------")

def loadfromJSON():
    with open("Sample.json","r") as a:
        data = json.load(a)
    print(data)
    print()
    print("----------------------------------------------------")

def searchBook():
    keyword = input("Enter a keyword to search like title/author: ")
    result = []
    for i in collection:
        if keyword.lower() in i['title'].lower() or keyword.lower() in i['author'].lower():
            result.append(i)
    if len(result) == 1:
        print(f"{len(result)} book found")
        print(result)
        print()
        print("----------------------------------------------------")
    else: 
        print(f"{len(result)} books found")
        print(result)
        print()
        print("----------------------------------------------------")

def removeBook():
    title = input("Enter the title to remove: ")
    for i in collection: 
        if i['title'].lower() == title.lower():
            collection.remove(i)
    print("Successfully removed the book from collection.")
    print()
    print("----------------------------------------------------")


def sortCollection():
    sort_by = input("Sort by title/author/year/genre: ")
    if sort_by == 'title':
        collection.sort(key=lambda x:x['title'].lower())
    elif sort_by == 'author':
        collection.sort(key=lambda x:x['author'].lower())
    elif sort_by == 'year':
        collection.sort(key=lambda x:x['year'].lower())
    elif sort_by == 'genre':
        collection.sort(key=lambda x:x['genre'].lower())
    
    print(f"collection is sorted by {sort_by}")
    viewCollection()
    print("----------------------------------------------------")


def main():
    print()
    print("Welcome to the Book Collection Manager: ")
    print()

    while True:
        print("----------------------------------------------------")
        print("Available operations: ")
        print("1. Add a book to the collection")
        print("2. View the collection")
        print("3. Save the collection in JSON format")
        print("4. Load the collection from JSON file")
        print("5. Search a book in the collection")
        print("6. Remove a book from the collection")
        print("7. Sort the collection")
        print("8. Exit the Book Collection Manager")
        print()
        print("----------------------------------------------------")
        print()
        choice = int(input("Please choose a serial number from the above: "))

        if choice == 1:
            addBook()
        elif choice == 2:
            viewCollection()
        elif choice == 3:
            savetoJSON()
        elif choice == 4:
            loadfromJSON()
        elif choice == 5:
            searchBook()
        elif choice == 6:
            removeBook()
        elif choice == 7:
            sortCollection()
        elif choice == 8:
            print("Thank you foor using Book Collection Manager. Bye!!!")
            break
        else: 
            print("Enter correct number from above.")

main()