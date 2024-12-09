import csv
import codecs

# Задаю файлы и кодировку
file_path = 'users1.csv'
output_file_path = 'clear_users1.csv'
encoding = 'koi8_r'

# Массивчик для переноса данных
arr = []

# Открываю файл с указанием кодировки
with codecs.open(file_path, 'r', encoding) as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        arr.append(row)

# Переношу данные в адекватном виде в другой csv
with open(output_file_path, mode='w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=['info'])
    for row in arr:
        row_dict = {field: value for field, value in zip(writer.fieldnames, row)}
        writer.writerow(row_dict)

# По факту создаю промежуточку csv-шник, чтобы потом его распарсить
