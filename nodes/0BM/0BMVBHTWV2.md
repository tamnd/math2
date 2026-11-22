---
tag: 0BMVBHTWV2
kind: definition
name: Coordinate vector
msc: ["15A03"]
topics: [MVH97H8B2J]
audience: ug1
defines: 04CYQHN6MC
uses: [0VTQTPQGAV, E2ZRZGXSNX]
sources:
  - url: https://en.wikipedia.org/wiki/Coordinate_vector
    locator: Definition
  - book: isbn:9780134860244
    locator: Section 2.2
---

## Definition

The coordinate vector of a vector lists the coefficients that build it from a fixed ordered basis.
Let $F$ be a field, let $V$ be a vector space over $F$, and let $B = (b_1, \dots, b_n)$ be an ordered [[basis|0VTQTPQGAV]] of $V$.
By [[unique coordinates|E2ZRZGXSNX]], each $v \in V$ equals $a_1 b_1 + \dots + a_n b_n$ for exactly one $(a_1, \dots, a_n) \in F^n$.
The *coordinate vector* of $v$ with respect to $B$ is the column
$$[v]_B = (a_1, \dots, a_n)^{\mathsf{T}} \in F^n.$$
The scalars $a_1, \dots, a_n$ are the *coordinates* of $v$ with respect to $B$.

## Notation

Some books write $\varphi_B(v)$ or $v_B$ in place of $[v]_B$, and some write the coordinate vector as a row.

## Remarks

Each hypothesis makes the definition work.
The family $B$ must span $V$, so that the coefficients exist, and it must be independent, so that they are unique; without both, $[v]_B$ would not be a single well-defined column.
The basis must be ordered, because the coordinates are listed in the order of the basis vectors: swapping $b_1$ and $b_2$ swaps the first two coordinates.

For example, in $\mathbb{R}^2$ with $B = ((1, 1), (1, -1))$, the vector $(3, 1)$ equals $2 (1, 1) + 1 (1, -1)$, so $[(3, 1)]_B = (2, 1)^{\mathsf{T}}$.
With the reversed basis $((1, -1), (1, 1))$, the same vector has coordinate vector $(1, 2)^{\mathsf{T}}$.
For the spanning family $((1, 0), (0, 1), (1, 1))$, which is not a basis, the vector $(1, 1)$ has the two coefficient lists $(1, 1, 0)$ and $(0, 0, 1)$, so no coordinate vector is defined.

The map $v \mapsto [v]_B$ is a linear isomorphism $V \to F^n$, by the [[isomorphism with the coordinate space|059THXBRBB]].
The concept page on the [[coordinate vector|04CYQHN6MC]] shows how to compute coordinates, and a [[change of basis matrix|0MKRHZB3WS]] converts coordinates for one basis into coordinates for another.

## Explanations

### L1 human

The coordinates of a vector tell you how much of each basis vector you need to build it.
With the steps $(1, 1)$ and $(1, -1)$, the point $(3, 1)$ takes two of the first step and one of the second, so its coordinates are $2$ and $1$.
A different basis gives different coordinates for the same vector.

### L2 human

In the space $P_1(\mathbb{R})$ of polynomials of degree at most $1$, take the ordered basis $B = (1 + x, 1 - x)$.
To find $[3 + x]_B$, solve $c(1 + x) + d(1 - x) = 3 + x$, that is, $c + d = 3$ and $c - d = 1$.
So $c = 2$ and $d = 1$, and $[3 + x]_B = (2, 1)^{\mathsf{T}}$.
Check: $2(1 + x) + (1 - x) = 3 + x$.
