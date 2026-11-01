---
tag: 7Y2CZ5B2SN
kind: definition
name: Adapted process
msc: [60G05, 60G07]
defines: YRNFE016FF
uses: [HNK1Y62G7V, 0QH5ENKZM1]
sources:
  - url: https://en.wikipedia.org/wiki/Adapted_process
---

## Definition

Let $(\Omega, \mathcal{F}, (\mathcal{F}_t)_{t \in T}, P)$ be a probability space with a [[filtration|HNK1Y62G7V]] indexed by a totally ordered set $T$.
Let $(S, \mathcal{S})$ be a measurable space.
A [[stochastic process|0QH5ENKZM1]] $X = (X_t)_{t \in T}$ with values in $S$ is *adapted* to $(\mathcal{F}_t)$ if the following holds.
For every $t \in T$, the map $X_t \colon \Omega \to S$ is measurable with respect to $\mathcal{F}_t$ and $\mathcal{S}$.

## Remarks

Every process is adapted to its natural filtration $\mathcal{F}_t^X = \sigma(X_s : s \le t)$, and this is the smallest filtration to which it is adapted.

Example: let $Y_1, Y_2, \dots$ be random variables with natural filtration $\mathcal{F}_n = \sigma(Y_1, \dots, Y_n)$.
The partial sums $S_n = Y_1 + \cdots + Y_n$ form an adapted process, since $S_n$ is a measurable function of $Y_1, \dots, Y_n$.

Non-example: let the $Y_k$ be independent fair signs, equal to $1$ or $-1$, with the same filtration, and let $X_n = Y_{n+1}$.
Then $X_n$ is independent of $\mathcal{F}_n$ and not almost surely constant, so it is not $\mathcal{F}_n$-measurable; the process $X$ looks one step into the future.

In continuous time a stronger notion is often needed: $X$ is *progressively measurable* if, for every $t$, the map $(s, \omega) \mapsto X_s(\omega)$ on $[0, t] \times \Omega$ is measurable with respect to $\mathcal{B}([0, t]) \otimes \mathcal{F}_t$.
An adapted process with right-continuous or left-continuous paths is progressively measurable.
