# Fungsi untuk melakukan sequential search
def sequential_search(arr, key):
    for i in range(len(arr)):
        if arr[i] == key:
            return i
    return -1

# Inisialisasi data buku dalam bentuk array
books = [
    ['B001', '978-3-16-148410-0', 'Mencari Cinta Sejati', 'Rudy', 'Gramedia'],
    ['B002', '978-1-23-456789-0', 'Python Programming', 'Wahyu', 'Elexmedia'],
    ['B003', '978-9-87-654321-0', 'Matematika Dasar', 'Indra', 'Erlangga'],
    ['B004', '978-2-34-567890-1', 'Cerita Anak-Anak', 'Ani', 'Bukune'],
    ['B005', '978-4-56-789012-3', 'Agama untuk Pemula', 'Taufik', 'Bukukita']
]

# Pencarian buku berdasarkan kata kunci
search_key = input("Masukkan kata kunci: ")
result = []
for i in range(len(books[0])):
    for j in range(len(books)):
        if books[j][i].lower().find(search_key.lower()) != -1:
            index = sequential_search(result, books[j])
            if index == -1:
                result.append(books[j])

# Menampilkan hasil pencarian
if len(result) > 0:
    print("Hasil pencarian:")
    for i in range(len(result)):
        print("Kode Buku:", result[i][0])
        print("ISBN:", result[i][1])
        print("Judul Buku:", result[i][2])
        print("Penulis:", result[i][3])
        print("Penerbit:", result[i][4])
else:
    print("Buku tidak ditemukan.")
