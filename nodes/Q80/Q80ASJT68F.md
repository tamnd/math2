---
tag: Q80ASJT68F
kind: definition
name: Polynomial identity ring
msc: [16R10, 16R20]
defines: C0EDT81EGH
uses: [0310REJJY8, 3CTW1P4HBP, 2P3Y2FRCSZ, 0B1261B5ED, 0MDMZ965VE]
sources:
  - url: https://en.wikipedia.org/wiki/Polynomial_identity_ring
---

## Definition

Let $k$ be a [[commutative ring|0310REJJY8]] with identity, and let $A$ be an [[associative algebra|3CTW1P4HBP]] over $k$.
Let $k\langle x_1, \ldots, x_n \rangle$ be the [[free algebra|2P3Y2FRCSZ]] on $n$ variables.
A polynomial $f \in k\langle x_1, \ldots, x_n \rangle$ is a *polynomial identity* of $A$ if $f(a_1, \ldots, a_n) = 0$ for all $a_1, \ldots, a_n \in A$.
The polynomial $f$ is *monic* if some monomial of $f$ of highest degree has coefficient $1$.
The algebra $A$ is a *PI algebra* if it satisfies some monic polynomial identity.
A [[ring|0B1261B5ED]] is a *polynomial identity ring*, or *PI ring*, if it is a PI algebra over $k = \Z$.

## Remarks

Over a field $k$, every nonzero polynomial is a scalar multiple of a monic one, so a $k$-algebra is PI when it satisfies some nonzero polynomial identity.
Monic polynomials are used for rings because, for example, every ring of characteristic $2$ satisfies the identity $2 x_1 = 0$, which says nothing about its multiplication.

Example: a commutative ring satisfies the monic identity $x_1 x_2 - x_2 x_1$.

Example: the ring $M_2(k)$ of $2 \times 2$ matrices over a commutative ring $k$ satisfies the monic identity $[[x_1, x_2]^2, x_3]$, where $[a, b] = ab - ba$.
Indeed, $c = [a_1, a_2]$ has trace $0$, so the Cayley–Hamilton theorem gives $c^2 = -\det(c) \, I$, a scalar matrix that commutes with every $a_3$.

Non-example: let $k$ be a field and $A = k\langle x, y \rangle$.
If $f(x_1, \ldots, x_n)$ is nonzero, then $f(x, xy, x y^2, \ldots, x y^{n-1}) \ne 0$, because distinct words in the $x y^i$ are distinct words in $x$ and $y$.
So the free algebra on two letters satisfies no nonzero identity and is not PI.

Every subring and every homomorphic image of a PI ring is a PI ring.
The [[exterior algebra|0MDMZ965VE]] of an infinite-dimensional vector space over a field of characteristic $0$ is PI, since it satisfies $[[x_1, x_2], x_3]$, but it satisfies no standard identity.
