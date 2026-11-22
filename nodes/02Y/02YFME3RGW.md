---
tag: 02YFME3RGW
kind: definition
name: Kernel of a linear map
msc: ["15A04"]
topics: [9080WQTZ3M]
audience: ug1
defines: 0S23E6YE83
uses: [0RJF668P1T]
formal:
  - system: lean4
    library: mathlib
    decl: LinearMap.ker
    match: exact
sources:
  - url: https://en.wikipedia.org/wiki/Kernel_(linear_algebra)
    locator: lead section
  - book: isbn:9780134860244
    locator: Section 2.1
inventory: [23SSF4JKJE]
---

## Definition

The kernel of a linear map is the set of vectors in its source that it sends to the zero vector.
Let $F$ be a field, let $V$ and $W$ be vector spaces over $F$, and let $T \colon V \to W$ be a [[linear map|0RJF668P1T]].
The *kernel* of $T$ is the subset
$$\ker T = \{v \in V : T(v) = 0\}$$
of $V$.

## Notation

Other notations are $\ker(T)$ and $N(T)$.
Some books call the kernel the *null space* of $T$.

## Remarks

The condition $T(v) = 0$ uses the zero vector of the target $W$, but the kernel is a subset of the source $V$, since it collects inputs.
It is never empty, because a linear map sends $0$ to $0$, so $0 \in \ker T$.
The definition only asks for a subset, and the [[lemma on the kernel|REWYZ8N7EN]] proves that this subset is a subspace.
Mathlib defines `LinearMap.ker f` directly as a submodule, so there the subspace property is built in.

For the map $x \mapsto Ax$ of a matrix $A$, the kernel is the [[null space|0PHDYNR24D]] of $A$, the solution set of $Ax = 0$.
For example, $T(x, y) = (x - y, \; 0)$ on $\R^2$ has kernel $\{(t, t) : t \in \R\}$.
The condition fails for every vector off this line: $T(1, 0) = (1, 0) \ne 0$, so $(1, 0) \notin \ker T$.
The [[concept page|0S23E6YE83]] gives more examples and the first properties.

## Explanations

### L1 human

The kernel collects the vectors that the map sends to zero.
It measures how much information the map loses.
If only the zero vector goes to zero, then the map loses nothing.

### L2 human

For $T(x, y, z) = (x, y)$ on $\R^3$, the equation $T(x, y, z) = 0$ means $x = 0$ and $y = 0$, with $z$ free.
So $\ker T = \{(0, 0, z) : z \in \R\}$, the $z$-axis.
Watch out: the kernel is a subset of $\R^3$, the source, and not of $\R^2$.
