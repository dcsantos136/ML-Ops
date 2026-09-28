import sqlite3
conn = sqlite3.connect('mlflow.db')
cur = conn.cursor()
print('Experiments:')
for row in cur.execute("select experiment_id, name from experiments"):
    print(row)

print('\nRuns (partial):')
# Print first 50 runs with columns available
rows = cur.execute("select * from runs limit 50").fetchall()
print('columns:', [c[0] for c in cur.description])
for r in rows:
    print(r)

conn.close()
