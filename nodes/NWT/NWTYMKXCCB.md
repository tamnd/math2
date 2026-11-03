---
tag: NWTYMKXCCB
kind: definition
name: Enthalpy method for phase change
msc: ["80A22", "80M20", 35R35]
defines: QTEWT0Z0EF
uses: [3B0HB3DHW1, 722RZK72P5, FN6Z9QKAH5, XBQBT9E7JT, SA40H8EGJZ]
sources:
  - url: https://en.wikipedia.org/wiki/Stefan_problem
---

## Definition

Let $\Omega \subseteq \R^n$ be a domain filled with a material that melts at temperature $T_m$.
Assume for simplicity that solid and liquid have the same density $\rho > 0$, specific heat $c > 0$ and [[thermal conductivity|XBQBT9E7JT]] $k > 0$.
Let $L > 0$ be the [[latent heat|FN6Z9QKAH5]] per unit mass.
Let $H$ be the [[enthalpy|722RZK72P5]] per unit volume, measured from the solid at $T_m$.
The temperature as a function of enthalpy is
$$\beta(H) = \begin{cases} T_m + H / (\rho c), & H < 0, \\ T_m, & 0 \le H \le \rho L, \\ T_m + (H - \rho L)/(\rho c), & H > \rho L. \end{cases}.$$
The *enthalpy formulation* of the [[Stefan problem|3B0HB3DHW1]] is the equation
$$\frac{\partial H}{\partial t} = \nabla \cdot \big( k \nabla \beta(H) \big) \text{ in } \Omega \times (0, \infty).$$
It is understood in the [[weak sense|SA40H8EGJZ]], with the initial enthalpy and boundary conditions for $T = \beta(H)$.
The *enthalpy method* is the numerical solution of this single equation for $H$ on a fixed grid, with the temperature recovered as $T = \beta(H)$.
The solid region is $\set{H < 0}$, the liquid region is $\set{H > \rho L}$, and the set $\set{0 \le H \le \rho L}$ contains the phase boundary.

## Remarks

Where the solution is smooth and away from the front, the equation is the heat equation $\rho c\, T_t = k \Delta T$.
Across a sharp front, the weak form encodes the Stefan condition that the jump of the heat flux equals $\rho L$ times the normal speed of the front.
Example: an explicit scheme in one dimension updates $H_j^{n+1} = H_j^n + (k \Delta t / \Delta x^2)\big(T_{j+1}^n - 2 T_j^n + T_{j-1}^n\big)$ with $T_j^n = \beta(H_j^n)$.
A cell with $H_j = \rho L / 2$ has temperature $T_m$ and is half melted, since its liquid fraction is $H_j / (\rho L)$.
Non-example: a front-tracking method moves a grid point with the interface and imposes the Stefan condition there.
It is not an enthalpy method, because it treats the front as an explicit unknown.
The function $\beta$ is continuous and nondecreasing but not strictly increasing, so the equation is a degenerate parabolic equation.
