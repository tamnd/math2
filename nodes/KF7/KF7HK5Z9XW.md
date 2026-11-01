---
tag: KF7HK5Z9XW
kind: definition
name: Strassen algorithm
msc: [65F30, 68Q25, 15A69]
defines: 3CVWXDS4JQ
uses: [0VD9ZSWWJG, 032Q9FB8MT, 0B1261B5ED, 0TGV80E6A4]
sources:
  - url: https://en.wikipedia.org/wiki/Strassen_algorithm
---

## Definition

Let $R$ be a [[ring|0B1261B5ED]], let $n = 2^m$ with $m \ge 0$, and let $A$, $B$ be $n \times n$ [[matrices|0VD9ZSWWJG]] over $R$.
The *Strassen algorithm* computes $C = AB$ as follows.
If $n = 1$, it returns the product of the two entries.
Otherwise it splits $A$, $B$ and $C$ into four blocks of size $n/2$, as in $A = \begin{pmatrix} A_{11} & A_{12} \\ A_{21} & A_{22} \end{pmatrix}$.
It computes seven products, each by a recursive call:
$$\begin{aligned}
M_1 &= (A_{11} + A_{22})(B_{11} + B_{22}), & M_2 &= (A_{21} + A_{22}) B_{11}, \\
M_3 &= A_{11}(B_{12} - B_{22}), & M_4 &= A_{22}(B_{21} - B_{11}), \\
M_5 &= (A_{11} + A_{12}) B_{22}, & M_6 &= (A_{21} - A_{11})(B_{11} + B_{12}), \\
M_7 &= (A_{12} - A_{22})(B_{21} + B_{22}).
\end{aligned}$$
Then it returns
$$C_{11} = M_1 + M_4 - M_5 + M_7, \quad C_{12} = M_3 + M_5, \quad C_{21} = M_2 + M_4, \quad C_{22} = M_1 - M_2 + M_3 + M_6.$$

## Remarks

The formulas never use commutativity of $R$, which is why they can be applied to blocks.
With $T(n)$ the number of ring operations, $T(n) = 7\,T(n/2) + 18 (n/2)^2$, so $T(n) = O(n^{\log_2 7})$ in [[big O notation|0TGV80E6A4]].
Matrices of other sizes are padded with zero rows and columns up to the next power of $2$.
Example: for $A = \begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix}$ and $B = \begin{pmatrix} 5 & 6 \\ 7 & 8 \end{pmatrix}$, the products are $M_1 = 65$, $M_2 = 35$, $M_3 = -2$, $M_4 = 8$, $M_5 = 24$, $M_6 = 22$, $M_7 = -30$, and they give $C = \begin{pmatrix} 19 & 22 \\ 43 & 50 \end{pmatrix}$, which equals $AB$.
Non-example: the schoolbook recursion with the eight block products $A_{i1} B_{1j} + A_{i2} B_{2j}$ satisfies $T(n) = 8\,T(n/2) + O(n^2)$, which gives only $O(n^3)$.
In practice one switches to the ordinary method below some block size, because the extra additions make the recursion slower for small matrices.
