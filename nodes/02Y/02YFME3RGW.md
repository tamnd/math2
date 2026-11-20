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

Let $F$ be a field, let $V$ and $W$ be vector spaces over $F$, and let $T \colon V \to W$ be a [[linear map|0RJF668P1T]].
The *kernel* of $T$ is the subset
$$\ker T = \{v \in V : T(v) = 0\}$$
of $V$.

## Notation

Other notations are $\ker(T)$ and $N(T)$.
Some books call the kernel the *null space* of $T$.

## Remarks

- The kernel is a subset of the source $V$, and not of the target $W$.
- The kernel always contains $0$, since a linear map sends $0$ to $0$.
- For the map $x \mapsto Ax$ of a matrix $A$, the kernel is the [[null space|0PHDYNR24D]] of $A$, the solution set of $Ax = 0$.
- Mathlib defines `LinearMap.ker f` directly as a submodule, so the subspace property is built in.

## Explanations

### L1 human

The kernel collects the vectors that the map sends to zero.
It measures how much information the map loses.
If only the zero vector goes to zero, then the map loses nothing.

### L2 human

For $T(x, y, z) = (x, y)$ on $\R^3$, $T(x, y, z) = 0$ means $x = 0$ and $y = 0$.
So $\ker T = \{(0, 0, z) : z \in \R\}$, the $z$-axis.
The trap is to write the kernel as a subset of $\R^2$; it lives in $\R^3$.
