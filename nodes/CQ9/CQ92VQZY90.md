---
tag: CQ92VQZY90
kind: definition
name: Nash equilibrium
msc: [91A10, 91A06]
defines: 745WYP9YJ0
uses: [5MZTZRC3CZ, P01KKHB155, QS6VCNJK60]
sources:
  - url: https://en.wikipedia.org/wiki/Nash_equilibrium
---

## Definition

Let $G = (N, (S_i), (u_i))$ be a finite [[normal-form game|5MZTZRC3CZ]].
A [[mixed strategy|P01KKHB155]] profile $\sigma^* = (\sigma_1^*, \dots, \sigma_n^*)$ is a *Nash equilibrium* if for every player $i \in N$
$$u_i(\sigma_i^*, \sigma_{-i}^*) \ge u_i(\tau_i, \sigma_{-i}^*) \quad \text{for all } \tau_i \in \Delta(S_i).$$
A *pure Nash equilibrium* is a Nash equilibrium in which every $\sigma_i^*$ is a pure strategy.

## Remarks

Equivalently, $\sigma_i^*$ is a [[best response|QS6VCNJK60]] to $\sigma_{-i}^*$ for every $i$.
It suffices to check deviations $\tau_i$ to pure strategies, since $u_i$ is linear in $\tau_i$.
In particular, at a Nash equilibrium every pure strategy in the support of $\sigma_i^*$ gives player $i$ the same payoff.
The same definition applies to games with infinite strategy sets, with pure strategy profiles.
Example: in the prisoner's dilemma, at $(D, D)$ player 1 gets $1$, and switching to $C$ gives $0$; by symmetry $(D, D)$ is a pure Nash equilibrium.
Non-example: $(C, C)$ is not one, because player 1 gets $5 > 3$ by switching to $D$.
