# Push-Method-Python-Programming
Membuat aplikasi sederhana dengan python

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
