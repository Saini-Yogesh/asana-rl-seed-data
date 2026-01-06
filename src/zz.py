import sqlite3
conn = sqlite3.connect("output/asana_simulation.sqlite")

print("Users:", conn.execute("SELECT COUNT(*) FROM users").fetchone()[0])
print("Projects:", conn.execute("SELECT COUNT(*) FROM projects").fetchone()[0])
print("Tasks:", conn.execute("SELECT COUNT(*) FROM tasks").fetchone()[0])
print("Subtasks:", conn.execute("SELECT COUNT(*) FROM tasks WHERE parent_task_id IS NOT NULL").fetchone()[0])
print("Unassigned:", conn.execute("SELECT COUNT(*) FROM tasks WHERE assignee_id IS NULL").fetchone()[0])

conn.close()
