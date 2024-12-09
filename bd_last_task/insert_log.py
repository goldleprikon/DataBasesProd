#!/usr/bin/python3

import csv
import sqlite3
import sys
import re

# Функция для парсинга данных
def extract_values(data):
    # Использую немного регулярных выражений для обработки
    user_id_ = re.search(r'user_(\d+)', data[0])
    user_id = user_id_.group(1) if user_id_ else -1

    date_ = data[1].strip('[') if len(data) > 1 else None
    time = date_.split(' ')[1] if date_ else None
    date = date_.split(' ')[0] if date_ else None
    date_time = None
    if date and time:
        date_time = date + " " + time

    bet = data[2] if len(data) > 2 else None
    win = data[3] if len(data) > 3 else None
    return user_id, date_time, bet, win

def main(fname):

    data = []
    with open(fname) as fin:
    	for row in csv.reader(fin):
            user_id, time, bet, win = extract_values(row)
            #print(user_id,";", time, ";", bet, ";", win, ";\n")
            user_id = int(user_id)
            if(bet != ""):  bet = float(bet)  
            else: bet = 0.0
            if(win != ""):  win = float(win)  
            else: win = 0.0
            data.append((user_id, time, bet, win))
    data.sort()

    with sqlite3.connect('log_users.s3db') as conn:
        cur = conn.cursor()
        for user_id, time, bet, win in data:
            cur.execute(
               'INSERT INTO LOG (user_id, time, bet, win)'
               ' VALUES (?, ?, ?, ?)',
               (user_id, time, bet, win)
	) 
        conn.commit()

if __name__ == '__main__':
    main(sys.argv[1])
