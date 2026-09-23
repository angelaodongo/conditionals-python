""" 
    In a file called extensions.py, implement a program that prompts the user for the name of a file and then outputs that file's media type if the file's name ends, case-insensitively, in any of these suffixes:
    .gif
    .jpg
    .jpeg
    .png
    .pdf
    .txt
    .zip
    If the file's name ends with some other suffix or has no suffix at all, output application/octet-stream instead, which is a common default.
"""

def prog_name(p):
    match p:
        case p.endswith(".gif"):
            return "Image/GIF"
        case p.endswith(".jpg"):
            return "Image/GIF"
        case p.endswith(".jpeg"):
            return "Image/GIF"
        case p.endswith(".png"):
            return "Image/GIF"
        case p.endswith(".pdf"):
            return "Document"
        case p.endswith(".txt"):
            return "Text File"
        case p.endswith(".zip"):
            return "ZIP Folder"
        case p.endswith(".gif"):
            return "Image/GIF"
        case _:
            return "application/octet-stream"
            
                
def main():
    program = input("What's the name of your file? ")
    print(prog_name(program))

main()