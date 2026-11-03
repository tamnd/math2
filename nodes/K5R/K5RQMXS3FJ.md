---
tag: K5RQMXS3FJ
kind: statement
role: theorem
name: Lanford's theorem on the Boltzmann–Grad limit
msc: [82C40, 35Q20, 82C05]
uses: [MH6CSWD7F0, CSEV80K9A4, 39NMDCPCCV, M0J697D782]
about: [MH6CSWD7F0]
sources:
  - url: https://en.wikipedia.org/wiki/Boltzmann_equation
---

## Statement

For $\varepsilon > 0$, consider $N$ [[hard spheres|39NMDCPCCV]] of diameter $\varepsilon$ in $\R^3$, moving freely between collisions and colliding elastically.
Assume the Boltzmann–Grad scaling $N \varepsilon^2 = 1$ as $N \to \infty$.
Let $f_0 \colon \R^3 \times \R^3 \to [0, \infty)$ be a continuous probability density with a Gaussian bound $f_0(x, v) \le C e^{-\beta \abs{v}^2/2}$ for some constants $C, \beta > 0$.
Let the initial law of the $N$ particles be the product density $f_0^{\otimes N}$, conditioned on the event that no two spheres overlap.
Let $f_N^{(1)}(t)$ be the one-particle marginal of the law of the particles at time $t$.
Then there is a time $T > 0$, depending only on $C$ and $\beta$, such that for every $t \in [0, T]$:

1. $f_N^{(1)}(t)$ converges almost everywhere to $f(t)$ as $N \to \infty$.
   Here $f$ is the solution on $[0, T]$ of the [[Boltzmann equation|MH6CSWD7F0]] for hard spheres with initial value $f_0$.
2. for each fixed $s$, the $s$-particle marginal converges almost everywhere to $f(t)^{\otimes s}$.

## Remarks

Oscar Lanford proved the theorem in 1975; Isabelle Gallagher, Laure Saint-Raymond and Bela Texier later gave a complete version of the proof with explicit convergence rates.
The scaling $N \varepsilon^2 = 1$ keeps the [[mean free path|M0J697D782]] of order $1$, while the volume fraction occupied by the spheres, of order $N \varepsilon^3 = \varepsilon$, tends to $0$.

Idea of the proof: the marginals solve the [[BBGKY hierarchy|CSEV80K9A4]] of hard spheres, whose collision terms involve particles at distance $\varepsilon$.
In the limit the hierarchy becomes the Boltzmann hierarchy, which the tensor powers $f(t)^{\otimes s}$ solve.
Both hierarchies are expanded in Duhamel series of collision trees, and these series converge on a short time interval uniformly in $N$.
The remaining work is to show that the trajectories with recollisions, which do not appear in the Boltzmann hierarchy, have a vanishing contribution.

Part 2 is called propagation of chaos: particles that were independent at time $0$ stay asymptotically independent.
It justifies the molecular chaos assumption that Boltzmann used, and so explains how the irreversible Boltzmann equation arises from reversible dynamics, the answer to [[Loschmidt's paradox|T9TCS3426N]] in this setting.
The restriction to a short time $T$, a fraction of the mean free time, comes from the convergence of the series expansion used in the proof.

## Explanations

### L1 human

The Boltzmann equation describes a dilute gas by the density of molecules at each position with each velocity.
Lanford's theorem shows that this equation really follows from Newton's laws for billiard balls, when there are very many very small balls.
The proof works only for a short time, a fraction of the average time between two collisions of a molecule.

### L2 human

The theorem is the main rigorous derivation of a kinetic equation from particle dynamics.
It connects the [[BBGKY hierarchy|CSEV80K9A4]] with the Boltzmann equation through the limit $N \to \infty$, $\varepsilon \to 0$, $N \varepsilon^2$ fixed.
The limit is irreversible, as the [[H-theorem|BMA7D1Z2W6]] shows.
This is consistent with reversible dynamics, because the convergence holds for chaotic initial data and in the sense of marginals, not along every trajectory.
