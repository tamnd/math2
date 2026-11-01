---
tag: JPD7Q0P4F6
kind: statement
role: theorem
name: Skorokhod's representation theorem
msc: [60B10, "60F05"]
uses: [0VKD1TP7F3, 0Z2P41SVDP, 059TJN0NZ1, 0AAXWGT5TD, 0X60VE98HN]
about: [0AAXWGT5TD]
sources:
  - url: https://en.wikipedia.org/wiki/Skorokhod%27s_representation_theorem
same_as:
  wikidata: Q401905
  wikipedia: Skorokhod's representation theorem
---

## Statement

Let $S$ be a [[separable|0Z2P41SVDP]] [[metric space|0VKD1TP7F3]] with its Borel σ-algebra.
Let $\mu, \mu_1, \mu_2, \dots$ be [[probability measures|059TJN0NZ1]] on $S$ such that $\mu_n$ converges weakly to $\mu$.
Then there are a probability space $(\Omega, \mathcal{F}, P)$ and random variables $X, X_1, X_2, \dots$ on it with values in $S$ with the following properties.
The variable $X$ has law $\mu$, each $X_n$ has law $\mu_n$, and $X_n \to X$ [[almost surely|0AAXWGT5TD]].

## Remarks

On $S = \R$ there is a short proof: let $U$ be uniform on $(0, 1)$, and set $X_n = F_n^{-1}(U)$ and $X = F^{-1}(U)$, where $F_n^{-1}$ and $F^{-1}$ are the [[quantile functions|0X60VE98HN]] of $\mu_n$ and $\mu$.
Weak convergence implies $F_n^{-1}(u) \to F^{-1}(u)$ at each continuity point $u$ of $F^{-1}$, and $F^{-1}$ is monotone, so it has only countably many discontinuities, a null set for $U$.
The general proof builds the variables from fine partitions of $S$ into small sets whose boundaries have $\mu$-measure $0$.
The theorem gives quick proofs of facts about weak convergence: for example, if $X_n \to X$ in distribution and $h$ is continuous, then $h(X_n) \to h(X)$ in distribution, which is the [[continuous mapping theorem|CFRN0G7GDB]].
It also gives $E[\abs{X}] \le \liminf_n E[\abs{X_n}]$ for real variables, by Fatou's lemma.
The new variables only have the right laws; the original random variables, if any, need not converge almost surely.

## Explanations

### L1 human

Convergence in distribution is a weak notion: it only says that the laws get close, not the random values.
Skorokhod's theorem says that one can always rebuild the random variables, with the same laws, on a new space where the values themselves converge.
This lets one use strong tools for almost sure convergence when only convergence in law is known.

### L2 human

The theorem is a standard device in weak convergence theory.
It appears in proofs of the [[continuous mapping theorem|CFRN0G7GDB]] and of results on uniform integrability and convergence of moments.
It is also used for stochastic processes with values in function spaces.
In the real case it is just the quantile coupling.
It should not be confused with Skorokhod's embedding theorem, which embeds a random walk into a Brownian motion.
