---
tag: 5RN835HTBD
kind: statement
role: theorem
name: Takens's theorem
msc: [37M10, 37C05, 57R40]
uses: [F45VQ47GPV, 0KZZ70ZHXP, 6RW68JGBHC, BBZP1R872N]
about: [BBZP1R872N]
sources:
  - url: https://en.wikipedia.org/wiki/Takens's_theorem
same_as:
  wikidata: Q11722674
  wikipedia: Takens's theorem
---

## Statement

Let $M$ be a compact [[smooth manifold|F45VQ47GPV]] of dimension $m$.
For a $C^2$ [[diffeomorphism|0KZZ70ZHXP]] $\phi \colon M \to M$ and a $C^2$ function $y \colon M \to \R$, define the delay map
$$\Phi_{(\phi, y)} \colon M \to \R^{2m+1}, \qquad \Phi_{(\phi, y)}(x) = \big( y(x), y(\phi(x)), \ldots, y(\phi^{2m}(x)) \big).$$
An embedding here is an injective [[immersion|6RW68JGBHC]] that is a homeomorphism onto its image.
Give the space of all pairs $(\phi, y)$ the $C^2$ topology.
Then the set of pairs for which $\Phi_{(\phi, y)}$ is an embedding contains an open dense subset.

## Remarks

The proof follows the proof of the [[Whitney embedding theorem|2GSRBDT96M]].
For generic $\phi$ the periodic points of low period are finite in number and have distinct eigenvalues.
A perturbation of $y$ near them makes the delay map an immersion and injective there.
Away from these points a transversality argument shows that a generic perturbation of $y$ removes self-intersections, since $2m + 1 > 2m$.

The point of the theorem is that $2m + 1$ consecutive measurements of one scalar quantity along an orbit determine the state.
In applications $M$ is often an attractor of a flow, $\phi$ is the time-$\tau$ map, and $y$ is a measured quantity.
The image of the attractor under $\Phi$ is a faithful copy that can be reconstructed from a time series.
Sauer, Yorke and Casdagli extended the result to compact sets of box-counting dimension $d$, with $2m + 1$ replaced by any integer larger than $2d$, in a probabilistic sense of genericity.

Genericity is needed.
If $y$ is constant, then $\Phi_{(\phi, y)}$ is constant and is not injective.
If $\phi = \id$, then $\Phi_{(\phi, y)}(x) = (y(x), \ldots, y(x))$, which cannot be injective on a manifold of dimension $m \ge 1$.

## Explanations

### L1 human

Suppose a complicated system, like the weather, moves on some hidden space of states, and you can measure only one number, such as the temperature, at regular times.
The theorem says that, in typical situations, a list of enough consecutive measurements is as good as knowing the full state.
So the shape of the hidden dynamics can be rebuilt from a single time series.

### L2 human

Takens's theorem is the basis of delay-coordinate reconstruction in time series analysis.
One plots vectors $(y_n, y_{n+1}, \ldots, y_{n + k})$ built from data and studies the resulting cloud of points.
Since the delay map is an embedding, invariants that survive smooth changes of coordinates, such as [[Lyapunov exponents|NJ1FJSNK6A]], dimensions and entropies, can be estimated from the reconstruction.
The theorem is a dynamical analogue of the Whitney embedding theorem, which embeds an $m$-manifold in $\R^{2m}$ without any dynamics.
