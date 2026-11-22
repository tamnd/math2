---
tag: PGCAMM8J4T
kind: example
name: A translation is not the linear map of a matrix
msc: ["15A04"]
topics: [S6559D61BP]
audience: ug1
not_instance_of:
  - target: 06HMCTAQH3
    note: the map x ↦ x + (1, 0) sends 0 to (1, 0), so it is not linear
uses: [009892PZ30, 0RJF668P1T]
sources:
  - url: https://en.wikipedia.org/wiki/Affine_transformation
    locator: lead section
---

## Example

Sliding the plane one unit to the right is a simple motion, but no matrix describes it.
Let $f \colon \mathbb{R}^2 \to \mathbb{R}^2$ be the translation $f(x) = x + (1, 0)$, that is, $f(x, y) = (x + 1, y)$.

1. Every [[linear map|0RJF668P1T]] $T$ fixes the origin, because $T(0) = T(0 + 0) = T(0) + T(0)$, and subtracting $T(0)$ gives $T(0) = 0$.
2. The translation moves the origin, since $f(0, 0) = (1, 0) \ne (0, 0)$, so $f$ is not linear.
3. The [[linear map of a matrix|009892PZ30]] is linear for every matrix and every choice of bases, so $f$ is not the linear map of any $2 \times 2$ matrix.

A naive attempt shows what goes wrong.

4. The images of the basis vectors are $f(e_1) = (2, 0)$ and $f(e_2) = (1, 1)$, and they give the matrix $M = \begin{pmatrix} 2 & 1 \\ 0 & 1 \end{pmatrix}$.
5. Test $M$ on $(1, 1)$:
$$M \begin{pmatrix} 1 \\ 1 \end{pmatrix} = \begin{pmatrix} 3 \\ 1 \end{pmatrix}, \qquad \text{but} \qquad f(1, 1) = (2, 1).$$
So $M$ does not compute $f$, even though it agrees with $f$ on $e_1$ and $e_2$.

## Remarks

The map $f$ is affine: $f(x) = Ax + b$ with $A = I$ and $b = (1, 0)$.
Affine maps have a linear part and a shift, and only the linear part has a matrix in the sense of the dictionary.
What fails is additivity: $f(e_1) + f(e_2) = (3, 1)$, while $f(e_1 + e_2) = (2, 1)$, so the values on a basis do not determine $f$.

There is a standard way around this.
An affine map of $\mathbb{R}^n$ becomes linear on $\mathbb{R}^{n+1}$ if we write each point $(x, y)$ as $(x, y, 1)$, in homogeneous coordinates.
Here the matrix is
$$\begin{pmatrix} 1 & 0 & 1 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{pmatrix} \begin{pmatrix} x \\ y \\ 1 \end{pmatrix} = \begin{pmatrix} x + 1 \\ y \\ 1 \end{pmatrix},$$
and computer graphics uses this trick to combine rotations and translations into one product of matrices.

## Explanations

### L1 human

Sliding the whole plane moves the origin to a new place.
A matrix map always keeps the origin where it is, because a matrix times the zero vector is zero.
So no matrix can describe a slide, however you choose the numbers.

### L2 human

The test $f(0) = 0$ excludes every map with a constant term, such as $x \mapsto 2x + 3$ on $\mathbb{R}$.
Step 5 shows what happens when one builds a matrix from the images of the basis vectors anyway: the matrix and the map agree on $e_1$ and $e_2$ and disagree elsewhere.
Watch out: passing the test $f(0) = 0$ does not make a map linear, since $x \mapsto x^2$ on $\mathbb{R}$ fixes $0$ and is not linear.
