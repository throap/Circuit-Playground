def greet(lang):
  if lang == 'es':
    return'Hola,'
  elif lang == 'fr':
    return'Bonjour,'
  elif lang == 'vn':
    return'Xin Chao,'
  elif lang == 'jp':
    return'Konnichiwa,'
  elif lang == 'ko':
    return'Annyeonghaseyo,'
  elif lang == 'hn':
    return'Namaste,'
  else:
    return'Hello,'

def main():
    name = str(input('Hello, what is your name: '))
    language = str(input('What language do you speak: '))
    print(greet(language), name.capitalize())
    
main()
