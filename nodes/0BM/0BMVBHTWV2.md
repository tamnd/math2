---
tag: 0BMVBHTWV2
kind: definition
name: Coordinate vector
msc: [15A03]
defines: 04CYQHN6MC
uses: [0VTQTPQGAV]
sources:
  - url: https://en.wikipedia.org/wiki/Coordinate_vector
    locator: Definition
---

## Definition

Let $F$ be a field, let $V$ be a vector space over $F$, and let $B = (b_1, \dots, b_n)$ be a [[basis|0KCQ9Y3QKA]] of $V$.
Each $v \in V$ is equal to $a_1 b_1 + \cdots + a_n b_n$ for exactly one $(a_1, \dots, a_n) \in F^n$.
The *coordinate vector* of $v$ in the basis $B$ is
$$[v]_B = (a_1, \dots, a_n)^T \in F^n.$$
The scalars $a_i$ are the *coordinates* of $v$ in $B$.

## Remarks

The coordinates depend on the order of the basis vectors, so $B$ is an ordered basis.
The map $v \mapsto [v]_B$ is a linear isomorphism $V \to F^n$, see [[isomorphism with the coordinate space|059THXBRBB]].
In $\R^2$ with $B = ((1, 1), (1, -1))$, the vector $(3, 1)$ has coordinate vector $(2, 1)^T$.
A [[change of basis matrix|0MKRHZB3WS]] converts coordinates in one basis into coordinates in another basis.

## Explanations

### L1 human

The coordinates of a vector tell us how much of each basis vector we need to build it.
Different bases give different coordinates for the same vector.
After we fix a basis, each vector is just a list of numbers.
