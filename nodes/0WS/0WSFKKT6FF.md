---
tag: 0WSFKKT6FF
kind: concept
name: Image of a linear map
aliases: [range-of-a-linear-map]
msc: ["15A04"]
topics: [9080WQTZ3M]
audience: ug1
specializes: [00YC1D652K]
uses: [0NRYHJPQG2, 00YC1D652K]
sources:
  - url: https://en.wikipedia.org/wiki/Image_(mathematics)
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Linear_map
    locator: Kernel, image and the rank–nullity theorem
  - book: isbn:9780134860244
    locator: Section 2.1
---

## Summary

The image of a linear map is the set of all its outputs, and it tells you which equations $T(v) = w$ can be solved.
For a [[linear map|0NRYHJPQG2]] $T \colon V \to W$ it is
$$\im T = \{T(v) : v \in V\},$$
and the [[formal definition|0JB228DCWB]] states it.
The image is a [[subspace|00YC1D652K]] of the target $W$, and $T$ is surjective exactly when $\im T = W$.

## Motivation

The equation $T(v) = w$ has a solution exactly when $w$ lies in the image of $T$.
For a linear system $Ax = b$ this says that the system is solvable exactly when $b$ is a combination of the columns of $A$.
So the image answers the question of existence for linear equations, while the [[kernel|0S23E6YE83]] answers the question of uniqueness.

The image also measures how much a map keeps.
A map that flattens space onto a plane has a two-dimensional image, and its dimension is the [[rank|0ZZXSBTR4J]], one of the main numbers of the area.
Later sub-areas return to it as the [[column space|03AJKXH1AV]] of a matrix and in the four fundamental subspaces.

## Notation

The image is written $\im T$, $\operatorname{Im} T$, $T(V)$ or $\operatorname{ran} T$.
Some books call it the *range* $R(T)$, and others use "range" for the target $W$, so check the book's convention.
For a matrix $A$, the image of $x \mapsto Ax$ is the column space $\operatorname{Col} A$.
Mathlib writes `LinearMap.range f`, a submodule of the target.

## Remarks

### A first computation

Let $T \colon \R^2 \to \R^3$ be $T(x, y) = (x, \; y, \; x + y)$.
Every input is $x e_1 + y e_2$, so every output is a combination of
$$T(e_1) = (1, 0, 1) \quad \text{and} \quad T(e_2) = (0, 1, 1).$$
These two vectors are independent, so $\im T$ is the plane they span.
Its equation is $c = a + b$, which each output $(x, y, x + y)$ satisfies.
So $(2, 3, 5)$ is an output, namely $T(2, 3)$, and $(1, 1, 0)$ is not.

### More examples

For [[a matrix map of R³|RZNXVEHTCE]] the image is again the plane $c = a + b$, found from the columns of the matrix.
For [[differentiation on cubic polynomials|SMEX3CNE69]] the image is the space of polynomials of degree at most $2$.
The projection $(x, y, z) \mapsto (x, y, 0)$ of $\R^3$ has the $xy$-plane as image.
The [[trace|0XC1RDBY7A]] $M_n(F) \to F$ has all of $F$ as image, since $\tr(c E_{11}) = c$ for every $c$.

### What it is not

The set of values of the non-linear map $x \mapsto (x, x^2)$ is a parabola, and [[a parabola is not a subspace|YF3Y7THM81]], so it is not the image of any linear map.
The image is also not the target in general.
The projection $(x, y) \mapsto (x, 0)$ of $\R^2$ has target $\R^2$, but its image is only the $x$-axis.

### The rules you can use

The image is a subspace of $W$, and it is spanned by the images of any spanning set of $V$, by the [[theorem on the image|B6KFVB1H5F]].
So if $V$ is finite-dimensional, then $\dim \im T \le \dim V$, and a linear map $\R^2 \to \R^3$ is never surjective.
For a second linear map $S \colon W \to U$, we have $\im(S \circ T) \subseteq \im S$, because $S(T(v))$ is a value of $S$.
Finally, $\im T \cong V / \ker T$, by the [[first isomorphism theorem|0MTBGVZ4XJ]].

### Watch out

The image lives in the target $W$, while the kernel lives in the source $V$.
For a matrix, row reduction finds the pivot positions, but the basis of the image is the pivot columns of $A$ itself.
For $A = \begin{pmatrix} 1 & 2 \\ 2 & 4 \end{pmatrix}$ the reduced form has first column $(1, 0)$, while the image is the line spanned by $(1, 2)$; the vector $(1, 0)$ is not in it.

### History

The criterion "$Ax = b$ is solvable exactly when $b$ lies in the column space of $A$" is usually stated with ranks, as the [[Rouché-Capelli theorem|0HV1SKWPMS]].
In different countries the theorem also carries the names of Kronecker, Frobenius and Fontené.

### Try it

First, find the image of $T(x, y) = (x + y, \; 2x + 2y)$ on $\R^2$.
Every value is $(x + y)(1, 2)$, so the image is the line spanned by $(1, 2)$.

Second, is $(1, 0, 0)$ in the image of $T(x, y) = (x, y, x + y)$?
No: it would need $x = 1$, $y = 0$ and $x + y = 0$, and these conditions contradict each other.

## Explanations

### L1 human

The image of a linear map is the set of all its outputs.
For a map of space that flattens everything onto a plane, the image is that plane.
The image is always a subspace: it contains $0$, and sums and multiples of outputs are again outputs.
For example, if $(1, 0, 1)$ and $(0, 1, 1)$ are outputs, so is their sum $(1, 1, 2)$.

### L2 human

Here is the standard method for $A = \begin{pmatrix} 1 & 2 & 0 \\ 2 & 4 & 1 \\ 3 & 6 & 1 \end{pmatrix}$.
Subtract $2$ times row $1$ from row $2$ and $3$ times row $1$ from row $3$, then subtract the new row $2$ from row $3$:
$$\begin{pmatrix} 1 & 2 & 0 \\ 0 & 0 & 1 \\ 0 & 0 & 0 \end{pmatrix}.$$
The pivots are in columns $1$ and $3$, so columns $1$ and $3$ of $A$, namely $(1, 2, 3)$ and $(0, 1, 1)$, form a basis of the image.
Check: column $2$ of $A$ is $(2, 4, 6) = 2 \cdot (1, 2, 3)$, so it adds nothing new.
The rank is $2$, the number of pivots, and $Ax = b$ is solvable exactly when $b$ lies in this plane.
Watch out: the columns of the reduced matrix, such as $(0, 1, 0)$, need not lie in the image at all.

### L3 human

The image is the categorical image in the category of vector spaces: the smallest subspace through which $T$ factors.
The cokernel $W / \im T$ measures the failure of surjectivity, in the same way that the kernel measures the failure of injectivity.
For a module homomorphism over a ring the image is a submodule, with the same proof.
In the sub-area on matrices of linear maps the image becomes the column space, one of the four fundamental subspaces of a matrix.
