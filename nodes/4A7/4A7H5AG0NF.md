---
tag: 4A7H5AG0NF
kind: definition
name: Homotopic maps
msc: [55Q05, 55P10]
defines: F2F143KQ2M
uses: [9YA6S6HD9V, 0VGFHTM75Y, 0G8VEZ3WTK]
sources:
  - url: https://en.wikipedia.org/wiki/Homotopy
---

## Definition

Let $X$ and $Y$ be topological spaces and let $f, g \colon X \to Y$ be [[continuous maps|0VGFHTM75Y]].
The maps $f$ and $g$ are *homotopic*, written $f \simeq g$, if there is a [[homotopy|9YA6S6HD9V]] from $f$ to $g$.

## Remarks

The relation $\simeq$ is an [[equivalence relation|0G8VEZ3WTK]] on the set of continuous maps $X \to Y$.
Reflexivity uses the constant homotopy $H(x, t) = f(x)$, symmetry reverses time, and transitivity runs two homotopies one after the other, each at double speed.
The equivalence class of $f$ is its *homotopy class* $[f]$, and the set of classes is written $[X, Y]$.
Homotopy is compatible with composition: if $f \simeq f'$ and $g \simeq g'$, then $g \circ f \simeq g' \circ f'$.
Example: the maps $f(x) = x$ and $g(x) = 0$ from $[0, 1]$ to $\R$ are homotopic via $H(x, t) = (1 - t)x$.
Non-example: the identity of the [[circle|060W5CBZP6]] $S^1$ and a constant map $S^1 \to S^1$ are not homotopic, because they induce different maps on the [[fundamental group|S1XK3HXHFX]].
