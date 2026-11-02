---
tag: WDJSNMG1EZ
kind: statement
role: theorem
name: Harmonic measure as exit distribution
msc: [60J45, 31A15, 60J65]
uses: [CFD7BPM51W, 22735FGJV6, CCEKM4241P, WND87FBAKC, TCYSWCTYYM, 0Q4CBD3HX0, DYR1QFNGNJ]
about: [CFD7BPM51W, 22735FGJV6]
sources:
  - url: https://en.wikipedia.org/wiki/Harmonic_measure
    locator: The harmonic measure of a diffusion
---

## Statement

Let $d \ge 2$ and let $D \subset \R^d$ be a bounded [[domain|0Q4CBD3HX0]] whose boundary points are all regular for the Dirichlet problem.
For $x \in D$, let $\omega_x$ be the [[harmonic measure|CFD7BPM51W]] of $D$ at $x$.
It is the [[Borel probability measure|DYR1QFNGNJ]] on $\partial D$ such that $\int \varphi \, d\omega_x = u_\varphi(x)$ for every continuous $\varphi$ on $\partial D$.
Here $u_\varphi$ is the solution of the Dirichlet problem with boundary data $\varphi$.
Let $(B_t)$ be a [[Brownian motion|22735FGJV6]] in $\R^d$ started at $x$, with law $P^x$, and let $\tau = \inf\set{t > 0 : B_t \notin D}$.
Then for every Borel set $A \subseteq \partial D$,
$$P^x(B_\tau \in A) = \omega_x(A).$$

## Remarks

Proof idea: by [[Kakutani's theorem|CCEKM4241P]], $E^x[\varphi(B_\tau)]$ is the solution of the Dirichlet problem with data $\varphi$, for each continuous $\varphi$.
So the law of $B_\tau$ and $\omega_x$ give the same integral to each continuous function on the compact set $\partial D$, and the two Borel measures are equal.
Example: for the ball $\abs{y} < 1$ in $\R^d$, the exit point from $x$ has density, with respect to normalized surface measure, equal to the [[Poisson kernel|TCYSWCTYYM]] $(1 - \abs{x}^2)/\abs{x - \zeta}^d$.
From the centre $x = 0$ this density is $1$, so the exit point is uniform on the sphere.
Without regularity, the identity still holds when $\omega_x$ is the harmonic measure defined through Perron solutions.
The set of irregular boundary points is then polar, and it gets no mass.

## Explanations

### L1 human

Release a particle at a point inside a region and let it move at random until it reaches the boundary.
The harmonic measure of a piece of the boundary is the chance that the particle first arrives there.
Pieces close to the start point, or wide open to it, get more probability; pieces hidden in narrow fjords get very little.

### L2 human

The probabilistic picture explains many properties of harmonic measure at once.
It is a probability measure, it depends harmonically on the starting point, and it is monotone in the domain.
In the plane, Brownian motion is conformally invariant up to a time change, which explains the conformal invariance of harmonic measure.
Estimates such as Beurling's projection theorem have natural proofs and interpretations in this language.
