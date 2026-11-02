---
tag: 70KRD7X6SY
kind: definition
name: Hurewicz fibration
msc: [55R05]
defines: Y773B7EQA7
uses: [0CQHFPGJ45, 0VGFHTM75Y, 9YA6S6HD9V, G4QDM01P6J]
sources:
  - url: https://en.wikipedia.org/wiki/Fibration
---

## Definition

Let $E$ and $B$ be [[topological spaces|0CQHFPGJ45]] and let $p \colon E \to B$ be a [[continuous map|0VGFHTM75Y]].
Write $I = [0, 1]$.
The map $p$ is a *Hurewicz fibration* if it has the [[homotopy lifting property|G4QDM01P6J]] with respect to every topological space $X$.
This means the following.
Let $H \colon X \times I \to B$ be a [[homotopy|9YA6S6HD9V]] and let $\tilde{h}_0 \colon X \to E$ be continuous with $p \circ \tilde{h}_0 = H(-, 0)$.
Then there is a homotopy $\tilde{H} \colon X \times I \to E$ with
$$p \circ \tilde{H} = H \quad \text{and} \quad \tilde{H}(-, 0) = \tilde{h}_0.$$

## Remarks

Example: for spaces $B$ and $F$, the projection $p \colon B \times F \to B$ is a Hurewicz fibration.
Given $H$ and $\tilde{h}_0 = (H(-, 0), g)$, the lift $\tilde{H}(x, t) = (H(x, t), g(x))$ works.

Non-example: the inclusion $p \colon \set{0} \to I$ is not a fibration.
Take $X$ a point, $H(t) = t$ and $\tilde{h}_0 = 0$: a lift would satisfy $p(\tilde{H}(1)) = 1$, but $1$ is not in the image of $p$.

Covering maps and fibre bundles over paracompact Hausdorff bases are Hurewicz fibrations.
If $p$ is a Hurewicz fibration and $B$ is path-connected, all fibres $p^{-1}(b)$ are homotopy equivalent.
Every Hurewicz fibration is a [[Serre fibration|PB9JXQ2KC3]], where the lifting property is only required for $X$ a cube $I^n$ or a CW complex, but not conversely.
