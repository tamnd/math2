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

We use the adjugate of $t I_n - A$ and compare coefficients of powers of $t$.
All matrices with polynomial entries have entries in the [[polynomial ring|0Q9EZS90GY]] $K[t]$, which is commutative.

Matrices of polynomials.

1. Let $M_n(R)$ denote the $n \times n$ matrices over a commutative ring $R$. A matrix $X \in M_n(K[t])$ can be written in exactly one way as a finite sum $X = \sum_i t^i X_i$ with $X_i \in M_n(K)$. Entry $(j, l)$ of $X_i$ is the coefficient of $t^i$ in entry $(j, l)$ of $X$.
2. So two matrices in $M_n(K[t])$ are equal if and only if their coefficient matrices $X_i$ agree for each $i$.
3. The scalar $t$ commutes with every matrix over $K$. So for $X = \sum_i t^i X_i$ and $Y = \sum_j t^j Y_j$, the matrix product is $XY = \sum_k t^k \sum_{i + j = k} X_i Y_j$. In this product the order of $X_i$ and $Y_j$ is kept, because matrices over $K$ need not commute.

The adjugate identity.

4. Write $p_A(t) = \det(t I_n - A) = \sum_{i=0}^{n} c_i t^i$ with $c_i \in K$. By the [[definition of p_A|039HF58KQ5]], it is monic of degree $n$, so $c_n = 1$.
5. Case $n = 1$. Then $A = (a)$ and $p_A(t) = t - a$. So $p_A(A) = A - a I_1 = 0$. From now on let $n \ge 2$.
6. Let $B = \operatorname{adj}(t I_n - A) \in M_n(K[t])$ be the [[adjugate|0GMPYM0NSR]] over the commutative ring $K[t]$. Each entry of $B$ is a [[cofactor|0W2QAVJQ1W]], that is, up to sign the determinant of an $(n-1) \times (n-1)$ submatrix of $t I_n - A$.
7. Each entry of $t I_n - A$ has degree at most $1$ in $t$. By the [[Leibniz formula|016PE4VZ8Q]], an $(n-1) \times (n-1)$ determinant is a sum of products of $n - 1$ entries. So each entry of $B$ has degree at most $n - 1$.
8. By steps 1 and 7, $B = \sum_{i=0}^{n-1} t^i B_i$ with $B_i \in M_n(K)$.
9. By the [[product of a matrix and its adjugate|0528HKWZ1Z]] over $K[t]$, $(t I_n - A) B = p_A(t) I_n$.

Comparing coefficients.

10. By step 3, the left side of step 9 is $\sum_{i=0}^{n-1} t^{i+1} B_i - \sum_{i=0}^{n-1} t^i A B_i$. The right side is $\sum_{i=0}^{n} t^i c_i I_n$.
11. By step 2, the coefficients of each power of $t$ agree. For $t^n$: $B_{n-1} = c_n I_n$. For $1 \le i \le n-1$: $B_{i-1} - A B_i = c_i I_n$. For $t^0$: $-A B_0 = c_0 I_n$.
12. These are $n + 1$ equations in $M_n(K)$. Multiply the equation for $t^i$ on the left by $A^i$, for each $i = 0, 1, \dots, n$, with $A^0 = I_n$. Then add all $n + 1$ equations.
13. The right sides add up to $\sum_{i=0}^{n} c_i A^i$, which is the [[value p_A(A)|0BNEXSKNRV]].
14. The left sides add up to $A^n B_{n-1} + \sum_{i=1}^{n-1} (A^i B_{i-1} - A^{i+1} B_i) - A B_0$. Regrouping, this is $\sum_{i=1}^{n} A^i B_{i-1} - \sum_{i=0}^{n-1} A^{i+1} B_i$.
15. Substituting $j = i + 1$ in the second sum turns it into $\sum_{j=1}^{n} A^j B_{j-1}$. This equals the first sum, so the left sides add up to $0$.
16. By steps 13 and 15, $p_A(A) = 0$.

## Idea

The adjugate identity $(t I_n - A) \operatorname{adj}(t I_n - A) = p_A(t) I_n$ holds over the commutative ring $K[t]$.
Writing the adjugate as a polynomial in $t$ with matrix coefficients turns it into $n + 1$ equations between constant matrices.
Multiplying them by powers of $A$ and adding makes the left side telescope to $0$, while the right side becomes $p_A(A)$.

The proof does not put $t = A$ into the identity of step 9.
That substitution is not a ring homomorphism from $M_n(K)[t]$ to $M_n(K)$, because $A$ need not commute with the coefficients $B_i$.
The multiplication by $A^i$ on the left in step 12 is the correct replacement.

## Variants

- Triangularisation and density: over $\C$, prove $p_U(U) = 0$ for an upper triangular $U$ through the flag $\operatorname{span}(e_1, \dots, e_i)$, and pass to all matrices through $A = SUS^{-1}$ by [[triangularisation|0363JMQ42Y]]. Then extend to every commutative ring because the entries of $p_A(A)$ are integer polynomials in the entries of $A$.
- Modules: the [[Cayley-Hamilton theorem for modules|SH3R5VTMZH]] applies the adjugate to the matrix $tI - A$ acting on the column of basis vectors of $K^n$, viewed as a $K[t]$-module.
- The tempting proof "$p_A(A) = \det(A - A) = 0$" is wrong. The statement of the [[Cayley-Hamilton theorem|0F765KFC2J]] explains why.
