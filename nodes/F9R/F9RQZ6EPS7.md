---
tag: F9RQZ6EPS7
kind: definition
name: Yoneda embedding
msc: [18A25, 18A22]
defines: 4DKB6AQ8J7
uses: [A2DE66937D, 28NQ0KRHD3, VJXS8AK67E, AND2WHZC8P, KYCPCC57FT, 1X0WKFQX8K, D6DF1ARPVD, GRG8WEBSH5]
sources:
  - url: https://en.wikipedia.org/wiki/Yoneda_lemma
---

## Definition

Let $\mathcal{C}$ be a locally small [[category|A2DE66937D]], and let $[\mathcal{C}^{\mathrm{op}}, \mathbf{Set}]$ be the [[functor category|1X0WKFQX8K]] of [[presheaves|AND2WHZC8P]] on $\mathcal{C}$, with [[natural transformations|KYCPCC57FT]] as morphisms.
The *Yoneda embedding* is the [[functor|28NQ0KRHD3]] $y \colon \mathcal{C} \to [\mathcal{C}^{\mathrm{op}}, \mathbf{Set}]$ given by:

1. on objects, $y(A) = \Hom(-, A)$, the contravariant [[hom functor|VJXS8AK67E]] of $A$;
2. on morphisms, for $f \colon A \to B$, $y(f) \colon \Hom(-, A) \to \Hom(-, B)$ is the natural transformation with components $y(f)_X(g) = f \circ g$ for $g \colon X \to A$.

## Remarks

The components $y(f)_X$ are natural in $X$ because $f \circ (g \circ h) = (f \circ g) \circ h$.
By the [[Yoneda lemma|D6DF1ARPVD]] with $F = \Hom(-, B)$, the map $f \mapsto y(f)$ is a bijection $\Hom(A, B) \to \mathrm{Nat}(y(A), y(B))$, so $y$ is [[full and faithful|GRG8WEBSH5]].
Since $y$ is fully faithful, $y(A) \cong y(B)$ implies $A \cong B$.
The dual functor $A \mapsto \Hom(A, -)$ embeds $\mathcal{C}^{\mathrm{op}}$ into $[\mathcal{C}, \mathbf{Set}]$.

Example: let $P$ be a preorder seen as a category, with one morphism $a \to b$ when $a \le b$.
Then $y(a)$ is the presheaf with $y(a)(x)$ a one-point set when $x \le a$ and empty otherwise, so $y$ sends $a$ to the down-set $\set{x : x \le a}$.
The map $a \mapsto \set{x : x \le a}$ is the classical embedding of a preorder into its down-sets ordered by inclusion.

Non-example: the assignment $A \mapsto \Hom(A, -)$ is not a functor $\mathcal{C} \to [\mathcal{C}, \mathbf{Set}]$; a morphism $f \colon A \to B$ induces $\Hom(B, -) \to \Hom(A, -)$, which goes the wrong way, so clause 2 fails for this assignment.
