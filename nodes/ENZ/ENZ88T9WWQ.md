---
tag: ENZ88T9WWQ
kind: definition
name: Discrete Painlevé equations
msc: [39A36, 34M55, 37K60]
defines: 5PFJBYDD2H
uses: [0XDK9CGYKJ, AZ17JCMRKB]
sources:
  - url: https://en.wikipedia.org/wiki/Painlev%C3%A9_transcendents
---

## Definition

Let $R(n, x, y)$ be a [[rational function|0XDK9CGYKJ]] of $x$ and $y$ whose coefficients depend on $n \in \Z$.
Consider the second-order difference equation
$$x_{n+1} = R(n, x_n, x_{n-1}), \qquad n \in \Z.$$
It is a *discrete Painlevé equation* if the following hold.

1. the map $(x_{n-1}, x_n) \mapsto (x_n, x_{n+1})$ is birational for each $n$;
2. the equation is integrable, for example in the sense that it is the compatibility condition of a Lax pair of linear problems;
3. the equation has one of the [[Painlevé equations|AZ17JCMRKB]] as a continuum limit.

In Sakai's geometric classification, these equations arise as translations of affine Weyl groups acting on families of rational surfaces.
The dependence on $n$ may also enter through $q^n$ for a fixed $q$, which gives $q$-discrete Painlevé equations.

## Remarks

Example: the equation called d-$\mathrm{P_I}$,
$$x_{n+1} + x_n + x_{n-1} = \frac{\alpha n + \beta}{x_n} + \gamma,$$
with constants $\alpha \ne 0$, $\beta$, $\gamma$, is a discrete Painlevé equation; under a suitable scaling it tends to $\mathrm{P_I}$, $y'' = 6y^2 + t$.

Non-example: the logistic recurrence $x_{n+1} = r x_n (1 - x_n)$ is a rational recurrence, but its map $x \mapsto r x (1 - x)$ is two-to-one, so it is not birational and clause 1 fails.

Clause 2 has several versions in the literature, so the definition is less rigid than most.
A practical test is singularity confinement: a singularity met at one step disappears after finitely many steps.
Another standard example is d-$\mathrm{P_{II}}$, $x_{n+1} + x_{n-1} = \dfrac{(\alpha n + \beta) x_n + a}{1 - x_n^2}$.
