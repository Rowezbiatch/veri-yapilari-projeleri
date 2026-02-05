Binary Search Tree (BST) Proje Analizi

Veri Seti: [7, 5, 1, 8, 3, 6, 0, 9, 4, 2]

1. BST Mantığı ve Kurallar

Binary Search Tree yapısında her düğüm (node) için şu kural geçerlidir:

Sol Alt Ağaç: Düğüm değerinden küçük olanlar.

Sağ Alt Ağaç: Düğüm değerinden büyük olanlar.

2. Adım Adım Oluşturma Süreci

Adım

Eleman

İşlem

Konum

1

7

İlk eleman

Root (Kök)

2

5

5 < 7

7'nin Solu

3

1

1 < 7, 1 < 5

5'in Solu

4

8

8 > 7

7'nin Sağı

5

3

3 < 7, 3 < 5, 3 > 1

1'in Sağı

6

6

6 < 7, 6 > 5

5'in Sağı

7

0

0 < 7, 0 < 5, 0 < 1

1'in Solu

8

9

9 > 7, 9 > 8

8'in Sağı

9

4

4 < 7, 4 < 5, 4 > 1, 4 > 3

3'ün Sağı

10

2

2 < 7, 2 < 5, 2 > 1, 2 < 3

3'ün Solu

3. Görsel BST Yapısı

          7
        /   \
       5     8
      / \     \
     1   6     9
    / \
   0   3
      / \
     2   4


4. Big O Gösterimi

Ekleme (Insertion): Ortalama $O(\log n)$, En kötü $O(n)$

Arama (Search): Ortalama $O(\log n)$, En kötü $O(n)$
