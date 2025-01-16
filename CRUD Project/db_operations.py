import pymysql

# Konfigurasi koneksi database
connection = pymysql.connect(
    host='localhost',
    user='root',
    password='Unknown@23',  # Sesuaikan dengan password MySQL Anda
    database='dbitems'  # Ganti dengan nama database Anda
)

# Fungsi untuk mengambil semua item
def get_all_items():
    with connection.cursor() as cursor:
        cursor.execute('SELECT * FROM items')
        return cursor.fetchall()

# Fungsi untuk mengambil item berdasarkan ID
def get_item(item_id):
    with connection.cursor() as cursor:
        cursor.execute('SELECT * FROM items WHERE id = %s', (item_id,))
        return cursor.fetchone()

# Fungsi untuk menambah item
def add_item(name, description):
    with connection.cursor() as cursor:
        cursor.execute('INSERT INTO items (name, description) VALUES (%s, %s)', (name, description))
        connection.commit()

# Fungsi untuk memperbarui item
def update_item(item_id, name, description):
    with connection.cursor() as cursor:
        cursor.execute('UPDATE items SET name = %s, description = %s WHERE id = %s', (name, description, item_id))
        connection.commit()

# Fungsi untuk menghapus item
def delete_item(item_id):
    with connection.cursor() as cursor:
        cursor.execute('DELETE FROM items WHERE id = %s', (item_id,))
        connection.commit()
