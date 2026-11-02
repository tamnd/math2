---
tag: VM5V845JGZ
kind: definition
name: Condenser capacity
msc: [31B15, 31A15, 30C85]
defines: NTEFMRR3HR
uses: [0R6EWFKRCF, 0DEB0JMN0W]
sources:
  - url: https://en.wikipedia.org/wiki/Capacity_of_a_set
---

## Definition

Let $n \ge 2$, let $\Omega \subseteq \R^n$ be an open set, and let $K \subseteq \Omega$ be a [[compact set|0R6EWFKRCF]].
The pair $(K, \Omega)$ is called a *condenser*.
Let $C_c^\infty(\Omega)$ be the set of smooth real functions with compact support in $\Omega$.
The *capacity* of the condenser $(K, \Omega)$ is
$$\operatorname{cap}(K, \Omega) = \inf \set{ \int_\Omega \abs{\nabla u}^2 \, dx : u \in C_c^\infty(\Omega), \ u \ge 1 \text{ on } K }.$$

## Remarks

When $\Omega$ is bounded and its boundary and that of $K$ are regular, the infimum is attained in a larger class by the potential $u$ of the condenser.
This is the [[harmonic function|0DEB0JMN0W]] on $\Omega \setminus K$ with $u = 1$ on $\partial K$ and $u = 0$ on $\partial \Omega$.

Example: in $\R^3$ let $0 < r < R$, $K = \bar B_r$ and $\Omega = B_R$.
The potential is $u(x) = (1/\abs{x} - 1/R) / (1/r - 1/R)$ for $r \le \abs{x} \le R$, and $\abs{\nabla u} = \abs{x}^{-2} / (1/r - 1/R)$.
Integration over spheres gives $4 \pi \int_r^R s^{-2} \, ds / (1/r - 1/R)^2 = 4 \pi / (1/r - 1/R)$.
So $\operatorname{cap}(\bar B_r, B_R) = 4 \pi r R / (R - r)$.
In the plane the same computation with $u(x) = \log(R/\abs{x}) / \log(R/r)$ gives $\operatorname{cap}(\bar B_r, B_R) = 2 \pi / \log(R/r)$.

Non-example: if $K$ is compact but not contained in $\Omega$, the pair is not a condenser.
No $u \in C_c^\infty(\Omega)$ can be at least $1$ at a point of $K$ outside $\Omega$.

Some authors normalize by a constant, such as $1/(4\pi)$ in $\R^3$ or $1/(2\pi)$ in the plane, or define the capacity with $\abs{\nabla u}^n$, which makes it invariant under conformal maps.
