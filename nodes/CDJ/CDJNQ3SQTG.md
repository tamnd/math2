---
tag: CDJNQ3SQTG
kind: definition
name: Lipschitz domain
msc: [31B25, 35J25, 26B35]
defines: 1GNKQ7NBAG
uses: [02BH3MCBQB, 0AW1E6YTJY, 05D5EGMFYV, 0DC3MPR7C9]
sources:
  - url: https://en.wikipedia.org/wiki/Lipschitz_domain
---

## Definition

Let $n \ge 2$ and let $\Omega \subseteq \R^n$ be an [[open set|02BH3MCBQB]].
The set $\Omega$ is a *Lipschitz domain* if for every point $p$ of its [[boundary|05D5EGMFYV]] $\partial\Omega$ there are:

1. a radius $r > 0$;
2. a rigid motion of $\R^n$ giving coordinates $x = (x', x_n)$ with $x' \in \R^{n-1}$ and $x_n \in \R$;
3. a [[Lipschitz|0AW1E6YTJY]] function $\varphi \colon \R^{n-1} \to \R$,

such that, in these coordinates,
$$\Omega \cap B(p, r) = \set{x \in B(p, r) : x_n > \varphi(x')},$$
where $B(p, r)$ is the [[open ball|0DC3MPR7C9]] of radius $r$ about $p$.

## Remarks

It follows that $\partial\Omega \cap B(p, r) = \set{x \in B(p, r) : x_n = \varphi(x')}$.
Many authors also require $\Omega$ to be bounded, and sometimes connected.
If $\Omega$ is bounded, finitely many such charts cover $\partial\Omega$, so one can use a common radius and a common Lipschitz constant.
These numbers are called the Lipschitz character of $\Omega$.
Example: the square $(0, 1)^2$.
Near an edge point the square is the region above a horizontal line.
Near the corner $(0, 0)$, in coordinates rotated by $45$ degrees, it is the region $\set{x_2 > \abs{x_1}}$ near the corner, and $\abs{x_1}$ is Lipschitz with constant $1$.
Non-example: the slit disc $\set{\abs{z} < 1} \setminus [0, 1)$ in $\R^2$.
Near the point $1/2$ of the slit, the set lies on both sides of the slit, so it cannot be the region on one side of a graph.
Every bounded open set with $C^1$ boundary is a Lipschitz domain.
