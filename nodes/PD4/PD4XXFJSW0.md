---
tag: PD4XXFJSW0
kind: definition
name: Commutative algebra over a ring
msc: [13B02, 13A99]
defines: DPBJ04JMH8
uses: [0GYGHKX834, 0GGE0Z0JQ1, 09VDS2W1E8]
sources:
  - url: https://en.wikipedia.org/wiki/Associative_algebra
---

## Definition

Let $R$ be a [[commutative ring|0GYGHKX834]].
A *commutative $R$-algebra* is a pair $(A, f)$ where $A$ is a commutative ring and $f \colon R \to A$ is a [[ring homomorphism|0GGE0Z0JQ1]].
The map $f$ is the *structure map* of the algebra.
For $r \in R$ and $a \in A$ one writes $r a = f(r) a$.
If $(A, f)$ and $(B, g)$ are commutative $R$-algebras, an *$R$-algebra homomorphism* is a ring homomorphism $h \colon A \to B$ with $h \circ f = g$.

## Remarks

Example: for $R = \Z$ and $A = \Z/n\Z$, the reduction map $\Z \to \Z/n\Z$ is a ring homomorphism, so $\Z/n\Z$ is a $\Z$-algebra.
Example: the polynomial ring $R[x_1, \ldots, x_n]$ with the inclusion of constants is an $R$-algebra.
Non-example: the ring $M_2(\R)$ of $2 \times 2$ real matrices receives the ring homomorphism $c \mapsto c I$ from $\R$.
But $M_2(\R)$ is not commutative, so it is an associative $\R$-algebra and not a commutative one.
Equivalent form: a commutative $R$-algebra is a commutative ring $A$ with an $R$-[[module|09VDS2W1E8]] structure such that $r(ab) = (ra)b$ for all $r \in R$ and $a, b \in A$; the structure map is then $r \mapsto r \cdot 1$.
The notion of a [[finite type algebra|AC5TFFQT9M]] and the [[tensor product of algebras|1735VGRT2P]] are built on this definition.
