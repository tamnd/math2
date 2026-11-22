---
tag: 0VMWGYY35Q
kind: statement
role: theorem
name: Cartan-Dieudonné theorem
aliases: [cartan-dieudonne-theorem, isometries-are-products-of-reflections]
msc: ["51F15", "15B10"]
topics: [AZS5BPF5H3]
audience: grad
about: [WWK2E8BRGF, 06BRDF3F0E]
uses: [025158VEYZ, 0QRBVFJ50X, 0717XXPWM6, 06BRDF3F0E]
sources:
  - url: https://en.wikipedia.org/wiki/Cartan–Dieudonné_theorem
    locator: Formal statement
  - url: https://en.wikipedia.org/wiki/Orthogonal_group
    locator: Reflections
same_as:
  wikidata: Q2540738
  wikipedia: Cartan–Dieudonné theorem
inventory: [J2J2K35KSR]
---

## Statement

Every linear isometry of an $n$-dimensional space is a chain of at most $n$ mirror reflections.

1. (Euclidean case.) Let $V$ be a real inner product space of finite dimension $n$. Then each [[linear isometry|0717XXPWM6]] $T \colon V \to V$ is a composition of at most $n$ [[reflections|06BRDF3F0E]] in hyperplanes of $V$.
2. (Matrix form.) Each $Q \in O(n)$ is a product of at most $n$ matrices $I_n - 2uu^{\mathsf{T}}$ with $u \in \R^n$ a unit vector.
3. (General case.) Let $V$ be a vector space of finite dimension $n$ over a field of characteristic not $2$, with a nondegenerate symmetric bilinear form $B$. Then each element of the orthogonal group $O(V, B)$ is a composition of at most $n$ reflections $x \mapsto x - 2\frac{B(x, u)}{B(u, u)}u$ with $B(u, u) \neq 0$.

The identity is the composition of zero reflections.
[[The proof by induction|AYYJXYNT01]] proves parts 1 and 2.
Part 3 needs a longer argument, because a vector $u \neq 0$ can have $B(u, u) = 0$.

## Remarks

### A product of three reflections

Take $T = \begin{pmatrix} 0 & 0 & -1 \\ -1 & 0 & 0 \\ 0 & -1 & 0 \end{pmatrix}$, as in [[the example of three reflections|YXTM3P2YV8]].
It sends $e_1$ to $-e_2$, a vector of the same length, so the reflection $s_{(1, 1, 0)}$ in the normal vector $e_1 - (-e_2)$ swaps them.
Multiplying gives
$$s_{(1, 1, 0)}T = \begin{pmatrix} 0 & -1 & 0 \\ -1 & 0 & 0 \\ 0 & 0 & 1 \end{pmatrix}\begin{pmatrix} 0 & 0 & -1 \\ -1 & 0 & 0 \\ 0 & -1 & 0 \end{pmatrix} = \begin{pmatrix} 1 & 0 & 0 \\ 0 & 0 & 1 \\ 0 & -1 & 0 \end{pmatrix} = S.$$
Now $S$ fixes $e_1$ and sends $e_2$ to $-e_3$, so the reflection $s_{(0, 1, 1)}$ swaps $e_2$ and $-e_3$, and $s_{(0, 1, 1)}S = \operatorname{diag}(1, 1, -1) = s_{(0, 0, 1)}$.
So $T = s_{(1, 1, 0)}s_{(0, 1, 1)}s_{(0, 0, 1)}$, three reflections in $\R^3$.
Check: $\det T = (-1)^3 = -1$, and indeed $T$ is $-1$ times a cyclic permutation matrix, whose determinant is $1$.

### Why each hypothesis is needed

The bound $n$ cannot be lowered.
A product of $k$ reflections fixes each vector of the intersection of $k$ hyperplanes, a subspace of dimension at least $n - k$.
The map $-\id$ fixes only $0$, so it needs at least $n$ reflections.

Finite dimension is needed.
On the space $\ell^2$ of square-summable sequences, the right shift keeps norms but is not surjective, while every finite product of reflections is invertible.

Part 3 needs characteristic not $2$.
In characteristic $2$ the coefficient $2$ is $0$, so the formula for a reflection gives only the identity map.
The statement then fails, since the swap of coordinates keeps the form $x_1y_1 + x_2y_2$ on $\mathbb{F}_2^2$ and is not the identity.
Part 3 also needs the reflections to use vectors with $B(u, u) \neq 0$, since otherwise the formula divides by zero.

### What it gives you

Each element of [[SO(n)|6WBVP2PB1Y]] is a product of an even number of reflections, at most $n$, because each reflection has determinant $-1$.
So each rotation of $\R^3$ is a product of two reflections, in two planes that contain its axis, and an element of $O(3)$ with determinant $-1$ is a product of one or three reflections.
In the plane, the rotation $R(\theta)$ is the product of two reflections in lines through $0$ at the angle $\theta / 2$ to each other, as [[the composition of two plane reflections|SRN03D73AJ]] shows.
A property that holds for each reflection and is kept under products therefore holds for every orthogonal map.

### The converse

Each composition of reflections is a linear isometry, because each reflection is one by [[the reflection theorem|FEER10D15S]].
So the linear isometries of $V$ are exactly the compositions of at most $n$ reflections.

### Generalizations

Part 3 applies to the [[indefinite orthogonal groups|M2900DMEW6]] over $\R$, for example to the Lorentz group, with reflections in vectors $u$ with $B(u, u) \neq 0$.
For the unitary group there is a simpler analogue.
Each element of $U(n)$ is a product of at most $n$ complex reflections $x \mapsto x - (1 - \lambda)\frac{\ip{x}{u}}{\ip{u}{u}}u$ with $\abs{\lambda} = 1$.
The proof takes an orthonormal basis of eigenvectors $u_1, \dots, u_n$ with eigenvalues $\lambda_1, \dots, \lambda_n$, and uses one such map for each $u_j$.

## History

The theorem is named after Élie Cartan and Jean Dieudonné.

## Explanations

### L1 human

A mirror flips space across a flat wall through the origin.
Every motion that keeps lengths and keeps the origin fixed is a chain of such flips.
In a space of dimension $n$, at most $n$ flips are needed.
In the plane, a quarter turn is two flips, in two mirrors that meet at half of a right angle.

### L2 human

Here is a typical use: write the half turn $-I_2$ of the plane as reflections.
The fixed space of $-I_2$ is $\{ 0 \}$, of dimension $0$, so it needs $2 - 0 = 2$ reflections.
Take the two coordinate mirrors:
$$s_{e_1}s_{e_2} = \begin{pmatrix} -1 & 0 \\ 0 & 1 \end{pmatrix}\begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix} = \begin{pmatrix} -1 & 0 \\ 0 & -1 \end{pmatrix}.$$
The two mirrors, the $y$-axis and the $x$-axis, meet at the angle $\frac{\pi}{2}$, which is half of the angle $\pi$ of the half turn.
Watch out: the reflections in a decomposition are not unique, since any two perpendicular lines would do here, but the parity of their number is fixed by $\det T$.

### L3 human

The theorem says that $O(V, B)$ is generated by involutions whose fixed spaces are hyperplanes.
The least number of reflections needed for $T$ is the reflection length of $T$.
In the Euclidean case, the reflection length of $T$ is the codimension of the fixed space $\ker(T - \id)$, and the half turn above shows a case with codimension $2$.
The finite subgroups of $O(n)$ generated by reflections are the [[Coxeter groups|G6FND7X69J]] of group theory.
