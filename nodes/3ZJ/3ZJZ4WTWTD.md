---
tag: 3ZJZ4WTWTD
kind: definition
name: Risk-neutral measure
msc: [91G20, 60G42]
defines: 858BHBY2BD
uses: [Q626SC54P7, 059TJN0NZ1, P0P21KDV6E, 0D0GBNDKDH, 0TTDGTEFMN]
sources:
  - url: https://en.wikipedia.org/wiki/Risk-neutral_measure
---

## Definition

Consider a market as in the definition of [[arbitrage|Q626SC54P7]]: a filtered probability space $(\Omega, \mathcal{F}, (\mathcal{F}_t)_{t = 0, \dots, T}, P)$ and discounted prices $S_t \in \R^d$ of the risky assets.
A *risk-neutral measure* (or *equivalent martingale measure*) is a [[probability measure|059TJN0NZ1]] $Q$ on $(\Omega, \mathcal{F})$ such that:

1. $Q$ is equivalent to $P$: for every $A \in \mathcal{F}$, $Q(A) = 0$ exactly when $P(A) = 0$;
2. each $S_t$ is integrable under $Q$;
3. $S$ is a [[martingale|0D0GBNDKDH]] under $Q$: $\mathbb{E}_Q[S_t \mid \mathcal{F}_{t-1}] = S_{t-1}$ for $t = 1, \dots, T$.

## Remarks

Clause 1 says that $Q$ and $P$ are each [[absolutely continuous|P0P21KDV6E]] with respect to the other.
The [[conditional expectation|0TTDGTEFMN]] in clause 3 is taken under $Q$.
If the riskless asset grows by the factor $1 + r$ per period, clause 3 says $\mathbb{E}_Q[\tilde S_t \mid \mathcal{F}_{t-1}] = (1 + r) \tilde S_{t-1}$ for undiscounted prices $\tilde S$.

Example: one period, $\Omega = \set{u, d}$ with $P(u) = P(d) = 1/2$, interest rate $0$, $S_0 = 100$, $S_1(u) = 120$ and $S_1(d) = 90$.
The measure $Q(u) = 1/3$, $Q(d) = 2/3$ is equivalent to $P$, and $\mathbb{E}_Q[S_1] = 40 + 60 = 100 = S_0$.
So $Q$ is a risk-neutral measure, and it is the only one.

Non-example: $P$ itself is not risk-neutral here, since $\mathbb{E}_P[S_1] = 105 \ne 100$.
The measure with $Q(u) = 1$ is not either: it is not equivalent to $P$, and $\mathbb{E}_Q[S_1] = 120$.
