---
tag: C9EDBYCRAY
kind: definition
name: Detailed balance
msc: [60J10, 82C05]
defines: CTGN6CK1ZS
uses: [033TJBZDG0, 0F462493EA, 0KRH5157WP, 00C0BR7D7H]
sources:
  - url: https://en.wikipedia.org/wiki/Detailed_balance
---

## Definition

Let $P = (p_{ij})_{i, j \in S}$ be the [[transition matrix|0F462493EA]] of a time-homogeneous [[Markov chain|033TJBZDG0]] on a countable set $S$.
A probability distribution $\pi = (\pi_i)_{i \in S}$ on $S$ satisfies *detailed balance* for $P$ if
$$\pi_i \, p_{ij} = \pi_j \, p_{ji} \quad \text{for all } i, j \in S.$$
The chain is then called *reversible* with respect to $\pi$.

## Remarks

Detailed balance implies that $\pi$ is [[stationary|0KRH5157WP]]: $\sum_i \pi_i p_{ij} = \sum_i \pi_j p_{ji} = \pi_j$.
If $X_0$ has law $\pi$, then $(X_0, \ldots, X_n)$ and $(X_n, \ldots, X_0)$ have the same law.
Example: on a finite connected [[graph|00C0BR7D7H]] with edge set $E$, let $p_{ij} = 1/\deg(i)$ when $j$ is a neighbour of $i$.
With $\pi_i = \deg(i) / (2\abs{E})$, both sides equal $1/(2\abs{E})$ for neighbours, and both vanish otherwise.
Non-example: on $S = \set{1, 2, 3}$ let the chain move deterministically $1 \to 2 \to 3 \to 1$.
The uniform law is stationary, but $\pi_1 p_{12} = 1/3$ while $\pi_2 p_{21} = 0$, so detailed balance fails.
Kolmogorov's criterion says that an irreducible chain with a stationary distribution is reversible if and only if $p_{i_1 i_2} p_{i_2 i_3} \cdots p_{i_n i_1} = p_{i_1 i_n} p_{i_n i_{n-1}} \cdots p_{i_2 i_1}$ for every finite cycle of states.
