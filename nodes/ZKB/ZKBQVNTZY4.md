---
tag: ZKBQVNTZY4
kind: proof
name: Proof of the equivalent conditions for an orthogonal matrix
msc: ["15B10"]
topics: [AZS5BPF5H3]
audience: ug1
proves: F7M8ZXB4P7
uses: [0QRBVFJ50X, 04CPJ6AF00, 0ZZQ2E1MTE, FBSAPTP1PR, 0FWJ0VW561, 05FKHRT0B4]
methods: [0NTF6DMVAP]
sources:
  - url: https://en.wikipedia.org/wiki/Orthogonal_matrix
    locator: Matrix properties
  - book: isbn:9780134860244
    locator: Section 6.5
---

## Proof

We first link conditions 1, 2 and 3 through the determinant, then read conditions 4 and 5 off the entries of $Q^TQ$ and $QQ^T$, and last link conditions 1, 6 and 7 through the dot product.
Let $q_1, \dots, q_n$ be the columns of $Q$ and $r_1, \dots, r_n$ its rows, written as column vectors, and let $\delta_{jk}$ be $1$ for $j = k$ and $0$ for $j \ne k$.

**From 1 to 3.**

1. Assume $Q^TQ = I_n$. By the [[multiplicativity of the determinant|04CPJ6AF00]], $\det(Q^T)\det(Q) = \det(I_n) = 1$.
2. So $\det Q \ne 0$, and $Q$ is invertible by the [[determinant test|FBSAPTP1PR]].
3. Then $Q^{-1} = (Q^TQ)Q^{-1} = Q^T(QQ^{-1}) = Q^T$, which is condition 3.

**From 3 to 2.**

4. If $Q^{-1} = Q^T$, then $QQ^T = QQ^{-1} = I_n$.

**From 2 to 1.**

5. Assume $QQ^T = I_n$, and put $P = Q^T$. Then $P^TP = QQ^T = I_n$, because $(Q^T)^T = Q$.
6. Steps 1 to 3 applied to $P$ show that $P$ is invertible with $P^{-1} = P^T = Q$.
7. So $Q^T = P = Q^{-1}$, and $Q^TQ = Q^{-1}Q = I_n$.

**Conditions 1 and 4.**

8. The entry $(j, k)$ of $Q^TQ$ is row $j$ of $Q^T$ times column $k$ of $Q$, that is, $q_j^Tq_k = q_j \cdot q_k$.
9. So $Q^TQ = I_n$ exactly when $q_j \cdot q_k = \delta_{jk}$ for all $j$ and $k$, that is, when the columns are orthonormal.
10. Orthonormal vectors are linearly independent: if $\sum_k c_k q_k = 0$, the dot product with $q_j$ gives $c_j = 0$. So $n$ orthonormal vectors in $\R^n$ form an [[orthonormal basis|0FWJ0VW561]].

**Conditions 2 and 5.**

11. The entry $(j, k)$ of $QQ^T$ is row $j$ of $Q$ times column $k$ of $Q^T$, that is, $r_j \cdot r_k$.
12. As in steps 9 and 10, $QQ^T = I_n$ exactly when the rows form an orthonormal basis.

**Conditions 1, 6 and 7.**

13. Assume condition 1. The rule $(AB)^T = B^TA^T$ gives $Qx \cdot Qy = (Qx)^T(Qy) = x^TQ^TQy = x^Ty = x \cdot y$, which is condition 6.
14. Assume condition 6, and take $y = x$. Then $\norm{Qx}^2 = Qx \cdot Qx = x \cdot x = \norm{x}^2$, which is condition 7.
15. Assume condition 7. The [[polarization identity|05FKHRT0B4]] and linearity give $Qx \cdot Qy = \frac{1}{4}\left(\norm{Q(x + y)}^2 - \norm{Q(x - y)}^2\right) = \frac{1}{4}\left(\norm{x + y}^2 - \norm{x - y}^2\right) = x \cdot y$.
16. Let $e_1, \dots, e_n$ be the standard basis. Then $Qe_j = q_j$, and step 15 gives $q_j \cdot q_k = e_j \cdot e_k = \delta_{jk}$.
17. So the columns are orthonormal, and condition 1 holds by step 9.

All seven conditions are therefore equivalent.

## Idea

The entries of $Q^TQ$ are the dot products of the columns, and the entries of $QQ^T$ are the dot products of the rows.
For a square matrix a one-sided inverse is a two-sided inverse, and the determinant shows this in one line.
The formula $x \cdot y = x^Ty$ turns the matrix identity $Q^TQ = I$ into the statement that $Q$ keeps dot products, and polarization brings us back from lengths to dot products.

## Variants

Steps 1 to 3 can use rank in place of determinants.
If $Q^TQ = I$, then $Qx = 0$ gives $x = Q^TQx = 0$, so $x \mapsto Qx$ is injective, and $Q$ is invertible by the rank-nullity theorem.

Conditions 1, 6 and 7 are also the case $V = W = \R^n$ of the [[equivalent conditions for a linear isometry|95ST99SEW7]], because the adjoint of $x \mapsto Qx$ for the dot product has the matrix $Q^T$.
