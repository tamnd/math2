---
tag: EFJ77PFF88
kind: definition
name: Cofibration
msc: [55P05]
defines: W5WS5EY8ZM
uses: [9YA6S6HD9V, D42X0F1EG1, 0VGFHTM75Y]
sources:
  - url: https://en.wikipedia.org/wiki/Cofibration
---

## Definition

Let $A$ and $X$ be topological spaces and let $I = [0, 1]$.
Let $i \colon A \to X$ be a [[continuous map|0VGFHTM75Y]].
The map $i$ is a *cofibration* if the following holds for every topological space $Y$.
For every continuous map $f \colon X \to Y$ and every [[homotopy|9YA6S6HD9V]] $h \colon A \times I \to Y$ with $h(a, 0) = f(i(a))$ for all $a \in A$, there is a homotopy $H \colon X \times I \to Y$ with:

1. $H(x, 0) = f(x)$ for all $x \in X$;
2. $H(i(a), t) = h(a, t)$ for all $a \in A$ and $t \in I$.

## Remarks

For the inclusion of a subspace $A \subseteq X$, this says that the pair $(X, A)$ has the [[homotopy extension property|D42X0F1EG1]].
Every cofibration is a homeomorphism onto its image, and if $X$ is Hausdorff the image is closed in $X$.
Example: the inclusion $S^{n-1} \to D^n$ is a cofibration, and so is the inclusion of a subcomplex of a CW complex.
Non-example: the inclusion $(0, 1) \to [0, 1]$ is not a cofibration, since $[0, 1]$ is Hausdorff and $(0, 1)$ is not closed in it.
Cofibrations are stable under pushout and under composition.
