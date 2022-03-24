import sqlite3
import pandas as pd

# Observing data
genstudio = pd.read_csv('genstudio.csv')
metadata = pd.read_csv('metadata.csv')
genstudio.head()
genstudio.shape
genstudio = genstudio.drop('Unnamed: 0', axis=1)
metadata.head()
metadata = metadata.drop('Unnamed: 0', axis=1)
metadata.shape
genstudio['Sample ID'].isin(metadata.dna_chip_id)

# Creation of database
connection = sqlite3.connect('genstudio.db')
cursor = connection.cursor()
genstudio.to_sql('genstudio', con=connection, if_exists="replace")
pd.read_sql('''SELECT *
                FROM genstudio
            ''', connection)
metadata.to_sql('metadata', con=connection, if_exists="replace")
pd.read_sql('''SELECT *
                FROM metadata
            ''', connection)

# Operations with db
# 1
joined_tables = """SELECT genstudio.*, metadata.breed, metadata.sex FROM genstudio
JOIN metadata ON genstudio.'Sample ID' = metadata.dna_chip_id;"""
cursor.execute(joined_tables)
result = cursor.fetchall()
result_df = pd.DataFrame(result)
result_df.head()

# 2
select_query = """
                SELECT "Sample ID", SNP, Chr, Position
                FROM genstudio
                WHERE "GC score" >= 0.5
				"""
connection.execute(select_query).fetchall()

# 3
joined_select = """SELECT genstudio.'Sample ID', genstudio.'GC score', metadata.breed FROM genstudio
JOIN metadata ON genstudio.'Sample ID' = metadata.dna_chip_id;"""
connection.execute(joined_select).fetchall()

# 4
add_string = ['[T/C]', 3, 12345]
add_query = """INSERT INTO genstudio (SNP, Chr, Position)
Values (?, ?, ?)"""
connection.execute(add_query, add_string)
connection.commit()

# 5
drop_query = """ALTER TABLE genstudio
DROP COLUMN Theta;"""
connection.execute(drop_query)
connection.commit()
connection.close()
