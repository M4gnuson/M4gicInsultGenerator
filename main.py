# https://github.com/



# Libraries
from typing import Text
import requests
import tkinter as tk
import pyperclip

# Variables
langs = ['en', 'ru', 'cn', 'de', 'el', 'es', 'fr', 'sw']
count = 0

# Function of displaying text from the service with insults in insulttext
def click():
    global langs, count
    # An insult is written to the url variable with the language we have chosen
    url = requests.get(f'https://evilinsult.com/generate_insult.php?type=plain&lang={langs[count]}')
    ''' Debugging
    if url.ok:
        print('Sucefull')
    else:
        print('Error')
    '''
    url = url.text

    # Text wrapping system
    split = 35
    if len(url) > split:
        for j in range(int(len(url)/25)-1):
            i = url.find(' ', split*(j+1), len(url) - 1)
            url = url[0:i] + '\n' + url[i:len(url)-1]
            insulttext.set(url)
    else:
        # Insult output in insulttext
        insulttext.set(url)

# Language change function
def lang():
    global count, langs
    if(count < 7):  #
        count +=1   # Scrolling system for all available languages
    else:           # 
        count = 0   #
    langtext.set(f'Language: {langs[count]}') # We display which language has been selected

# Copy function generated insult
'''
def copy():
    root.clipboard_clear() # Clearing the clipboard
    root.clipboard_append(labelins['textvariable']) # Copying the generated insult
'''

# Creating a window with tkinter
root = tk.Tk()
root.title("M4gicInsult")
root.wm_iconbitmap('logo.ico')
root.resizable(False, False)
root.geometry("450x250")
root['bg'] = '#F7E6AD'

# Creating a text where the generated insult will be displayed
insulttext = tk.StringVar()
insulttext.set('')
labelins = tk.Label(root, textvariable = insulttext, bg = '#FF4848', font = ('Oswald', 13, 'bold')).pack(fill = tk.BOTH, pady = 20)


# Creating a button when clicking on which an insult will be generated
tk.Button(root, text='Generate', bg = '#2D46B9', fg = 'black', font = ('Oswald', 13, 'bold'), command=click).pack(pady = 2)

# Creating a button when clicking on which the insult will be copied
tk.Button(root, text='Copy Insult', bg = '#FFCCD2', fg = 'black', font = ('Oswald', 13, 'bold')).pack(pady = 2)

# Creating a button when you click on which will change the language of the generated offenses
tk.Button(root, text='Change language', bg = 'black', fg = 'white', font = ('Oswald', 13, 'bold'), command=lang).pack(pady = 2)

# Create text where the current language will be displayed
langtext = tk.StringVar()
langtext.set(f'Language: {langs[count]}')
label = tk.Label(root, textvariable = langtext, font = ('Oswald', 13, 'bold')).pack(fill = tk.BOTH, pady = 20)

# End
root.mainloop()