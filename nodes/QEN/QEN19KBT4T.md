---
tag: QEN19KBT4T
kind: definition
name: Method of characteristics in gas dynamics
msc: [76N15, 35L60]
defines: 6R71SY5N3Q
uses: [7XAPBCJK3B, RW0JK9VDZE, SN4J6KP03C, GB7R2ERCTA]
sources:
  - url: https://en.wikipedia.org/wiki/Method_of_characteristics
---

## Definition

Consider one-dimensional isentropic flow of a polytropic gas with adiabatic exponent $\gamma > 1$.
The unknowns are the density $\rho(x, t) > 0$ and the velocity $u(x, t)$, and the pressure is $p = K \rho^\gamma$ with a constant $K > 0$.
The [[Euler equations|RW0JK9VDZE]] are
$$\rho_t + (\rho u)_x = 0, \qquad u_t + u u_x + \frac{p_x}{\rho} = 0.$$
Let $c = \sqrt{\gamma p / \rho}$ be the [[speed of sound|SN4J6KP03C]].
For a $C^1$ solution, the $C_+$ characteristics are the curves with $\dfrac{dx}{dt} = u + c$, and the $C_-$ characteristics are the curves with $\dfrac{dx}{dt} = u - c$.
The [[Riemann invariants|GB7R2ERCTA]] of the flow are
$$r = u + \frac{2c}{\gamma - 1}, \qquad s = u - \frac{2c}{\gamma - 1}.$$
The *method of characteristics* is the construction of the solution from the following facts.

1. The quantity $r$ is constant along each $C_+$ characteristic.
2. The quantity $s$ is constant along each $C_-$ characteristic.
3. The flow is recovered from $u = \dfrac{r + s}{2}$ and $c = \dfrac{(\gamma - 1)(r - s)}{4}$.

## Remarks

Facts 1 and 2 follow from the equations: for a $C^1$ solution, $r_t + (u + c) r_x = 0$ and $s_t + (u - c) s_x = 0$.
In practice one starts from the data on an initial line, follows both families of curves, and updates $u$ and $c$ at each crossing point.

Example: a gas at rest with constant sound speed $c_0$ has $r = 2c_0/(\gamma - 1)$ and $s = -2c_0/(\gamma - 1)$ everywhere.
The characteristics are the straight lines $x = x_0 + c_0 t$ and $x = x_0 - c_0 t$, and indeed $u = (r + s)/2 = 0$ and $(\gamma - 1)(r - s)/4 = c_0$.
If $s$ is constant in a whole region, the flow is a simple wave and all $C_+$ characteristics there are straight lines.

Non-example: across a [[shock wave|FRVV0NHBXT]] the solution is not $C^1$, so the method does not apply there.
The invariants jump across the shock, and the entropy changes, so the isentropic relation $p = K\rho^\gamma$ fails behind a strong shock.
For non-isentropic flow a third family of characteristics, the particle paths $dx/dt = u$, carries the entropy.

In steady two-dimensional supersonic flow the characteristics are the [[Mach lines|C5QBSMGHCR]].
Along each family of Mach lines one of the two quantities $\theta + \nu(M)$ and $\theta - \nu(M)$ is constant, where $\theta$ is the flow angle and $\nu$ is the [[Prandtl–Meyer function|88XSF5YV97]].
