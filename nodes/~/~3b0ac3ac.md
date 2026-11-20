---
tag: ~3b0ac3ac
kind: proof
name: Proof of the classification and count of conjugacy classes of GL_n over a finite field
msc: ["20G40", "15A21"]
topics: [GEBYZKYV3D]
audience: grad
proves: ~82afa2e3
uses: [042JWAR3Q0, ~dd227218, 0D6KH8Y59N, 033WGN00BF, 0578PA53VA, ~0a19e561, 0FCCDXH97W, 0FNN9B4W64, 0VK5V9P8G3, 0JQ1KNQW2K, 0ZXZ82FTX2]
sources:
  - url: https://en.wikipedia.org/wiki/Frobenius_normal_form
    locator: General case and theory
---

## Proof

Write $F = \mathbb{F}_q$ and $G = GL_n(F)$.

1. Part 1. Matrices $A, B \in G$ are conjugate in $G$ if and only if $B = P A P^{-1}$ for some $P \in G$, that is, if and only if they are similar over $F$. A matrix similar to an invertible matrix has the same nonzero determinant. So the classes of $G$ are the similarity classes of $M_n(F)$ that lie in $G$.
2. By the [[rational canonical form theorem|042JWAR3Q0]], each similarity class contains exactly one $R = C(d_1) \oplus \cdots \oplus C(d_r)$ with $d_1 \mid \cdots \mid d_r$ monic and nonconstant, and $\sum \deg d_i = n$. Two matrices are similar if and only if they have the same invariant factors $d_i$.
3. By the [[characteristic polynomial of a companion matrix|~dd227218]], $\chi_{C(d)} = d$, so $\det C(d) = (-1)^{\deg d} d(0)$. Hence $\det R = \pm \prod_i d_i(0)$, and $R$ is invertible if and only if $d_i(0) \ne 0$ for all $i$.
4. $d_i(0) = 0$ means $x \mid d_i$. Since $d_i \mid d_r$, this implies $x \mid d_r$. So $R$ is invertible if and only if $d_r(0) \ne 0$. This proves part 1.
5. Part 2. $F[x]$ has [[unique factorization|0D6KH8Y59N]]. For a list as in part 1 and a monic irreducible $f$, let $e_i(f)$ be the exponent of $f$ in $d_i$. Then $e_1(f) \le \cdots \le e_r(f)$ since $d_i \mid d_{i+1}$, and $e_i(x) = 0$ since $d_r(0) \ne 0$.
6. Let $\lambda(f)$ be the partition whose parts are the nonzero numbers among $e_r(f) \ge \cdots \ge e_1(f)$. Then $\sum_{f \in \Phi} \deg f \cdot |\lambda(f)| = \sum_i \sum_f e_i(f) \deg f = \sum_i \deg d_i = n$.
7. Conversely, given $\lambda$ with $\sum_f \deg f \cdot |\lambda(f)| = n \ge 1$, let $r$ be the largest number of parts of a $\lambda(f)$, and write $\lambda(f) = (\lambda_1(f) \ge \cdots \ge \lambda_r(f))$, with zeros added at the end. Put $d_{r+1-j} = \prod_{f \in \Phi} f^{\lambda_j(f)}$ for $j = 1, \dots, r$.
8. Since $\lambda_{j+1}(f) \le \lambda_j(f)$ for every $f$, we get $d_1 \mid d_2 \mid \cdots \mid d_r$. Some $\lambda(f)$ has $r$ nonzero parts, so $d_1$ is nonconstant. The degrees add up to $n$, and $d_r(0) \ne 0$ because $x \notin \Phi$.
9. By unique factorization, the constructions of steps 6 and 7 are inverse to each other. With part 1, this proves part 2.
10. Part 3. Let $N(d)$ be the number of monic irreducible polynomials of degree $d$ in $F[x]$, and $N^*(d)$ the number of those in $\Phi$. So $N^*(1) = q - 1$ and $N^*(d) = N(d)$ for $d \ge 2$.
11. In the ring of [[formal power series|033WGN00BF]] $\mathbb{Z}[[u]]$, consider $\prod_{d \ge 1} (1 - u^d)^{-N(d)}$. Only the factors with $d \le n$ affect the coefficient of $u^n$, so the product is defined.
12. Expand each factor $(1 - u^{\deg f})^{-1} = \sum_{m \ge 0} u^{m \deg f}$, one for each monic irreducible $f$. The coefficient of $u^n$ counts the choices of exponents $m_f$ with $\sum_f m_f \deg f = n$. By unique factorization, these choices correspond to the monic polynomials $\prod_f f^{m_f}$ of degree $n$, and there are $q^n$ of them.
13. So $\prod_{d \ge 1} (1 - u^d)^{-N(d)} = \sum_n q^n u^n = (1 - q u)^{-1}$. Removing the factor $(1 - u)^{-1}$ of $f = x$ gives $\prod_{d \ge 1} (1 - u^d)^{-N^*(d)} = (1 - u)/(1 - q u)$.
14. By the [[generating function for partitions|0578PA53VA]], $\sum_{\mu} t^{|\mu|} = \prod_{k \ge 1} (1 - t^k)^{-1}$, the sum over all partitions $\mu$. For $f \in \Phi$, put $t = u^{\deg f}$: the factor $\prod_k (1 - u^{k \deg f})^{-1}$ counts the choices of $\lambda(f)$, each with weight $u^{\deg f \cdot |\lambda(f)|}$.
15. By part 2, $c_n(q)$ is the number of maps $\lambda$ of total weight $n$. Multiplying the factors of step 14 over $f \in \Phi$ and grouping them by $\deg f$ gives
$$\sum_n c_n(q)\, u^n = \prod_{k \ge 1} \prod_{d \ge 1} \bigl(1 - (u^k)^d\bigr)^{-N^*(d)} = \prod_{k \ge 1} \frac{1 - u^k}{1 - q u^k},$$
by step 13 with $u$ replaced by $u^k$.
16. Small coefficients. Each factor is $\frac{1 - u^k}{1 - q u^k} = 1 + \sum_{j \ge 1} a_j u^{jk}$ with $a_j = (q - 1) q^{j-1}$. A term of $u^n$ in the product chooses $j_k \ge 0$ for each $k$ with $\sum_k k j_k = n$.
17. For $n = 1$, the only choice is $j_1 = 1$, so $c_1 = a_1 = q - 1$. For $n = 2$, the choices are $j_1 = 2$ and $j_2 = 1$, so $c_2 = a_2 + a_1 = (q - 1)(q + 1) = q^2 - 1$.
18. For $n = 3$, the choices are $j_1 = 3$; $j_1 = j_2 = 1$; and $j_3 = 1$. So $c_3 = a_3 + a_1^2 + a_1 = (q - 1)(q^2 + q - 1 + 1) = q^3 - q$.
19. For $n = 4$, the choices are $j_1 = 4$; $j_1 = 2, j_2 = 1$; $j_1 = j_3 = 1$; $j_2 = 2$; and $j_4 = 1$. So $c_4 = a_4 + a_2 a_1 + a_1^2 + a_2 + a_1 = (q - 1)\bigl(q^3 + q(q - 1) + (q - 1) + q + 1\bigr) = (q - 1)(q^3 + q^2 + q) = q^4 - q$.
20. Part 4, the classes. By part 1 with $n = 2$, either $r = 2$ and $d_1 = d_2 = x - a$ with $a \ne 0$, which gives the $q - 1$ scalar matrices, or $r = 1$ and $d_1 = \chi_A$ is monic of degree $2$ with $\chi_A(0) \ne 0$.
21. In the case $r = 1$, $\chi_A$ is $(x - a)^2$ with $a \ne 0$, or $(x - a)(x - b)$ with $a \ne b$ both nonzero, or irreducible. There are $q - 1$, $(q - 1)(q - 2)/2$ and $q^2 - q - q(q - 1)/2 = (q^2 - q)/2$ of these, since $q^2$ monic quadratics exist and $q + q(q - 1)/2$ of them split. An irreducible quadratic has no root, so its value at $0$ is not $0$.
22. The matrices $\begin{pmatrix} a & 1 \\ 0 & a \end{pmatrix}$ and $\operatorname{diag}(a, b)$ with $a \ne b$ are not scalar, so each has the single invariant factor $\chi_A$, and they represent the second and third types.
23. Part 4, the centralizers. A scalar matrix commutes with all of $G$. A nonscalar $A$ has $r = 1$, so it is cyclic, and by the [[theorem on commuting matrices|~0a19e561]], the matrices that commute with $A$ form $F[A] \cong F[x]/(\chi_A)$.
24. If $X \in F[A]$ is invertible, then by the [[Cayley-Hamilton theorem|0FCCDXH97W]] for $X$, $X^{-1}$ is a polynomial in $X$ and lies in $F[A]$. So $C_G(A)$ is the group of units of $F[x]/(\chi_A)$.
25. For $\chi_A = (x - a)^2$, the element $c_0 + c_1 (x - a)$ is a unit if $c_0 \ne 0$, with inverse $c_0^{-1} - c_0^{-2} c_1 (x - a)$, and is nilpotent if $c_0 = 0$. So there are $q(q - 1)$ units.
26. For $\chi_A = (x - a)(x - b)$ with $a \ne b$, the [[Chinese remainder theorem|0FNN9B4W64]] gives $F[x]/(\chi_A) \cong F \times F$, with $(q - 1)^2$ units. For irreducible $\chi_A$, the quotient is a field with $q^2$ elements and $q^2 - 1$ units.
27. Part 4, the sizes. By the [[class size formula|0VK5V9P8G3]] and the [[order of $GL_2(\mathbb{F}_q)$|0JQ1KNQW2K]], $|G| = (q^2 - 1)(q^2 - q)$ and the class sizes are $1$, $(q^2 - 1)(q^2 - q)/(q(q - 1)) = q^2 - 1$, $(q^2 - 1)(q^2 - q)/(q - 1)^2 = q(q + 1)$ and $(q^2 - 1)(q^2 - q)/(q^2 - 1) = q(q - 1)$.
28. Check. $(q - 1) \cdot 1 + (q - 1)(q^2 - 1) + \frac{(q - 1)(q - 2)}{2} q (q + 1) + \frac{q^2 - q}{2} (q^2 - q) = (q - 1)\bigl(q^2 + q^3 - q^2 - q\bigr) = (q - 1)(q^3 - q)$, which equals $(q^2 - 1)(q^2 - q)$.

## Idea

Conjugacy in $GL_n(\mathbb{F}_q)$ is similarity, and similarity is decided by the invariant factors.
Regroup the invariant factors by irreducible polynomials to get one partition for each irreducible $f \ne x$.
Counting partition-valued functions is a product of partition generating functions, and unique factorization in $\mathbb{F}_q[x]$ turns the product into a closed form.

## Variants

For $n = 2$, part 4 also follows without part 3.
A nonscalar $2 \times 2$ matrix is similar to the companion matrix of its characteristic polynomial.
So the nonscalar classes in $G$ correspond to the $q(q - 1)$ monic quadratics with nonzero constant term.
With the $q - 1$ scalar classes this gives $q^2 - 1$ classes.
