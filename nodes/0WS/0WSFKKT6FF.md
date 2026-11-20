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

The image of a [[linear map|0NRYHJPQG2]] $T \colon V \to W$ is the set of all values $T(v)$ with $v \in V$.
It is a [[subspace|00YC1D652K]] of the target $W$.
The map $T$ is surjective exactly when its image is all of $W$.

## Motivation

The equation $T(v) = w$ has a solution exactly when $w$ lies in the image of $T$.
For a linear system $Ax = b$, this says: the system is solvable exactly when $b$ is a combination of the columns of $A$.
So the image answers the existence question for linear equations, as the kernel answers the uniqueness question.

## Notation

The image is written $\im T$, $\operatorname{Im} T$, $T(V)$ or $\operatorname{ran} T$.
Some books call it the *range* $R(T)$, and others use "range" for the target $W$.
For a matrix $A$, the image of $x \mapsto Ax$ is the [[column space|03AJKXH1AV]] $\operatorname{Col} A$.

## Remarks

### Examples

- [[A matrix map of $\R^3$|RZNXVEHTCE]]: the image is the plane $c = a + b$.
- [[Differentiation on cubic polynomials|SMEX3CNE69]]: the image is the space of polynomials of degree at most $2$.
- The image of the projection $(x, y, z) \mapsto (x, y, 0)$ of $\R^3$ is the $xy$-plane.
- The image of the [[trace|0XC1RDBY7A]] $M_n(F) \to F$ is all of $F$, since $\tr(c E_{11}) = c$.

### Non-examples

- [[The image of $x \mapsto (x, x^2)$|YF3Y7THM81]] is a parabola. It is not a subspace, because the map is not linear.
- The target $W$ is not the image in general. The projection $\R^2 \to \R^2$, $(x, y) \mapsto (x, 0)$, has target $\R^2$ and image the $x$-axis.

### Basic properties

- $\im T$ is a subspace of $W$, and it is spanned by the images of any spanning set of $V$, by the [[theorem on the image|B6KFVB1H5F]].
- If $V$ is finite-dimensional, then $\dim \im T \le \dim V$. The dimension of the image is the [[rank|0ZZXSBTR4J]].
- $\im(S \circ T) \subseteq \im S$ for each linear map $S \colon W \to U$.
- $\im T \cong V / \ker T$, by the [[first isomorphism theorem|0MTBGVZ4XJ]].

### History

The solvability criterion "$b$ lies in the column space of $A$" is the content of the Rouché-Capelli theorem of the 19th century.
In different countries the theorem also carries the names of Kronecker, Frobenius and Fontené.

### Common errors

- Confusing the image, a subspace of $W$, with the kernel, a subspace of $V$.
- Taking the columns of the reduced row echelon form as a basis of the column space. Row operations change the column space, so one must take the pivot columns of $A$ itself.
- Confusing the image with the target (the codomain).

## Explanations

### L1 human

The image of a linear map is the set of all its outputs.
For a map of space that flattens everything onto a plane, the image is that plane.
The image is always a subspace: it contains $0$, and sums and multiples of outputs are again outputs.

### L2 human

To find the image of $x \mapsto Ax$, row reduce $A$ and find the pivot columns.
The matching columns of $A$ form a basis of the image.
The rank is the number of pivots, and the system $Ax = b$ is solvable exactly when $b$ lies in the image.

### L3 human

The image is the categorical image in the category of vector spaces.
The cokernel $W / \im T$ measures the failure of surjectivity, as the kernel measures the failure of injectivity.
Mathlib writes `LinearMap.range f`, a submodule of the target.
