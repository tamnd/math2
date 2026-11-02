---
tag: N8NXNCMSK5
kind: statement
role: theorem
name: Disintegration theorem
msc: [28A50, 60A10]
uses: [584GXXY73M, 059TJN0NZ1, 3N66TM3TSQ, YYNCJSR0PJ]
about: [059TJN0NZ1, PHHT5W3BEJ]
sources:
  - url: https://en.wikipedia.org/wiki/Disintegration_theorem
same_as:
  wikidata: Q5282247
  wikipedia: Disintegration theorem
---

## Statement

Let $Y$ and $X$ be [[Polish spaces|584GXXY73M]] with their Borel σ-algebras.
Let $\mu$ be a Borel [[probability measure|059TJN0NZ1]] on $Y$, let $\pi \colon Y \to X$ be a Borel [[measurable map|YYNCJSR0PJ]], and let $\nu = \pi_* \mu$ be the [[pushforward measure|3N66TM3TSQ]].
Then there is a family $(\mu_x)_{x \in X}$ of Borel probability measures on $Y$ with the following properties.

1. For every Borel set $B \subseteq Y$, the map $x \mapsto \mu_x(B)$ is Borel measurable.
2. For $\nu$-almost every $x \in X$, $\mu_x$ is concentrated on the fibre: $\mu_x(Y \setminus \pi^{-1}(x)) = 0$.
3. For every Borel function $f \colon Y \to [0, \infty]$,
$$\int_Y f \, d\mu = \int_X \int_{\pi^{-1}(x)} f(y) \, d\mu_x(y) \, d\nu(x).$$

The family is unique up to $\nu$-null sets: two such families agree for $\nu$-almost every $x$.

## Remarks

One way to prove it is through [[regular conditional probabilities|PHHT5W3BEJ]].
For a Borel set $B$, the measure $A \mapsto \mu(B \cap \pi^{-1}(A))$ is absolutely continuous with respect to $\nu$, and the [[Radon–Nikodym theorem|1ZSZS5G1Q4]] gives a density $x \mapsto \mu_x(B)$.
The Polish assumption lets one choose these densities for a countable generating algebra of Borel sets at once and extend them to measures.

Example: let $\mu$ be Lebesgue measure on $Y = [0, 1]^2$ and $\pi(x, y) = x$.
Then $\nu$ is Lebesgue measure on $[0, 1]$, and $\mu_x$ is Lebesgue measure on the vertical segment $\set{x} \times [0, 1]$.
Property 3 is then Fubini's theorem.

The theorem is often stated for Radon spaces, which include Polish spaces.
Without such a regularity assumption a disintegration may fail to exist.

## Explanations

### L1 human

A measure on a big space can be cut into slices along the fibres of a map.
Each slice carries its own probability measure, and the total measure is recovered by averaging the slices according to how much weight each fibre gets.
It is the measure-theoretic form of computing a probability by first conditioning on the value of $\pi$.

### L2 human

Disintegration makes conditioning on events of probability zero rigorous: $\mu_x$ is the conditional law of the point $y$ given $\pi(y) = x$.
It is used in optimal transport to decompose transport plans, in ergodic theory for the ergodic decomposition, and in geometric measure theory together with the coarea formula.
The measures $\mu_x$ are only defined for almost every $x$.
So a conditional law given a single null event depends on the choice of the map $\pi$, as the [[Borel–Kolmogorov paradox|9RMS0ZJ618]] shows.
