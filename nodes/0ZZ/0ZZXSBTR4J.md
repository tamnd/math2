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

The rank of a [[linear map|0NRYHJPQG2]] $T \colon V \to W$ is the [[dimension|03GSZ8RTZJ]] of its [[image|0WSFKKT6FF]].
It counts the independent directions that survive the map.
In finite dimension, it equals the rank of any matrix of $T$.

## Motivation

Two maps can have the same source and target and still lose very different amounts of information.
The rank measures what is kept: it is the number of independent outputs.
For a linear system $Ax = b$, the rank decides how many equations are really independent.

## Notation

The rank is written $\rank T$, $\operatorname{rk} T$ or $r(T)$.
For a matrix $A$, the rank of $x \mapsto Ax$ is the [[rank of the matrix|0ZC9YTXZRY]] $\rank A$.

## Remarks

### Examples

- [[A $3 \times 3$ matrix map|RZNXVEHTCE]] has image a plane, so its rank is $2$.
- [[Differentiation on cubic polynomials|SMEX3CNE69]] has image $P_2$, so its rank is $3$.
- The projection $(x, y, z) \mapsto (x, y)$ of $\R^3$ onto $\R^2$ has rank $2$.
- The zero map has rank $0$, and the identity of an $n$-dimensional space has rank $n$.

### Non-examples

- [[The number of nonzero columns of a matrix|R7N2K2EVJP]] is not its rank.
- The dimension of the target is not the rank in general. The projection $\R^2 \to \R^2$, $(x, y) \mapsto (x, 0)$, has target of dimension $2$ but rank $1$.

### Basic properties

- $\rank T \le \dim V$, since the image of a basis spans the image, by the [[theorem on the image|B6KFVB1H5F]].
- $\rank T \le \dim W$, since the image is a subspace of $W$.
- $\rank T = \dim W$ if and only if $T$ is surjective, when $W$ is finite-dimensional.
- $\rank T + \dim \ker T = \dim V$, by the [[rank-nullity theorem|0W4FSW1TVB]].
- For any bases of $V$ and $W$, $\rank T$ equals the rank of the [[matrix of $T$|0YQSGNYE3K]]. The image is the column space of that matrix, read in coordinates.
- $\rank(S \circ T) \le \min(\rank S, \rank T)$, as for the [[rank of a product of matrices|02FDWY55AS]].

### History

In 1884 Sylvester proved the rank inequality $\rank A + \rank B - n \le \rank(AB)$ for an $m \times n$ matrix $A$ and an $n \times p$ matrix $B$.
The rank of an abstract linear map came later, with the axiomatic vector spaces of the 20th century.

### Common errors

- Counting nonzero columns, or nonzero rows of the matrix before row reduction. Only the number of independent columns counts.
- Confusing the rank with the dimension of the target.
- Thinking that the rank depends on the choice of bases. It is the dimension of a subspace, so it does not.

## Explanations

### L1 human

The rank of a linear map counts the dimensions of its output.
A map from space onto a plane has rank $2$, and a map onto a line has rank $1$.
The zero map has rank $0$.

### L2 human

To compute the rank of $x \mapsto Ax$, row reduce $A$ and count the pivots.
The rank is also the largest number of independent columns, and also the largest number of independent rows.
The trap is to stop before the matrix is in echelon form; dependent rows can hide behind nonzero entries.

### L3 human

For maps between infinite-dimensional spaces, the rank can be an infinite cardinal.
The maps of finite rank form a two-sided ideal in $\End(V)$, studied as [[finite-rank operators|Z8FABSYQTS]].
In Mathlib the rank is `LinearMap.rank`, and `LinearMap.finrank_range_add_finrank_ker` is the rank-nullity theorem.
