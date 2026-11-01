---
tag: XBZ99KH3RP
kind: definition
name: Associated graded ring
msc: [13A30, 13A02]
defines: 8HFAEGFQT1
uses: [0310REJJY8, 096Z9MP2ME, 0076HWHGHQ, 8KB4SQGC0C]
sources:
  - url: https://en.wikipedia.org/wiki/Associated_graded_ring
---

## Definition

Let $R$ be a [[commutative ring|0310REJJY8]] and let $I$ be an [[ideal|096Z9MP2ME]] of $R$, with $I^0 = R$.
The *associated graded ring* of $R$ with respect to $I$ is the abelian group
$$\operatorname{gr}_I(R) = \bigoplus_{n \ge 0} I^n / I^{n+1}$$
with the following multiplication.
For $a \in I^m$ and $b \in I^n$ it is
$$(a + I^{m+1})(b + I^{n+1}) = ab + I^{m+n+1},$$
and it is extended to all elements by distributivity.

## Remarks

The product is well defined: if $a' - a \in I^{m+1}$ and $b' - b \in I^{n+1}$, then $a'b' - ab = (a' - a) b' + a (b' - b) \in I^{m+n+1}$.
With this product $\operatorname{gr}_I(R)$ is a commutative [[graded ring|8KB4SQGC0C]] whose degree $0$ part is the [[quotient ring|0076HWHGHQ]] $R/I$.
Example: for $R = \Z$ and $I = p\Z$ with $p$ prime, each $p^n\Z/p^{n+1}\Z$ is $\F_p$ spanned by the class of $p^n$, and $p^m p^n = p^{m+n}$, so $\operatorname{gr}_I(\Z) \cong \F_p[t]$.
Non-example: the direct sum $\bigoplus_{n \ge 0} I^n$ with the same rule is not $\operatorname{gr}_I(R)$; it is the [[Rees algebra|W8ZAH8TTHS]] $R[It]$, and $\operatorname{gr}_I(R)$ is its quotient by $I R[It]$.
Let $(R, \mathfrak m)$ be a Noetherian local ring with residue field $k$.
Then the ring $\operatorname{gr}_{\mathfrak m}(R)$ is a polynomial ring over $k$ in $\dim R$ variables if and only if $R$ is a [[regular local ring|63XXTF6B5M]].
