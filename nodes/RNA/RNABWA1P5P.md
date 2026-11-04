---
tag: RNABWA1P5P
kind: proof
name: Proof that a convex function on an open interval is continuous
msc: [26A51]
proves: 011HV2GAWF
uses: [0BY5FTHEEE, 0VV0HSW1ZS, 0P27W9RW0G, 0EEE2CZB2A]
sources:
  - url: https://proofwiki.org/wiki/Convex_Real_Function_is_Continuous
---

## Proof

We use the slope inequalities to bound chord slopes from a fixed point, which gives a local Lipschitz bound.

1. Fix $y \in I$. Since $I$ is open, there are $x, z \in I$ with $x < y < z$.
2. For $w \in I$ with $w \ne y$, let $\sigma(w) = \dfrac{f(w) - f(y)}{w - y}$. Note that $\sigma(w)$ is also $\dfrac{f(y) - f(w)}{y - w}$.
3. Let $s_- = \dfrac{f(y) - f(x)}{y - x}$ and $s_+ = \dfrac{f(z) - f(y)}{z - y}$.
4. Let $y < w < z$. The [[slope inequalities|0BY5FTHEEE]] for $x < y < w$, first against last quotient, give $s_- \le \sigma(w)$.
5. The slope inequalities for $y < w < z$, first against middle quotient, give $\sigma(w) \le s_+$.
6. Let $x < w < y$. The slope inequalities for $x < w < y$, middle against last quotient, give $s_- \le \sigma(w)$.
7. The slope inequalities for $w < y < z$, first against last quotient, give $\sigma(w) \le s_+$.
8. So $s_- \le \sigma(w) \le s_+$ for all $w \in (x, z)$ with $w \ne y$. Let $C = \abs{s_-} + \abs{s_+}$. Then $\abs{\sigma(w)} \le C$.
9. Hence $\abs{f(w) - f(y)} \le C \abs{w - y}$ for all $w \in (x, z)$. For $w = y$ this is trivial.
10. Let $V$ be an open interval containing $f(y)$. Choose $\varepsilon > 0$ with $(f(y) - \varepsilon, f(y) + \varepsilon) \subseteq V$.
11. Let $\delta = \min\set{y - x, \, z - y, \, \varepsilon/(C + 1)}$ and $U = (y - \delta, y + \delta)$. Then $U \subseteq (x, z)$.
12. For $w \in U$, step 9 gives $\abs{f(w) - f(y)} \le C \delta \le C \varepsilon/(C + 1) < \varepsilon$. So $f(w) \in V$.
13. Thus $f$ is [[continuous at|0EEE2CZB2A]] $y$. Since $y \in I$ was arbitrary, $f$ is [[continuous|0P27W9RW0G]] on $I$.

## Idea

Near an interior point $y$, every chord slope from $y$ is squeezed between two fixed slopes. They are the slopes from a point on the left and to a point on the right. Bounded slopes mean $f(w)$ is within a constant times $\abs{w - y}$ of $f(y)$. Openness of $I$ is what gives room on both sides of $y$.
