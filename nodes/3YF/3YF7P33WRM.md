---
tag: 3YF7P33WRM
kind: definition
name: Steiner symmetrization
msc: [52A20, 52A40]
defines: 8BMM456H7G
uses: [437FSG3419]
sources:
  - url: https://en.wikipedia.org/wiki/Isoperimetric_inequality
---

## Definition

Let $n \ge 2$, let $K \subseteq \R^n$ be a [[convex body|437FSG3419]], and let $u \in \R^n$ be a unit vector.
Let $u^\perp = \set{x \in \R^n : x \cdot u = 0}$.
For $x \in u^\perp$, the set $K \cap \set{x + t u : t \in \R}$ is empty or a closed segment; let $\ell(x)$ be its length when it is nonempty.
The *Steiner symmetrization* of $K$ in the direction $u$ is the set
$$S_u K = \set{x + t u : x \in u^\perp, \ K \cap (x + \R u) \ne \emptyset, \ \abs{t} \le \tfrac{1}{2} \ell(x)}.$$

## Remarks

The set $S_u K$ is again a convex body, it is symmetric under the reflection in $u^\perp$, and it has the same volume as $K$.
Its surface area and its diameter are at most those of $K$.
Example: let $K$ be the triangle with vertices $(0, 0)$, $(2, 0)$, $(0, 2)$ in $\R^2$ and $u = (0, 1)$.
The vertical chord over $x \in [0, 2]$ has length $2 - x$.
So $S_u K = \set{(x, t) : 0 \le x \le 2, \ \abs{t} \le (2 - x)/2}$, the triangle with vertices $(0, 1)$, $(0, -1)$, $(2, 0)$, of area $2$ like $K$.
Non-example: the set $\set{x + t u : 0 \le t \le \ell(x)}$ has the same chord lengths as $S_u K$, but its chords are not centred on $u^\perp$, so it is not the Steiner symmetrization.
Some authors write $\mathrm{st}_u K$ for $S_u K$; the operation is also defined for compact sets, with $\ell(x)$ the one-dimensional measure of the section.
