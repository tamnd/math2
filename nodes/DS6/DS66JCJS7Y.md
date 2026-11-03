---
tag: DS66JCJS7Y
kind: definition
name: BGK collision operator
msc: [82C40, 76P05, 35Q20]
defines: YQRS1ZMRAC
uses: [MH6CSWD7F0, 3QSVWQJX11, HHTG8JVGKQ]
sources:
  - url: https://en.wikipedia.org/wiki/Bhatnagar%E2%80%93Gross%E2%80%93Krook_operator
---

## Definition

Let $f(v) \ge 0$ be a velocity distribution on $\R^3$ with $\int (1 + \abs{v}^2) f \, dv < \infty$ and $\int f \, dv > 0$, not concentrated at a single velocity.
Let $n$, $u$ and $T$ be its density, bulk velocity and temperature, as in the [[kinetic theory of gases|HHTG8JVGKQ]].
Let $M[f]$ be the [[Maxwell–Boltzmann distribution|3QSVWQJX11]] with the same $n$, $u$ and $T$.
Let $\nu > 0$ be a collision frequency, which may depend on $n$ and $T$.
The *BGK collision operator* is
$$Q_{BGK}(f) = \nu \big( M[f] - f \big).$$
The BGK equation is the [[Boltzmann equation|MH6CSWD7F0]] with $Q_{BGK}$ in place of the Boltzmann collision operator: $\partial_t f + v \cdot \nabla_x f = \nu (M[f] - f)$.

## Remarks

Since $M[f]$ and $f$ have the same moments, $\int (1, v, \abs{v}^2)\, Q_{BGK}(f) \, dv = 0$: mass, momentum and energy are conserved.
The H-theorem holds: $\log M[f]$ is a combination of $1$, $v$ and $\abs{v}^2$, so $\int Q_{BGK}(f) \log M[f] \, dv = 0$, and therefore $\int Q_{BGK}(f) \log f \, dv = \nu \int (M[f] - f)(\log f - \log M[f]) \, dv \le 0$.
The operator is nonlinear in $f$, through the dependence of $M[f]$ on the moments of $f$.
In the Navier–Stokes limit, the BGK model gives Prandtl number $1$, while the Boltzmann equation for a monatomic gas gives a value close to $2/3$.

Example: if $f$ is itself a Maxwellian, then $M[f] = f$ and $Q_{BGK}(f) = 0$.

Non-example: the relaxation $\nu (M_0 - f)$ towards a fixed Maxwellian $M_0$ is not the BGK operator.
It does not conserve mass, momentum and energy when $f$ has moments different from those of $M_0$.
