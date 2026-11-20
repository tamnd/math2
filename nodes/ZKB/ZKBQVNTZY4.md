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

Let $q_1, \dots, q_n$ be the columns of $Q$ and $r_1, \dots, r_n$ its rows, written as column vectors.
Let $\delta_{jk}$ be $1$ for $j = k$ and $0$ for $j \neq k$.

**From 1 to 3.**

1. Assume $Q^TQ = I_n$. By [[the multiplicativity of the determinant|04CPJ6AF00]], $\det(Q^T)\det(Q) = \det(I_n) = 1$.
2. So $\det Q \neq 0$, and $Q$ is invertible, by [[the determinant test|FBSAPTP1PR]].
3. Then $Q^{-1} = (Q^TQ)Q^{-1} = Q^T(QQ^{-1}) = Q^T$. This is condition 3.

**From 3 to 2.**

4. If $Q^{-1} = Q^T$, then $QQ^T = QQ^{-1} = I_n$.

**From 2 to 1.**

5. Assume $QQ^T = I_n$. Put $P = Q^T$. Then $P^TP = QQ^T = I_n$, because $(Q^T)^T = Q$.
6. By steps 1 to 3 applied to $P$, the matrix $P$ is invertible with $P^{-1} = P^T = Q$.
7. So $Q^T = P = Q^{-1}$, and $Q^TQ = Q^{-1}Q = I_n$.

**Conditions 1 and 4.**

8. The $(j, k)$ entry of $Q^TQ$ is row $j$ of $Q^T$ times column $k$ of $Q$, that is, $q_j^Tq_k = q_j \cdot q_k$.
9. So $Q^TQ = I_n$ exactly when $q_j \cdot q_k = \delta_{jk}$ for all $j, k$, that is, when the columns are orthonormal.
10. $n$ orthonormal vectors in $\R^n$ are linearly independent: if $\sum_k c_k q_k = 0$, the dot product with $q_j$ gives $c_j = 0$. So they form an [[orthonormal basis|0FWJ0VW561]].

**Conditions 2 and 5.**

11. The $(j, k)$ entry of $QQ^T$ is row $j$ of $Q$ times column $k$ of $Q^T$, that is, $r_j \cdot r_k$.
12. As in steps 9 and 10, $QQ^T = I_n$ exactly when the rows form an orthonormal basis.

**Conditions 1, 6 and 7.**

13. Assume condition 1. Then $Qx \cdot Qy = (Qx)^T(Qy) = x^TQ^TQy = x^Ty = x \cdot y$, by the rule $(AB)^T = B^TA^T$. This is condition 6.
14. Assume condition 6. Take $y = x$: $\norm{Qx}^2 = Qx \cdot Qx = x \cdot x = \norm{x}^2$. This is condition 7.
15. Assume condition 7. By the [[polarization identity|05FKHRT0B4]], $Qx \cdot Qy = \frac{1}{4}\left(\norm{Q(x + y)}^2 - \norm{Q(x - y)}^2\right) = \frac{1}{4}\left(\norm{x + y}^2 - \norm{x - y}^2\right) = x \cdot y$.
16. Let $e_1, \dots, e_n$ be the standard basis. Then $Qe_j = q_j$, and step 15 gives $q_j \cdot q_k = e_j \cdot e_k = \delta_{jk}$.
17. So the columns are orthonormal, and condition 1 holds by step 9.

All seven conditions are therefore equivalent.

## Idea

The entries of $Q^TQ$ are the dot products of the columns, and the entries of $QQ^T$ are the dot products of the rows.
For a square matrix, a one-sided inverse is a two-sided inverse, and the determinant gives this quickly.
The dot product $x^Ty$ turns the matrix identity $Q^TQ = I$ into the statement that $Q$ keeps dot products.

## Variants

- Steps 1 to 3 can use rank instead of determinants: $Q^TQ = I$ makes $x \mapsto Qx$ injective, so $Q$ is invertible by the rank-nullity theorem.
- Conditions 1, 6 and 7 are the case $V = W = \R^n$ of the [[equivalent conditions for a linear isometry|95ST99SEW7]], since the adjoint of $x \mapsto Qx$ has the matrix $Q^T$.
