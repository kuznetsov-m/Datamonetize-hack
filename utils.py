#рецепт с пробемами парсинга
#https://www.russianfood.com/recipes/recipe.php?rid=150140

from parser import getContent

id = 150140
text = getContent(id)
file = open("text.html", "w")
file.write(text)
file.close()