import sqlite3
import os

def connect_db():
    db_path = os.path.join(os.path.dirname(__file__), 'bank.db')
    conn = sqlite3.connect(db_path)
    return conn

def create_table():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS accounts (
            account_number TEXT PRIMARY KEY,
            name TEXT NOT NULL,
            balance REAL NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def add_account(account_number, name, initial_balance):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO accounts (account_number, name, balance) VALUES (?, ?, ?)',
                   (account_number, name, initial_balance))
    conn.commit()
    conn.close()

def get_account(account_number):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM accounts WHERE account_number = ?', (account_number,))
    account = cursor.fetchone()
    conn.close()
    return account

def update_balance(account_number, new_balance):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('UPDATE accounts SET balance = ? WHERE account_number = ?', (new_balance, account_number))
    conn.commit()
    conn.close()