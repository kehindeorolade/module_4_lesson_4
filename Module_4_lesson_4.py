import sqlite3

con = sqlite3.connect('celebs.db')


cur = con.cursor()

# Create table
# cur.execute('''CREATE TABLE celebrity
#             (name text, genre text, num_album integer, age integer, awards integer, years_in_industry integer)''')


#Save commit the changes
con.commit()

print("successful")

celebrity_data = [
    ('Adekunle Gold', 'afro', 20, 32, 25, 15),
    ('Burnaboy', 'hiphop', 25, 31, 50, 23),
    ('Patoranking', 'reggae', 20, 32, 20, 18),
    ('Adewale Ayuba', 'fuji', 9, 51, 18, 40),
    ('Banky W', 'R&B', 27, 41, 30, 20),
    ('Blaqbonez', 'hiphop', 5, 26, 11, 10),
    ('Harrysong', 'afro-pop', 15, 42, 21, 14),
    ('Niniola', 'afro-house', 19, 35, 13, 8),
    ('Saheed Osupa', 'Fuji', 25, 52, 40, 31),
    ('Simi', 'afro-pop',34, 13, 20, 16),
    ('Shina Peters', 'juju', 30, 64, 44, 40),
    ('Ycee', 'hiphop', 5, 29, 12, 10),
    ('Zlatan', 'afrobeat', 15, 27, 21, 8),
    ('Yemi Alade', 'R&B', 22, 33, 50, 17),
    ('Davido', 'pop', 34, 29, 60, 13),
    ('Duncan mighty', 'reggae', 19, 38, 28, 16),
    ('Falz', 'afro-pop', 16, 31, 27, 13),
    ('Fireboy', 'afrobeats', 9, 26, 31, 10),
    ('Ice Prince', 'hiphop', 30, 37, 36, 18),
    ('Wizkid', 'reggae', 40, 32, 70, 21),
]


cur.executemany('INSERT INTO celebrity VALUES(?, ?, ?, ?, ?, ?)', celebrity_data)

print("execution successful")





for row in cur.execute('SELECT * FROM celebrity'):
     print(row)

#print(cur.fetchall())



#the most decorated celebrity
cur.execute(''' SELECT name, MAX(awards)
FROM celebrity'''
)
item = cur.fetchall()
print(item)


#The oldest celebrity
cur.execute('''SELECT name,MAX(age)
FROM celebrity'''
)
item = cur.fetchall()
print(item)

#The celebrity that has been in the industry the longest
cur.execute('''SELECT name,MAX(years_in_industry)
FROM celebrity'''
)
item = cur.fetchall()
print(item)


#The celebrity with the least number of albums
#cur.execute('''SELECT name,MIN(num_ album)
#FROM celebrity'''
#)
#item = cur.fetchall()
#print(item)


#the most popular genre of music amongst all celebrities in the dataset
cur.execute('''SELECT MAX(genre)
FROM celebrity'''
)
item = cur.fetchall()
print(item)


#Save commit the changes
con.commit()

#close the connection
con.close()