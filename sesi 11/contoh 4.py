# -*- coding: utf-8 -*-
"""
Created on Wed Jul 17 09:39:13 2019

@author: ROG-GL553VD
"""

from sqlalchemy import create_engine
import pandas as pd
import pandas.io as sql

def export_json(datas):
    """Export dataframe to JSON"""
    data_export = pd.DataFrame(datas,columns=['ID','Name','Salary','StartDate','Dept'])
    data_export.to_json("input.json")

data = pd.read_json("input.json")

# Create db engine
engine = create_engine('sqlite:///:memory:')

# store dataframe to table
data.to_sql('data_table',engine)

#Query 1
result_1 = pd.read_sql_query("SELECT * FROM data_table", engine)
print("Result 1")
print(result_1)
print()

#Query 2
result_2 = pd.read_sql_query("SELECT dept,SUM(salary) AS jumSalary FROM data_table GROUP BY dept", engine)
print("Result 2")
print(result_2)
print()

#Insert Datas
sql.sql.execute("INSERT INTO data_table VALUES(?,?,?,?,?,?)", engine, params=[('id',9,'Ruby',711.20,'2015-03-27','IT')])

result_1 = pd.read_sql_query("SELECT * FROM data_table ORDER BY Name", engine)
print(result_1)
print()

#export_json(result_1)

#Delete Datas
sql.sql.execute("DELETE FROM data_table WHERE name = (?) AND Dept = (?)",engine,params=[('Simon','Operations')])

result_1 = pd.read_sql_query("SELECT * FROM data_table ORDER BY Name", engine)
print(result_1)
print()

export_json(result_1)