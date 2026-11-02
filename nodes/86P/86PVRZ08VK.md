---
tag: 86PVRZ08VK
kind: definition
name: Reduced function
msc: [31B05, 31C15, 31D05]
defines: 909B1WYQ4Q
uses: [X4V2S56YQQ, 02BH3MCBQB, RJK6ZKNF6R, C95QJ7YH5T]
sources:
  - url: https://en.wikipedia.org/wiki/Balayage
---

## Definition

Let $n \ge 2$, let $\Omega \subseteq \R^n$ be an [[open set|02BH3MCBQB]], and let $u \ge 0$ be a [[superharmonic function|X4V2S56YQQ]] on $\Omega$.
Let $E \subseteq \Omega$.
The *reduced function* of $u$ on $E$ is the function $R^E_u \colon \Omega \to [0, +\infty]$ given by
$$R^E_u(x) = \inf \set{v(x) : v \ge 0 \text{ is superharmonic on } \Omega \text{ and } v \ge u \text{ on } E}.$$
The *regularised reduced function* $\widehat{R}^E_u$ is its lower semicontinuous regularisation:
$$\widehat{R}^E_u(x) = \min\left(R^E_u(x), \liminf_{y \to x} R^E_u(y)\right).$$

## Remarks

The function $u$ itself is admissible, so $0 \le \widehat{R}^E_u \le R^E_u \le u$, and $R^E_u = u$ on $E$.
By the [[fundamental convergence theorem|RJK6ZKNF6R]], $\widehat{R}^E_u$ is superharmonic and differs from $R^E_u$ only on a [[polar set|C95QJ7YH5T]] contained in $E$.
The function $\widehat{R}^E_u$ is harmonic on $\Omega \setminus \overline{E}$.
Example: let $\Omega = \R^3$, $u = 1$ and $E = \set{x : \abs{x} \le 1}$.
The function $v(x) = \min(1, 1/\abs{x})$ is positive, superharmonic and equal to $1$ on $E$.
Any admissible $v$ satisfies $v \ge 1/\abs{x}$ on $\abs{x} > 1$ by the minimum principle, so $R^E_1 = \widehat{R}^E_1 = \min(1, 1/\abs{x})$.
Non-example of an admissible function: in the same example, the indicator function of the closed ball $E$ equals $u = 1$ on $E$.
It is not superharmonic, since it is not lower semicontinuous at the points of the unit sphere.
Other notations are $R_u^E$, $\operatorname{red}_E u$, and the French name réduite.
