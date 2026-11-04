---
tag: Y4MWFGD909
kind: proof
name: Proof of the Cayley–Hamilton theorem with the adjugate
msc: [15A24, 15A18]
proves: 0F765KFC2J
uses: [039HF58KQ5, 0BNEXSKNRV, 0GMPYM0NSR, 0528HKWZ1Z, 0W2QAVJQ1W, 016PE4VZ8Q]
sources:
  - url: https://en.wikipedia.org/wiki/Cayley–Hamilton_theorem
    locator: A direct algebraic proof
---

## Proof

We use the adjugate of $t I_n - A$ and compare coefficients of powers of $t$.

1. Write $p_A(t) = \det(t I_n - A) = \sum_{i=0}^{n} c_i t^i$ with $c_i \in K$. By the [[definition of $p_A$|039HF58KQ5]], it is monic of degree $n$, so $c_n = 1$.
2. Case $n = 1$. Then $A = (a)$ and $p_A(t) = t - a$. So $p_A(A) = A - a I_1 = 0$. From now on let $n \ge 2$.
3. A matrix with entries in $K[t]$ can be written in exactly one way as $\sum_i t^i M_i$ with matrices $M_i$ over $K$. Here entry $(j, l)$ of $M_i$ is the coefficient of $t^i$ in entry $(j, l)$. Two such matrices are equal if and only if all their coefficient matrices are equal.
4. Let $B = \operatorname{adj}(t I_n - A)$ be the [[adjugate|0GMPYM0NSR]] over the commutative ring $K[t]$. Each entry of $B$ is a [[cofactor|0W2QAVJQ1W]], that is, up to sign the determinant of an $(n-1) \times (n-1)$ submatrix of $t I_n - A$.
5. Each entry of $t I_n - A$ has degree at most $1$ in $t$. By the [[Leibniz formula|016PE4VZ8Q]], an $(n-1) \times (n-1)$ determinant is a sum of products of $n - 1$ entries. So each entry of $B$ has degree at most $n - 1$.
6. By steps 3 and 5, $B = \sum_{i=0}^{n-1} t^i B_i$ with $n \times n$ matrices $B_i$ over $K$.
7. By the [[product of a matrix and its adjugate|0528HKWZ1Z]] over $K[t]$, $(t I_n - A) B = p_A(t) I_n$.
8. Expanding the left side gives $\sum_{i=0}^{n-1} t^{i+1} B_i - \sum_{i=0}^{n-1} t^i A B_i$. The right side is $\sum_{i=0}^{n} t^i c_i I_n$.
9. Comparing coefficients by step 3 gives three kinds of equations. For $t^n$: $B_{n-1} = c_n I_n$. For $1 \le i \le n-1$: $B_{i-1} - A B_i = c_i I_n$. For $t^0$: $-A B_0 = c_0 I_n$.
10. Multiply the equation for $t^i$ on the left by $A^i$, for each $i = 0, 1, \dots, n$, with $A^0 = I_n$. Then add all $n + 1$ equations.
11. The right sides add up to $\sum_{i=0}^{n} c_i A^i$, which is the [[value $p_A(A)$|0BNEXSKNRV]].
12. The left sides add up to $A^n B_{n-1} + \sum_{i=1}^{n-1} (A^i B_{i-1} - A^{i+1} B_i) - A B_0$. Regrouping, this is $\sum_{i=1}^{n} A^i B_{i-1} - \sum_{i=0}^{n-1} A^{i+1} B_i$.
13. Substituting $j = i + 1$ in the second sum turns it into $\sum_{j=1}^{n} A^j B_{j-1}$. This equals the first sum, so the left sides add up to $0$.
14. By steps 11 and 13, $p_A(A) = 0$.

## Idea

The adjugate identity $(t I_n - A) \operatorname{adj}(t I_n - A) = p_A(t) I_n$ holds over the ring $K[t]$. Writing the adjugate as a polynomial in $t$ with matrix coefficients turns it into $n + 1$ equations between constant matrices. Multiplying them by powers of $A$ and adding makes the left side telescope to $0$, while the right side becomes $p_A(A)$.
