---
tag: 6JTAZHMRKB
kind: definition
name: Lp spaces on groups
msc: [43A15, "46E30"]
defines: VVE1P3SM6E
uses: [AHV05ZBCYW, VY0HXD3GC4, SASP14MA1Z]
sources:
  - url: https://en.wikipedia.org/wiki/Lp_space
---

## Definition

Let $G$ be a [[locally compact group|AHV05ZBCYW]] with a left [[Haar measure|VY0HXD3GC4]] $\mu$, and let $1 \le p \le \infty$.
The space $L^p(G)$ is the [[Lp space|SASP14MA1Z]] $L^p(G, \mu)$.
It consists of the measurable functions $f \colon G \to \C$ with $\norm{f}_p < \infty$, modulo equality almost everywhere, where
$$\norm{f}_p = \left( \int_G \abs{f(x)}^p \, d\mu(x) \right)^{1/p} \quad (p < \infty)$$
and $\norm{f}_\infty$ is the essential supremum of $\abs{f}$.
For $y \in G$, the *left translate* of $f$ is $(L_y f)(x) = f(y^{-1}x)$.

## Remarks

Another Haar measure $c\mu$ gives the same space with the norm multiplied by $c^{1/p}$, so $L^p(G)$ does not depend on the choice of $\mu$ up to isometric scaling.
Each $L_y$ is a linear isometry of $L^p(G)$, since $\mu$ is left-invariant.
For $1 \le p < \infty$ and $f \in L^p(G)$, the map $y \mapsto L_y f$ from $G$ to $L^p(G)$ is continuous.
For groups that are not $\sigma$-compact, $L^\infty(G)$ is usually defined modulo locally null sets, so that it is the dual of $L^1(G)$.

Example: $G = \Z$ with counting measure, a Haar measure.
Then $L^p(\Z) = \ell^p(\Z)$, and $L_m$ shifts a sequence: $(L_m a)_n = a_{n - m}$, which keeps $\sum_n \abs{a_n}^p$.

Non-example of continuity for $p = \infty$: let $f = \mathbf{1}_{[0, \infty)}$ on $\R$.
For $y > 0$, $L_y f - f = -\mathbf{1}_{[0, y)}$, so $\norm{L_y f - f}_\infty = 1$ for every $y > 0$, and $L_y f$ does not tend to $f$ as $y \to 0$.
