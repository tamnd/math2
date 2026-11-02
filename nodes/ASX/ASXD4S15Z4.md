---
tag: ASXD4S15Z4
kind: example
name: Non-surjective epimorphism of algebras
msc: ["08C05", "18A20", "16B50"]
instance_of: [RVXDSY04KG]
uses: [ZD0GTPSJS1, 0B1261B5ED, 0GGE0Z0JQ1, 0C4JS9RF5M, 0NCJ5WXN6Z]
sources:
  - url: https://en.wikipedia.org/wiki/Epimorphism
---

## Example

Work in the [[concrete category|ZD0GTPSJS1]] $\mathbf{Ring}$ of [[rings|0B1261B5ED]] with identity and [[ring homomorphisms|0GGE0Z0JQ1]] that preserve $1$.
The inclusion $i \colon \Z \to \Q$ of the [[integers|0C4JS9RF5M]] into the [[rationals|0NCJ5WXN6Z]] is an [[epimorphism|RVXDSY04KG]] in $\mathbf{Ring}$, but it is not surjective.

Check: let $R$ be a ring and let $f, g \colon \Q \to R$ be ring homomorphisms with $f \circ i = g \circ i$, so $f(n) = g(n)$ for every integer $n$.
For $n \ne 0$, $f(1/n) \, f(n) = f(1) = 1$ and $f(n) \, f(1/n) = 1$, so $f(n)$ is a unit of $R$ with inverse $f(1/n)$.
In the same way $g(1/n)$ is the inverse of $g(n) = f(n)$.
Inverses are unique, so $f(1/n) = g(1/n)$, and then $f(m/n) = f(m) f(1/n) = g(m) g(1/n) = g(m/n)$ for all $m, n$.
Hence $f = g$, so $i$ is right-cancellable, that is, an epimorphism.
It is not surjective, since $1/2 \notin \Z$.

## Remarks

In a concrete category of algebras every surjective homomorphism is an epimorphism, but the converse can fail.
It holds in the categories of groups and of abelian groups, where every epimorphism is surjective.
Other non-surjective epimorphisms are the inclusion $(\N, +) \to (\Z, +)$ in the category of monoids, and more generally every localization map $R \to S^{-1} R$ of commutative rings.

## Explanations

### L1 human

In category theory, an epimorphism is an arrow that can be cancelled on the right, which for functions means being onto.
For rings this goes wrong.
Once a homomorphism out of $\Q$ is known on the integers, it is already known on all fractions, because $1/n$ must go to the inverse of the image of $n$.
So the integers "control" the rationals, even though they are a small part of them.
