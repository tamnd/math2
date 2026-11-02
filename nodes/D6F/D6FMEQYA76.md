---
tag: D6FMEQYA76
kind: statement
role: theorem
name: Prokhorov's theorem
msc: [60B10, 28A33]
uses: [MBW9JCGZC1, MNMJC8YVBS, 059TJN0NZ1, 0VKD1TP7F3, 0BY52JW6NK, 0Z2P41SVDP, 0R6EWFKRCF]
about: [MNMJC8YVBS, MBW9JCGZC1]
sources:
  - url: https://en.wikipedia.org/wiki/Prokhorov%27s_theorem
same_as:
  wikidata: Q7249519
  wikipedia: Prokhorov's theorem
---

## Statement

Let $X$ be a [[metric space|0VKD1TP7F3]] and let $\mathcal{M}$ be a set of Borel [[probability measures|059TJN0NZ1]] on $X$.
Call $\mathcal{M}$ relatively compact if every sequence in $\mathcal{M}$ has a subsequence that [[converges weakly|MBW9JCGZC1]] to some Borel probability measure on $X$.

1. If $\mathcal{M}$ is [[tight|MNMJC8YVBS]], then $\mathcal{M}$ is relatively compact.
2. If $X$ is [[separable|0Z2P41SVDP]] and [[complete|0BY52JW6NK]], and $\mathcal{M}$ is relatively compact, then $\mathcal{M}$ is tight.

## Remarks

Tight means that for every $\varepsilon > 0$ there is a [[compact set|0R6EWFKRCF]] $K$ with $\mu(K) > 1 - \varepsilon$ for all $\mu \in \mathcal{M}$.
For a compact space $X$, part 1 follows from the Riesz representation theorem and the weak-* compactness of the unit ball of the dual of $C(X)$.
The general case reduces to compact sets by tightness.
For $X = \R$, part 1 is close to Helly's selection theorem for distribution functions.

Example: the normal distributions $N(m, \sigma^2)$ with $\abs{m} \le 1$ and $0 < \sigma \le 1$ form a tight family, using $K = [-M, M]$ with $M$ large.
So every sequence of them has a weakly convergent subsequence.
The family of Dirac measures $\delta_n$, $n \in \N$, on $\R$ is not tight, and no subsequence converges weakly.
The mass escapes to infinity.

## Explanations

### L1 human

A family of probability measures is tight when no mass runs away to infinity.
The theorem says that tightness is exactly what one needs to extract convergent subsequences.
It plays the role of the Bolzano–Weierstrass theorem for measures.

### L2 human

In probability, one proves convergence in distribution in two steps.
First one shows tightness, which gives limit points by part 1.
Then one shows that all limit points are the same measure, for example through characteristic functions or finite-dimensional distributions.
This scheme proves Donsker's invariance principle for random walks.
On a Polish space, the set of probability measures with the weak topology is itself a Polish space, metrized by the Lévy–Prokhorov metric.
