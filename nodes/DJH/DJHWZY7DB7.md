---
tag: DJHWZY7DB7
kind: definition
name: Galois symbol
msc: [19D45, 12G05, 19F15]
defines: N4NNC0BB7A
uses: [04C5ZBG1WT, 2YXDQ7Q445, 9MPCZ3EAJM, JJ91A1V8NQ, XZQENYV15Y, JX47MS1R1H, 0WX11EA3F3, YFF8B5A0QG]
sources:
  - url: https://en.wikipedia.org/wiki/Norm_residue_isomorphism_theorem
---

## Definition

Let $F$ be a [[field|04C5ZBG1WT]], let $m \ge 1$ be an integer invertible in $F$, and let $F^s$ be a [[separable closure|JJ91A1V8NQ]] of $F$.
Let $\mu_m \subseteq F^s$ be the group of $m$-th [[roots of unity|0WX11EA3F3]], and for $n \ge 0$ let $\mu_m^{\otimes n}$ be its $n$-fold tensor power over $\Z$, with $\mu_m^{\otimes 0} = \Z/m\Z$.
Write $H^n(F, M)$ for the [[Galois cohomology|9MPCZ3EAJM]] of $\Gal(F^s/F)$ with coefficients in $M$.
Let $\delta \colon F^\times \to H^1(F, \mu_m)$ be the connecting map of the Kummer sequence $1 \to \mu_m \to (F^s)^\times \xrightarrow{x \mapsto x^m} (F^s)^\times \to 1$, as in [[Kummer theory|XZQENYV15Y]].
The *Galois symbol* in degree $n$ is the homomorphism
$$h_{F, m}^n \colon K_n^M(F)/m \to H^n(F, \mu_m^{\otimes n}), \qquad \set{a_1, \ldots, a_n} \mapsto \delta(a_1) \cup \cdots \cup \delta(a_n),$$
from [[Milnor K-theory|2YXDQ7Q445]] modulo $m$, where $\cup$ is the [[cup product|JX47MS1R1H]].

## Remarks

The map is well defined: the cup product is multilinear, the target is killed by $m$, and Tate showed that $\delta(a) \cup \delta(1 - a) = 0$ for $a \ne 0, 1$.
Concretely, for $\sigma \in \Gal(F^s/F)$ and $\alpha^m = a$, the class $\delta(a)$ is represented by the cocycle $\sigma \mapsto \sigma(\alpha)/\alpha$.

Example: in degree $1$, $h^1_{F, m} \colon F^\times / (F^\times)^m \to H^1(F, \mu_m)$ is an isomorphism, by Kummer theory and [[Hilbert's Theorem 90|YFF8B5A0QG]].
Example: $F = \R$ and $m = 2$.
Then $H^*(\R, \Z/2\Z)$ is a polynomial ring $\F_2[x]$ with $x = \delta(-1)$, so $h^n_{\R, 2}(\set{-1, \ldots, -1}) = x^n \ne 0$.

Non-example: let $F$ have characteristic $p > 0$ and let $m = p$.
Then the map $x \mapsto x^p$ is injective on $(F^s)^\times$, and $\mu_p$ is trivial.
So the Kummer sequence is not exact on the right in general, and the construction does not apply.
This is why $m$ must be invertible in $F$.
