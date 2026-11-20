---
tag: 0FRYPZ6D0X
kind: statement
role: theorem
name: Coefficients of the characteristic polynomial
aliases: [trace-is-a-coefficient-of-the-characteristic-polynomial]
msc: ["15A15", "15A18"]
topics: [6R1D6QPY3S]
audience: ug2
about: [0VSSPAFM2C]
uses: [039HF58KQ5, 07PTPSZPME, 0C3CFHDN6R, 0BT9BYWVRY]
sources:
  - url: https://en.wikipedia.org/wiki/Characteristic_polynomial
    locator: Properties
  - book: isbn:9780135367971
---

## Statement

Let $K$ be a commutative ring, let $n \ge 1$, and let $A$ be an $n \times n$ matrix over $K$.
For a subset $S \subseteq \{1, \dots, n\}$, let $A_S$ be the principal submatrix of $A$ with the rows and the columns in $S$.
For $0 \le k \le n$, let $E_k(A) = \sum_{|S| = k} \det A_S$ be the sum of the principal [[minors|0BT9BYWVRY]] of size $k$, with $E_0(A) = 1$.
Then the [[characteristic polynomial|0VSSPAFM2C]] of $A$ is
$$p_A(t) = \det(t I_n - A) = \sum_{k=0}^{n} (-1)^k E_k(A)\, t^{n-k}.$$
In particular:

1. The coefficient of $t^{n-1}$ is $-E_1(A) = -\tr A$, where $\tr$ is the [[trace|0XC1RDBY7A]].
2. The constant term is $(-1)^n E_n(A) = (-1)^n \det A$; see also the statement on [[the constant coefficient|0T0X8GTYYS]].
3. For $n = 2$, $p_A(t) = t^2 - (\tr A)\, t + \det A$.
4. For $n = 3$, $p_A(t) = t^3 - (\tr A)\, t^2 + E_2(A)\, t - \det A$, where $E_2(A)$ is the sum of the three $2 \times 2$ principal minors.

## Remarks

### Why each hypothesis is needed

- $K$ must be commutative, because the determinant and the polynomial ring $K[t]$ with a central variable need commutativity.
- The minors must be principal, with the same rows and columns. For $A = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$, the sum of all $1 \times 1$ minors is $2$, but $\tr A = 0$.

### Consequences

- Similar matrices have the same $E_k$ for each $k$, because they have the same characteristic polynomial. In particular, the trace and the determinant are similarity invariants.
- If $p_A$ splits as $\prod_i (t - \lambda_i)$, then $E_k(A)$ is the $k$-th [[elementary symmetric polynomial|0X5QVCF06N]] of $\lambda_1, \dots, \lambda_n$. So [[the trace is the sum of the eigenvalues|0NMXDCNNKR]] and [[the determinant is their product|0C2F40MEBC]].
- The formula gives a second method to check a characteristic polynomial computed by cofactor expansion.

### Converse

The numbers $E_1(A), \dots, E_n(A)$ determine $p_A$, but they do not determine $A$ up to similarity: $I_2$ and $\begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}$ have $E_1 = 2$ and $E_2 = 1$.

### Generalizations

- The coefficients are also given by the traces of the exterior powers: $E_k(A) = \tr(\Lambda^k A)$.
- Over a field of characteristic $0$, [[Newton's identities|0WG2A3HE0S]] express $E_k(A)$ through the power traces $\tr(A^j)$ for $j \le k$.

## History

Over an algebraically closed field, the sum of the principal minors of size $k$ equals the elementary symmetric polynomial of degree $k$ in the eigenvalues.
So the expansion connects the theory of determinants with the formulas of Viète for the roots of a polynomial.

## Explanations

### L1 human

The characteristic polynomial of a square matrix has $n + 1$ coefficients.
The first one is $1$.
The second one is minus the sum of the diagonal entries.
The last one is the determinant, with a sign.
The ones in between are sums of determinants of smaller square pieces centred on the diagonal.

### L2 human

We compute $p_A$ for $A = \begin{pmatrix} 4 & 1 & 1 \\ 1 & 4 & 1 \\ 1 & 1 & 4 \end{pmatrix}$ by the principal minors.

1. $E_1 = \tr A = 12$.
2. Each $2 \times 2$ principal minor is $\det \begin{pmatrix} 4 & 1 \\ 1 & 4 \end{pmatrix} = 15$, so $E_2 = 45$.
3. $E_3 = \det A = 4 (16 - 1) - 1 (4 - 1) + 1 (1 - 4) = 60 - 3 - 3 = 54$.
4. So $p_A(t) = t^3 - 12 t^2 + 45 t - 54$.
5. Check: $(t - 3)^2 (t - 6) = (t^2 - 6t + 9)(t - 6) = t^3 - 12t^2 + 45t - 54$.

The typical use is a quick computation or check of $p_A$ for $n = 2$ and $n = 3$.
A trap: for $n = 3$, the sign of the constant term is $-\det A$, not $+\det A$.

### L3 human

The identity $\det(t + X) = \sum_k t^{n-k} \tr(\Lambda^k X)$ is the expansion of the determinant on $\Lambda^n(K[t]^n)$.
Each $E_k$ is a polynomial function in the entries of $A$ that is invariant under conjugation.
Over $\C$, these functions generate the ring of all such invariant polynomial functions.
