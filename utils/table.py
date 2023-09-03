from config import Table
from models.my_table import MyTable

# Создание объекта для вывода данных в виде таблицы
table = MyTable(
    Table.th,
    hrules=True,
    max_table_width=Table.max_table_width,
    min_width=Table.min_width,
)
