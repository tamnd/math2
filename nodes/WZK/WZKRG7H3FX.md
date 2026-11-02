---
tag: WZKRG7H3FX
kind: definition
name: Lie symmetry method
msc: [34C14, 34A05]
defines: X3S9XHX83H
uses: [0P97V20RW7, 05AXG3QRKR, 0BW9N5CDSB]
sources:
  - url: https://en.wikipedia.org/wiki/Lie_point_symmetry
---

## Definition

Let $U \subseteq \R^2$ be open and let $\omega : U \to \R$ be smooth; consider the [[ordinary differential equation|0P97V20RW7]] $y' = \omega(x, y)$.
Let $\Gamma_\varepsilon : (x, y) \mapsto (\hat x, \hat y)$ be a smooth local one-parameter group of maps, with $\Gamma_0 = \id$ and $\Gamma_\varepsilon \circ \Gamma_\delta = \Gamma_{\varepsilon + \delta}$.
It is a *Lie point symmetry* of the equation if it maps graphs of solutions to graphs of solutions.
Its infinitesimal generator is the vector field $X = \xi \partial_x + \eta \partial_y$ with $\xi = \partial \hat x / \partial \varepsilon$ and $\eta = \partial \hat y / \partial \varepsilon$ at $\varepsilon = 0$.
The group is a symmetry if and only if the linearized symmetry condition holds:
$$\eta_x + (\eta_y - \xi_x)\, \omega - \xi_y\, \omega^2 = \xi\, \omega_x + \eta\, \omega_y,$$
where subscripts denote [[partial derivatives|05AXG3QRKR]].
The *Lie symmetry method* solves the equation from a known symmetry, near a point where $X \ne 0$, as follows.

1. Find canonical coordinates $(r, s)$, functions of $(x, y)$ with $X r = 0$ and $X s = 1$.
2. In these coordinates the equation takes the form $ds/dr = \Omega(r)$, with no dependence on $s$.
3. Integrate: $s = \int \Omega(r)\, dr + C$, then return to $(x, y)$.

## Remarks

Example: for $\omega(x, y) = F(y/x)$, the scalings $(x, y) \mapsto (e^\varepsilon x, e^\varepsilon y)$ have generator $X = x \partial_x + y \partial_y$.
Check of the condition: the left side is $0 + (1 - 1)\omega - 0 = 0$, and the right side is $x \cdot (-y/x^2) F' + y \cdot (1/x) F' = 0$.
Canonical coordinates are $r = y/x$ and $s = \ln\abs{x}$, since $X r = -y/x + y/x = 0$ and $X s = 1$.
Then $ds/dr = 1/(F(r) - r)$, and the equation is solved by an [[antiderivative|0BW9N5CDSB]].
Non-example: the translations $(x, y) \mapsto (x, y + \varepsilon)$ are not symmetries of $y' = x y$, since $\xi = 0$, $\eta = 1$ give left side $0$ and right side $\omega_y = x \ne 0$.
For equations of order $n$, a symmetry reduces the order by one.
