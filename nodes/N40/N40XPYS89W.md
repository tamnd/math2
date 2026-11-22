---
tag: N40XPYS89W
kind: statement
role: theorem
name: Geometric series for a nilpotent matrix
msc: ["15A09", "15A99"]
topics: [Y1ESNQ2V52]
audience: ug1
about: [07BSPZPSMF, 0EB9N0S33C]
uses: [0419GJC84P, 0EB9N0S33C, 6NHZRCKJNW]
sources:
  - url: https://en.wikipedia.org/wiki/Nilpotent_matrix
    locator: Properties
---

## Statement

The theorem gives the inverse of $I - N$ for a nilpotent $N$ as a finite geometric series.
Let $R$ be a ring, let $I$ be the $n \times n$ [[identity matrix|6NHZRCKJNW]] over $R$, and let $N$ be an $n \times n$ matrix over $R$ with $N^k = 0$ for some integer $k \ge 1$.
Then $I - N$ is [[invertible|0EB9N0S33C]], and
$$(I - N)^{-1} = I + N + N^2 + \dots + N^{k-1}.$$

## Remarks

### Why the hypothesis is needed

For numbers, $1/(1 - x) = 1 + x + x^2 + \cdots$ holds only when $|x| < 1$, and the series is infinite.
Nilpotency is what makes the matrix series stop.
Without it the formula can fail in two ways.
For $N = \tfrac{1}{2} I$, the inverse $(I - N)^{-1} = 2I$ exists but is the sum of an infinite series $I + \tfrac12 I + \tfrac14 I + \cdots$, and no finite sum gives it.
For $N = I$, the matrix $I - N = 0$ has no inverse at all.

### A worked use

Take $N = \begin{pmatrix} 0 & 1 & 2 \\ 0 & 0 & 3 \\ 0 & 0 & 0 \end{pmatrix}$, with $N^2 = \begin{pmatrix} 0 & 0 & 3 \\ 0 & 0 & 0 \\ 0 & 0 & 0 \end{pmatrix}$ and $N^3 = 0$.
The theorem gives
$$(I - N)^{-1} = I + N + N^2 = \begin{pmatrix} 1 & 1 & 5 \\ 0 & 1 & 3 \\ 0 & 0 & 1 \end{pmatrix}.$$
Check the first row of the product with $I - N = \begin{pmatrix} 1 & -1 & -2 \\ 0 & 1 & -3 \\ 0 & 0 & 1 \end{pmatrix}$: it is $(1, \; 1 - 1, \; 5 - 3 - 2) = (1, 0, 0)$.
The other two rows give $(0, 1, 0)$ and $(0, 0, 1)$ in the same way.
[[A nilpotent 2 × 2 matrix with no zero entries|YHCD6MTSV8]] checks the case $k = 2$, where the inverse is just $I + N$.

### What it gives you

Replacing $N$ by $-N$, which is also nilpotent, shows that $I + N$ is invertible with inverse $I - N + N^2 - \dots + (-1)^{k-1} N^{k-1}$.
So every unitriangular matrix $I + N$, with $N$ strictly upper triangular, is invertible, and its inverse is again unitriangular, since every power of $N$ is strictly upper triangular.
More generally, if $U$ is invertible, $N$ is nilpotent and $UN = NU$, then $U - N = U (I - U^{-1} N)$ is invertible, because $(U^{-1} N)^k = U^{-k} N^k = 0$.

### Generalizations

The proof uses only the ring axioms, so it works for a nilpotent element $x$ of any ring with $1$: the element $1 - x$ is a unit.
For a real or complex matrix $A$ with $\|A\| < 1$ in an operator norm, the infinite series $\sum_{j \ge 0} A^j$ converges to $(I - A)^{-1}$; this is the Neumann series, and the theorem is its finite case.

## Explanations

### L1 human

For numbers, $1 / (1 - x) = 1 + x + x^2 + \cdots$ when $x$ is small, and the sum goes on forever.
For a nilpotent matrix, the powers become zero after a few steps.
So the same sum stops, and a few terms give the exact inverse.

### L2 human

The whole proof is one identity that holds in every ring:
$$(1 - x)(1 + x + \dots + x^{k-1}) = 1 - x^k.$$
When $x^k = 0$ the right side is $1$, so the second factor is the inverse of $1 - x$.
The typical use is to invert unitriangular matrices quickly, as in the worked use above.
Watch out: the formula inverts $I - N$, not $N$, and a nilpotent $N$ itself is never invertible.
