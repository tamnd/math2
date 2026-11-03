---
tag: 3QM3WDNAT7
kind: definition
name: Maxwell–Boltzmann distribution
msc: [82B40, 82C40, 76P05]
defines: 3QSVWQJX11
uses: [HHTG8JVGKQ, 05AQE0QR0D]
sources:
  - url: https://en.wikipedia.org/wiki/Maxwell%E2%80%93Boltzmann_distribution
---

## Definition

Let $m > 0$ be the particle mass and $k > 0$ the Boltzmann constant.
Let $n > 0$, $u \in \R^3$ and $T > 0$.
The *Maxwell–Boltzmann distribution*, or Maxwellian, with density $n$, bulk velocity $u$ and temperature $T$ is the function $M \colon \R^3 \to (0, \infty)$,
$$M(v) = n \left( \frac{m}{2\pi k T} \right)^{3/2} \exp\left( - \frac{m \abs{v - u}^2}{2 k T} \right).$$
A *local Maxwellian* is a function $f(t, x, v) = M(v)$ in which $n$, $u$ and $T$ depend on $(t, x)$.

## Remarks

The function $M/n$ is the density of the [[normal distribution|05AQE0QR0D]] on $\R^3$ with mean $u$ and covariance $(kT/m) I$.
In the [[kinetic description|HHTG8JVGKQ]] of a gas, $M$ has number density $n$, bulk velocity $u$ and temperature $T$.
For $u = 0$, the speed $s = \abs{v}$ has the density $4\pi s^2 (m/(2\pi kT))^{3/2} e^{-ms^2/(2kT)}$ on $(0, \infty)$, after normalising by $n$.
Its most probable value is $\sqrt{2kT/m}$, its mean is $\sqrt{8kT/(\pi m)}$, and its root mean square is $\sqrt{3kT/m}$.

Example: check of the temperature for $u = 0$.
Each component $v_i$ has variance $kT/m$ under $M/n$, so $\int \tfrac{m}{2} \abs{v}^2 M \, dv = n \cdot \tfrac{m}{2} \cdot 3 \cdot \tfrac{kT}{m} = \tfrac32 n k T$, as required.

Non-example: the uniform distribution of velocities on a ball $\set{\abs{v} \le R}$ is not a Maxwellian, since it vanishes outside the ball while every Maxwellian is positive everywhere.
