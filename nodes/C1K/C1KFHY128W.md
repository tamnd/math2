---
tag: C1KFHY128W
kind: object
name: Split-quaternions
msc: [17A75, 11R52]
instance_of: [ZWXW0T3EAC, 1Q9G6AST10]
uses: [0GE4DVQKR8, 0FHVPRAE60, T9XW7RBEHY]
sources:
  - url: https://en.wikipedia.org/wiki/Split-quaternion
same_as:
  wikidata: Q2996919
  wikipedia: Split-quaternion
---

## Description

The *split-quaternions* form the $4$-dimensional real algebra with basis $1, i, j, k$, a bilinear associative product with unit $1$, and the rules
$$i^2 = -1, \quad j^2 = 1, \quad k^2 = 1, \quad ij = k = -ji.$$
These give $jk = -i = -kj$ and $ki = j = -ik$.
The conjugate of $q = a + bi + cj + dk$ is $\bar{q} = a - bi - cj - dk$, and $q\bar{q} = a^2 + b^2 - c^2 - d^2$.

## Remarks

The split-quaternions are a [[quaternion algebra|ZWXW0T3EAC]] over $\R$ that is not a division algebra, unlike Hamilton's [[quaternions|0GE4DVQKR8]].
For example $(1 + j)(1 - j) = 1 - j^2 = 0$.
They are isomorphic to the [[ring|0FHVPRAE60]] of $2 \times 2$ real matrices, by $i \mapsto \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}$ and $j \mapsto \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}$.
Under this map the norm $a^2 + b^2 - c^2 - d^2$ becomes the determinant.
So they form a [[composition algebra|1Q9G6AST10]] whose norm has signature $(2, 2)$.
They are the [[Cayley–Dickson double|T9XW7RBEHY]] of $\C$ with parameter $\mu = 1$.

## Explanations

### L1 human

Split-quaternions look like Hamilton's quaternions, but two of the three imaginary units square to $+1$ instead of $-1$.
This change allows nonzero elements with zero norm, and such elements have no inverse.
In fact, the split-quaternions are just the $2 \times 2$ real matrices written in a different basis.
