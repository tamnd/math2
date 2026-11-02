---
tag: FZ6RYHNRWN
kind: definition
name: Zariski tangent space
msc: [14A10, 14B05]
defines: E7A5DHFT01
uses: [JERVQT4C12, HH6VEVM6Z0, 09EGC6F8PT, 047NDTEPCV, G9WB27VWP7, 0PV74TR5FP, Z1CGB483J6, 000AYPA9AJ, MZ02BKPHJA]
sources:
  - url: https://en.wikipedia.org/wiki/Zariski_tangent_space
---

## Definition

Let $k$ be an algebraically closed field, let $X \subseteq k^n$ be an [[affine variety|JERVQT4C12]] with [[ideal|HH6VEVM6Z0]] $I(X)$, and let $p \in X$.
For $f \in k[x_1, \dots, x_n]$, its differential at $p$ is the linear form
$$d_p f(v) = \sum_{i=1}^{n} \frac{\partial f}{\partial x_i}(p) \, v_i, \qquad v \in k^n,$$
with the formal [[partial derivatives|09EGC6F8PT]].
The *Zariski tangent space* of $X$ at $p$ is the linear subspace
$$T_p X = \set{v \in k^n : d_p f(v) = 0 \text{ for all } f \in I(X)}.$$

## Remarks

If $I(X) = (f_1, \dots, f_r)$, then $T_p X$ is the kernel of the [[Jacobian matrix|047NDTEPCV]] $\left(\frac{\partial f_j}{\partial x_i}(p)\right)$, because $d_p(gf) = g(p) \, d_p f$ when $f(p) = 0$.

Intrinsic form: let $\mathfrak m_p$ be the [[maximal ideal|0PV74TR5FP]] of the [[coordinate ring|G9WB27VWP7]] $k[X]$ of functions vanishing at $p$.
Then $T_p X$ is isomorphic to the dual [[vector space|000AYPA9AJ]] of $\mathfrak m_p / \mathfrak m_p^2$.
The same space is the dual of the [[cotangent space|Z1CGB483J6]] of the [[local ring|MZ02BKPHJA]] $k[X]_{\mathfrak m_p}$, so $T_p X$ only depends on a neighbourhood of $p$ and is defined for every variety.

Example: for the parabola $X = V(y - x^2)$ at $p = (a, a^2)$, $d_p(y - x^2) = -2a \, v_1 + v_2$, so $T_p X$ is the line $v_2 = 2a v_1$, of dimension $1$.

Example: for the cusp $X = V(y^2 - x^3)$ at the origin, the polynomial $y^2 - x^3$ generates $I(X)$ and both of its partial derivatives vanish at $(0, 0)$, so $T_{(0,0)} X = k^2$ has dimension $2 > \dim X = 1$.

One always has $\dim T_p X \ge \dim X$.
