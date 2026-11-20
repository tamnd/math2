---
tag: VMHPYDZERM
kind: counterexample
name: A real rotation with zero quadratic form
msc: ["15A04", "47B15"]
topics: [3YM9EK6VMB]
audience: ug1
uses: [WAYMK9GR5S, 0MB8HQW495, 0ST8QF9T3T, XS5H42KEP5]
sources:
  - url: https://en.wikipedia.org/wiki/Polarization_identity
    locator: lead section
  - book: isbn:9783031410253
    locator: Chapter 7
---

## Counterexample

Let $V = \mathbb{R}^2$ with the dot product, and let $R(x, y) = (-y, x)$.
This is [[the rotation by a right angle|XS5H42KEP5]], with the matrix $\begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}$.

1. For $v = (x, y)$, we get $\ip{Rv}{v} = (-y) x + x y = 0$. So the quadratic form of $R$ is $0$ at every vector.
2. But $R(1, 0) = (0, 1) \neq 0$, so $R \neq 0$.
3. Every value $\ip{Rv}{v}$ is the real number $0$.
4. The [[adjoint|0ST8QF9T3T]] of $R$ has the transposed matrix $\begin{pmatrix} 0 & 1 \\ -1 & 0 \end{pmatrix}$, which is $-R$. So $R^* = -R \neq R$, and $R$ is not [[self-adjoint|0MB8HQW495]].

So over $\mathbb{R}$, parts 1 and 2 of [[the quadratic form statement|WAYMK9GR5S]] fail.
Part 3 fails without the hypothesis that $T$ is self-adjoint.

## Remarks

- Over $\mathbb{C}$ the same matrix does not give a counterexample. On $\mathbb{C}^2$ with the standard inner product, take $v = (1, i)$. Then $Rv = (-i, 1)$, and $\ip{Rv}{v} = (-i) \cdot \overline{1} + 1 \cdot \overline{i} = -2i \neq 0$.
- The value $-2i$ is not real, which agrees with part 2, because $R$ is not self-adjoint on $\mathbb{C}^2$.
- Every skew-symmetric real matrix $A$, with $A^T = -A$, has $x^T A x = 0$ for all real $x$. The reason: $x^T A x$ is a $1 \times 1$ matrix, so it equals its transpose $x^T A^T x = -x^T A x$.
- Over $\mathbb{R}$, the quadratic form determines only the symmetric part $\tfrac{1}{2}(A + A^T)$ of a matrix $A$. Here the symmetric part of $R$ is $0$.

## Explanations

### L1 human

A quarter turn moves every arrow in the plane to a perpendicular arrow.
The dot product of an arrow with its turned copy is therefore $0$.
So the test "is $\ip{Tv}{v}$ zero for every $v$" cannot tell the quarter turn from the zero map.
Over the real numbers this test is too weak.

### L2 human

Worked example: we check one vector by hand and then the complex case.

1. Take $v = (3, 4)$. Then $Rv = (-4, 3)$, and $Rv \cdot v = -12 + 12 = 0$.
2. The matrix of $R$ is not symmetric, because its entries $-1$ and $1$ off the diagonal differ.
3. Now let $R$ act on $\mathbb{C}^2$. For $v = (1, i)$ we get $\ip{Rv}{v} = -2i$.
4. So over $\mathbb{C}$ the quadratic form is not $0$, and part 1 of the statement is safe.

A trap: to prove $S = T$ for real operators from $\ip{Sv}{v} = \ip{Tv}{v}$, both $S$ and $T$ must be self-adjoint.

### L3 human

A real bilinear form $b$ splits into a symmetric part and an alternating part.
The quadratic form $v \mapsto b(v, v)$ sees only the symmetric part.
The rotation gives an alternating form $b(u, w) = \ip{Ru}{w}$, the area form of the plane, and so it is invisible to the quadratic form.
Over $\mathbb{C}$ there is no such loss, because a sesquilinear form is recovered from its diagonal by the complex polarization identity.
