---
tag: V0SCWNM4VR
kind: definition
name: Vogan diagram
msc: [17B20, 17B22]
defines: N8J09DSEVH
uses: [EY9DN7QAX1, 59DHW3BZTW, BB098JPWGA, CSBM217V1N, CS73JZQS66, K7VVYFE9YJ]
sources:
  - url: https://en.wikipedia.org/wiki/Vogan_diagram
---

## Definition

Let $\mathfrak{g}_0$ be a real [[semisimple Lie algebra|EY9DN7QAX1]] with complexification $\mathfrak{g}$.
Let $\theta$ be a Cartan involution of $\mathfrak{g}_0$, with [[Cartan decomposition|K7VVYFE9YJ]] $\mathfrak{g}_0 = \mathfrak{k}_0 \oplus \mathfrak{p}_0$.
Let $\mathfrak{h}_0 = \mathfrak{t}_0 \oplus \mathfrak{a}_0$ be a $\theta$-stable [[Cartan subalgebra|BB098JPWGA]] with $\mathfrak{t}_0 \subseteq \mathfrak{k}_0$ and $\mathfrak{a}_0 \subseteq \mathfrak{p}_0$, chosen so that $\dim \mathfrak{t}_0$ is as large as possible.
Let $\Delta$ be the set of roots of $\mathfrak{g}$ with respect to the complexification $\mathfrak{h}$ of $\mathfrak{h}_0$.
Choose positive roots $\Delta^+$ from an ordering in which $i\mathfrak{t}_0$ comes before $\mathfrak{a}_0$.
Then $\theta \Delta^+ = \Delta^+$.
So $\theta$ permutes the [[simple roots|CSBM217V1N]] of $\Delta^+$.
Each simple root fixed by $\theta$ is imaginary, that is, it vanishes on $\mathfrak{a}_0$.
Let $\mathfrak{k}$ and $\mathfrak{p}$ be the complexifications of $\mathfrak{k}_0$ and $\mathfrak{p}_0$.
An imaginary root $\alpha$ is *compact* if its root space lies in $\mathfrak{k}$, and *noncompact* if it lies in $\mathfrak{p}$.

The *Vogan diagram* of $(\mathfrak{g}_0, \mathfrak{h}_0, \Delta^+)$ is the [[Dynkin diagram|CS73JZQS66]] of $\Delta^+$ with these marks:

1. Each pair of simple roots exchanged by $\theta$ is joined by a two-headed arrow.
2. Each simple root fixed by $\theta$ is painted if it is noncompact, and left unpainted if it is compact.

## Remarks

Example: for $\mathfrak{g}_0 = \mathfrak{sl}_2(\R)$, the subalgebra $\mathfrak{so}(2)$ of skew-symmetric matrices is a Cartan subalgebra inside $\mathfrak{k}_0 = \mathfrak{so}(2)$, so $\mathfrak{a}_0 = 0$.
The one simple root is imaginary, and its root space is spanned by a complex matrix outside $\mathfrak{so}(2) \otimes \C$, so the root is noncompact.
The Vogan diagram is one painted dot; for the compact form $\mathfrak{su}(2)$ it is one unpainted dot.
Non-example: for $\mathfrak{sl}_2(\R)$ with the Cartan subalgebra of diagonal matrices, $\mathfrak{t}_0 = 0$, so $\dim \mathfrak{t}_0$ is not maximal; the root is real and the painting rule does not apply.
Every real semisimple Lie algebra has a Vogan diagram, and the diagram determines $\mathfrak{g}_0$ up to isomorphism.
Different choices of $\Delta^+$ can give different diagrams for the same algebra.
The arrows record the automorphism of the Dynkin diagram induced by $\theta$.
There are no arrows exactly when $\mathfrak{a}_0 = 0$, that is, when $\mathfrak{g}_0$ has a Cartan subalgebra inside $\mathfrak{k}_0$.
