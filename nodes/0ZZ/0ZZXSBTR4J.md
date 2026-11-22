---
tag: 0ZZXSBTR4J
kind: concept
name: Rank of a linear map
msc: ["15A03", "15A04"]
topics: [9080WQTZ3M]
audience: ug1
uses: [0WSFKKT6FF, 03GSZ8RTZJ]
sources:
  - url: https://en.wikipedia.org/wiki/Rank_(linear_algebra)
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Linear_map
    locator: Kernel, image and the rank–nullity theorem
  - book: isbn:9780134860244
    locator: Section 2.1
  - url: https://en.wikipedia.org/wiki/Sylvester_domain
    locator: lead section
inventory: [J89PWVW5GR]
---

## Summary

The rank of a linear map counts the independent directions that survive the map.
For a [[linear map|0NRYHJPQG2]] $T \colon V \to W$ it is the [[dimension|03GSZ8RTZJ]] of the [[image|0WSFKKT6FF]],
$$\rank T = \dim \im T,$$
and the [[formal definition|0JGB7A6GTS]] states it.
In finite dimension it equals the rank of any matrix of $T$.

## Motivation

Two maps can have the same source and target and still lose very different amounts of information.
A map of space onto a plane keeps two directions, a map onto a line keeps one, and the zero map keeps none.
The rank is the number that records this.

For a linear system $Ax = b$, the rank tells how many of the equations are really independent.
Together with the [[nullity|0APCFW7639]], it splits the dimension of the source into the part that is kept and the part that is lost, by the [[rank-nullity theorem|0W4FSW1TVB]].

## Notation

The rank is written $\rank T$, $\operatorname{rk} T$ or $r(T)$.
For a matrix $A$, the rank of $x \mapsto Ax$ is the [[rank of the matrix|0ZC9YTXZRY]], written $\rank A$.
Mathlib writes `LinearMap.rank f`, and `Module.finrank` of the range in finite dimension.

## Remarks

### Examples

For [[a 3 × 3 matrix map|RZNXVEHTCE]] the image is a plane, so the rank is $2$.
For [[differentiation on cubic polynomials|SMEX3CNE69]] the image is $P_2$, so the rank is $3$.
The projection $(x, y, z) \mapsto (x, y)$ of $\R^3$ onto $\R^2$ has rank $2$.
The zero map has rank $0$, and the identity of an $n$-dimensional space has rank $n$.

### What it is not

The rank is not [[the number of nonzero columns of a matrix|R7N2K2EVJP]]: the matrix with rows $(1, 2)$ and $(2, 4)$ has two nonzero columns but rank $1$.
The rank is also not the dimension of the target.
The projection $(x, y) \mapsto (x, 0)$ of $\R^2$ has a target of dimension $2$ but rank $1$.

### Bounds

The image of a basis spans the image, by the [[theorem on the image|B6KFVB1H5F]], so $\rank T \le \dim V$.
The image is a subspace of $W$, so $\rank T \le \dim W$.
If $W$ is finite-dimensional, then $\rank T = \dim W$ exactly when $T$ is surjective.
For a composite, $\rank(S \circ T) \le \min(\rank S, \rank T)$, as for the [[rank of a product of matrices|02FDWY55AS]].

### Rank and matrices

For any bases of $V$ and $W$, the rank of $T$ equals the rank of the [[matrix of T|0YQSGNYE3K]].
The reason is that the coordinate map sends $\im T$ onto the column space of that matrix, and it keeps dimensions.
So the rank does not depend on the bases, even though the matrix does.

### History

In 1884 Sylvester proved the inequality $\rank A + \rank B - n \le \rank(AB)$ for an $m \times n$ matrix $A$ and an $n \times p$ matrix $B$.
The rank of an abstract linear map came later, with the axiomatic treatment of vector spaces.

### Watch out

Counting nonzero columns, or nonzero rows before row reduction, gives only an upper bound.
Only the number of independent columns counts, and dependent columns need a computation to detect.
A second trap is to stop row reduction before the matrix is in echelon form, since a nonzero row can still be a combination of the others.

### Try it

First, find the rank of $T(x, y, z) = (x + y, \; y + z, \; x + 2y + z)$ on $\R^3$.
The images of the basis vectors are $(1, 0, 1)$, $(1, 1, 2)$ and $(0, 1, 1)$, and the middle one is the sum of the other two, which are independent, so the rank is $2$.

Second, find the rank of $T(x, y) = (2x, 3x)$ from $\R^2$ to $\R^2$.
Every value is $x\,(2, 3)$, so the image is a line and the rank is $1$.

## Explanations

### L1 human

The rank of a linear map counts the dimensions of its output.
A map from space onto a plane has rank $2$, and a map onto a line has rank $1$.
The zero map has rank $0$.

### L2 human

To compute the rank of $x \mapsto Ax$, row reduce $A$ and count the pivots.
The rank is also the largest number of independent columns, and also the largest number of independent rows.
For $A$ with rows $(1, 2, 3)$, $(2, 4, 6)$ and $(1, 0, 1)$, the second row is twice the first, and the first and third rows are independent, so $\rank A = 2$.
Watch out: the rank of $T$ is a property of the map, and every matrix of $T$ gives the same answer.

### L3 human

For maps between infinite-dimensional spaces, the rank can be an infinite cardinal.
The maps of finite rank form a two-sided ideal in $\End(V)$, studied as [[finite-rank operators|Z8FABSYQTS]].
In Mathlib, `LinearMap.finrank_range_add_finrank_ker` is the rank-nullity theorem in finite dimension.
