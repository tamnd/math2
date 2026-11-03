---
tag: PAFD50PFXX
kind: statement
role: theorem
name: Miles–Howard theorem
msc: ["76E05", "76E20"]
uses: [6CXB96Y39R, XQ82TE42FH, TXQQQG9T2S, H028A17Z55]
about: [H028A17Z55, 6CXB96Y39R]
sources:
  - url: https://en.wikipedia.org/wiki/Richardson_number
---

## Statement

Consider an inviscid, non-diffusive, incompressible fluid in the [[Boussinesq approximation|TXQQQG9T2S]], between rigid horizontal walls $z = z_1$ and $z = z_2$.
The base state is a horizontal parallel shear flow $U(z)$ with a stable density stratification $\rho_0(z)$.
Let $g$ be the gravitational acceleration and let $N^2(z) = -\frac{g}{\rho_*} \frac{d\rho_0}{dz}$ be the square of the [[buoyancy frequency|XQ82TE42FH]], where $\rho_*$ is a constant reference density.
Let $\mathrm{Ri}(z) = N^2(z) / U'(z)^2$ be the gradient [[Richardson number|6CXB96Y39R]].
Suppose that $N^2(z) \ge \tfrac14 U'(z)^2$ for every $z$ in $[z_1, z_2]$, that is, $\mathrm{Ri}(z) \ge 1/4$ wherever $U'(z) \neq 0$.
Then the flow is linearly stable: no normal mode disturbance $e^{i \alpha (x - c t)}$ with real $\alpha \neq 0$ has $\operatorname{Im} c > 0$.

## Remarks

Normal modes with stream function amplitude $\varphi(z)$ satisfy the Taylor–Goldstein equation
$$(U - c)(\varphi'' - \alpha^2 \varphi) - U'' \varphi + \frac{N^2}{U - c} \varphi = 0, \qquad \varphi(z_1) = \varphi(z_2) = 0.$$
Howard's proof substitutes $\varphi = (U - c)^{1/2} G$, multiplies by $\bar G$ and integrates.
The imaginary part of the result is
$$c_i \left[ \int \left( \abs{G'}^2 + \alpha^2 \abs{G}^2 \right) dz + \int \frac{N^2 - U'^2/4}{\abs{U - c}^2} \abs{G}^2 \, dz \right] = 0,$$
with $c = c_r + i c_i$, and when $N^2 \ge U'^2/4$ the bracket is positive, so $c_i = 0$.

The theorem was proved by Miles and by Howard in 1961.
The condition is sufficient for stability, not necessary: a flow with $\mathrm{Ri} < 1/4$ somewhere may still be stable.
With $N = 0$ the condition fails wherever $U' \neq 0$; the unstratified case of the Euler equations is covered by Rayleigh's inflection point criterion instead.
The theorem and its proof extend to unbounded layers with disturbances that decay at infinity.
Example: for the stratified mixing layer $U = \tanh z$, $N^2 = J \operatorname{sech}^2 z$ on the whole line, one has $\mathrm{Ri}(z) = J \cosh^2 z \ge J$, so the flow is stable when $J \ge 1/4$.

## Explanations

### L1 human

In the ocean and the atmosphere, light fluid often lies on top of heavy fluid, and different layers move at different speeds.
The density layering resists mixing, while the speed difference between layers tries to roll them up into waves and eddies.
The Richardson number compares these two effects.
The Miles–Howard theorem says that if the layering is strong enough everywhere, namely the Richardson number is at least one quarter, then small waves cannot grow.

### L2 human

The theorem is the stratified counterpart of the inviscid criteria of [[hydrodynamic stability|H028A17Z55]] for parallel flows.
The threshold $1/4$ is widely used in oceanography and meteorology as a rule of thumb for when shear-driven turbulence and Kelvin–Helmholtz billows can occur.
Its proof is the same energy-type identity as in Rayleigh's criterion, after Howard's substitution.
The same substitution gives Howard's semicircle theorem, which bounds the complex wave speed of unstable modes.
