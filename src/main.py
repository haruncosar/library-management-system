import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.database import create_tables
from src.repository import LibraryRepository

def main():
    create_tables()
    repo = LibraryRepository()
    
    while True:
        print("\n--- KUTUPHANE YONETIM SISTEMI ---")
        print("1. Yeni Kitap Ekle")
        print("2. Kitaplari Listele")
        print("3. Kitap Sil")
        print("4. Yeni Uye Ekle")
        print("5. Uyeleri Listele")
        print("6. Kitap Odunc Ver")
        print("7. Kitap Iade Al")
        print("8. Cikis")
        
        choice = input("Seciminiz (1-8): ")
        
        if choice == "1":
            title = input("Kitap Adi: ")
            author = input("Yazar: ")
            isbn = input("ISBN: ")
            if repo.add_book(title, author, isbn):
                print("Kitap basariyla eklendi!")
            else:
                print("Hata: Bu ISBN zaten kayitli olabilir.")
        elif choice == "2":
            books = repo.get_all_books()
            print("\nID | Baslik | Yazar | ISBN | Durum (1:Musait, 0:Oduncte)")
            print("-" * 60)
            for b in books:
                print(f"{b[0]} | {b[1]} | {b[2]} | {b[3]} | {b[4]}")
        elif choice == "3":
            b_id = input("Silinecek Kitap ID: ")
            if repo.delete_book(int(b_id)):
                print("Kitap silindi.")
            else:
                print("Kitap bulunamadi.")
        elif choice == "4":
            name = input("Uye Adi Soyadi: ")
            email = input("E-posta: ")
            if repo.add_member(name, email):
                print("Uye basariyla kaydedildi!")
            else:
                print("Hata: Bu e-posta zaten kullanimda.")
        elif choice == "5":
            members = repo.get_all_members()
            print("\nID | Isim | E-posta")
            print("-" * 40)
            for m in members:
                print(f"{m[0]} | {m[1]} | {m[2]}")
        elif choice == "6":
            b_id = input("Odunc Verilecek Kitap ID: ")
            m_id = input("Odunc Alacak Uye ID: ")
            if repo.loan_book(int(b_id), int(m_id)):
                print("Kitap basariyla odunc verildi.")
            else:
                print("Islem basarisiz!")
        elif choice == "7":
            b_id = input("Iade Edilecek Kitap ID: ")
            if repo.return_book(int(b_id)):
                print("Kitap iade edildi.")
            else:
                print("Islem basarisiz!")
        elif choice == "8":
            print("Cikis yapiliyor.")
            break
        else:
            print("Gecersiz secim!")

if __name__ == "__main__":
    main()
