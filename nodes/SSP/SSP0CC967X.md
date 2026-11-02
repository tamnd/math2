---
tag: SSP0CC967X
kind: definition
name: Monomorphism
msc: [18A20]
defines: Y2NP1JFR86
uses: [A2DE66937D, 859F0TFVA3, 09NWETVTNY]
sources:
  - url: https://en.wikipedia.org/wiki/Monomorphism
---

## Definition

Let $\mathcal{C}$ be a [[category|A2DE66937D]] and let $f \colon A \to B$ be a [[morphism|859F0TFVA3]] of $\mathcal{C}$.
The morphism $f$ is a *monomorphism* if, for every object $X$ and all morphisms $g_1, g_2 \colon X \to A$, the equality $f \circ g_1 = f \circ g_2$ implies $g_1 = g_2$.

## Remarks

Equivalently, for every object $X$ the map $\Hom_{\mathcal{C}}(X, A) \to \Hom_{\mathcal{C}}(X, B)$, $g \mapsto f \circ g$, is injective.
One writes $f \colon A \rightarrowtail B$, or says that $f$ is *monic*.
Example: in the category of sets, every [[injective function|09NWETVTNY]] $f$ is a monomorphism.
If $f \circ g_1 = f \circ g_2$, then $f(g_1(x)) = f(g_2(x))$ for each $x \in X$, so $g_1(x) = g_2(x)$ by injectivity.
Non-example: the map $f \colon \set{1, 2} \to \set{0}$ is not a monomorphism.
The two maps $g_1, g_2 \colon \set{0} \to \set{1, 2}$ with $g_1(0) = 1$ and $g_2(0) = 2$ satisfy $f \circ g_1 = f \circ g_2$ but $g_1 \ne g_2$.
Every isomorphism is a monomorphism, and a composite of monomorphisms is a monomorphism.
If $g \circ f$ is a monomorphism, then $f$ is a monomorphism.
