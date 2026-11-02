---
tag: HJEFC4CC6M
kind: definition
name: Relative homotopy
msc: [55Q05, 55P10]
defines: ADDS6HE5SV
uses: [9YA6S6HD9V, 0WS9P12FQR]
sources:
  - url: https://en.wikipedia.org/wiki/Homotopy
---

## Definition

Let $X$ and $Y$ be topological spaces and let $A \subseteq X$.
Let $f, g \colon X \to Y$ be continuous maps with $f(a) = g(a)$ for all $a \in A$.
A *homotopy from $f$ to $g$ relative to $A$* is a [[homotopy|9YA6S6HD9V]] $H$ from $f$ to $g$ with $H(a, t) = f(a)$ for all $a \in A$ and $t \in [0, 1]$.
The maps $f$ and $g$ are *homotopic relative to $A$*, written $f \simeq g \ (\mathrm{rel}\ A)$, if such a homotopy exists.

## Remarks

For $A = \emptyset$ this is an ordinary homotopy.
Being homotopic relative to $A$ is an equivalence relation on the continuous maps $X \to Y$ that agree with a given map on $A$.
Example: for $X = [0, 1]$, $A = \set{0, 1}$, $Y = \R^2$, and two paths $f, g$ with $f(0) = g(0)$ and $f(1) = g(1)$, the map $H(s, t) = (1 - t) f(s) + t g(s)$ is a homotopy relative to $A$, since $H(0, t) = f(0)$ and $H(1, t) = f(1)$.
Non-example: in $\R^2 \setminus \set{0}$, the upper and lower half circles from $(1, 0)$ to $(-1, 0)$ are homotopic as maps, since $[0, 1]$ is contractible, but they are not homotopic relative to $\set{0, 1}$.
