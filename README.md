🌳 BST Visualizer & Logic Analyzer

Rowez Elite Series v2.0 — Binary Search Tree (İkili Arama Ağacı) yapısını derinlemesine inceleyen, adım adım işlem takibi ve görselleştirme sunan profesyonel bir simülatör.

⚡ Proje Vizyonu

Veri yapılarının temelini oluşturan BST algoritmasını statik bir yapıdan çıkarıp, çalışma anındaki (runtime) karar mekanizmalarını görselleştirmek ve analiz etmek için tasarlanmıştır.

🛠️ Teknik Özellikler

Recursive Insertion Engine: Verileri hiyerarşik kurallara göre otomatik olarak konumlandırır.

Step-by-Step Logger: Her bir elemanın kökten başlayarak izlediği yolu (Pathfinding) analiz eder.

Top-Down Tree Visualization: Ağaç yapısını terminal üzerinde hiyerarşik ve okunaklı bir formatta görselleştirir.

Big O Analysis: İşlem karmaşıklığını ve düğüm istatistiklerini raporlar.

🧬 BST Kuralları (Mekanik)

Simülatör aşağıdaki mantıksal operatörleri kullanır:

Root (Kök): Dizinin ilk elemanı sistemin merkezini oluşturur.

Left Branch: Değer < Düğüm ise sol kola yönlenir.

Right Branch: Değer ≥ Düğüm ise sağ kola yönlenir.

🚀 Hızlı Başlangıç

Projeyi çalıştırmak için Python 3.x yeterlidir. Herhangi bir harici kütüphaneye ihtiyaç duymaz (Pure Logic).

python bst_simulator.py


📊 Örnek Veri Seti Analizi

Giriş Dizisi: [7, 5, 1, 8, 3, 6, 0, 9, 4, 2]

Algoritma Çıktısı (Kısmi):

      Root: [7]
      L── [5]
            L── [1]
                  L── [0]
                  R── [3]
                        L── [2]
                        R── [4]
            R── [6]
      R── [8]
            R── [9]


🛡️ Gelişmiş Analiz Verileri

Time Complexity: $O(\log n)$ (Dengeli durumda).

Space Complexity: $O(n)$.

Traversal: Depth-First Search (DFS) tabanlı ekleme.

Developed by Rowez - Coding for Performance & Security
