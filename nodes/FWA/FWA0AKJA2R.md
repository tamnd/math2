---
tag: FWA0AKJA2R
kind: statement
role: theorem
name: The Gram determinant is the squared volume of the parallelepiped
msc: ["15A63", "15A15", "51M25"]
topics: [1D4JTZ9VS3]
audience: ug1
about: [00SPJSDT3Z]
uses: [0HX8HZ1WTQ, A1Y41YZFB6, 0EVHJFTG9Z, 0C3CFHDN6R]
sources:
  - url: https://en.wikipedia.org/wiki/Gram_matrix
    locator: Gram determinant
  - url: https://en.wikipedia.org/wiki/Gram_matrix
    locator: Constructing an orthonormal basis
---

## Statement

The determinant of a Gram matrix is the square of the volume of the box that the vectors span, so it is never negative and it is zero exactly for dependent vectors.
Let $V$ be an [[inner product space|01EK923SKP]] over $\mathbb{K} = \mathbb{R}$ or $\mathbb{C}$, and let $v_1, \dots, v_k \in V$.
Let $G = G(v_1, \dots, v_k)$ be their [[Gram matrix|0HX8HZ1WTQ]], and let $\det$ be the [[determinant|0C3CFHDN6R]].

1. Let $v_1, \dots, v_k$ be [[linearly independent|0EVHJFTG9Z]], and let $u_1, \dots, u_k$ be the orthogonal vectors that the [[Gram-Schmidt process|A1Y41YZFB6]] makes from them, before normalization. Then
$$\det G = \norm{u_1}^2 \norm{u_2}^2 \cdots \norm{u_k}^2 > 0.$$
2. If $v_1, \dots, v_k$ are linearly dependent, then $\det G = 0$. So $\det G \ge 0$ always, with equality exactly for dependent families.
3. Define the $k$-dimensional volume of the parallelepiped spanned by an independent family as $\operatorname{vol}(v_1, \dots, v_k) = \norm{u_1} \cdots \norm{u_k}$, and as $0$ for a dependent family. Then $\det G = \operatorname{vol}(v_1, \dots, v_k)^2$.
4. Let $k = n$, let $V = \mathbb{K}^n$ with the standard inner product, and let $A$ be the matrix with the columns $v_1, \dots, v_n$. Then $\det G = \abs{\det A}^2$, so $\operatorname{vol}(v_1, \dots, v_n) = \abs{\det A}$.

The [[proof|PPBYQY70BR]] factors $G$ through the Gram-Schmidt process.

## Remarks

### Why each hypothesis is needed

Part 1 needs independence, because otherwise some $u_j$ is $0$ and the product is $0$, not positive.
For $(1, 2)$ and $(2, 4)$ the process gives $u_1 = (1, 2)$ and $u_2 = (2, 4) - 2 (1, 2) = 0$, and part 2 covers this case with $\det G = 5 \cdot 20 - 10^2 = 0$.

Positive definiteness of the inner product is what makes the sign right.
For the [[Minkowski form|TFGECQ5C32]] $\beta(x, y) = x_1 y_1 - x_2 y_2$, the table of values on the independent pair $(1, 0)$, $(0, 1)$ is $\operatorname{diag}(1, -1)$, with determinant $-1$, which is the square of no real volume.

Part 4 needs $k = n$, since $\det A$ exists only for a square matrix.
For $k < n$ part 3 still gives the volume, and that is the main reason to use the Gram determinant at all.

### What it gives you

For two vectors the theorem reads
$$\det G(x, y) = \norm{x}^2 \norm{y}^2 - \abs{\ip{x}{y}}^2 \ge 0,$$
which is the [[Cauchy-Schwarz inequality|0RFWW56Y22]] together with its equality case.
In $\mathbb{R}^3$ the same number is $\norm{x \times y}^2$, the squared area of the parallelogram, as the [[example with two vectors in $\mathbb{R}^3$|QG8VQCE4QC]] checks.

Each $\norm{u_j}$ is at most $\norm{v_j}$, because $v_j$ is $u_j$ plus a vector orthogonal to it.
So $\det G \le \norm{v_1}^2 \cdots \norm{v_k}^2$, which is [[Hadamard's inequality|CGDN1X32NQ]], with equality for an orthogonal family of nonzero vectors.

The volume does not depend on the order of the vectors.
Reordering replaces $G$ by $P^{\mathsf{T}} G P$ for a permutation matrix $P$, and $\det P = \pm 1$.

A complex check of part 4: for $v_1 = (1, i)$ and $v_2 = (i, 1)$ in $\mathbb{C}^2$, the inner product $\ip{v_1}{v_2} = 1 \cdot \overline{i} + i \cdot \overline{1} = 0$, so $G = \operatorname{diag}(2, 2)$ and $\det G = 4$.
The matrix $A$ with these columns has $\det A = 1 - i^2 = 2$, and $\abs{2}^2 = 4$.

### The converse

The converse of part 2 is part 1: $\det G = 0$ happens only for dependent families.
Part 4 cannot be reversed to recover $\det A$ from $G$, because the sign is lost.
The columns of $A$ and of $A$ with two columns swapped have the same volume but determinants of opposite sign, so orientation is extra information that the Gram matrix does not hold.

### Generalizations

Each $\norm{u_j}$ is the distance from $v_j$ to the span of $v_1, \dots, v_{j-1}$, so part 3 is the rule "base times height", applied $k - 1$ times.
Over $\mathbb{R}$ with $k = n$, part 4 agrees with the [[determinant as a volume scaling factor|RC5BTSG8T2]], which measures volume with Lebesgue measure.
For $k < n$ real vectors, the [[Cauchy-Binet formula|08WE2W7DYS]] writes $\det(A^{\mathsf{T}} A)$ as the sum of the squares of the $k \times k$ minors of $A$, so the squared $k$-volume is the sum of the squared volumes of its shadows on the coordinate $k$-planes.

## Explanations

### L1 human

The determinant of the Gram matrix measures how much room the vectors fill.
For two arrows it is the square of the area of their parallelogram, and for three arrows it is the square of the volume of their slanted box.
For $(1, 0)$ and $(1, 1)$ the table is $\begin{pmatrix} 1 & 1 \\ 1 & 2 \end{pmatrix}$, its determinant is $1$, and the parallelogram has area $1$.
When the arrows lie flat, in a line or in a plane, the box has no volume and the determinant is zero.

### L2 human

Here is a typical computation, done in three ways: take $v_1 = (1, 1, 0)$, $v_2 = (0, 1, 1)$ and $v_3 = (1, 0, 1)$ in $\mathbb{R}^3$.
Each vector has squared length $2$ and each pair has dot product $1$, so expansion along the first row gives
$$\det G = \det \begin{pmatrix} 2 & 1 & 1 \\ 1 & 2 & 1 \\ 1 & 1 & 2 \end{pmatrix} = 2(4 - 1) - 1(2 - 1) + 1(1 - 2) = 4.$$
The Gram-Schmidt process gives $u_1 = (1, 1, 0)$, then $u_2 = v_2 - \frac12 u_1 = (-\frac12, \frac12, 1)$, then
$$u_3 = v_3 - \tfrac12 u_1 - \tfrac13 u_2 = (\tfrac23, -\tfrac23, \tfrac23).$$
Check: $u_3 \cdot u_1 = \frac23 - \frac23 = 0$ and $u_3 \cdot u_2 = -\frac13 - \frac13 + \frac23 = 0$.
The squared lengths are $2$, $\frac32$ and $\frac43$, and their product is $2 \cdot \frac32 \cdot \frac43 = 4$.
The matrix $A$ with the columns $v_j$ has $\det A = 1(1 - 0) - 0 + 1(1 - 0) = 2$, and $2^2 = 4$.
So the box has volume $2$, and all three routes agree.
Watch out: $\det G$ is the squared volume, so the volume is $\sqrt{4} = 2$, not $4$.

### L3 human

The theorem defines $k$-dimensional volume inside a space of any dimension using only the inner product.
This is how surface area is computed: a parametrized surface with Jacobian matrix $J$ has the area element $\sqrt{\det(J^{\mathsf{T}} J)}$, which is the square root of a Gram determinant of two tangent vectors.
In Riemannian geometry the metric $g$ is a Gram matrix at each point, and $\sqrt{\det g}$ is the density of the volume form.
In exterior algebra the same number is $\norm{v_1 \wedge \dots \wedge v_k}^2$ for the induced inner product on $\Lambda^k V$.
