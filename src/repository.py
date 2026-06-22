from src.database import get_connection

class LibraryRepository:
    def add_book(self, title, author, isbn):
        try:
            with get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute("INSERT INTO books (title, author, isbn) VALUES (?, ?, ?)", (title, author, isbn))
                conn.commit()
                return True
        except Exception:
            return False

    def get_all_books(self):
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM books")
            return cursor.fetchall()

    def delete_book(self, book_id):
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM books WHERE id = ?", (book_id,))
            conn.commit()
            return cursor.rowcount > 0

    def add_member(self, name, email):
        try:
            with get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute("INSERT INTO members (name, email) VALUES (?, ?)", (name, email))
                conn.commit()
                return True
        except Exception:
            return False

    def get_all_members(self):
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM members")
            return cursor.fetchall()

    def loan_book(self, book_id, member_id):
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT is_available FROM books WHERE id = ?", (book_id,))
            result = cursor.fetchone()
            if not result or result[0] == 0:
                return False
            cursor.execute("INSERT INTO loans (book_id, member_id) VALUES (?, ?)", (book_id, member_id))
            cursor.execute("UPDATE books SET is_available = 0 WHERE id = ?", (book_id,))
            conn.commit()
            return True

    def return_book(self, book_id):
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT is_available FROM books WHERE id = ?", (book_id,))
            result = cursor.fetchone()
            if not result or result[0] == 1:
                return False
            cursor.execute("UPDATE loans SET return_date = date('now') WHERE book_id = ? AND return_date IS NULL", (book_id,))
            cursor.execute("UPDATE books SET is_available = 1 WHERE id = ?", (book_id,))
            conn.commit()
            return True
