---
tag: R50ERM9AHR
kind: definition
name: Cauchy–Riemann operator
msc: [32W05, 35J46, 30A99]
defines: PPSSTHTEDE
uses: [09EGC6F8PT, 0NAHXR1FRH, 0T71SSYZ39]
sources:
  - url: https://en.wikipedia.org/wiki/Cauchy%E2%80%93Riemann_equations
---

## Definition

Let $\Omega \subseteq \C$ be an open set, and write $z = x + iy$ with $x, y$ real.
For a function $f \colon \Omega \to \C$ that has [[partial derivatives|09EGC6F8PT]] $\partial_x f$ and $\partial_y f$, the *Cauchy–Riemann operator* applied to $f$ is
$$\frac{\partial f}{\partial \bar z} = \frac12 \left( \frac{\partial f}{\partial x} + i \frac{\partial f}{\partial y} \right).$$
It is also written $\bar\partial f$.

## Remarks

Writing $f = u + iv$ with $u, v$ real, $\partial f / \partial \bar z = 0$ is equivalent to $u_x = v_y$ and $u_y = -v_x$, the [[Cauchy–Riemann equations|0T71SSYZ39]].
So a continuously differentiable function $f$ on $\Omega$ is [[holomorphic|0NAHXR1FRH]] if and only if $\partial f / \partial \bar z = 0$ on $\Omega$.
Example: $\partial z / \partial \bar z = \tfrac12 (1 + i \cdot i) = 0$, so $z$ is in the kernel.
Non-example: $\partial \bar z / \partial \bar z = \tfrac12 (1 + i \cdot (-i)) = 1 \ne 0$, so $\bar z$ is not holomorphic.
The companion operator $\partial / \partial z = \tfrac12 (\partial_x - i \partial_y)$ satisfies $4 \, \partial_z \partial_{\bar z} = \Delta$.
In distributions on $\C$, $\partial_{\bar z} \big( 1/(\pi z) \big) = \delta_0$, the Dirac measure at $0$.
