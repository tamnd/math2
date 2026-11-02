---
tag: NPS5GGXBDP
kind: definition
name: Topological mixing
msc: [37B02, 37B05]
defines: B763QH5521
uses: [0CQHFPGJ45, 0VGFHTM75Y, 02BH3MCBQB, FR49Y9GQHR]
sources:
  - url: https://en.wikipedia.org/wiki/Mixing_(mathematics)
---

## Definition

Let $X$ be a [[topological space|0CQHFPGJ45]] and let $f \colon X \to X$ be a [[continuous map|0VGFHTM75Y]].
The map $f$ is *topologically mixing* if for all nonempty [[open sets|02BH3MCBQB]] $U, V \subseteq X$ there is $N \ge 1$ with $f^n(U) \cap V \neq \emptyset$ for every $n \ge N$.

## Remarks

Every topologically mixing map is [[topologically transitive|FR49Y9GQHR]].
Example: the doubling map $f(x) = 2x \bmod 1$ on the circle $\R / \Z$.
A nonempty open set $U$ contains an open arc of length $\ell > 0$; choose $k$ with $2^k \ell > 1$.
The map $f^n$ multiplies lengths of small arcs by $2^n$, so for $n \ge k$ the image $f^n(U)$ is the whole circle and meets every $V$.
Non-example: the rotation $f(x) = x + \alpha \bmod 1$ with $\alpha$ irrational, and $U = V = (-1/8, 1/8)$.
Here $f^n(U) \cap U \neq \emptyset$ only when $n\alpha$ is within $1/4$ of an integer.
By Weyl's equidistribution theorem, about half of all $n$ fail this, so there is no $N$ as required.

## Explanations

### L1 human

A mixing map brings each open region into each other open region and keeps it meeting that region at all large times.
