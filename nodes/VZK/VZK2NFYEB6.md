---
tag: VZK2NFYEB6
kind: problem
name: Graetz problem
msc: [80A19, 76R05, 35K20]
uses: [QFBG7W198Q, THH3V9AHDN, CS4ZZX092Z, 47NFRVB564, 7WV6B2502K]
about: [QFBG7W198Q]
sources:
  - url: https://en.wikipedia.org/wiki/Graetz_number
history:
  posed_by: "Leo Graetz"
  first_stated: "1883"
---

## Problem

A fluid with constant properties flows steadily in a circular tube of radius $R$.
Its velocity has the laminar Poiseuille profile $u(r) = 2U(1 - r^2/R^2)$, where $U$ is the mean velocity and $r$ the distance from the axis.
For $x < 0$ the fluid has the uniform temperature $T_0$, and for $x > 0$ the wall is held at the temperature $T_w \ne T_0$.
Axial heat conduction and viscous heating are neglected, and $\alpha$ is the [[thermal diffusivity|CS4ZZX092Z]] of the fluid.
Find the temperature $T(x, r)$ for $x > 0$, bounded at $r = 0$, that solves
$$u(r) \, \frac{\partial T}{\partial x} = \frac{\alpha}{r} \frac{\partial}{\partial r}\Big(r \frac{\partial T}{\partial r}\Big), \qquad T(0, r) = T_0, \qquad T(x, R) = T_w,$$
and find the local [[Nusselt number|THH3V9AHDN]] $\mathrm{Nu}(x)$ at the wall.

## Remarks

The problem is solved by [[separation of variables|47NFRVB564]].
With $\eta = r/R$ and $\theta = (T - T_w)/(T_0 - T_w)$, the solution is
$$\theta = \sum_{n \ge 0} c_n \, \varphi_n(\eta) \exp\!\Big(-\lambda_n^2 \frac{x}{R \, \mathrm{Re} \Pr}\Big),$$
where $\mathrm{Re} = 2RU/\nu$, $\Pr = \nu/\alpha$, and $\varphi_n$, $\lambda_n$ are the eigenfunctions and eigenvalues of the [[Sturm–Liouville problem|7WV6B2502K]] $(\eta \varphi')' + \lambda^2 \eta (1 - \eta^2) \varphi = 0$, $\varphi'(0) = 0$, $\varphi(1) = 0$.
The coefficients $c_n$ come from the orthogonality of the $\varphi_n$ with the weight $\eta(1 - \eta^2)$.
Far downstream only the first term survives, and the Nusselt number tends to about $3.66$.
Near the entrance the series converges slowly, and the Lévêque approximation is used instead.
The dimensionless group $\mathrm{Gz} = \mathrm{Re} \Pr D / x$, with $D = 2R$, is called the Graetz number.
Wilhelm Nusselt later treated the same problem independently.

## Explanations

### L1 human

Cold fluid flows slowly through a pipe, and from some point on the pipe wall is hot.
The fluid near the wall warms first, and the heat slowly spreads toward the centre while the fluid moves on.
The Graetz problem asks for the temperature everywhere in the pipe and for the rate of heat transfer at the wall.
Far down the pipe, the heat transfer coefficient at the wall settles to a fixed value that does not depend on the flow speed.
