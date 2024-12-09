#!/usr/bin/python3

import csv
import sqlite3
import sys
import re

# Функция для извлечения user_id, email и geo из строки
def parse_data(data):
    # Опять немного магии с регулярными выражениями
    match = re.match(r'User_(\d+)(.*?)@(\S+?)\.(\S+)\s+(.*)', data)
    if match:
        user_id = match.group(1)
        email = match.group(2) + '@' + match.group(3) + '.' + match.group(4)
        geo = match.group(5).strip()
        return user_id, email, geo
    return None, None, None


def main(fname):

    data = []
    with open(fname) as fin:
        for row in csv.reader(fin):
            dat = row[0]
            user_id, email, geo = parse_data(dat)
            #print(user_id, email, geo, "\n")
            if (user_id == None): user_id = -1
            else: user_id = int(user_id)
            data.append((user_id, email, geo))
    data.sort()

    with sqlite3.connect('log_users.s3db') as conn:
        cur = conn.cursor()
        for user_id, email, geo in data:
            cur.execute(
               'INSERT INTO USERS (user_id, email, geo)'
               ' VALUES (?, ?, ?)',
               (user_id, email, geo)
	)
        conn.commit()

if __name__ == '__main__':
    main(sys.argv[1])
