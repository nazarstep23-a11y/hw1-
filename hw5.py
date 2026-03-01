import colorama

print(colorama.Fore.BLUE)

help(colorama)

print(type(colorama))

print(colorama.Fore.MAGENTA)

for method in dir(colorama):
    print(method)

print(colorama.Back.BLACK)
print(colorama.Fore.BLUE + "Fore змінює колір тексту")
print(colorama.Fore.BLUE + "Style змінює стиль тексту")
print(colorama.Fore.BLUE + "Back змінює фон тексту")
print(colorama.Back.BLUE)
print(colorama.Fore.BLACK + "help(colorama) інформація про бібліотеку")
print(colorama.Fore.BLACK + "type(colorama) тип бібліотеки")
print(colorama.Fore.BLACK + "dir(colorama) атрибути і методи")
