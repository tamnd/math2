---
tag: 9CMAJWWBNZ
kind: definition
name: Skew group ring
msc: [16S35, 16W22]
defines: PCKK4SFZEK
uses: [0B1261B5ED, G5S1M9, 0WCY42EV9V, 4NMTSX0XDS, 0FHVPRAE60]
sources:
  - url: https://en.wikipedia.org/wiki/Crossed_product
---

## Definition

Let $R$ be a [[ring|0B1261B5ED]] with identity and let $G$ be a [[group|G5S1M9]].
Let $\alpha \colon G \to \Aut(R)$ be a group homomorphism, written $g \mapsto \alpha_g$; it is an [[action|0WCY42EV9V]] of $G$ on $R$ by ring automorphisms.
The *skew group ring* $R * G$, also written $R \rtimes_\alpha G$, is the set of finite formal sums $\sum_{g \in G} r_g g$ with $r_g \in R$.
Addition is termwise, and multiplication is the biadditive extension of
$$(r g)(s h) = r \, \alpha_g(s) \, gh \qquad (r, s \in R, \ g, h \in G).$$

## Remarks

The product is associative because $\alpha_{gh} = \alpha_g \circ \alpha_h$: both $((rg)(sh))(tk)$ and $(rg)((sh)(tk))$ equal $r \alpha_g(s) \alpha_{gh}(t) \, ghk$.
The identity is $1 \cdot e$, where $e$ is the identity of $G$, and $R$ is a subring through $r \mapsto r e$.
If $\alpha$ is trivial, $R * G$ is the [[group ring|4NMTSX0XDS]] $R[G]$.
Example: let $G = \set{e, c}$ act on $\C$ by complex conjugation, $\alpha_c(z) = \bar z$.
Then $R * G = \C * G$ has dimension $4$ over $\R$.
The map sending $z$ to multiplication by $z$ and $c$ to conjugation, both as $\R$-linear maps of $\C = \R^2$, is an isomorphism onto the [[matrix ring|0FHVPRAE60]] $M_2(\R)$.
Non-example: if $\alpha \colon G \to \Aut(R)$ is a map that is not a homomorphism, the same formula fails associativity, since $(1g)((1h)(s e)) = \alpha_g(\alpha_h(s)) gh$ while $((1g)(1h))(s e) = \alpha_{gh}(s) gh$.
When a twisting cocycle is also allowed, $g h$ is replaced by a scalar multiple of $gh$, and one gets a crossed product.
