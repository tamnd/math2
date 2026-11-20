---
tag: 0MQXVZEBMT
kind: statement
role: theorem
name: Change of basis formula
msc: ["15A04"]
topics: [S6559D61BP]
audience: ug1
about: [0YQSGNYE3K, 0MKRHZB3WS]
uses: [0KWXYZPJKN, 0YYMY95FWS]
sources:
  - url: https://en.wikipedia.org/wiki/Change_of_basis
    locator: Endomorphisms
  - book: isbn:9780134860244
    locator: Section 2.5
---

## Statement

Let $F$ be a field and let $V$ and $W$ be finite-dimensional vector spaces over $F$.
Let $B, B'$ be bases of $V$, and let $C, C'$ be bases of $W$.
Let $P$ be the [[change of basis matrix|0MKRHZB3WS]] from $B$ to $B'$, and $Q$ the change of basis matrix from $C$ to $C'$.

1. For each $v \in V$, $[v]_B = P[v]_{B'}$, and $P$ is invertible, so $[v]_{B'} = P^{-1}[v]_B$.
2. For each linear map $T \colon V \to W$,
$$[T]_{C',B'} = Q^{-1} [T]_{C,B} P,$$
where $[T]$ denotes the [[matrix of $T$|0YQSGNYE3K]] in the given bases.
3. For an endomorphism $T$ of $V$, with $C = B$ and $C' = B'$, $[T]_{B'} = P^{-1} [T]_B P$.

## Remarks

### Why each hypothesis is needed

- The spaces must be finite-dimensional, so that the bases are finite and the matrices exist.
- Part 2 uses two independent changes of basis, one in the domain and one in the codomain. In part 3 both are the same change, so $Q = P$.

### Consequences

- For endomorphisms, the two matrices are [[similar|0E89HQATM8]].
- For linear maps between two spaces, the two matrices are [[equivalent|0CMHSGTWXB]].
- The [[trace of a linear map|0WCPH5Z7FA]] and its determinant do not depend on the basis.

### Converse

Every matrix similar to $[T]_B$ is the matrix of $T$ in some basis $B'$: for $P$ invertible, take $b'_j = \sum_i p_{ij} b_i$.
Every matrix equivalent to $[T]_{C,B}$ is the matrix of $T$ in some pair of bases.

### Generalizations

The formula is the [[matrix of a composition|05Q1B7MH0M]] applied to $T = \id_W \circ T \circ \id_V$, with $P = [\id_V]_{B, B'}$ and $Q^{-1} = [\id_W]_{C', C}$.
For bilinear forms the rule is $P^\top M P$ instead, by the [[change of basis for a bilinear form|0SPYAGE7T0]].

**Warning.** Books define the change of basis matrix in two opposite directions.
With the other convention, the formula reads $[T]_{B'} = P [T]_B P^{-1}$.
Mathlib's `LinearMap.toMatrix` puts the coordinates of the images of the domain basis in the columns, as here.

## History

The transformation of a matrix by $P^{-1} A P$ goes back to the study of linear substitutions in quadratic forms and in linear differential equations in the nineteenth century.

## Explanations

### L1 human

When the bases change, the matrix of a linear map changes in a fixed way.
Translate the input from the new to the old coordinates, apply the old matrix, and translate the result back.
This gives the product $Q^{-1} A P$.

### L2 human

Read $Q^{-1} A P$ from right to left.
$P$ turns $B'$-coordinates into $B$-coordinates, $A$ applies $T$ in the old bases, and $Q^{-1}$ turns $C$-coordinates into $C'$-coordinates.
New coordinates of a vector come from the old ones by the inverse matrix $P^{-1}$, not by $P$.

### L3 human

The formula says that $T \mapsto [T]_{C,B}$ is equivariant for the action of $GL_m(F) \times GL_n(F)$ on bases and on matrices.
For endomorphisms, the orbits of the action $A \mapsto P^{-1} A P$ are the similarity classes.
