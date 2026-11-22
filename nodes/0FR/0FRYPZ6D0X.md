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

Each coefficient of the characteristic polynomial is, up to sign, a sum of determinants of square pieces of the matrix centered on the diagonal, running from the trace to the determinant.
Let $K$ be a commutative ring, let $n \ge 1$, and let $A$ be an $n \times n$ matrix over $K$.
For a subset $S \subseteq \{1, \dots, n\}$, let $A_S$ be the principal submatrix of $A$ with the rows and the columns in $S$.
For $0 \le k \le n$, let $E_k(A) = \sum_{|S| = k} \det A_S$ be the sum of the principal [[minors|0BT9BYWVRY]] of size $k$, with $E_0(A) = 1$.
Then the [[characteristic polynomial|0VSSPAFM2C]] of $A$ is
$$p_A(t) = \det(t I_n - A) = \sum_{k=0}^{n} (-1)^k E_k(A)\, t^{n-k}.$$
In particular:

1. The coefficient of $t^{n-1}$ is $-E_1(A) = -\operatorname{tr} A$, where $\operatorname{tr}$ is the [[trace|0XC1RDBY7A]].
2. The constant term is $(-1)^n E_n(A) = (-1)^n \det A$; see also the statement on [[the constant coefficient|0T0X8GTYYS]].
3. For $n = 2$, $p_A(t) = t^2 - (\operatorname{tr} A)\, t + \det A$.
4. For $n = 3$, $p_A(t) = t^3 - (\operatorname{tr} A)\, t^2 + E_2(A)\, t - \det A$, where $E_2(A)$ is the sum of the three $2 \times 2$ principal minors.

## Remarks

### A 3 by 3 computation

Take
$$A = \begin{pmatrix} 4 & 0 & 1 \\ -2 & 1 & 0 \\ -2 & 0 & 1 \end{pmatrix}.$$
The trace is $E_1 = 4 + 1 + 1 = 6$.
The principal minors of size $2$ use the rows and columns $\{1, 2\}$, $\{1, 3\}$ and $\{2, 3\}$:
$$\det \begin{pmatrix} 4 & 0 \\ -2 & 1 \end{pmatrix} = 4, \qquad \det \begin{pmatrix} 4 & 1 \\ -2 & 1 \end{pmatrix} = 6, \qquad \det \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix} = 1,$$
so $E_2 = 11$.
Expanding along the second column gives $E_3 = \det A = 1 \cdot (4 + 2) = 6$.
Part 4 then gives $p_A(t) = t^3 - 6t^2 + 11t - 6 = (t - 1)(t - 2)(t - 3)$.
Check: the products of pairs of roots add up to $2 + 3 + 6 = 11 = E_2$.

### Why each hypothesis is needed

The ring $K$ must be commutative, because the determinant over $K$ and over $K[t]$ is defined by the Leibniz formula, and that formula needs entries that commute.

The minors must be principal, with the same set of rows and columns.
For $A = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$ the sum of all four $1 \times 1$ minors is $2$, but $\operatorname{tr} A = 0$ and $p_A(t) = t^2 - 1$.

The signs $(-1)^k$ belong to the convention $\det(tI - A)$.
With $\det(A - tI)$ every coefficient is multiplied by $(-1)^n$, so for $n = 3$ the coefficient of $t^2$ becomes $+\operatorname{tr} A$.

### What it gives you

Similar matrices have the same characteristic polynomial, so they have the same $E_k$ for every $k$.
In particular the trace and the determinant are similarity invariants.

If $p_A$ splits as $\prod_i (t - \lambda_i)$, then comparing coefficients shows that $E_k(A)$ is the $k$-th [[elementary symmetric polynomial|0X5QVCF06N]] of $\lambda_1, \dots, \lambda_n$.
So [[the trace is the sum of the eigenvalues|0NMXDCNNKR]] and [[the determinant is their product|0C2F40MEBC]], each counted with multiplicity.
The formula also gives a second, independent way to check a characteristic polynomial that you computed by cofactor expansion.

### The converse

The numbers $E_1(A), \dots, E_n(A)$ determine $p_A$, but they do not determine $A$ up to similarity.
The matrices $I_2$ and $\begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}$ both have $E_1 = 2$ and $E_2 = 1$, and they are not similar.

### Generalizations

The coefficients are the traces of the exterior powers: $E_k(A) = \operatorname{tr}(\Lambda^k A)$.
Over a field of characteristic $0$, [[Newton's identities|0WG2A3HE0S]] express each $E_k(A)$ through the power traces $\operatorname{tr}(A^j)$ for $j \le k$; for example $E_2 = \tfrac{1}{2}\big((\operatorname{tr} A)^2 - \operatorname{tr}(A^2)\big)$.

## Explanations

### L1 human

The characteristic polynomial of a square matrix has $n + 1$ coefficients.
The first one is $1$.
The second one is minus the sum of the diagonal entries.
The last one is the determinant, with the sign $(-1)^n$.
The ones in between are sums of determinants of smaller square pieces whose diagonals lie on the diagonal of the matrix.

### L2 human

Here is a typical use: find $p_A$ for $A = \begin{pmatrix} 4 & 1 & 1 \\ 1 & 4 & 1 \\ 1 & 1 & 4 \end{pmatrix}$ without expanding $\det(tI - A)$.

1. The trace is $E_1 = 12$.
2. Each $2 \times 2$ principal minor is $\det \begin{pmatrix} 4 & 1 \\ 1 & 4 \end{pmatrix} = 15$, so $E_2 = 45$.
3. Expanding along the first row, $E_3 = \det A = 4 (16 - 1) - 1 (4 - 1) + 1 (1 - 4) = 60 - 3 - 3 = 54$.
4. So $p_A(t) = t^3 - 12t^2 + 45t - 54$.
5. Check: $(t - 3)^2 (t - 6) = (t^2 - 6t + 9)(t - 6) = t^3 - 12t^2 + 45t - 54$.

For $n = 2$ and $n = 3$ this is the fastest way to compute or check $p_A$.
Watch out: for $n = 3$ the constant term is $-\det A$, not $+\det A$.

### L3 human

The identity $\det(t + X) = \sum_k t^{n-k} \operatorname{tr}(\Lambda^k X)$ comes from expanding the top exterior power $\Lambda^n$ of $K[t]^n$.
Each $E_k$ is a polynomial function of the entries of $A$ that does not change under conjugation $A \mapsto P^{-1}AP$.
Over $\mathbb{C}$, the functions $E_1, \dots, E_n$ generate the ring of all polynomial functions on matrices with this property.
