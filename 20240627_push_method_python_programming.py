# -*- coding: utf-8 -*-
"""20240627 - Push Method Python Programming.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1xWZOKC77K5bfQqptQ--8zX-parCBgYgw

#PUSH METHOD PYTHON PROGRAMMING

Task 1: Anda ditugaskan untuk membuat program Python yang mensimulasikan sebuah pipeline data untuk memproses dan mentransformasi catatan data.
Catatan data mewakili pesanan pelanggan dalam sistem e-commerce. Setiap pesanan memiliki atribut berikut:

*   Order ID (string)
*   Customer Name (string)
*   Order Date (string)
*   Total Amount (float)

Task 2: Buat sebuah kelas bernama Order untuk merepresentasikan setiap pesanan.
Kelas ini harus memiliki metode-metode berikut:
*   __init__(self, order_id, customer_name, order_date, total_amount):Menginisialisasi atribut pesanan.
*   calculate_tax(self, tax rate): Menghitung dan mengembalikan jumlah pajak berdasarkan jumlah total dan tarif pajak yang diberikan (float antara 0 dan 1).
*   display_order(self): Mencetak detail pesanan dalam format yang mudah digunakan.

Task 3 Buat sebuah kelas bernama Order Processor untuk mengelola daftar pesanan.
Kelas ini harus memiliki metode-metode berikut:
*   __init__(self): Menginisialisasi list kosong untuk menyimpan pesanan.
*   add_order(self, order): Menambahkan pesanan ke dalam list pesanan.
*   calculate_total_revenue(self): Menghitung dan mengembalikan total pendapatan (jumlah total) untuk semua pesanan dalam list.
*   calculate_total_tax(self, tax_rate): Menghitung dan mengembalikan jumlah total pajak untuk semua pesanan dalam list berdasarkan tarif pajak yang diberikan.
*   display_orders (self): Menampilkan rincian semua pesanan dalam list.

Task 4: Buatlah sebuah program utama yang mendemonstrasikan fungsionalitas dari kelas-kelas Anda.


*   Buat beberapa objek Order dengan data yang berbeda.
*   Tambahkan pesanan-pesanan ini ke objek Order Processor
*   Hitung dan tampilkan total pendapatan dan total pajak untuk semua pesanan
*   Menampilkan detail dari semua pesanan.
*   List item
*   List item

Task 5: Buat repositori di Github dan push file kode Python.
Kamu harus membuat repositori dan melakukan push file kode Python bersama dengan dokumen singkat yang menjelaskan prinsip-prinsip OOP yang digunakan dalam kode dan bagaimana kamu mengujinya.
"""

class Order:
    def __init__(self, order_id, customer_name, order_date, total_amount):
        self.order_id = order_id
        self.customer_name = customer_name
        self.order_date = order_date
        self.total_amount = total_amount

    def calculate_tax(self, tax_rate):
        return self.total_amount * tax_rate

    def display_order(self):
        print(f"Order ID: {self.order_id}")
        print(f"Customer Name: {self.customer_name}")
        print(f"Order Date: {self.order_date}")
        print(f"Total Amount: ${self.total_amount:.2f}")

class OrderProcessor:
    def __init__(self):
        self.orders = []

    def add_order(self, order):
        self.orders.append(order)

    def calculate_total_revenue(self):
        total_revenue = sum(order.total_amount for order in self.orders)
        return total_revenue

    def calculate_total_tax(self, tax_rate):
        total_tax = sum(order.calculate_tax(tax_rate) for order in self.orders)
        return total_tax

    def display_orders(self):
        for order in self.orders:
            order.display_order()
            print("-----")

# Membuat beberapa objek Order dengan data yang berbeda
order1 = Order("001", "Alice", "2024-06-01", 150.0)
order2 = Order("002", "Bob", "2024-06-02", 200.0)
order3 = Order("003", "Charlie", "2024-06-03", 250.0)

# Membuat objek OrderProcessor dan menambahkan pesanan
processor = OrderProcessor()
processor.add_order(order1)
processor.add_order(order2)
processor.add_order(order3)

# Menghitung dan menampilkan total pendapatan dan total pajak untuk semua pesanan
total_revenue = processor.calculate_total_revenue()
total_tax = processor.calculate_total_tax(0.1)  # Menggunakan tarif pajak 10%

print(f"Total Revenue: ${total_revenue:.2f}")
print(f"Total Tax: ${total_tax:.2f}")
print("-----")

# Menampilkan detail dari semua pesanan
processor.display_orders()