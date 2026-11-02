---
tag: B94AB2AA0S
kind: definition
name: Intersection multiplicity
msc: [14C17, 13H15]
defines: GPQF9GK4T9
uses: [HV6YBS0YDH, 36X2WTHYCB, QAGW4V0S62, V6JBKT168T, 63XXTF6B5M]
sources:
  - url: https://en.wikipedia.org/wiki/Intersection_number
---

## Definition

Let $X$ be a smooth [[algebraic variety|HV6YBS0YDH]] of [[dimension|36X2WTHYCB]] $n$ over a field.
Let $V, W \subset X$ be irreducible closed subvarieties that meet *properly*: every irreducible component of $V \cap W$ has dimension $\dim V + \dim W - n$.
Let $Z$ be an irreducible component of $V \cap W$, and let $A = \mathcal{O}_{X, Z}$ be the local ring of $X$ at the generic point of $Z$.
Let $I_V, I_W \subset A$ be the ideals of $V$ and $W$.
The *intersection multiplicity* of $V$ and $W$ along $Z$ is
$$i(Z; V \cdot W) = \sum_{j \ge 0} (-1)^j \, \ell_A\big(\operatorname{Tor}_j^A(A/I_V, A/I_W)\big),$$
where $\operatorname{Tor}$ is the [[Tor functor|QAGW4V0S62]] and $\ell_A$ is the [[length|V6JBKT168T]] of an $A$-module.

## Remarks

The sum is finite because $A$ is a [[regular local ring|63XXTF6B5M]], and each term has finite length because $Z$ is a component of $V \cap W$.
This is Serre's Tor formula, and $i(Z; V \cdot W) \ge 1$.
When $A/I_V$ and $A/I_W$ are Cohen–Macaulay, the higher Tor terms vanish and $i(Z; V \cdot W) = \ell_A\big(A/(I_V + I_W)\big)$.
For two plane curves $f = 0$ and $g = 0$ without common component, meeting at a point $P$, this gives $i_P(f, g) = \dim_k \mathcal{O}_{\mathbb{A}^2, P}/(f, g)$.
Example: for $f = y - x^2$ and $g = y$ at $P = (0, 0)$, $\mathcal{O}_{\mathbb{A}^2, P}/(y - x^2, y) \cong k[x]_{(x)}/(x^2)$, of dimension $2$.
Non-example: if $V = W$ is a line in $X = \mathbb{A}^2$, then $V \cap W$ has dimension $1$, not $1 + 1 - 2 = 0$, so the intersection is not proper and the multiplicity is not defined.
