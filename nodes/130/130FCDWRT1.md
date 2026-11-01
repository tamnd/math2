---
tag: 130FCDWRT1
kind: definition
name: Filtration
msc: [60G05, 60G07]
defines: HNK1Y62G7V
uses: [0NFPJVJJHX, 0SV8K0TDGY]
sources:
  - url: https://en.wikipedia.org/wiki/Filtration_(probability_theory)
---

## Definition

Let $(\Omega, \mathcal{F}, P)$ be a [[probability space|0NFPJVJJHX]], and let $T$ be a totally ordered index set, such as $\N$, $\set{0, 1, \dots, N}$ or $[0, \infty)$.
A *filtration* is a family $(\mathcal{F}_t)_{t \in T}$ of [[sigma-algebras|0SV8K0TDGY]] on $\Omega$ such that:

1. $\mathcal{F}_t \subseteq \mathcal{F}$ for every $t \in T$;
2. $\mathcal{F}_s \subseteq \mathcal{F}_t$ whenever $s, t \in T$ and $s \le t$.

The quadruple $(\Omega, \mathcal{F}, (\mathcal{F}_t)_{t \in T}, P)$ is a *filtered probability space*.

## Remarks

Example: for a [[stochastic process|0QH5ENKZM1]] $(X_t)_{t \in T}$, the *natural filtration* is $\mathcal{F}_t^X = \sigma(X_s : s \le t)$, the smallest $\sigma$-algebra for which all $X_s$ with $s \le t$ are measurable.
If $s \le t$, every generator of $\mathcal{F}_s^X$ is a generator of $\mathcal{F}_t^X$, so clause 2 holds.

Non-example: let $X$ be a random variable that is not almost surely constant, so that $\sigma(X) \neq \set{\emptyset, \Omega}$.
On $T = \set{0, 1}$, the family $\mathcal{F}_0 = \sigma(X)$, $\mathcal{F}_1 = \set{\emptyset, \Omega}$ fails clause 2, since $\mathcal{F}_0 \not\subseteq \mathcal{F}_1$: information would be forgotten.

In continuous time one often assumes the *usual conditions*: $\mathcal{F}_0$ contains all $P$-null sets of the completion of $\mathcal{F}$, and the filtration is right-continuous, that is $\mathcal{F}_t = \bigcap_{s > t} \mathcal{F}_s$ for every $t$.
