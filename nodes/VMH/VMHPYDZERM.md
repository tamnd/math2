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
We show that its quadratic form is zero, although $R$ is neither zero nor self-adjoint.

1. The quadratic form vanishes. For $v = (x, y)$ we get
$$\ip{Rv}{v} = (-y) \cdot x + x \cdot y = 0.$$
2. The operator is not zero, since $R(1, 0) = (0, 1)$.
3. Every value $\ip{Rv}{v}$ is the real number $0$, so the values are all real.
4. The operator is not [[self-adjoint|0MB8HQW495]]. The standard basis is orthonormal, so the [[adjoint|0ST8QF9T3T]] has the transposed matrix:
$$R^* = \begin{pmatrix} 0 & 1 \\ -1 & 0 \end{pmatrix} = -R \ne R.$$

So over $\mathbb{R}$, parts 1 and 2 of [[the quadratic form statement|WAYMK9GR5S]] fail, and part 3 fails without the hypothesis that $T$ is self-adjoint.

## Remarks

### What goes wrong over the reals

A quarter turn sends each vector to a perpendicular vector, so the dot product of $v$ with $Rv$ is always $0$.
The same happens for every real skew-symmetric matrix $A$, with $A^{\mathsf{T}} = -A$.
The number $x^{\mathsf{T}} A x$ is a $1 \times 1$ matrix, so it equals its own transpose:
$$x^{\mathsf{T}} A x = (x^{\mathsf{T}} A x)^{\mathsf{T}} = x^{\mathsf{T}} A^{\mathsf{T}} x = -x^{\mathsf{T}} A x,$$
and hence $x^{\mathsf{T}} A x = 0$.
In general the real quadratic form of $A$ sees only the symmetric part $\tfrac{1}{2}(A + A^{\mathsf{T}})$, and for $R$ this part is $0$.

### What changes over the complex numbers

Let the same matrix act on $\mathbb{C}^2$ with the standard inner product, and take $v = (1, i)$.
Then $Rv = (-i, 1)$, and
$$\ip{Rv}{v} = (-i) \cdot \overline{1} + 1 \cdot \overline{i} = -i - i = -2i.$$
This is not $0$, so the counterexample does not survive over $\mathbb{C}$, in line with part 1.
The value $-2i$ is also not real, which agrees with part 2, since $R$ is not self-adjoint on $\mathbb{C}^2$ either.

## Explanations

### L1 human

A quarter turn moves every arrow in the plane to a perpendicular arrow.
The dot product of an arrow with its turned copy is therefore $0$.
For example, $(3, 4)$ turns into $(-4, 3)$, and $3 \cdot (-4) + 4 \cdot 3 = 0$.
So the test "is $\ip{Tv}{v}$ zero for every $v$" cannot tell the quarter turn from the zero map, and over the real numbers this test is too weak.

### L2 human

Suppose you want to prove $S = T$ for two real operators from $\ip{Sv}{v} = \ip{Tv}{v}$ for all $v$.
The rotation shows that this step is wrong in general: take $S = R$ and $T = 0$.
The step is correct when $S$ and $T$ are both self-adjoint, because then $S - T$ is self-adjoint and part 3 applies.
It is also correct for any operators on a complex space, by part 1.
So before you compare quadratic forms over $\mathbb{R}$, check that both operators are symmetric.
