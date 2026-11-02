---
tag: KP23SF2Z0Q
kind: statement
role: theorem
name: Koebe's theorem on the mean value property
msc: [31B05]
uses: [CQ7E0V6T2G, 0HYPR64JM2, 0DEB0JMN0W, 0X3WGX95FE, PCZBE7EX01]
about: [0DEB0JMN0W]
sources:
  - url: https://en.wikipedia.org/wiki/Harmonic_function
---

## Statement

Let $U \subseteq \R^n$ be an open set and let $u \colon U \to \R$ be [[continuous|0X3WGX95FE]].
Assume that for every $x \in U$ there is $\rho(x) > 0$ such that
$$u(x) = \frac{1}{\abs{\partial B(x, r)}} \int_{\partial B(x, r)} u \, dS \quad \text{for all } 0 < r < \rho(x),$$
where $\abs{\partial B(x, r)}$ is the area of the sphere $\partial B(x, r)$.
Then $u$ is [[harmonic|0DEB0JMN0W]] on $U$.

## Remarks

The radius $\rho(x)$ may depend on the point, so the mean value property is only asked for small spheres; this strengthens the [[converse of the mean value property|CQ7E0V6T2G]].
Proof idea: fix a ball $B$ with closure in $U$, and let $h$ be the harmonic function on $B$ with boundary values $u$ given by the [[Poisson integral formula|PCZBE7EX01]].
The difference $v = u - h$ is continuous on $\overline{B}$, vanishes on $\partial B$, and has the local mean value property inside $B$.
Suppose $v$ had a positive maximum $m$, and choose a point $x$ of the compact set $\set{v = m}$ farthest from the centre of $B$.
On each small sphere about $x$, $v \le m$, with $v < m$ on an open piece of the sphere.
So the average is less than $m = v(x)$, a contradiction.
The same applies to $-v$, so $v = 0$ and $u = h$ is harmonic on $B$.
Example: for $u(x) = \abs{x}^{2-n}$ on $U = \R^n \setminus \set{0}$ with $n \ge 3$, one may take $\rho(x) = \abs{x}$.
The mean value property on these spheres follows from the potential of a uniform spherical shell, and the theorem then shows that $u$ is harmonic.

## Explanations

### L1 human

To know that a continuous function is harmonic, it is enough to check the averaging property on tiny spheres.
Each point may come with its own size limit for the spheres.
This makes harmonicity a purely local property that can be tested by averages.

### L2 human

The proof combines the solvability of the Dirichlet problem on balls with a maximum principle that only uses small spheres.
This style of argument, comparing a function with the harmonic function that has the same boundary values, reappears in Perron's method and in the theory of subharmonic functions.
Even weaker versions exist, where the mean value property is asked only for one sequence of radii tending to $0$ at each point; the same proof works for them.
