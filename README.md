# Veri Yapıları ve Algoritmalar: Sorting Projesi

Bu çalışma Patika.dev Veri Yapıları ve Algoritmalar eğitimi kapsamında hazırlanmıştır.

## Proje 1: Insertion Sort Analizi

**Verilen Dizi:** `[22, 27, 16, 2, 18, 6]`

### 1. Sıralama Aşamaları (Insertion Sort)
Insertion Sort, her adımda elemanı sol taraftaki sıralı alt dizideki doğru yerine yerleştirir.

1. **Adım:** `[22, 27, 16, 2, 18, 6]` -> (22 ve 27 sıralı, değişim yok)
2. **Adım:** `[16, 22, 27, 2, 18, 6]` -> (16 araya girer, en başa taşınır)
3. **Adım:** `[2, 16, 22, 27, 18, 6]` -> (2 en küçük olduğu için en başa gelir)
4. **Adım:** `[2, 16, 18, 22, 27, 6]` -> (18; 16 ile 22 arasına girer)
5. **Adım:** `[2, 6, 16, 18, 22, 27]` -> (6; 2 ile 16 arasına girer ve dizi sıralanır)

### 2. Big-O Gösterimi
* **O(n²)** (İç içe döngülerden dolayı karesel artış gösterir)

### 3. Time Complexity (18 Sayısı İçin)
Dizi sıralandıktan sonraki hali: `[2, 6, 16, 18, 22, 27]`
18 sayısı dizinin ortasında yer aldığı için kapsamı:
* **Average Case**

---

## Proje 2: Selection Sort Analizi

**Verilen Dizi:** `[7, 3, 5, 8, 2, 9, 4, 15, 6]`

### İlk 4 Adım
Selection Sort, her adımda dizideki en küçük elemanı bulur ve baştaki sayı ile yer değiştirir.

1. **Adım:** En küçük `2`. `7` ile yer değiştirir.
   * `[2, 3, 5, 8, 7, 9, 4, 15, 6]`
   
2. **Adım:** Kalan kısımdaki en küçük `3`. Yeri doğrudur, değişim olmaz.
   * `[2, 3, 5, 8, 7, 9, 4, 15, 6]`
   
3. **Adım:** Kalan kısımdaki en küçük `4`. `5` ile yer değiştirir.
   * `[2, 3, 4, 8, 7, 9, 5, 15, 6]`
   
4. **Adım:** Kalan kısımdaki en küçük `5`. `8` ile yer değiştirir.
   * `[2, 3, 4, 5, 7, 9, 8, 15, 6]`

---