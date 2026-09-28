import sqlite3
conn=sqlite3.connect('mlflow.db')
cur=conn.cursor()
print('experiments:', cur.execute('select experiment_id, name from experiments').fetchall())
rows=cur.execute('select run_uuid, name, experiment_id from runs').fetchall()
print('runs count:', len(rows))
for r in rows[:50]:
    print(r)
conn.close()
