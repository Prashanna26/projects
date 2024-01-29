import os

def delete_file(dict, exce1):
    for file_name in  os.listdir(dict):
        if file_name!=exce1:
            file_path = os.path.join(dict,file_name)
            try:
                if os.path.isfile(file_path):
                    os.remove(file_path)

            except FileNotFoundError:
                print("File not found")

            except PermissionError:
                print("Permission not granted")   

dicto = "/Users/macbook/Documents/Python/books"
exce_1 = "books.py"

delete_file(dicto, exce_1)

books = [{'name': 'The Magic Tree'},
        {'name': 'Winter Fairy'},
        {'name': 'Silas Dai Hero'}
]

with open('index.html','w') as file:
    
    a = ''
    for bk in books:
        a+=f'<a href="{bk.get("name")}.html"><li>{bk.get("name")}</li></a>'
        
    content = f'''
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Document</title>
        </head>
        <body>
            <ol>
                {a}
            </ol>
            <button class="editButton">Edit</button>
        </body>
        </html>'''
    file.write(content)


for book in books:
    with open(f'{book['name']}.html','w') as file:
        v= f'''<!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>Document</title>
            </head>
            <body>
                <h1> {book["name"]} </h1>

                <pre>
                    Author: Mary Pope Osborne
                    Publisher ‏ : ‎ Random House Books for Young Readers; First Edition (September 28, 2004)
                    Language ‏ : ‎ English
                    Hardcover ‏ : ‎ 128 pages
                    ISBN-10 ‏ : ‎ 0375827366
                    ISBN-13 ‏ : ‎ 978-0375827365
                    Reading age ‏ : ‎ 6 - 9 years, from customers
                    Lexile measure ‏ : ‎ 530L
                    Grade level ‏ : ‎ 2 - 5
                    Item Weight ‏ : ‎ 9.6 ounces
                    Dimensions ‏ : ‎ 6.14 x 0.65 x 8.58 inches  
                </pre>
            </body>
            </html>'''
        file.write(v)


