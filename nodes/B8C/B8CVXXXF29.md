---
tag: B8CVXXXF29
kind: definition
name: Non-wandering set
msc: [37B20]
defines: EY2W34JZA4
uses: [0CQHFPGJ45, 0VGFHTM75Y, VNW5FHCQ2M, 4SQHHRPKMV, 0AA97XA70K]
sources:
  - url: https://en.wikipedia.org/wiki/Wandering_set
---

## Definition

Let $X$ be a [[topological space|0CQHFPGJ45]] and let $f \colon X \to X$ be a [[continuous map|0VGFHTM75Y]].
A point $x \in X$ is *non-wandering* for $f$ if for every open neighbourhood $U$ of $x$ there is an integer $n \ge 1$ with $f^n(U) \cap U \neq \emptyset$.
The *non-wandering set* $\Omega(f)$ is the set of non-wandering points.

## Remarks

So $x$ is non-wandering exactly when it is not a wandering point in the sense of [[wandering sets|VNW5FHCQ2M]].
The set $\Omega(f)$ is closed, and $f(\Omega(f)) \subseteq \Omega(f)$.
If $X$ is compact and nonempty, then $\Omega(f)$ is nonempty.
Every [[recurrent point|4SQHHRPKMV]], and so every point on a [[periodic orbit|0AA97XA70K]], is non-wandering.
A non-wandering point need not be recurrent.
Example: for $f(x) = x/2$ on $\R$, the point $0$ is fixed, so $0 \in f^n(U) \cap U$ for every neighbourhood $U$ of $0$.
Non-example: for the same map, a point $x > 0$ has the neighbourhood $U = (2x/3, 4x/3)$, and $f^n(U) \subseteq (0, 2x/3]$ for $n \ge 1$, so $f^n(U) \cap U = \emptyset$.
In fact $\Omega(f) = \set{0}$ for this map.

## Explanations

### L1 human

A point is non-wandering when every small region around it comes back, at some later time, to overlap with itself.
The non-wandering set collects these points.
