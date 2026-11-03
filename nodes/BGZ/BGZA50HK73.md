---
tag: BGZA50HK73
kind: definition
name: Complete market
msc: [91G15, 91G20]
defines: A1V152H2CA
uses: [Q626SC54P7, 0PNRKMRC55]
sources:
  - url: https://en.wikipedia.org/wiki/Complete_market
---

## Definition

Consider a market as in the definition of [[arbitrage|Q626SC54P7]], with discounted prices $S_t$, $t = 0, \dots, T$, on a filtered probability space $(\Omega, \mathcal{F}, (\mathcal{F}_t), P)$.
A *contingent claim* is a [[random variable|0PNRKMRC55]] $H$ that is $\mathcal{F}_T$-measurable, expressed in units of the numéraire.
A claim $H$ is *attainable* if there is a self-financing strategy with initial value $V_0$ and final value $V_T = H$ almost surely.
The market is *complete* if it is free of arbitrage and every contingent claim is attainable.

## Remarks

Example: one period, $\Omega = \set{u, d}$, interest rate $0$, $S_0 = 100$, $S_1(u) = 120$, $S_1(d) = 90$.
A claim with values $H(u), H(d)$ is replicated by $\xi = (H(u) - H(d))/30$ shares and the initial value $V_0 = H(d) + 10\xi$.
Indeed $V_0 + 20\xi = H(u)$ and $V_0 - 10\xi = H(d)$.

Non-example: interest rate $0$, $S_0 = 100$, three states with $S_1 \in \set{120, 100, 90}$, and the claim $H = (0, 1, 0)$.
Replication would need $V_0 = 1$ from the middle state, then $\xi = -1/20$ from the up state, and then $V_0 - 10\xi = 3/2 \ne 0$ in the down state.
So $H$ is not attainable and the market is incomplete, although it is free of arbitrage.

In a finite one-period market with $K$ states, completeness requires that the payoff vectors of the traded assets, numéraire included, span $\R^K$.
