---
tag: KMMK6H43C9
kind: statement
role: theorem
name: Geroch's splitting theorem
msc: ["53C50", "83C05"]
uses: [PZGHVCQB13, R8KDE9QYNP, 0QT00PB5G2, 0KZZ70ZHXP, BY4QYYS788]
about: [PZGHVCQB13, R8KDE9QYNP]
sources:
  - url: https://en.wikipedia.org/wiki/Globally_hyperbolic_spacetime
---

## Statement

Let $(M, g)$ be a time-oriented [[Lorentzian manifold|BY4QYYS788]].
Then $(M, g)$ is [[globally hyperbolic|PZGHVCQB13]] if and only if it has a [[Cauchy surface|R8KDE9QYNP]].
In that case, for any Cauchy surface $\Sigma$, the manifold $M$ is [[homeomorphic|0QT00PB5G2]] to $\R \times \Sigma$, and any two Cauchy surfaces of $M$ are homeomorphic.

## Remarks

The idea of Geroch's proof is to fix a finite measure $\mu$ on $M$ with a positive smooth density and to consider the function $t(p) = \ln\left(\mu(I^-(p)) / \mu(I^+(p))\right)$.
Global hyperbolicity makes $t$ continuous, and $t$ increases strictly along every future-directed causal curve and tends to $\pm\infty$ along inextendible ones.
Each level set of $t$ is then a Cauchy surface, and flowing along a timelike vector field identifies $M$ with $\R \times \Sigma$.

Bernal and Sánchez proved a smooth version: $M$ is [[diffeomorphic|0KZZ70ZHXP]] to $\R \times \Sigma$, with metric $-\beta\, dt^2 + h_t$.
Here $\beta > 0$ is a smooth function, and each slice $\set{t} \times \Sigma$ is a smooth spacelike Cauchy surface with Riemannian metric $h_t$.

Example: Minkowski space $\R^{1,3}$ is globally hyperbolic with Cauchy surface $\set{t = 0} \cong \R^3$, and indeed $\R^{1,3} = \R \times \R^3$.

The theorem implies strong topological restrictions: a globally hyperbolic spacetime cannot be compact, since $\R \times \Sigma$ is never compact.

## Explanations

### L1 human

The theorem says that a spacetime in which the future is predictable from the present always looks, topologically, like a fixed space evolving in time.
One can slice it into instants, and all instants are the same space.
So predictability rules out spacetimes whose shape changes from one moment to the next.

### L2 human

Geroch's theorem is the bridge between the causal definition of global hyperbolicity and the initial value problem.
Einstein's equations are posed on a Cauchy surface $\Sigma$, and the solution lives on $\R \times \Sigma$.
It also shows that topology change cannot happen in a globally hyperbolic spacetime.
The smooth splitting of Bernal and Sánchez is what one needs in practice to write the metric in the form used by the ADM and other $3 + 1$ formalisms.
