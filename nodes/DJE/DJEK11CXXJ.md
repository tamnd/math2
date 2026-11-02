---
tag: DJEK11CXXJ
kind: definition
name: Quasi-primal algebra
msc: [08A40, 08B05]
defines: QWSBDFM47K
uses: [72PG6XCQ7D, N9M2N27END, 070R982G4B]
sources:
  - url: https://en.wikipedia.org/wiki/Functional_completeness
---

## Definition

Let $A$ be an algebra whose universe is a nonempty [[finite set|070R982G4B]].
The algebra $A$ is *quasi-primal* if the [[ternary discriminator|72PG6XCQ7D]] $t$ on $A$ is a [[term operation|N9M2N27END]] of $A$.
Here $t(x, y, z) = z$ if $x = y$, and $t(x, y, z) = x$ if $x \ne y$.

## Remarks

Example: every finite field $F$ with $q$ elements, as a ring, is quasi-primal.
Check: the term $x + (z - x)\bigl(1 - (x - y)^{q - 1}\bigr)$ gives $z$ when $x = y$, and gives $x$ otherwise since then $(x - y)^{q - 1} = 1$.
Non-example: the two-element lattice $(\set{0, 1}, \wedge, \vee)$ is not quasi-primal.
Its term operations are monotone, but the discriminator is not, since $t(0, 0, 1) = 1$ while $t(0, 1, 1) = 0$.
A finite algebra is quasi-primal if and only if it generates an arithmetical variety and every nontrivial subalgebra of it is simple.
This characterization is due to Alden Pixley.
