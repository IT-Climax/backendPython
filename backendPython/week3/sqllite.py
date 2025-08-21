import sqlite3
import os

# SQLite comes with Python's standard library, so no extra installation is needed.
# This script will use the sqlite3 module.

# Connect to the database (this creates 'example.db' if it doesn't exist)
conn = sqlite3.connect("backdb.db")
cursor = conn.cursor()

# 1. Create the 'projects' table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS projects (
        project_id INTEGER PRIMARY KEY,
        name TEXT,
        location TEXT,
        budget REAL
    )
""")
print("Table 'projects' created.")

# 2. Create the 'materials' table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS materials (
        material_id INTEGER PRIMARY KEY,
        project_id INTEGER,
        material_name TEXT,
        quantity INTEGER,
        FOREIGN KEY(project_id) REFERENCES projects(project_id)
    )
""")
print("Table 'materials' created.")

# 3. Insert records into the 'projects' table
cursor.execute("INSERT INTO projects (name, location, budget) VALUES (?, ?, ?)",
               ("Mall Construction", "Downtown", 500000))
cursor.execute("INSERT INTO projects (name, location, budget) VALUES (?, ?, ?)",
               ("Bridge Construction", "Uptown", 750000))
conn.commit()
print("Records inserted into 'projects'.")

# 4. Insert records into the 'materials' table
cursor.execute("INSERT INTO materials (project_id, material_name, quantity) VALUES (?, ?, ?)",
               (1, "Cement", 500))
cursor.execute("INSERT INTO materials (project_id, material_name, quantity) VALUES (?, ?, ?)",
               (1, "Bricks", 2000))
cursor.execute("INSERT INTO materials (project_id, material_name, quantity) VALUES (?, ?, ?)",
               (2, "Steel", 150))
conn.commit()
print("Records inserted into 'materials'.")

# 5. Update a record in 'projects' (update the budget for project 1)
cursor.execute("UPDATE projects SET budget = ? WHERE project_id = ?",
               (550000, 1))
conn.commit()
print("Updated budget for project 1.")

# 6. Update (patch) a record in 'materials' (change quantity for material with id 2)
cursor.execute("UPDATE materials SET quantity = ? WHERE material_id = ?",
               (2100, 2))
conn.commit()
print("Updated quantity for material with id 2.")

# 7. Delete a record from 'materials' (delete the material with id 3)
cursor.execute("DELETE FROM materials WHERE material_id = ?", (3,))
conn.commit()
print("Deleted material with id 3.")

# 8. Create a view that joins 'projects' and 'materials'
cursor.execute("""
    CREATE VIEW project_materials AS
    SELECT p.name as project_name, m.material_name, m.quantity
    FROM projects p
    JOIN materials m ON p.project_id = m.project_id
""")
conn.commit()
print("View 'project_materials' created.")

# 9. SELECT query: Retrieve data from the 'projects' table
cursor.execute("SELECT * FROM projects")
projects_data = cursor.fetchall()
print("Selected data from 'projects':", projects_data)

# 10. SELECT query: Retrieve data from the view 'project_materials'
cursor.execute("SELECT * FROM project_materials")
view_data = cursor.fetchall()
print("Selected data from view 'project_materials':", view_data)

# 11. Drop the 'materials' table (remove the table from the database)
cursor.execute("DROP TABLE IF EXISTS materials")
conn.commit()
print("Table 'materials' dropped.")

# 12. Delete the entire database by closing the connection and removing the file
conn.close()
# os.remove("backdb.db")
print("Database 'backdb.db' deleted.")
