---

## Proje 2: Merge Sort Analizi

**Verilen Dizi:** `[16, 21, 11, 8, 12, 22]`

### 1. Sıralama Aşamaları (Merge Sort)

Merge Sort, diziyi önce tek eleman kalana kadar böler (**Divide**), sonra sıralı bir şekilde birleştirir (**Conquer**). 

#### 1.1 Bölme (Divide) Aşaması
1. `[16, 21, 11]` ve `[8, 12, 22]`
2. `[16, 21]`, `[11]` ve `[8, 12]`, `[22]`
3. `[16]`, `[21]`, `[11]` ve `[8]`, `[12]`, `[22]`

#### 1.2 Birleştirme (Merge) Aşaması
1. `[16, 21]` ve `[11]` -> **`[11, 16, 21]`**
2. `[8, 12]` ve `[22]` -> **`[8, 12, 22]`**
3. `[11, 16, 21]` ve `[8, 12, 22]` -> **`[8, 11, 12, 16, 21, 22]`** (Sıralanmış dizi)

### 2. Big-O Gösterimi
Merge Sort'un en iyi, ortalama ve en kötü durum zaman karmaşıklığı:
* **$O(n \log n)$**

---