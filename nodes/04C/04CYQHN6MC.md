---
tag: 04CYQHN6MC
kind: concept
name: Coordinate vector
msc: ["15A03"]
topics: [MVH97H8B2J]
audience: ug1
uses: [0KCQ9Y3QKA, 0VTQTPQGAV]
sources:
  - url: https://en.wikipedia.org/wiki/Coordinate_vector
    locator: Definition
  - book: isbn:9783031410253
    locator: Section 3C
  - book: isbn:9780134860244
    locator: Section 2.2
same_as:
  wikidata: Q1057996
  wikipedia: Coordinate vector
---

## Summary

Let $B = (b_1, \dots, b_n)$ be an ordered [[basis|0KCQ9Y3QKA]] of a vector space $V$ over $F$.
The coordinate vector $[v]_B \in F^n$ of $v \in V$ is the list of the unique coefficients $a_i$ with $v = a_1 b_1 + \cdots + a_n b_n$; see the [[definition|0BMVBHTWV2]].
The map $v \mapsto [v]_B$ is a [[linear isomorphism $V \to F^n$|059THXBRBB]], so coordinates turn every $n$-dimensional space into $F^n$.

## Motivation

Abstract vectors, such as polynomials or matrices, cannot be fed directly into row reduction.
Coordinates translate them into columns of numbers, where the algorithms of matrix algebra work.
The translation respects sums and scalar multiples, so the answers translate back.

## Notation

We write $[v]_B$ as a column vector.
Some books write $\varphi_B(v)$ or $\operatorname{coord}_B(v)$.
In Mathlib, `b.repr v` is the coordinate function of `v` in the basis `b`.

## Remarks

### Examples

1. In $F^n$ with the [[standard basis|C5QA672NPH]] $E$, we have $[x]_E = x$.
2. In $\R^2$ with $B = ((1, 1), (1, -1))$: $[(3, 1)]_B = (2, 1)^T$, because $2(1, 1) + 1(1, -1) = (3, 1)$.
3. In $P_2(\R)$ with $B = (1, x - 1, (x - 1)^2)$: $[x^2]_B = (1, 2, 1)^T$, because $x^2 = 1 + 2(x - 1) + (x - 1)^2$.
4. In $M_2(F)$ with the matrix units $(E_{11}, E_{12}, E_{21}, E_{22})$: the coordinates of $\begin{pmatrix} a & b \\ c & d \end{pmatrix}$ are $(a, b, c, d)^T$.

### Non-examples

1. In the spanning family $S = ((1, 0), (0, 1), (1, 1))$ of $\R^2$, the vector $(1, 1)$ has the two coefficient lists $(1, 1, 0)$ and $(0, 0, 1)$.
   So "$[v]_S$" is not defined, because $S$ fails independence.
2. For the unordered set $\set{(1, 1), (1, -1)}$, the list "$[(3, 1)]$" could be $(2, 1)$ or $(1, 2)$; coordinates need an order.

### Basic properties

1. $[v + w]_B = [v]_B + [w]_B$ and $[cv]_B = c[v]_B$.
2. $[b_i]_B = e_i$.
3. The map $v \mapsto [v]_B$ is a linear isomorphism $V \to F^n$; see [[this statement|059THXBRBB]].
4. A list of vectors is independent, or spans, or is a basis, exactly when the same holds for the list of its coordinate vectors.
5. For two bases $B$ and $C$, a [[change of basis matrix|0MKRHZB3WS]] $P$ satisfies $[v]_C = P[v]_B$.

### History

Coordinates in the plane go back to Descartes and Fermat in the seventeenth century.
Coordinates in an arbitrary basis appear with Grassmann in 1844, and they became standard with the abstract theory in the twentieth century.

### Common errors

1. The coordinate vector depends on the basis and on its order, not only on $v$.
2. In $F^n$, the coordinates of $x$ in a basis $B$ are not the entries of $x$, unless $B$ is the standard basis.
3. To find $[v]_B$ in $F^n$, solve the system $Ac = v$, where $A$ has the vectors of $B$ as columns; do not compute the product $Av$.

## Explanations

### L1 human

The coordinates of a vector tell us how much of each basis vector we need to build it.
Different bases give different coordinates for the same vector.
After we fix a basis, each vector is just a list of numbers.

### L2 human

To compute $[v]_B$ in $F^n$, put the basis vectors as the columns of a matrix $A$ and solve $Ac = v$.
Example: $B = ((1, 2), (3, 4))$ and $v = (5, 6)$.
The equations $c_1 + 3c_2 = 5$ and $2c_1 + 4c_2 = 6$ give $c_2 = 2$ and $c_1 = -1$.
Check: $-(1, 2) + 2(3, 4) = (5, 6)$, so $[v]_B = (-1, 2)^T$.
