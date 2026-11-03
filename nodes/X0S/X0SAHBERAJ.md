---
tag: X0SAHBERAJ
kind: definition
name: Vlasov–Poisson system
msc: [35Q83, 82C40, 82D10]
defines: SB4N1BTRAQ
uses: [SJH7M2VCTE, DWK5N5SKTK, GC5BDZ6QBC, 0ABK9V9Y64]
sources:
  - url: https://en.wikipedia.org/wiki/Vlasov_equation
---

## Definition

Let $T > 0$ and $\gamma \in \set{1, -1}$.
The unknowns are a density $f \colon [0, T) \times \R^3 \times \R^3 \to [0, \infty)$ with $\iint f(t, x, v) \, dx \, dv < \infty$, and a potential $\phi(t, \cdot)$ that tends to $0$ at infinity.
The *Vlasov–Poisson system* is the system of [[partial differential equations|GC5BDZ6QBC]]
$$\partial_t f + v \cdot \nabla_x f - \gamma \nabla_x \phi \cdot \nabla_v f = 0, \qquad -\Delta_x \phi = \rho, \qquad \rho(t, x) = \int_{\R^3} f(t, x, v) \, dv.$$
Here $\nabla_x$ and $\nabla_v$ are the [[gradients|0ABK9V9Y64]] in $x$ and $v$, and $\Delta_x$ is the Laplacian in $x$.
The second equation is [[Poisson's equation|DWK5N5SKTK]], so $\phi(t, x) = \frac{1}{4\pi} \int_{\R^3} \frac{\rho(t, y)}{\abs{x - y}} \, dy$.
The case $\gamma = 1$ is the repulsive, or plasma, case, and $\gamma = -1$ is the attractive, or gravitational, case.

## Remarks

It is the [[Vlasov equation|SJH7M2VCTE]] with the force $F = -\gamma \nabla_x \phi$.
For smooth solutions with enough decay, the mass $\iint f \, dx \, dv$ and the energy
$$\frac12 \iint \abs{v}^2 f \, dx \, dv + \frac{\gamma}{2} \int \abs{\nabla_x \phi}^2 \, dx$$
are constant in time.
Pfaffelmoser in 1992 and Lions and Perthame in 1991 proved, by different methods, that the system has global smooth solutions in three dimensions for suitable smooth initial data.

Example: let $h \colon \R \to [0, \infty)$ be differentiable and let $\phi$ be any smooth function of $x$ alone.
Then $f(x, v) = h(\frac12 \abs{v}^2 + \gamma \phi(x))$ satisfies the first equation, since
$$v \cdot \nabla_x f - \gamma \nabla_x \phi \cdot \nabla_v f = h' \, (\gamma \, v \cdot \nabla_x \phi - \gamma \nabla_x \phi \cdot v) = 0.$$
It is a stationary solution of the whole system exactly when $\phi$ also solves $-\Delta \phi = \int h(\frac12 \abs{v}^2 + \gamma \phi) \, dv$.

Non-example: for an external potential $\phi$ not linked to $f$, such as $\phi(x) = \abs{x}^2$, the function $f = h(\frac12 \abs{v}^2 + \gamma \abs{x}^2)$ solves the first equation but not the system.
Indeed $-\Delta \phi = -6$ is negative and cannot equal the density $\rho \ge 0$.
