---
tag: 7KK111QGBZ
kind: definition
name: Simple algebra
msc: [08A30, 08A05]
defines: 9CJCXNYNK8
uses: [QJGPT2W0FT, DCSXXT4SER, REE07CSXHR]
sources:
  - url: https://en.wikipedia.org/wiki/Simple_algebra_(universal_algebra)
---

## Definition

Let $\mathbf{A}$ be an [[algebra|QJGPT2W0FT]] with universe $A$.
Let $\Delta_A = \set{(a, a) : a \in A}$ and $\nabla_A = A \times A$.
The algebra $\mathbf{A}$ is *simple* when $A$ has at least two elements and its only [[congruences|DCSXXT4SER]] are $\Delta_A$ and $\nabla_A$.

## Remarks

Equivalently, the [[congruence lattice|REE07CSXHR]] of $\mathbf{A}$ is the two-element chain.
By the correspondence theorem, a quotient $\mathbf{A}/\theta$ is simple exactly when $\theta$ is a maximal element of $\operatorname{Con} \mathbf{A} \setminus \set{\nabla_A}$.

Example: the group $\Z/p\Z$ with $p$ prime is simple.
Its congruences come from its subgroups, and by Lagrange's theorem these are only $\set{0}$ and $\Z/p\Z$.

Non-example: the ring $\Z$ is not simple.
Congruence modulo $2$ is a congruence, and it is neither $\Delta_\Z$, since $(0, 2)$ belongs to it, nor $\nabla_\Z$, since $(0, 1)$ does not.

A field, viewed as a ring, is simple, since its only ideals are $\set{0}$ and the whole field.
The one-element algebra is excluded, because there $\Delta_A = \nabla_A$.
