---
tag: FEER10D15S
kind: statement
role: theorem
name: Properties of reflections and generation of the orthogonal group
aliases: [reflections-generate-the-orthogonal-group, householder-reflection-swaps-vectors-of-equal-length]
msc: ["15A04", "15B10", "51F15"]
topics: [AZS5BPF5H3]
audience: ug2
about: [06BRDF3F0E, WWK2E8BRGF]
uses: [025158VEYZ, 0717XXPWM6, 0ST8QF9T3T, 0C3CFHDN6R, 0QRBVFJ50X]
sources:
  - url: https://en.wikipedia.org/wiki/Reflection_(mathematics)
    locator: Reflection through a hyperplane in n dimensions
  - url: https://en.wikipedia.org/wiki/Householder_transformation
    locator: Properties
  - url: https://en.wikipedia.org/wiki/Orthogonal_group
    locator: Reflections
---

## Statement

A reflection is a linear isometry of determinant $-1$ that undoes itself, any two vectors of the same length are swapped by one reflection, and the reflections generate the orthogonal group.

Let $V$ be a real inner product space of finite dimension $n \ge 1$, let $u \in V$ with $u \neq 0$, and let $s_u(x) = x - 2\frac{\ip{x}{u}}{\ip{u}{u}}u$ be the [[reflection|025158VEYZ]] in $u^\perp$.

1. The map $s_u$ is linear, $s_u(x) = x$ for each $x \in u^\perp$, and $s_u(u) = -u$.
2. We have $s_u \circ s_u = \id_V$, the map $s_u$ is self-adjoint, and $s_u$ is a [[linear isometry|0717XXPWM6]].
3. We have $\det s_u = -1$.
4. For a unit vector $u \in \R^n$, the matrix of $s_u$ is $H = I_n - 2uu^{\mathsf{T}}$, and $H$ is symmetric and [[orthogonal|0QRBVFJ50X]] with $\det H = -1$.
5. If $x, y \in V$ with $\norm{x} = \norm{y}$ and $x \neq y$, then $s_{x - y}(x) = y$ and $s_{x - y}(y) = x$.
6. Each $Q \in O(n)$ is a product of at most $n$ reflections of $\R^n$, where $I_n$ is the empty product, so the reflections generate the [[orthogonal group|WWK2E8BRGF]].

## Remarks

### Why each hypothesis is needed

Part 5 needs $\norm{x} = \norm{y}$, because a reflection keeps lengths.
No reflection sends $(1, 0)$ to $(2, 0)$, and no linear isometry does either.
Part 5 also needs $x \neq y$, because the formula for $s_0$ divides by $\ip{0}{0} = 0$; when $x = y$, the identity already does the job.
The formula needs a positive definite inner product, so that $\ip{u}{u} \neq 0$ for every $u \neq 0$.
For the form $x_1 y_1 - x_2 y_2$ on $\R^2$, the vector $u = (1, 1)$ has $\ip{u}{u} = 0$, and $s_u$ is not defined.
Finite dimension is used in parts 3 and 6, where determinants and an induction on $n$ appear.

### What it gives you

Part 3 turns the number of reflections into a sign.
If $Q = s_{u_1} \cdots s_{u_k}$, then $\det Q = (-1)^k$, so an element of $SO(n)$ is a product of an even number of reflections and an element of determinant $-1$ a product of an odd number.
Part 5 is the basic step of the Householder QR method.
For example, $x = (3, 4)$ and $y = (5, 0)$ both have length $5$, so $u = x - y = (-2, 4)$ and
$$s_u(x) = (3, 4) - 2 \cdot \frac{-6 + 16}{20}(-2, 4) = (3, 4) - (-2, 4) = (5, 0).$$
The matrix of this reflection is $I - \frac{2}{20}uu^{\mathsf{T}} = \frac{1}{5}\begin{pmatrix} 3 & 4 \\ 4 & -3 \end{pmatrix}$.
Check: its determinant is $\frac{1}{25}(-9 - 16) = -1$.
Part 6 with the bound $n$ is the Euclidean case of the [[Cartan-Dieudonné theorem|0VMWGYY35Q]].

### The converse

An orthogonal map $T$ with $T^2 = \id$ and $\det T = -1$ need not be a reflection.
The map $-I_3$ has both properties, but it fixes only $0$.
The correct converse is this: an orthogonal map that fixes a hyperplane $W$ pointwise and is not the identity is the reflection in $W$.
Indeed, it maps the line $W^\perp$ to itself and keeps lengths there, so it acts on that line as $1$ or as $-1$, and $1$ would make it the identity.

### Generalizations

For a nondegenerate symmetric bilinear form $B$ over a field of characteristic not $2$, the map $x \mapsto x - 2\frac{B(x, u)}{B(u, u)}u$ with $B(u, u) \neq 0$ has the properties of parts 1 to 3, and the general Cartan-Dieudonné theorem uses these reflections.
In a complex inner product space, the same formula gives a unitary and self-adjoint map with determinant $-1$.

## Explanations

### L1 human

A reflection keeps the mirror fixed and flips the direction across it.
Two flips in the same mirror undo each other.
For two arrows of the same length from the origin, there is always a mirror that swaps them: the mirror that lies halfway between them.
With enough mirrors used one after the other, we get every rotation and every mirror image of space.

### L2 human

Here is a typical use of part 6 in the plane: write the rotation $R(\pi/2) = \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}$ as a product of reflections.
It sends $e_2$ to $-e_1$, and both have length $1$, so the reflection $s$ with normal vector $e_2 - (-e_1) = (1, 1)$ swaps them.
That reflection is the swap with a sign change, $s = \begin{pmatrix} 0 & -1 \\ -1 & 0 \end{pmatrix}$.
Then
$$sR(\pi/2) = \begin{pmatrix} 0 & -1 \\ -1 & 0 \end{pmatrix}\begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix} = \begin{pmatrix} -1 & 0 \\ 0 & 1 \end{pmatrix},$$
which is the reflection $s_{e_1}$.
So $R(\pi/2) = s \, s_{e_1}$, a product of two reflections, as the determinant $+1$ requires.
Watch out: $s_{x - y}$ swaps $x$ and $y$, but $s_{x + y}$ sends $x$ to $-y$.

### L3 human

The theorem shows that $O(n)$ is generated by a single conjugacy class, the reflections.
The determinant is then the parity of the number of reflections, and it is the homomorphism $O(n) \to \{ \pm 1 \}$ with kernel $SO(n)$.
The finite subgroups of $O(n)$ generated by reflections are the finite reflection groups, studied as [[Coxeter groups|G6FND7X69J]] in group theory.
