---
tag: RRZE1PC4NB
kind: proof
name: Proof of the classification and count of conjugacy classes of GL_n over a finite field
msc: ["20G40", "15A21"]
topics: [GEBYZKYV3D]
audience: grad
proves: 4FV9TDGWWH
uses: [042JWAR3Q0, XYR7GPH20K, 0D6KH8Y59N, 033WGN00BF, 0578PA53VA, GXZGWZSJ2J, 0F765KFC2J, 0FNN9B4W64, 0VK5V9P8G3, 0JQ1KNQW2K, 0ZXZ82FTX2]
sources:
  - url: https://en.wikipedia.org/wiki/Frobenius_normal_form
    locator: General case and theory
---

## Proof

We reduce conjugacy to similarity, regroup the invariant factors by irreducible polynomials, and count the resulting data with generating functions.

Write $F = \mathbb{F}_q$ and $G = GL_n(F)$.

*Part 1.*

1. Matrices $A, B \in G$ are conjugate in $G$ when $B = P A P^{-1}$ for some $P \in G$, and this is the definition of similarity over $F$. A matrix similar to an invertible matrix has the same nonzero determinant, so the classes of $G$ are the similarity classes of $M_n(F)$ that lie in $G$.
2. By the [[rational canonical form theorem|042JWAR3Q0]], each similarity class contains exactly one $R = C(d_1) \oplus \cdots \oplus C(d_r)$ with $d_1 \mid \cdots \mid d_r$ monic and nonconstant and $\sum_i \deg d_i = n$. Two matrices are similar exactly when they have the same invariant factors $d_i$.
3. By the [[characteristic polynomial of a companion matrix|XYR7GPH20K]], $\chi_{C(d)} = d$, so $\det C(d) = (-1)^{\deg d} d(0)$. Hence $\det R = \pm \prod_i d_i(0)$, and $R$ is invertible exactly when $d_i(0) \ne 0$ for all $i$.
4. The condition $d_i(0) = 0$ means $x \mid d_i$, and then $x \mid d_r$ because $d_i \mid d_r$. So $R$ is invertible exactly when $d_r(0) \ne 0$, which proves part 1.

*Part 2.*

5. The ring $F[x]$ has [[unique factorization|0D6KH8Y59N]]. For a list as in part 1 and a monic irreducible $f$, let $e_i(f)$ be the exponent of $f$ in $d_i$. Then $e_1(f) \le \cdots \le e_r(f)$ because $d_i \mid d_{i+1}$, and $e_i(x) = 0$ because $d_r(0) \ne 0$.
6. Let $\lambda(f)$ be the partition whose parts are the nonzero numbers among $e_r(f) \ge \cdots \ge e_1(f)$. Comparing degrees on both sides of the factorizations gives
$$\sum_{f \in \Phi} \deg f \cdot |\lambda(f)| = \sum_{i=1}^{r} \sum_{f \in \Phi} e_i(f) \deg f = \sum_{i=1}^{r} \deg d_i = n.$$
7. Conversely, let $\lambda$ satisfy $\sum_f \deg f \cdot |\lambda(f)| = n \ge 1$, and let $r$ be the largest number of parts of a $\lambda(f)$. Write $\lambda(f) = (\lambda_1(f) \ge \cdots \ge \lambda_r(f))$ with zeros added at the end, and put $d_{r+1-j} = \prod_{f \in \Phi} f^{\lambda_j(f)}$ for $j = 1, \dots, r$.
8. Since $\lambda_{j+1}(f) \le \lambda_j(f)$ for every $f$, we get $d_1 \mid d_2 \mid \cdots \mid d_r$. Some $\lambda(f)$ has $r$ nonzero parts, so $d_1$ is nonconstant. The degrees add up to $n$, and $d_r(0) \ne 0$ because $x \notin \Phi$.
9. By unique factorization, the constructions of steps 6 and 7 are inverse to each other. With part 1, this proves part 2.

*Part 3.*

10. Let $N(d)$ be the number of monic irreducible polynomials of degree $d$ in $F[x]$, and let $N^*(d)$ be the number of those in $\Phi$. Then $N^*(1) = q - 1$ and $N^*(d) = N(d)$ for $d \ge 2$.
11. In the ring of [[formal power series|033WGN00BF]] $\mathbb{Z}[[u]]$, consider $\prod_{d \ge 1} (1 - u^d)^{-N(d)}$. Only the factors with $d \le n$ affect the coefficient of $u^n$, so the infinite product is defined.
12. Expand one factor $(1 - u^{\deg f})^{-1} = \sum_{m \ge 0} u^{m \deg f}$ for each monic irreducible $f$. The coefficient of $u^n$ counts the choices of exponents $m_f$ with $\sum_f m_f \deg f = n$. By unique factorization these choices match the monic polynomials $\prod_f f^{m_f}$ of degree $n$, and there are $q^n$ of them.
13. So $\prod_{d \ge 1} (1 - u^d)^{-N(d)} = \sum_n q^n u^n = (1 - q u)^{-1}$. Removing the factor $(1 - u)^{-1}$ of $f = x$ gives
$$\prod_{d \ge 1} (1 - u^d)^{-N^*(d)} = \frac{1 - u}{1 - q u}.$$
14. By the [[generating function for partitions|0578PA53VA]], $\sum_{\mu} t^{|\mu|} = \prod_{k \ge 1} (1 - t^k)^{-1}$, where the sum runs over all partitions $\mu$. For $f \in \Phi$ put $t = u^{\deg f}$, so that $\prod_k (1 - u^{k \deg f})^{-1}$ counts the choices of $\lambda(f)$, each with weight $u^{\deg f \cdot |\lambda(f)|}$.
15. By part 2, $c_n(q)$ is the number of maps $\lambda$ of total weight $n$. Multiply the factors of step 14 over all $f \in \Phi$, group them by $\deg f$, and use step 13 with $u$ replaced by $u^k$:
$$\sum_n c_n(q)\, u^n = \prod_{k \ge 1} \prod_{d \ge 1} \bigl(1 - (u^k)^d\bigr)^{-N^*(d)} = \prod_{k \ge 1} \frac{1 - u^k}{1 - q u^k}.$$
16. For the small coefficients, write each factor as $\frac{1 - u^k}{1 - q u^k} = 1 + \sum_{j \ge 1} a_j u^{jk}$ with $a_j = (q - 1) q^{j-1}$. A term of $u^n$ in the product chooses $j_k \ge 0$ for each $k$ with $\sum_k k j_k = n$.
17. For $n = 1$ the only choice is $j_1 = 1$, so $c_1 = a_1 = q - 1$. For $n = 2$ the choices are $j_1 = 2$ and $j_2 = 1$, so $c_2 = a_2 + a_1 = (q - 1)(q + 1) = q^2 - 1$.
18. For $n = 3$ the choices are $j_1 = 3$, then $j_1 = j_2 = 1$, then $j_3 = 1$. So $c_3 = a_3 + a_1^2 + a_1 = (q - 1)(q^2 + q) = q^3 - q$.
19. For $n = 4$ the choices are $j_1 = 4$, then $j_1 = 2$ with $j_2 = 1$, then $j_1 = j_3 = 1$, then $j_2 = 2$, then $j_4 = 1$. So
$$c_4 = a_4 + a_2 a_1 + a_1^2 + a_2 + a_1 = (q - 1)\bigl(q^3 + q(q - 1) + (q - 1) + q + 1\bigr) = (q - 1)(q^3 + q^2 + q) = q^4 - q.$$

*Part 4.*

20. By part 1 with $n = 2$, either $r = 2$ and $d_1 = d_2 = x - a$ with $a \ne 0$, which gives the $q - 1$ scalar matrices, or $r = 1$ and $d_1 = \chi_A$ is a monic quadratic with $\chi_A(0) \ne 0$.
21. In the case $r = 1$, $\chi_A$ is $(x - a)^2$ with $a \ne 0$, or $(x - a)(x - b)$ with $a \ne b$ both nonzero, or irreducible. There are $q^2$ monic quadratics, and $q + q(q - 1)/2$ of them split, so $q^2 - q - q(q - 1)/2 = (q^2 - q)/2$ are irreducible. An irreducible quadratic has no root, so its value at $0$ is not $0$, and the three counts are $q - 1$, $(q - 1)(q - 2)/2$ and $(q^2 - q)/2$.
22. The matrices $\begin{pmatrix} a & 1 \\ 0 & a \end{pmatrix}$ and $\operatorname{diag}(a, b)$ with $a \ne b$ are not scalar, so each has the single invariant factor $\chi_A$. So they represent the second and third types.
23. For the centralizers: a scalar matrix commutes with all of $G$. A nonscalar $A$ has $r = 1$, so it is cyclic, and by the [[theorem on commuting matrices|GXZGWZSJ2J]] the matrices that commute with $A$ form $F[A] \cong F[x]/(\chi_A)$.
24. If $X \in F[A]$ is invertible, then the [[Cayley-Hamilton theorem|0F765KFC2J]] for $X$ writes $X^{-1}$ as a polynomial in $X$, so $X^{-1} \in F[A]$. Hence $C_G(A)$ is the group of units of $F[x]/(\chi_A)$.
25. For $\chi_A = (x - a)^2$, the element $c_0 + c_1 (x - a)$ is a unit when $c_0 \ne 0$, with inverse $c_0^{-1} - c_0^{-2} c_1 (x - a)$, and it is nilpotent when $c_0 = 0$. So there are $q(q - 1)$ units.
26. For $\chi_A = (x - a)(x - b)$ with $a \ne b$, the [[Chinese remainder theorem|0FNN9B4W64]] gives $F[x]/(\chi_A) \cong F \times F$, with $(q - 1)^2$ units. For an irreducible $\chi_A$, the quotient is a field with $q^2$ elements and $q^2 - 1$ units.
27. For the sizes, the [[class size formula|0VK5V9P8G3]] and the [[order of GL_2(F_q)|0JQ1KNQW2K]], $|G| = (q^2 - 1)(q^2 - q)$, give
$$\frac{|G|}{q(q - 1)} = q^2 - 1, \qquad \frac{|G|}{(q - 1)^2} = q(q + 1), \qquad \frac{|G|}{q^2 - 1} = q(q - 1).$$
28. Check with the class equation:
$$(q - 1) + (q - 1)(q^2 - 1) + \frac{(q - 1)(q - 2)}{2} q (q + 1) + \frac{q^2 - q}{2} (q^2 - q) = (q - 1)(q^3 - q),$$
and $(q - 1)(q^3 - q) = (q - 1)^2 q (q + 1) = (q^2 - 1)(q^2 - q)$.

## Idea

Conjugacy in $GL_n(\mathbb{F}_q)$ is similarity, and similarity is decided by the invariant factors.
Regroup the invariant factors by irreducible polynomials, and you get one partition for each irreducible $f \ne x$.
Counting partition-valued functions is a product of partition generating functions, one for each $f$.
Unique factorization in $\mathbb{F}_q[x]$, which says that there are $q^n$ monic polynomials of degree $n$, collapses that product into a closed form.

## Variants

For $n = 2$, the count in part 4 also follows without part 3.
A nonscalar $2 \times 2$ matrix is similar to the companion matrix of its characteristic polynomial, by the [[similarity classes of 2 × 2 matrices|H6R274A93F]].
So the nonscalar classes in $G$ correspond to the $q(q - 1)$ monic quadratics with nonzero constant term.
With the $q - 1$ scalar classes this gives $q^2 - 1$ classes.
