#рецепт с пробемами парсинга
#https://www.russianfood.com/recipes/recipe.php?rid=150140

from parser import getContent
import requests

# id = 150140
# text = getContent(id)
# file = open("text.html", "w")
# file.write(text)
# file.close()


def get_text(url):
    print('getContent(): send request to %s' % url)
    
    r = requests.get(url, timeout=30)

    content = ''
    if r.reason == 'OK':
        print('getContent(): status OK')
        
        content = r.text
    
    return content


url = 'https://www.perekrestok.ru/catalog/ryba-i-moreprodukty'
text = get_text(url)
file = open("text.html", "w")
file.write(text)
file.close()