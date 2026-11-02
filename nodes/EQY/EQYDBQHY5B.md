---
tag: EQYDBQHY5B
kind: definition
name: Morphism of schemes
msc: [14A15]
defines: JXRKH6P1Z4
uses: [5A35TYZD02, B7FPT8JTXR, P8YTMGEN9R, 0VGFHTM75Y]
sources:
  - url: https://en.wikipedia.org/wiki/Morphism_of_schemes
---

## Definition

Let $X$ and $Y$ be [[schemes|5A35TYZD02]].
A *morphism of schemes* $X \to Y$ is a morphism of [[locally ringed spaces|B7FPT8JTXR]], that is, a pair $(f, f^\#)$ such that:

1. $f \colon X \to Y$ is a [[continuous map|0VGFHTM75Y]].
2. $f^\# \colon \mathcal{O}_Y \to f_* \mathcal{O}_X$ is a morphism of sheaves of rings, so for each open $V \subseteq Y$ it gives a ring map $\mathcal{O}_Y(V) \to \mathcal{O}_X(f^{-1}(V))$, compatible with restrictions.
3. For every $x \in X$, the induced map of stalks $f^\#_x \colon \mathcal{O}_{Y,f(x)} \to \mathcal{O}_{X,x}$ is a [[local homomorphism|P8YTMGEN9R]].

The composite of $(f, f^\#) \colon X \to Y$ and $(g, g^\#) \colon Y \to Z$ is $(g \circ f, g_*(f^\#) \circ g^\#)$.

## Remarks

Example: a ring homomorphism $\varphi \colon A \to B$ gives a morphism $\operatorname{Spec} B \to \operatorname{Spec} A$ with $f(\mathfrak{q}) = \varphi^{-1}(\mathfrak{q})$.
On stalks it is the map $A_{\varphi^{-1}(\mathfrak q)} \to B_{\mathfrak q}$, which sends the maximal ideal into $\mathfrak{q} B_{\mathfrak q}$, so it is local.
Non-example: let $R$ be a discrete valuation ring with fraction field $K$.
Let $f$ send the single point of $\operatorname{Spec} K$ to the closed point of $\operatorname{Spec} R$, and let $f^\#$ come from the inclusion $R \to K$.
This is a morphism of ringed spaces, but it fails clause 3.
The stalk map $R \to K$ is not local, since it sends the maximal ideal of $R$ into the units of $K$.
