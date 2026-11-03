---
tag: XK5VS1EBTX
kind: definition
name: Best response
msc: [91A10, 91A26]
defines: QS6VCNJK60
uses: [5MZTZRC3CZ, P01KKHB155]
sources:
  - url: https://en.wikipedia.org/wiki/Best_response
---

## Definition

Let $G = (N, (S_i), (u_i))$ be a finite [[normal-form game|5MZTZRC3CZ]] with [[mixed strategies|P01KKHB155]] $\Delta(S_j)$.
Let $i \in N$ and let $\sigma_{-i}$ be a profile of mixed strategies of the players other than $i$.
A mixed strategy $\sigma_i \in \Delta(S_i)$ is a *best response* to $\sigma_{-i}$ if
$$u_i(\sigma_i, \sigma_{-i}) \ge u_i(\tau_i, \sigma_{-i}) \quad \text{for all } \tau_i \in \Delta(S_i).$$
The set of best responses is written $\mathrm{BR}_i(\sigma_{-i})$.

## Remarks

Since $u_i$ is linear in $\sigma_i$, a mixed strategy is a best response if and only if every pure strategy in its support is a best response.
So $\mathrm{BR}_i(\sigma_{-i})$ is a nonempty face of the simplex $\Delta(S_i)$.
Example: in matching pennies let player 2 play $H$ with probability $q = 3/4$.
Player 1 gets $q - (1 - q) = 1/2$ from $H$ and $-1/2$ from $T$, so $H$ is the unique best response.
Non-example: against the same $\sigma_2$, the mixed strategy $\sigma_1 = (1/2, 1/2)$ gets payoff $0 < 1/2$, so it is not a best response.
