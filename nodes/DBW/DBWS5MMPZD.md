---
tag: DBWS5MMPZD
kind: definition
name: Ternary discriminator
msc: [08B05, 08A40]
defines: 72PG6XCQ7D
uses: [WC47MFR6GW, 5C91SFVTY7]
sources:
  - book: isbn:9780387905785
---

## Definition

Let $A$ be a nonempty set.
The *ternary discriminator* on $A$ is the following [[ternary operation|WC47MFR6GW]] $t \colon A^3 \to A$.
$$t(x, y, z) = \begin{cases} z & \text{if } x = y, \\ x & \text{if } x \neq y. \end{cases}$$
A term $s(x, y, z)$ is a *discriminator term* for an algebra $A$ if its term operation on $A$ is the ternary discriminator on $A$.

## Remarks

Example: on a field $F$ with $q$ elements, the polynomial $s(x, y, z) = x + (z - x)\bigl(1 - (x - y)^{q - 1}\bigr)$ gives the discriminator.
Check: if $x = y$ then $(x - y)^{q - 1} = 0$ and $s = z$; if $x \neq y$ then $(x - y)^{q - 1} = 1$ and $s = x$.
Non-example: on $\set{0, 1}$ the lattice term $(x \wedge y) \vee (y \wedge z) \vee (x \wedge z)$ is not the discriminator, since at $(0, 1, 1)$ it gives $1$ while the discriminator gives $0$.
The discriminator satisfies $t(x, y, y) = x$, $t(x, x, y) = y$ and $t(x, y, x) = x$, so it is a [[Pixley term|5C91SFVTY7]] operation.
