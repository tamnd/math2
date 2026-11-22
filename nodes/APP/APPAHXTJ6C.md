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

Over a field $F$, let
$$D = \begin{pmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 2 \end{pmatrix}, \qquad N = \begin{pmatrix} 0 & 1 & 0 \\ 0 & 0 & 1 \\ 0 & 0 & 0 \end{pmatrix}.$$
We find the characteristic and the minimal polynomial of each matrix.

*The diagonal matrix $D$.*

1. By the [[determinant of a triangular matrix|0K1KKMFHYH]], $p_D(t) = \det(tI - D) = (t - 1)^2 (t - 2)$.
   Check: $\operatorname{tr} D = 4$, the principal $2 \times 2$ minors are $1 \cdot 1$, $1 \cdot 2$ and $1 \cdot 2$ with sum $5$, and $\det D = 2$, so $p_D(t) = t^3 - 4t^2 + 5t - 2$, which expands from $(t - 1)^2 (t - 2)$.
2. Multiply the two linear factors at $D$:
$$(D - I)(D - 2I) = \operatorname{diag}(0, 0, 1) \operatorname{diag}(-1, -1, 0) = \operatorname{diag}(0, 0, 0) = 0.$$
   So $(x - 1)(x - 2)$ is an [[annihilating polynomial|052M4SX57M]] of $D$.
3. Its proper monic divisors are $1$, $x - 1$ and $x - 2$.
   None of them annihilates $D$, because $I \ne 0$, $D - I = \operatorname{diag}(0, 0, 1) \ne 0$ and $D - 2I = \operatorname{diag}(-1, -1, 0) \ne 0$.
4. So the [[minimal polynomial|0V58FPM3EQ]] is $m_D(x) = (x - 1)(x - 2)$, a proper divisor of $p_D$.

*The nilpotent matrix $N$.*

5. The matrix $N$ is strictly upper triangular, so $tI - N$ is upper triangular with diagonal $t, t, t$, and $p_N(t) = t^3$.
6. Read the columns of $N$: $N e_1 = 0$, $N e_2 = e_1$ and $N e_3 = e_2$.
   So $N \ne 0$, and $N^2 e_3 = N e_2 = e_1$, so $N^2 \ne 0$.
   In fact $N^2$ has a single entry $1$, in position $(1, 3)$.
7. Each basis vector reaches $0$ after at most three steps of the chain $e_3 \mapsto e_2 \mapsto e_1 \mapsto 0$, so $N^3 = 0$.
8. The proper monic divisors of $x^3$ are $1$, $x$ and $x^2$, and none of them annihilates $N$ by step 6.
   So $m_N(x) = x^3 = p_N(x)$.

## Remarks

The two matrices sit at the two ends of what can happen.
For $D$ the minimal polynomial has degree $2 < 3$, because the repeated eigenvalue $1$ needs only one factor $x - 1$.
For $N$ the minimal polynomial has the full degree $3$, because the chain $e_3 \mapsto e_2 \mapsto e_1$ has length $3$.
In both cases $m$ and $p$ have the same roots, as the theorem that the [[eigenvalues are the roots of the minimal polynomial|0QF4ZEFG52]] says, and $m$ divides $p$, as the theorem that the [[minimal polynomial divides the characteristic polynomial|093X6MN6Y6]] says.

Change the numbers and the pattern stays.
Any diagonal matrix has as minimal polynomial the product of $x - \lambda$ over its distinct diagonal entries $\lambda$, with no repeated factor.
If you replace the entry $1$ in position $(2, 3)$ of $N$ by $0$, the chain breaks into $e_2 \mapsto e_1 \mapsto 0$ and $e_3 \mapsto 0$, so the new matrix has square zero and minimal polynomial $x^2$, while its characteristic polynomial is still $t^3$.

## Explanations

### L1 human

For a diagonal matrix, each different number on the diagonal gives one factor of the minimal polynomial.
A number that appears twice still gives only one factor.
The shift matrix $N$ moves $e_3$ to $e_2$, then $e_2$ to $e_1$, then $e_1$ to $0$.
It takes three steps to kill every vector, so the minimal polynomial is $x^3$.

### L2 human

Here is the method in general: find the characteristic polynomial, list its monic divisors that contain every eigenvalue as a root, and test them from the lowest degree up.
For $D$ the candidates are $(x - 1)(x - 2)$ and $(x - 1)^2 (x - 2)$, and the first one already works by step 2.
For $N$ the candidates are $x$, $x^2$ and $x^3$, and only the last one works.
Watch out: do not take $m_D = p_D$ just because $1$ is a double eigenvalue, since a diagonal matrix never needs a repeated factor.
