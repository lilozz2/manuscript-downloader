import subprocess

def generateBookUrl(book, chp, ver):
    currBook = book.replace(" ", "%20") + "%20" + str(chp)
    url = "https://www.biblegateway.com/passage/?search=" \
        + currBook \
        + "&version=" + ver \
        + "&interface=print"
    return url

def getBookPage(urls, toSave):
    command = ["wkhtmltopdf", 
            #    "--cookie", "BGP_pslookup_showfootnotes", "no",
               "--cookie", "BGP_pslookup_showversenums", "no",
               "--user-style-sheet", "custom.css", "--disable-javascript",
            #    "--cookie", "BGP_pslookup_showwoj", "yes",
            #    "--cookie", "BGP_default_version", "NKJV",
            #    "--cookie", "bg_id", "d29367e729f7a7859c53b85222f7ba4e",
            #    "--cookie", "hide-slider", "1",
               ]
    
    # TODO 
    # add cookies for removal of verse numbers and footer references
    # custom css to remove footer navbar
    # Add checks for whether url is accessible, whether input is good and for general sanitization, if modules have been installed e.g. wkhtmltopdf
    # Add suriv

    command = command + urls
    command.append(toSave)
    print(" ".join(command))
    subprocess.run(command)

def getBook(book, no_of_chapters, ver, toSave):
    urls = []
    for chp in range(1, no_of_chapters+1):
        urls.append(generateBookUrl(book, chp, ver))
    getBookPage(urls, toSave)