---
tag: 0FP4BVDAAQ
kind: definition
name: Scalar potential
msc: [26B12]
defines: 0H7C3T1GJY
uses: [0N67NBKQ5T, 0NS2QYVC4Y, 05R9NF2J49]
sources:
  - url: https://en.wikipedia.org/wiki/Scalar_potential
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Conservative_vector_field
    locator: Definition
---

## Definition

Let $U \subseteq \mathbb{R}^n$ be open, and let $F \colon U \to \mathbb{R}^n$ be a continuous [[vector field|0N67NBKQ5T]].
A scalar potential of $F$ is a function $\phi \colon U \to \mathbb{R}$ of class $C^1$ with $\nabla \phi = F$ on $U$.

## Remarks

In physics, a potential is often a function $V$ with $F = -\nabla V$, so that $V$ is a potential energy. The two conventions differ by a sign.
If $U$ is connected, two scalar potentials of $F$ differ by a constant. Indeed, their difference has zero gradient on $U$.
On a connected open set $U$ one finds a potential by fixing $p \in U$ and setting $\phi(x) = \int_\gamma F \cdot d\mathbf{r}$ for a path $\gamma$ from $p$ to $x$. This works when $F$ is [[conservative|05R9NF2J49]].
Example: the gravitational field $F(x) = -x / \|x\|^3$ on $\mathbb{R}^3 \setminus \{0\}$ has the scalar potential $\phi(x) = 1 / \|x\|$.

## Explanations

### L1 human

A scalar potential is a height function for a vector field.
The field points in the direction in which the potential grows fastest, and its length is the rate of growth.
