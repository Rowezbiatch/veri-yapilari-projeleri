

## Proje 3: Binary Search Tree (BST) Oluşturma

**Verilen Dizi:** `[7, 5, 1, 8, 3, 6, 0, 9, 4, 2]`

### BST Oluşturma Aşamaları

BST kuralı: Düğümün solunda kendinden küçük, sağında kendinden büyük elemanlar bulunur.

1.  **7:** Diziye giren ilk eleman **Root** olur.
    * **Root: 7**

2.  **5:** 7'den küçük, bu yüzden **7'nin solundan** devam edilir.
    * 7'nin Solu: 5

3.  **1:** 7'den küçük, 5'ten küçük, bu yüzden **5'in solundan** devam edilir.
    * 5'in Solu: 1

4.  **8:** 7'den büyük, bu yüzden **7'nin sağından** devam edilir.
    * 7'nin Sağı: 8

5.  **3:** 7'den küçük, 5'ten küçük, 1'den büyük, bu yüzden **1'in sağından** devam edilir.
    * 1'in Sağı: 3

6.  **6:** 7'den küçük, 5'ten büyük, bu yüzden **5'in sağından** devam edilir.
    * 5'in Sağı: 6

7.  **0:** 7'den küçük, 5'ten küçük, 1'den küçük, bu yüzden **1'in solundan** devam edilir.
    * 1'in Solu: 0

8.  **9:** 7'den büyük, 8'den büyük, bu yüzden **8'in sağından** devam edilir.
    * 8'in Sağı: 9

9.  **4:** 7'den küçük, 5'ten küçük, 1'den büyük, 3'ten büyük, bu yüzden **3'ün sağından** devam edilir.
    * 3'ün Sağı: 4

10. **2:** 7'den küçük, 5'ten küçük, 1'den büyük, 3'ten küçük, bu yüzden **3'ün solundan** devam edilir.
    * 3'ün Solu: 2

### Final BST Yapısı
* **Root:** 7
    * **Sol Kol:** 5 -> (Sol: 1 -> (Sol: 0, Sağ: 3 -> (Sol: 2, Sağ: 4))), (Sağ: 6)
    * **Sağ Kol:** 8 -> (Sağ: 9)

    