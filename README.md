📂 Proje 1: Insertion Sort
Dizi: [22, 27, 16, 2, 18, 6]

1. Aşamalar (Sorting Steps): Insertion Sort, her adımda elemanı sol taraftaki sıralı alt dizideki doğru yerine yerleştirir.

Adım 1: [22, 27, 16, 2, 18, 6] (27, 22'den büyük, yer değişmez)

Adım 2: [16, 22, 27, 2, 18, 6] (16 araya girer, başa geçer)

Adım 3: [2, 16, 22, 27, 18, 6] (2 en başa yerleşir)

Adım 4: [2, 16, 18, 22, 27, 6] (18; 16 ile 22 arasına girer)

Adım 5: [2, 6, 16, 18, 22, 27] (6; 2 ile 16 arasına girer ve dizi sıralanır)


Shutterstock
2. Big-O Gösterimi:

O(n 
2
 ) (İç içe iki döngüden dolayı)

3. Time Complexity (18 Sayısı İçin): Dizi sıralandıktan sonraki hali: [2, 6, 16, 18, 22, 27] 18 sayısı dizinin ortasında yer aldığı için:

Cevap: Average Case

📂 Selection Sort (İlk 4 Adım)
Dizi: [7, 3, 5, 8, 2, 9, 4, 15, 6]

Selection Sort, her adımda kalan kısmın en küçük (minimum) elemanını bulur ve baştaki elemanla takas eder (swap).

Adım 1: En küçük 2. 7 ile takas edilir.

[2, 3, 5, 8, 7, 9, 4, 15, 6]

Adım 2: Kalan kısımda (3'ten itibaren) en küçük 3. Yeri değişmez (kendiyle takas).

[2, 3, 5, 8, 7, 9, 4, 15, 6]

Adım 3: Kalan kısımda (5'ten itibaren) en küçük 4. 5 ile takas edilir.

[2, 3, 4, 8, 7, 9, 5, 15, 6]

Adım 4: Kalan kısımda (8'den itibaren) en küçük 5. 8 ile takas edilir.

[2, 3, 4, 5, 7, 9, 8, 15, 6]