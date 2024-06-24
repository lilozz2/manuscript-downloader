import PySimpleGUI as sg
import os.path

def get_user_input():
    """
    Gets the input from the user.  The values are returned via a dictionary.  Note that input fields will need to be converted to integers.
    If input validation is desired, then it would be added inside the event loop, prior to the user closing the window.

    :return: Union[dict, None] - Dictionary of input values or None if the user cancelled
    """

    books = [
        "Matthew",
        "Mark",
        "Luke",
        "John",
        "1 Samuel",
        "2 Samuel"
    ]

    book_to_no_of_chps_dict = {
        "Matthew" : 28,
        "Mark": 16,
        "Luke": 24,
        "John": 21,
        "1 Samuel": 31,
        "2 Samuel": 24
    }

    versions = [
        "KJV",
        "NIV"
    ]

    sg.change_look_and_feel('Dark Blue 3')

    t = (15,1)      
    # The size of the text Elements so they all line up
    # The window's layout

    # TODO
    # Add checkboxes for footers and verse numbers
    # Progress bar for file download

    layout = [  [sg.Text('Manuscript downloader', font='Any 16')],
                [sg.Text('Book:', size=t,), sg.Combo(books, key='-BOOK-', enable_events=True, readonly=True)],
                [sg.Text('Version:', size=t,), sg.Combo(versions, key='-VERSION-', enable_events=True, readonly=True)],
                [sg.Text('Where to save:'), sg.In(size=(25,1), enable_events=True ,key='-FOLDER-'), sg.FolderBrowse()],
                [sg.Text('File name:'), sg.Push(), sg.Input(key='-TO SAVE-')],
                [sg.Button('Go'), sg.Button('Cancel')] 
    ]
    
    # Make the window
    window = sg.Window('Manuscript downloader', layout)
    # The event loop
    while True:
        event, values = window.read()
        if event in (None, 'Cancel'):         # if the user exits
            values = None
            break
        if event == 'Go':
            break
    window.close()

    values['-NO OF CHAPTERS-'] = book_to_no_of_chps_dict[values['-BOOK-']]
    return values

if __name__ == '__main__':
    sg.popup('User choices were', get_user_input())
