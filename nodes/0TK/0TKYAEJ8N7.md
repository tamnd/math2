---
tag: 0TKYAEJ8N7
kind: object
name: Orthogonal group
msc: [15B10, 20G20]
topics: [AZS5BPF5H3]
audience: ug2
instance_of: [G5S1M9]
uses: [0QRBVFJ50X]
sources:
  - url: https://en.wikipedia.org/wiki/Orthogonal_group
    locator: lead section
same_as:
  wikidata: Q1783179
  wikipedia: Orthogonal group
---

## Description

The orthogonal group is the group of all linear maps of $\mathbb{R}^n$ that keep lengths: the rotations and reflections that fix the origin, and their products.
It is the symmetry group of Euclidean space with a fixed point, and every symmetry group of a figure centered at $0$ lies inside it.

Let $n \ge 1$.
The *orthogonal group* is the set of real $n \times n$ [[orthogonal matrices|0W02QESPJQ]],
$$O(n) = \{ Q \in M_n(\mathbb{R}) : Q^{\mathsf{T}} Q = I_n \},$$
with matrix multiplication as the operation.
We check that it is a [[group|G5S1M9]], and in fact a [[subgroup|0X1JXT47GA]] of the [[general linear group|0FCHE902D7]] $GL_n(\mathbb{R})$.

1. Each $Q \in O(n)$ is invertible with $Q^{-1} = Q^{\mathsf{T}}$, because $Q^{\mathsf{T}} Q = I_n$ and a one-sided inverse of a square matrix is two-sided.
2. The identity is in $O(n)$, because $I_n^{\mathsf{T}} I_n = I_n$.
3. For $P, Q \in O(n)$ the product is in $O(n)$, because $(PQ)^{\mathsf{T}} (PQ) = Q^{\mathsf{T}} (P^{\mathsf{T}} P) Q = Q^{\mathsf{T}} Q = I_n$.
4. For $Q \in O(n)$ the inverse is in $O(n)$, because $(Q^{\mathsf{T}})^{\mathsf{T}} Q^{\mathsf{T}} = Q Q^{\mathsf{T}} = I_n$ by step 1.

So $O(n)$ is a subgroup of $GL_n(\mathbb{R})$, and its elements are exactly the matrices of the [[linear isometries|07SJXTWVQW]] of $\mathbb{R}^n$ with the dot product.

## Remarks

### The smallest cases

For $n = 1$, a $1 \times 1$ matrix $(a)$ is orthogonal when $a^2 = 1$, so $O(1) = \{1, -1\}$, the [[orthogonal group of degree one|D9VHRJRMAS]].
For $n = 2$ there are two families.
The rotations $R(\theta)$ turn the plane by the angle $\theta$, and the reflections
$$S_\varphi = \begin{pmatrix} \cos\varphi & \sin\varphi \\ \sin\varphi & -\cos\varphi \end{pmatrix}$$
mirror it in the line through $0$ at the angle $\varphi / 2$.
Check for $S_\varphi$: its columns have length $\cos^2\varphi + \sin^2\varphi = 1$, their dot product is $\cos\varphi \sin\varphi - \sin\varphi \cos\varphi = 0$, and its determinant is $-\cos^2\varphi - \sin^2\varphi = -1$.
The [[classification of O(2)|C97Z06HHB2]] shows that there is nothing else.

### A matrix to test

Is the following matrix in $O(3)$?
$$Q = \frac{1}{3} \begin{pmatrix} 2 & -1 & 2 \\ 2 & 2 & -1 \\ -1 & 2 & 2 \end{pmatrix}$$
Each column has squared length $\tfrac{1}{9}(4 + 4 + 1) = 1$.
The dot products of the columns are $\tfrac{1}{9}(-2 + 4 - 2)$, $\tfrac{1}{9}(4 - 2 - 2)$ and $\tfrac{1}{9}(-2 - 2 + 4)$, and all three are $0$.
So $Q^{\mathsf{T}} Q = I_3$ and $Q \in O(3)$.
By the [[rule of Sarrus|0H8SZFFDXJ]] the integer matrix has determinant $15 - (-12) = 27$, so $\det Q = 27 / 27 = 1$, and $Q$ is a rotation.

### Why it keeps lengths and angles

For $Q \in O(n)$ and $x, y \in \mathbb{R}^n$, the dot product does not change:
$$(Qx) \cdot (Qy) = (Qx)^{\mathsf{T}} (Qy) = x^{\mathsf{T}} Q^{\mathsf{T}} Q y = x^{\mathsf{T}} y = x \cdot y.$$
With $y = x$ this says $\lVert Qx \rVert = \lVert x \rVert$, so lengths are kept, and then angles are kept too.
The converse also holds: a linear map that keeps all lengths keeps all dot products, by [[the polarization argument|0R7VXTYHYZ]], so its matrix is orthogonal.

### Two components

Every element of $O(n)$ has [[determinant 1 or -1|QDZJMFATRW]], because $(\det Q)^2 = \det(Q^{\mathsf{T}} Q) = 1$.
The map $\det \colon O(n) \to \{1, -1\}$ is a surjective [[homomorphism|0JYTG5K9Y4]], since $\operatorname{diag}(-1, 1, \dots, 1)$ has determinant $-1$.
Its kernel is the [[special orthogonal group|0CGYNDCWRR]] $SO(n)$, and the other coset is the set of orthogonal matrices with determinant $-1$.

These two cosets are the two connected components of $O(n)$.
The determinant is continuous and takes only the values $1$ and $-1$, so no path in $O(n)$ goes from one coset to the other.
Each coset is connected, because $SO(n)$ is connected and the second coset is its image under multiplication by $\operatorname{diag}(-1, 1, \dots, 1)$.

### Size and shape

The group $O(n)$ is compact.
It is closed in $M_n(\mathbb{R})$, because it is the solution set of the polynomial equations $Q^{\mathsf{T}} Q = I_n$, and it is bounded, because each column is a unit vector and so every entry lies in $[-1, 1]$.
Its dimension is $\tfrac{n(n-1)}{2}$.
The $n^2$ entries are tied by the equations $Q^{\mathsf{T}} Q = I_n$, and since $Q^{\mathsf{T}} Q$ is symmetric there are $\tfrac{n(n+1)}{2}$ of them, which leaves $n^2 - \tfrac{n(n+1)}{2} = \tfrac{n(n-1)}{2}$ free parameters.
For $n = 2$ this is $1$, the angle, and for $n = 3$ it is $3$, an axis and an angle.

### What it is not

The matrix $2 I_2$ has orthogonal columns, but $(2 I_2)^{\mathsf{T}} (2 I_2) = 4 I_2$, so it is not in $O(2)$; the [[matrix with orthogonal columns that is not orthogonal|B5SD0BTPZG]] shows the same failure.
The [[matrices with determinant 1 or -1|R304WJSMWX]] form a larger group, which contains the shear $\begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}$, and the shear sends $(0, 1)$ to $(1, 1)$, of length $\sqrt{2}$.
A translation $x \mapsto x + b$ with $b \ne 0$ keeps distances but moves $0$, so it is not linear and not in $O(n)$.

### Watch out

The test $Q^{\mathsf{T}} Q = I$ is enough only for square matrices.
The $3 \times 2$ matrix $Q$ with the columns $e_1$ and $e_2$ has $Q^{\mathsf{T}} Q = I_2$, but $Q Q^{\mathsf{T}} = \operatorname{diag}(1, 1, 0) \ne I_3$, and it lies in no orthogonal group.
Some books say "orthogonal transformation" only for rotations, so check which meaning a text uses.

### Try it

First, is $\begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$ in $O(2)$, and which component is it in?
Its columns are $e_2$ and $e_1$, so it is orthogonal, and its determinant is $-1$, so it is the reflection in the line $y = x$.

Second, for which numbers $a$ and $b$ is $\begin{pmatrix} a & b \\ -b & a \end{pmatrix}$ in $O(2)$?
The columns are always orthogonal, and they are unit vectors when $a^2 + b^2 = 1$.

## Explanations

### L1 human

Imagine a picture pinned to a table at one point.
You may turn the picture about the pin, or flip it over along a line through the pin, and lengths in the picture never change.
Every such move is an element of the orthogonal group of the plane.
Doing two moves in a row gives another move, and every move can be undone, so the moves form a group.
A flip followed by a flip is a turn, which is why the group has two kinds of elements.

### L2 human

Here is a typical problem: show that the product of two reflections of the plane is a rotation, and find its angle.
Multiply $S_\varphi$ by $S_\psi$ and use the addition formulas for cosine and sine:
$$S_\varphi S_\psi = \begin{pmatrix} \cos\varphi \cos\psi + \sin\varphi \sin\psi & \cos\varphi \sin\psi - \sin\varphi \cos\psi \\ \sin\varphi \cos\psi - \cos\varphi \sin\psi & \sin\varphi \sin\psi + \cos\varphi \cos\psi \end{pmatrix} = R(\varphi - \psi).$$
Check with $\varphi = \psi$: the result is $R(0) = I_2$, as it must be, since a reflection undoes itself.
The determinants agree as well: $(-1)(-1) = 1$, so the product is in $SO(2)$.
The mirror lines are at the angles $\varphi / 2$ and $\psi / 2$, so the rotation angle is twice the angle between them, the rule of [[two reflections of the plane|SRN03D73AJ]].
This is the typical use of the group: questions about doing one motion after another become products of matrices.

### L3 human

The group $O(n)$ is a compact [[Lie group|7JBRGCVJRB]] of dimension $\tfrac{n(n-1)}{2}$, and its Lie algebra is the space of real skew-symmetric matrices; the area on Lie groups studies this structure.
For a nondegenerate symmetric bilinear form $B$ on a vector space over any field, the maps that keep $B$ form the orthogonal group $O(B)$, and $O(n)$ is the case of the dot product on $\mathbb{R}^n$.
The [[Cartan-Dieudonné theorem|0VMWGYY35Q]] writes each element of $O(n)$ as a product of at most $n$ reflections.
Mathlib writes `Matrix.orthogonalGroup (Fin n) ℝ` for this group.
