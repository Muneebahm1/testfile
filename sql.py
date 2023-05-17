import sqlite3

def login(username, password):
    # Vulnerable to SQL injection attack
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    
    query = f"SELECT * FROM users WHERE username='{username}' AND password='{password}'"
    cursor.execute(query)
    
    user = cursor.fetchone()
    conn.close()
    
    if user:
        return "Login successful"
    else:
        return "Invalid credentials"
