---
tag: 0SVR29SV1V
kind: definition
name: Quotient space
msc: [15A03]
defines: 0BR3FY5Q8M
uses: [0EPTJA5QV4]
sources:
  - url: https://en.wikipedia.org/wiki/Quotient_space_(linear_algebra)
    locator: Definition
---

## Definition

Let $F$ be a field, let $V$ be a vector space over $F$, and let $W$ be a [[linear subspace|00YC1D652K]] of $V$.
For $v \in V$, the *coset* of $v$ is $v + W = \{v + w : w \in W\}$.
The *quotient space* $V / W$ is the set of all cosets $v + W$ with $v \in V$, with the operations
$$(u + W) + (v + W) = (u + v) + W, \qquad a(v + W) = av + W$$
for $u, v \in V$ and $a \in F$.

## Remarks

The operations are well defined, because $W$ is a subspace: the result does not depend on the choice of $u$ and $v$ in their cosets.
Two cosets $u + W$ and $v + W$ are equal if and only if $u - v \in W$.
The zero vector of $V / W$ is the coset $0 + W = W$.
In $\R^2$ with $W$ the $x$-axis, the cosets are the horizontal lines, and $V / W$ is isomorphic to $\R$.

## Explanations

### L1 human

In the quotient space $V / W$, we treat two vectors as the same when they differ by a vector of $W$.
Each element of $V / W$ is a copy of $W$ shifted by some vector.
Dividing the plane by a line gives the set of all lines parallel to it, which behaves like a single line.
