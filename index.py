from lib.many_to_many import Author, Book, Contract

author1 = Author("Name 1")
book1 = Book("Title 1")
book2 = Book("Title 2")
book3 = Book("Title 3")
author2 = Author("Name 2")
book4 = Book("Title 4")
contract1 = Contract(author1, book1, "02/01/2001", 10)
contract2 = Contract(author1, book2, "01/01/2001", 20)
contract3 = Contract(author1, book3, "03/01/2001", 30)
contract4 = Contract(author2, book4, "01/01/2001", 40)