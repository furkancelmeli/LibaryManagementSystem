import os


class admin:
    def __init__(self, username, password):
        self.username = username
        self.password = password


class member:
    def __init__(self, name, email, userId, possessedbooks):
        self.name = name
        self.email = email
        self.userId = userId
        self.possessedbooks = []

    def __str__(self):
        tempName = self.name + " " + str(25 - len(self.name))
        tempMail = self.email + " " + str(30 - len(self.email))
        self.userId + " " + str(5 - len(self.userId))
        return f"Üye Adı...: {tempName} Üye Maili...: {tempMail} Üye Numarası...: {tempMail}"

    def __books__(self):
        for i in range(len(self.possessedbooks)):
            var = self.possessedbooks[i]

    def getBook(self, book):
        self.possessedbooks.append(book)
        book.isoccupled = True
        book.possessed = self

    def returnBook(self, book):
        self.possessedbooks.remove(book)
        book.isoccupled = False
        book.possessed = None


class book:
    def __init__(self, name, author, bookId, isoccupled=False, possessed=None):
        self.name = name
        self.author = author
        self.bookId = bookId
        self.isoccupled = isoccupled
        self.possessed = possessed

    def __str__(self):
        temp = "Mevcut değil" if self.isoccupled else "Mevcut"
        tempName = self.name + " " + str(40 - len(self.name))
        tempAuthor = self.author + " " + str(25 - len(self.author))
        tempBook = self.bookId + " " + str(len(self.bookId))
        return f"Kitap Adı...: {tempName} Yazarı...: {tempAuthor} Kitap Numarası...: {tempBook}"

    # Aramada kullanmak için...
    def __key__(self):
        return f"{self.name} {self.author} {self.bookId}".lower()


testUser1 = admin('furkancelmeli', 'Deneme123')
members = [
    member("Nathaniel Brayden", "nathan.bray@gmail.com", "1", "Python Programming"),
    member("Elon Musk", "elon.musk@outlook.com", "2", "Deep Learning"),
    member("Bill Gates", "bill.gates@outlook.com", "3", "Data Science Essentials"),
    member("Robert Downey Jr.", "jr.downey@gmail.com", "4", "Algorithms and Data Structures"),
    member("Viggo Mortensen", "v.mortensen@gmail.com", "5", "Cybersecurity Basics"),
    member("Orlando Bloo", "orl.bloom@gmail.com", "6", "Web Development")
]
books = [
    book("Python Programming", "Johnny Depp", "1"),
    book("Deep Learning", "Leonardo DiCaprio", "2"),
    book("Data Science Essentials", "Will Smith", "3"),
    book("Algorithms and Data Structures", "Scarlett Johansson", "4"),
    book("Web Development", "Vin Diesel", "5"),
    book("Cybersecurity Basics", "Morgan Freeman", "6")
]


def login():
    username = input("Kullanıcı Adınızı Giriniz:")
    for i in range(3):
        password = input("Şifrenizi Giriniz:")
        if username != testUser1.username:
            print("Kullanıcı bulunamadı...")
            return False
        if password != testUser1.password:
            print("Şifre hatalı!")
            if i == 2:
                print("3 kere hatalı giriş yapıldı. Uygulamadan çıkılıyor.")
                exit(0)
            continue
        print("Giriş başarılı, Hoşgeldiniz.", username)
        return True


def main():
    print("""
    *******************************
    KÜTÜPHANE SİSTEMİNE HOŞGELDİNİZ
    *******************************
    """)
    while (not login()):
        pass

    while (True):
        mainLoop()


def mainLoop():
    print("""
    **********************
    (1)Kitap Listesi
    (2)Kitap Ekle
    (3)Kitap Sil
    (4)Kitap Arama
    (5)Kullanıcı Listesi
    (6)Kitap Ödünç Verme/İade
    (Q)Çıkış
    **********************    
    """)
    option = input()
    if option == "1":
        showBooks()
    elif option == "2":
        addBook()
    elif option == "3":
        removeBook()
    elif option == "4":
        searchBook()
    elif option == "5":
        showUsers()
    elif option == "6":
        bookTransactions()
    elif option.upper() == "Q":
        exit(0)
    else:
        print("Yanlış Giriş Yaptınız...")


def addBook():
    bookname = input("Kitap Adı Giriniz: ")
    authorname = input("Yazar Adı Giriniz:")
    bookid = str(int(books[-1].bookId) + 1)
    books.append(book(bookname, authorname, bookid))
    print("Kitap Başarıyla Eklendi!")


def removeBook():
    bookid = input(("Silmek İstediğiniz Kitabın Numarasını Giriniz: "))
    for i in range(len(books)):
        if (books[i].bookId == bookid):
            books.pop(i)
            print("Kitap Başarıyla Silindi!")
            return


def showBooks():
    for i in range(len(books)):
        print(books[i])


def showUsers():
    for i in range(len(members)):
        print(members[i])


def searchBook():
    tempInput = input("Arama Yapın: ")
    for i in books:
        if (tempInput.lower() in i.__key__()):
            print(i)


def bookTransactions():
    print("""
    *********************
    (1)Kitap Ödünç Ver
    (2)Kitap İade
    (Q)Geri çıkış
    *********************   
    """)
    option = input()
    if (option == "1"):
        bookLending()
    elif (option == "2"):
        bookReturn()
    elif (option.upper() == "Q"):
        os.system('cls')
        return
    else:
        print("Yanlış Giriş Yaptınız...")


def bookReturn():
    tempMember = askUserID()
    tempBookList = askBookID()
    for i in tempBookList:
        if i not in tempMember.possessedbooks:
            print("Bu kitabın Sahibi Bu Değil!")
        else:
            tempMember.returnBook(i)
            print("Kitap Başarıyla İade Edildi...")


def bookLending():
    tempMember = askUserID()
    tempBookList = askBookID()

    for i in tempBookList:
        tempMember.getBook(i)

    print("Kitap Başarıyla Ödünç Verildi.")


def findMember(tempID):
    for i in range(len(members)):
        if (members[i].userId == tempID):
            return members[i]
    return False


def askUserID():
    while True:
        tempMember = findMember(input("Kullanıcının Numarası: "))
        if tempMember != False:
            break
        print("Kullanıcı Bulunamadı")


def askBookID():
    book_ids = input("Kitap numaralarını virgülle ayırarak giriniz: ").split(",")
    tempBookList = []
    for book_id in book_ids:
        for book in books:
            if book.bookId == book_id:
                tempBookList.append(book)
                break
        else:
            print(f"{book_id} numaralı kitap bulunamadı.")
    return tempBookList

main()
mainLoop()
