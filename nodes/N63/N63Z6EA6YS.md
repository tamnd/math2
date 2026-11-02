---
tag: N63Z6EA6YS
kind: example
name: Smale horseshoe
msc: [37D05, 37B10]
instance_of: [MPFD24TYW2]
illustrates: [EWFWTSVY0B]
uses: [0BXNDZFQME, HNXXAPQKG3]
sources:
  - url: https://en.wikipedia.org/wiki/Horseshoe_map
same_as:
  wikidata: Q557781
  wikipedia: Horseshoe map
---

## Example

Let $Q = [0,1]^2$, and let $H_0 = [0,1] \times [0, \tfrac13]$ and $H_1 = [0,1] \times [\tfrac23, 1]$ be two horizontal strips.
Consider a diffeomorphism $f$ of the plane that bends $Q$ into a horseshoe shape and is affine on the strips:
$$f(x, y) = \left(\tfrac{x}{3}, \; 3y\right) \text{ on } H_0, \qquad f(x, y) = \left(1 - \tfrac{x}{3}, \; 3 - 3y\right) \text{ on } H_1.$$
Then $f(H_0) = [0, \tfrac13] \times [0,1]$ and $f(H_1) = [\tfrac23, 1] \times [0, 1]$, and the middle strip of $Q$ is mapped outside $Q$.
Let $\Lambda = \bigcap_{n \in \Z} f^n(Q)$ be the set of points whose whole orbit stays in $Q$.

Check of the structure.
Consider the maps $y \mapsto 3y$ on $[0, \tfrac13]$ and $y \mapsto 3 - 3y$ on $[\tfrac23, 1]$.
A point stays in $Q$ for all forward times exactly when its $y$-coordinate never leaves $[0, \tfrac13] \cup [\tfrac23, 1]$ under these maps.
This means that $y$ lies in the middle-thirds [[Cantor set|0BXNDZFQME]] $C$.
By the same argument for $f^{-1}$, a point stays in $Q$ for all backward times exactly when $x \in C$.
So $\Lambda = C \times C$, a Cantor set.
The map $h \colon \Lambda \to \set{0,1}^{\Z}$, with $h(p)_n = i$ when $f^n(p) \in H_i$, is a homeomorphism with $h \circ f = \sigma \circ h$, so $f|_\Lambda$ is [[topologically conjugate|HNXXAPQKG3]] to the full shift on two symbols.
On $\Lambda$, $Df$ equals $\operatorname{diag}(\tfrac13, 3)$ or $\operatorname{diag}(-\tfrac13, -3)$.
So the horizontal direction is contracted and the vertical one expanded by the factor $3$, and $\Lambda$ is a [[hyperbolic set|MPFD24TYW2]] with $C = 1$ and $\lambda = \tfrac13$.

## Remarks

Through the conjugacy, $f|_\Lambda$ has $2^n$ points of period dividing $n$, a dense orbit, and topological entropy $\log 2$.
Hyperbolicity makes the horseshoe robust: every diffeomorphism $C^1$-close to $f$ has an invariant Cantor set on which it is conjugate to the same shift.
Smale showed that a transverse homoclinic point of a diffeomorphism produces a horseshoe for some iterate, which explains why such points imply chaotic behaviour.

## Explanations

### L1 human

Take a square, stretch it to a long thin strip, bend the strip into a horseshoe, and lay it back across the square.
Some points leave the square, and the points that stay forever form a dust of points, a Cantor set.
Each such point is described by an infinite list of $0$s and $1$s, telling whether it is in the lower or the upper part of the square at each time.
Every list occurs, so the motion is as unpredictable as tossing a coin, yet it comes from a simple smooth map.
