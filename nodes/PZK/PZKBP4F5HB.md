---
tag: PZKBP4F5HB
kind: definition
name: Epimorphism
msc: [18A20]
defines: RVXDSY04KG
uses: [A2DE66937D, 859F0TFVA3, 01RVCMSN5N, 0VTH8KPCG2]
sources:
  - url: https://en.wikipedia.org/wiki/Epimorphism
---

## Definition

Let $\mathcal{C}$ be a [[category|A2DE66937D]] and let $f \colon A \to B$ be a [[morphism|859F0TFVA3]] of $\mathcal{C}$.
The morphism $f$ is an *epimorphism* if, for every object $Y$ and all morphisms $g_1, g_2 \colon B \to Y$, the equality $g_1 \circ f = g_2 \circ f$ implies $g_1 = g_2$.

## Remarks

Equivalently, for every object $Y$ the map $\Hom_{\mathcal{C}}(B, Y) \to \Hom_{\mathcal{C}}(A, Y)$, $g \mapsto g \circ f$, is injective.
One writes $f \colon A \twoheadrightarrow B$, or says that $f$ is *epic*.
Example: in the category of sets, every [[surjective function|01RVCMSN5N]] $f$ is an epimorphism.
If $g_1 \circ f = g_2 \circ f$ and $b \in B$, write $b = f(a)$; then $g_1(b) = g_1(f(a)) = g_2(f(a)) = g_2(b)$.
Non-example: the inclusion $f \colon \set{0} \to \set{0, 1}$ is not an epimorphism of sets.
The identity of $\set{0, 1}$ and the constant map with value $0$ agree after $f$ but are different.
In the category of rings with unit, the inclusion $\Z \to \Q$ is an epimorphism that is not surjective.
Two [[ring homomorphisms|0VTH8KPCG2]] $g_1, g_2 \colon \Q \to R$ that agree on $\Z$ agree on $m/n$, since $g_i(m/n) = g_i(m) g_i(n)^{-1}$.
