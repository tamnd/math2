---
tag: GXDM4QPRN5
kind: example
name: Determinant of the substitution map p(x) to p(2x)
msc: [15A04, 15A15]
topics: [DTBK11SR77]
audience: ug2
instance_of: [0X0HQYSZ0K]
uses: [03F5KP94K0, 0KMN32XGPF, 0K1KKMFHYH]
sources:
  - url: https://en.wikipedia.org/wiki/Determinant
    locator: Determinant of an endomorphism
---

## Example

Let $V$ be the space of real polynomials of degree at most $2$, and let $T \colon V \to V$ be the substitution $T(p)(x) = p(2x)$.
We compute $\det T$ in two bases and get $8$ both times.

1. The map is linear, because $(p + q)(2x) = p(2x) + q(2x)$ and $(cp)(2x) = c \, p(2x)$.
   It sends a polynomial of degree at most $2$ to another one, so it is an endomorphism of $V$.
2. In the basis $1, x, x^2$ the images are $T(1) = 1$, $T(x) = 2x$ and $T(x^2) = (2x)^2 = 4x^2$.
   So the matrix is $\operatorname{diag}(1, 2, 4)$, and the [[definition|03F5KP94K0]] gives
$$\det T = 1 \cdot 2 \cdot 4 = 8.$$
3. Now take the basis $q_1 = 1$, $q_2 = 1 + x$, $q_3 = 1 + x + x^2$.
   The first image is $T(q_1) = 1 = q_1$.
4. The second image is $T(q_2) = 1 + 2x$.
   Matching the coefficient of $x$ gives $2 q_2$, and the constant left over is $1 - 2 = -1$, so $T(q_2) = -q_1 + 2 q_2$.
5. The third image is $T(q_3) = 1 + 2x + 4x^2$.
   The coefficient of $x^2$ forces $4 q_3$, which leaves $1 + 2x + 4x^2 - 4 q_3 = -3 - 2x$.
   Then $-3 - 2x = -2 q_2 - q_1$, so $T(q_3) = -q_1 - 2 q_2 + 4 q_3$.
6. The coordinates of these images are the columns of the matrix in the new basis:
$$\begin{pmatrix} 1 & -1 & -1 \\ 0 & 2 & -2 \\ 0 & 0 & 4 \end{pmatrix}.$$
7. This matrix is [[upper triangular|0K1KKMFHYH]], so its determinant is $1 \cdot 2 \cdot 4 = 8$, as the [[invariance theorem|0KMN32XGPF]] predicts.

## Remarks

The two matrices look different, but they are similar, and the determinant cannot tell them apart.
The map is invertible, with inverse $p(x) \mapsto p(x/2)$, and the rule for inverses gives $\det T^{-1} = \tfrac{1}{8}$.

Change the degree and the pattern stays.
On the polynomials of degree at most $n$, the basis $1, x, \dots, x^n$ gives the diagonal $1, 2, 4, \dots, 2^n$, so
$$\det T = 2^{0 + 1 + \dots + n} = 2^{n(n+1)/2}.$$
Change the factor $2$ to a number $c$, and the determinant becomes $c^{n(n+1)/2}$.
For $c = 0$ and $n \ge 1$ this is $0$, which fits: $p(x) \mapsto p(0)$ sends every polynomial to a constant and cannot be undone.

## Explanations

### L1 human

The map replaces $x$ by $2x$ in a polynomial.
It keeps the constant $1$, doubles $x$, and turns $x^2$ into $4x^2$.
So it stretches three independent directions by $1$, $2$ and $4$, and the determinant is $1 \cdot 2 \cdot 4 = 8$.

### L2 human

The basis of powers $1, x, x^2$ gives a diagonal matrix, which is the easiest choice for a substitution map.
The second basis gives a triangular matrix with other entries above the diagonal, but the same diagonal and so the same determinant.
Watch out: $T(x^2)$ is $(2x)^2 = 4x^2$, not $2x^2$, and the mistake would give the wrong answer $4$.
