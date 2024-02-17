class Library:
    def __init__(self):
        self.books = []
        self.file = open('books.txt', mode='+a')
        self.file.seek(0)
        self.books = [line.strip() for line in self.file.readlines()]

        
    def add_book(self):
        book_name = input("Please enter the book name: ")
        author_name=input("Please enter the author name: ")
        release_year=input("Please enter the first release year:")
        num_pages=input("Please enter the number of pages:")
        book_info=f"{book_name},{author_name},{release_year},{num_pages}"
        self.books.append(book_info)
        self.file.write(book_info + '\n')
        print(f" '{book_name}' added to the library")

    
    def list_books(self):
        self.file.seek(0)
        book_lines = self.file.readlines()
        if not book_lines:
            print("There are no books currently.")
        else:
            print("Current books:")
            for line in book_lines:
                book_info = line.strip().split(", ")
                if len(book_info) >= 2:
                    book_name = book_info[0]
                    author_name = book_info[1]
                    print(f"Book Name: {book_name}, Author Name: {author_name}")
                else:
                    print(f"Invalid book data: {line}")


    def remove_book(self):
        remove_book_name=input("Please enter the name of the book to remove:")
        self.file.seek(0)
        book_lines=self.file.readlines()
        self.books=[line.strip() for line in book_lines]

        index_to_remove=None
        for index, book in enumerate(self.books):
            if remove_book_name in book:
                index_to_remove=index
                break


        if index_to_remove is None:
            print(f"Book '{remove_book_name}' not found in the library.")
        else:
            self.books.remove(remove_book_name)
            self.file.seek(0)
            self.file.truncate()
            for book in self.books:
                self.file.write(book+'\n')
            print(f"Book '{remove_book_name}' removed from the library.")

    def close_file(self):
        self.file.close()

        
def menu():
    print("***MENU***")
    print("1-) List Books")
    print("2-) Add Book")
    print("3-) Remove Book")
    print("4-) Quit")



def main():
   lib=Library()
   while True:
      menu()
      choice=input("Please enter your choice: ")

      if choice=="1":
          lib.list_books()
      elif choice=="2":
          lib.add_book()
      elif choice=="3":
          lib.remove_book()
      elif choice=="4":
          print("Exiting the program.")
          lib.close_file()
          break
      else:
          print("Invalid choice. Please try again.")
          

if __name__ == "__main__":
    main()


