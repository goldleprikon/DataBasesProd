# LAST_TASK
## Как это использовать
1) Сначала Схема 
==last_schema.sql==
2) далее создал базу данных log_users.s3db
3) далее перевожу файл ==users1.csv==  в нормальный формат, это в файл
==clear_users1.csv==
4) Далее ввожу данные в таблицы ==через insert_log.py== и ==insert_users.py==
`python3 insert_log.py log1.csv`
`python3 insert_users.py clear_users1.csv`
5) Далее провожу очистку базы от некорректных данных 
-- 0) запрос в ==last_questions.txt==

Сейчас в ==log_users.s3db== лежит уже очищенная база
Остальные вопросы-запросы в ==last_questions.txt==