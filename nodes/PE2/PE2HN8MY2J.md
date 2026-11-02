---
tag: PE2HN8MY2J
kind: definition
name: Projection body
msc: [52A20, 52A21, 52A40]
defines: G7WP728SZH
uses: [437FSG3419, 1H92CYA4ZC, 0Q8HZTJC7G, ZMZZ2QRFTZ]
sources:
  - url: https://en.wikipedia.org/wiki/Projection_body
---

## Definition

Let $n \ge 2$, and let $K \subseteq \R^n$ be a [[convex body|437FSG3419]].
For a nonzero vector $u$, let $K | u^\perp$ be the [[orthogonal projection|0Q8HZTJC7G]] of $K$ onto the hyperplane $u^\perp = \set{x : x \cdot u = 0}$.
Let $\mathrm{vol}_{n-1}$ be the $(n-1)$-dimensional volume in $u^\perp$.
The *projection body* of $K$ is the convex body $\Pi K$ whose [[support function|1H92CYA4ZC]] is
$$h_{\Pi K}(x) = \abs{x} \, \mathrm{vol}_{n-1}\bigl(K | x^\perp\bigr) \quad \text{for } x \ne 0, \qquad h_{\Pi K}(0) = 0.$$

## Remarks

That this function is a support function follows from Cauchy's projection formula $\mathrm{vol}_{n-1}(K | u^\perp) = \frac{1}{2} \int_{S^{n-1}} \abs{u \cdot v} \, dS_K(v)$, where $S_K$ is the surface area measure of $K$.
The formula also shows that $\Pi K$ is symmetric about the origin and is a [[zonoid|ZMZZ2QRFTZ]].
Example: let $C = [0, 1]^n$.
For a unit vector $u$, the shadow of $C$ on $u^\perp$ has volume $\abs{u_1} + \cdots + \abs{u_n}$.
This is the support function of $[-1, 1]^n$ at $u$, so $\Pi C = [-1, 1]^n$.
Non-example: for $n \ge 3$, every projection of a segment $K$ has $(n-1)$-volume $0$.
So the formula gives $h = 0$ and the set $\set{0}$, which is not a convex body; this is why $K$ must have nonempty interior.
For the unit ball $B$, every shadow is an $(n-1)$-ball, so $\Pi B = \omega_{n-1} B$, with $\omega_{n-1}$ the volume of the unit ball of $\R^{n-1}$.
