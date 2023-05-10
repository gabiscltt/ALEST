from Desktop import Desktop
from Notebook import Notebook

desktop = Desktop("Acer", "Cinza", 3000, 500)
print("\n", desktop.getInformacoes())
desktop.cadastrar()

notebook = Notebook("Lenovo", "Preto", 4000, 6)
print("\n", notebook.getInformacoes())
notebook.cadastrar()