from gui import get_user_input
from book_generator import getBook

def main():
    user_input = get_user_input()
    to_save = user_input["-FOLDER-"] + "/" + user_input["-TO SAVE-"] + ".pdf"
    print(to_save)
    getBook(user_input["-BOOK-"],
            user_input["-NO OF CHAPTERS-"],
            user_input["-VERSION-"],
            to_save
    )

if __name__ == "__main__":
    main()