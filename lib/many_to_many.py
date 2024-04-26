class Author:

    all_authors = []
    tr = 0
    def __init__(self, name:str):
        self.name = name
        self.all_authors.append(self)

    def __repr__(self):
        return f"Author(name={self.name})"

    def contracts(self):
        return [ cont for cont in Contract.all_contracts if cont.author == self ]
    
    def books(self):
        return [ b for b in Book.all_books]
    
    def sign_contract(self, book:str, date:str, royalties:int):
        signed_conts = (Contract(author=self, book=book, date=date, royalties=royalties))
        # self.tr += royalties
        return signed_conts

    def total_royalties(self):
        total_conts = [ c for c in Contract.all_contracts if c.author == self]
        royalties = 0
        for c in total_conts:
            royalties += c.royalties
        return royalties
    

class Book:
    all_books = []
    def __init__(self, title:str):
        self.title = title
        self.all_books.append(self)

    def __repr__(self):
        return f"Book(name={self.title})"

    def contracts(self):
        return [ cont for cont in Contract.all_contracts if cont.book == self ]
    
    def authors(self):
        return [ auth for auth in Author.all_authors ]


class Contract:

    all_contracts = []

    def __init__(self, author:str, book:str, date:str, royalties:int):
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        self.all_contracts.append(self)

    def __repr__(self):
        return f"Contract(author={self.author}, book={self.book}, date={self.date}, royalties={self.royalties})"
    
    @classmethod
    def contracts_by_date(cls, date):
        return [ c for c in cls.all_contracts if c.date == date]
    
    @property
    def author(self):
        return self._author
    @author.setter
    def author(self, value):
        if type(value) == Author:
            self._author = value
        else:
            raise TypeError ('Must be of type Author')
        
    @property
    def book(self):
        return self._book
    @book.setter
    def book(self, value):
        if type(value) == Book:
            self._book = value
        else:
            raise TypeError ('Must be of type Book')
        
    @property
    def date(self):
        return self._date
    @date.setter
    def date(self, value):
        if type(value) == str:
            self._date = value
        else:
            raise TypeError ('Must be of type str')
        
    @property
    def royalties(self):
        return self._royalties
    @royalties.setter
    def royalties(self, value):
        if type(value) == int:
            self._royalties = value
        else:
            raise TypeError ('Must be of type int')