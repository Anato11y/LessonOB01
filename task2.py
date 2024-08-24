# 1. Создай класс Store:
# -Атрибуты класса:
# name: название магазина.
# address: адрес магазина.
# items: словарь, где ключ - название товара, а значение - его цена. Например, {'apples': 0.5, 'bananas': 0.75}.
# Методы класса:
# __init__ - конструктор, который инициализирует название и адрес, а также пустой словарь дляitems.
# -  метод для добавления товара в ассортимент.
#    метод для удаления товара из ассортимента.
#    метод для получения цены товара по его названию. Если товар отсутствует, возвращайте None.
class Store:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.items = {}

    # метод для добавления товара в ассортимент.
    def add_item(self, item_name, price):
        self.items[item_name] = price

    # метод для удаления товара из ассортимента.
    def remove_item(self, item_name):
        if item_name in self.items:
            del self.items[item_name]

    # метод для получения цены товара по его названию. Если товар отсутствует, возвращайте None.
    def get_price(self, item_name):
        return self.items.get(item_name, None)

    # метод для получения цены товара по его названию. Если товар отсутствует, возвращайте None.
    def update_price(self, item_name, new_price):
        if item_name in self.items:
            self.items[item_name] = new_price

    def __str__(self):
        return f"Магазин: {self.name}, Адрес: {self.address}, Товары: {self.items}"

# Создание объектов класса Store
store1 = Store("Магазин 1", "Улица 1, 123")
store2 = Store("Магазин 2", "Улица 2, 456")
store3 = Store("Магазин 3", "Улица 3, 789")

# Добавление товаров в магазины
store1.add_item("яблоки", 0.5)
store1.add_item("бананы", 0.75)

store2.add_item("хлеб", 1.2)
store2.add_item("молоко", 0.9)

store3.add_item("сыр", 3.5)
store3.add_item("масло", 2.0)

# Тестирование методов на store1
print(store1)

# Обновление цены товара
store1.update_price("яблоки", 0.55)
print(f"Цена на яблоки обновлена: {store1.get_price('яблоки')}")

# Удаление товара
store1.remove_item("бананы")
print(f"После удаления бананов: {store1}")

# Запрос цены на товар
print(f"Цена на хлеб в Магазин 2: {store2.get_price('хлеб')}")
