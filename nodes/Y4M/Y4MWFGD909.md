---
tag: Y4MWFGD909
kind: proof
name: Proof of the Cayley-Hamilton theorem with the adjugate
msc: ["15A24", "15A18"]
topics: [6R1D6QPY3S]
audience: ug2
proves: 0F765KFC2J
methods: [XP5SDYKJX0, 0NTF6DMVAP]
uses: [039HF58KQ5, 0BNEXSKNRV, 0Q9EZS90GY, 0GMPYM0NSR, 0528HKWZ1Z, 0W2QAVJQ1W, 016PE4VZ8Q]
sources:
  - url: https://en.wikipedia.org/wiki/Cayley%E2%80%93Hamilton_theorem
    locator: A direct algebraic proof
  - book: isbn:9780135367971
---

## Proof

We write the adjugate of $t I_n - A$ as a polynomial in $t$ with matrix coefficients, compare the coefficients of each power of $t$ in the adjugate identity, and add the resulting equations so that the left side telescopes.
All matrices with polynomial entries have their entries in the [[polynomial ring|0Q9EZS90GY]] $K[t]$, which is commutative.

*Matrices of polynomials.*

1. For a commutative ring $R$ let $M_n(R)$ be the ring of $n \times n$ matrices over $R$.
   Each $X \in M_n(K[t])$ can be written in exactly one way as a finite sum $X = \sum_i t^i X_i$ with $X_i \in M_n(K)$, where entry $(j, l)$ of $X_i$ is the coefficient of $t^i$ in entry $(j, l)$ of $X$.
2. So two matrices in $M_n(K[t])$ are equal exactly when their coefficient matrices agree for each power of $t$.
3. The scalar $t$ commutes with every matrix over $K$.
   So for $X = \sum_i t^i X_i$ and $Y = \sum_j t^j Y_j$ the product is
$$XY = \sum_k t^k \sum_{i + j = k} X_i Y_j,$$
   where the order of $X_i$ and $Y_j$ is kept, because matrices over $K$ need not commute.

*The adjugate identity.*

4. Write $p_A(t) = \det(t I_n - A) = \sum_{i=0}^{n} c_i t^i$ with $c_i \in K$.
   By the [[definition of the characteristic polynomial|039HF58KQ5]] it is monic of degree $n$, so $c_n = 1$.
5. If $n = 1$, then $A = (a)$ and $p_A(t) = t - a$, so $p_A(A) = A - a I_1 = 0$.
   From now on let $n \ge 2$.
6. Let $B = \operatorname{adj}(t I_n - A) \in M_n(K[t])$ be the [[adjugate|0GMPYM0NSR]], formed over the commutative ring $K[t]$.
   Each entry of $B$ is a [[cofactor|0W2QAVJQ1W]], that is, up to sign the determinant of an $(n-1) \times (n-1)$ submatrix of $t I_n - A$.
7. Each entry of $t I_n - A$ has degree at most $1$ in $t$.
   By the [[Leibniz formula|016PE4VZ8Q]], an $(n-1) \times (n-1)$ determinant is a sum of products of $n - 1$ entries, so each entry of $B$ has degree at most $n - 1$.
8. By steps 1 and 7 we can write $B = \sum_{i=0}^{n-1} t^i B_i$ with $B_i \in M_n(K)$.
9. The [[product of a matrix and its adjugate|0528HKWZ1Z]], applied over $K[t]$, gives
$$(t I_n - A) B = p_A(t) I_n.$$

*Comparing coefficients.*

10. By step 3, the left side of step 9 is
$$\sum_{i=0}^{n-1} t^{i+1} B_i - \sum_{i=0}^{n-1} t^i A B_i,$$
    and the right side is $\sum_{i=0}^{n} t^i c_i I_n$.
11. By step 2 the coefficients of each power of $t$ agree, which gives $n + 1$ equations in $M_n(K)$:
$$B_{n-1} = c_n I_n, \qquad B_{i-1} - A B_i = c_i I_n \ (1 \le i \le n-1), \qquad -A B_0 = c_0 I_n.$$
12. Multiply the equation for $t^i$ on the left by $A^i$, for each $i = 0, 1, \dots, n$, with $A^0 = I_n$, and add all $n + 1$ equations.
13. The right sides add up to $\sum_{i=0}^{n} c_i A^i$, which is the [[value of the polynomial at A|0BNEXSKNRV]], $p_A(A)$.
14. The left sides add up to
$$A^n B_{n-1} + \sum_{i=1}^{n-1} \left( A^i B_{i-1} - A^{i+1} B_i \right) - A B_0 = \sum_{i=1}^{n} A^i B_{i-1} - \sum_{i=0}^{n-1} A^{i+1} B_i.$$
15. Put $j = i + 1$ in the second sum.
    It becomes $\sum_{j=1}^{n} A^j B_{j-1}$, which is the first sum, so the left sides add up to $0$.
16. By steps 13 and 15, $p_A(A) = 0$.

## Idea

The adjugate identity $(t I_n - A) \operatorname{adj}(t I_n - A) = p_A(t) I_n$ holds over the commutative ring $K[t]$, and it is the honest form of "put $t = A$".
We cannot put $t = A$ into it directly, because $A$ need not commute with the coefficients $B_i$ of the adjugate.
So we split the identity into one matrix equation for each power of $t$.
Multiplying the equation for $t^i$ by $A^i$ on the left and adding makes the left side collapse in pairs to $0$, while the right side becomes $p_A(A)$.

For $n = 2$ and $A = \begin{pmatrix} a & b \\ c & d \end{pmatrix}$ you can see every piece.
The adjugate of $tI - A$ is $tI + \begin{pmatrix} -d & b \\ c & -a \end{pmatrix}$, so $B_1 = I$ and $B_0 = \begin{pmatrix} -d & b \\ c & -a \end{pmatrix}$.
The equations of step 11 read $B_1 = I$, $B_0 - A B_1 = -(a + d) I$ and $-A B_0 = (ad - bc) I$, and each one can be checked by multiplying out.

## Variants

The proof by [[triangularization|0363JMQ42Y]] works over $\mathbb{C}$.
It shows $p_U(U) = 0$ for an upper triangular $U$, because each factor $U - u_{ii} I$ maps the span of $e_1, \dots, e_i$ into the span of $e_1, \dots, e_{i-1}$.
It then passes to every matrix through $A = S U S^{-1}$, and to every commutative ring because the entries of $p_A(A)$ are integer polynomials in the entries of $A$.

The [[Cayley-Hamilton theorem for modules|SH3R5VTMZH]] applies the adjugate trick to $K^n$ as a module over $K[t]$ with $t$ acting as $A$.
There the matrix $tI - A^{\mathsf{T}}$ kills the column of basis vectors, and its adjugate turns this into $\det(tI - A) e_i = 0$ for each $i$.

The one-line argument $p_A(A) = \det(A - A) = 0$ is not a proof, and the statement of the [[Cayley-Hamilton theorem|0F765KFC2J]] explains why it fails.
