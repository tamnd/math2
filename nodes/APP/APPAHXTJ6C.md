---
tag: APPAHXTJ6C
kind: example
name: Minimal polynomials of a diagonal and a nilpotent matrix
msc: ["15A18"]
topics: [6R1D6QPY3S]
audience: ug2
instance_of: [03NDVCSHSB, 0PBN8VEKY8]
illustrates: [0QF4ZEFG52, 093X6MN6Y6]
uses: [0V58FPM3EQ, 052M4SX57M, 039HF58KQ5, 0K1KKMFHYH]
sources:
  - url: https://en.wikipedia.org/wiki/Minimal_polynomial_(linear_algebra)
    locator: Example
  - book: isbn:9780134860244
---

## Example

Let $D = \operatorname{diag}(1, 1, 2)$ and $N = \begin{pmatrix} 0 & 1 & 0 \\ 0 & 0 & 1 \\ 0 & 0 & 0 \end{pmatrix}$ over a field $F$.

1. By the [[determinant of a triangular matrix|0K1KKMFHYH]], $p_D(t) = (t - 1)^2(t - 2)$. Second method: $\tr D = 4$, the principal $2 \times 2$ minors are $1, 2, 2$ with sum $5$, and $\det D = 2$. This gives $t^3 - 4t^2 + 5t - 2 = (t - 1)^2(t - 2)$.
2. $(D - I)(D - 2I) = \operatorname{diag}(0, 0, 1)\operatorname{diag}(-1, -1, 0) = 0$.
3. The proper monic divisors of $(x - 1)(x - 2)$ are $1$, $x - 1$ and $x - 2$. None annihilates $D$, because $D - I = \operatorname{diag}(0, 0, 1) \ne 0$ and $D - 2I = \operatorname{diag}(-1, -1, 0) \ne 0$.
4. So the [[minimal polynomial|0V58FPM3EQ]] is $m_D(x) = (x - 1)(x - 2)$, a proper divisor of $p_D$.
5. $N$ is strictly upper triangular, so $p_N(t) = t^3$. Second method: $\tr N = 0$, every principal $2 \times 2$ minor is $0$, and $\det N = 0$.
6. $N e_1 = 0$, $N e_2 = e_1$ and $N e_3 = e_2$. So $N^2 e_3 = e_1$, and $N^2$ is the matrix with a single $1$ in position $(1, 3)$. In particular $N^2 \ne 0$.
7. $N^3 = N \cdot N^2 = 0$, because $N e_1 = 0$.
8. The proper monic divisors of $x^3$ are $1$, $x$ and $x^2$. None annihilates $N$, since $N \ne 0$ and $N^2 \ne 0$. So $m_N(x) = x^3 = p_N(x)$.

## Remarks

- For a diagonal matrix, the minimal polynomial is the product of $x - \lambda$ over the distinct diagonal entries $\lambda$.
- For both matrices, $m$ and $p$ have the same roots, as the theorem that the [[eigenvalues are the roots of the minimal polynomial|0QF4ZEFG52]] requires.
- The two matrices are at opposite ends: $\deg m_D = 2 < 3$, and $\deg m_N = 3$.

## Explanations

### L1 human

For a diagonal matrix, each distinct diagonal entry gives one factor of the minimal polynomial.
A repeated entry does not give a repeated factor.
For the shift matrix $N$, the powers $N$ and $N^2$ are not zero, and $N^3 = 0$.

### L2 human

The typical use is to find $m$ by testing the divisors of $p$ in order of degree.
A trap is to take the minimal polynomial of $D$ to be $p_D$ because $1$ is a double eigenvalue.
