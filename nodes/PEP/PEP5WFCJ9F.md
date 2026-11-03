---
tag: PEP5WFCJ9F
kind: definition
name: Incentive compatibility
msc: [91B03]
defines: T1GTBBMHCW
uses: [DTXJQKEHDP, 2XQ7VWT8KJ]
sources:
  - url: https://en.wikipedia.org/wiki/Incentive_compatibility
---

## Definition

Let $N = \set{1, \dots, n}$ be a set of agents, where agent $i$ has a set $\Theta_i$ of types.
Let $X$ be a set of outcomes, and let $u_i \colon X \times \Theta_i \to \R$ be the utility of agent $i$.
Let $g \colon \Theta_1 \times \cdots \times \Theta_n \to X$ be a direct [[mechanism|DTXJQKEHDP]], where each agent reports a type.
For a profile $\theta$ write $\theta_{-i}$ for the types of the agents other than $i$.

1. The mechanism $g$ is *dominant-strategy incentive compatible*, or *strategy-proof*, if for every $i$, every $\theta_i, \theta_i' \in \Theta_i$ and every $\theta_{-i}$:
$$u_i(g(\theta_i, \theta_{-i}), \theta_i) \ge u_i(g(\theta_i', \theta_{-i}), \theta_i).$$
2. Suppose the type profile is drawn from a common prior distribution on $\Theta = \Theta_1 \times \cdots \times \Theta_n$, as in a [[Bayesian game|2XQ7VWT8KJ]]. The mechanism $g$ is *Bayesian incentive compatible* if for every $i$ and every $\theta_i, \theta_i' \in \Theta_i$:
$$\mathbb{E}\bigl[u_i(g(\theta_i, \theta_{-i}), \theta_i) \mid \theta_i\bigr] \ge \mathbb{E}\bigl[u_i(g(\theta_i', \theta_{-i}), \theta_i) \mid \theta_i\bigr],$$
where the expectation is over $\theta_{-i}$ given $\theta_i$.

## Remarks

Every strategy-proof mechanism is Bayesian incentive compatible for every prior, but not conversely.
Example: one object, two bidders with values $\theta_1, \theta_2 \ge 0$, and the second-price rule: the higher report wins and pays the lower report.
If bidder $1$ wins by reporting truthfully, she pays $\theta_2 \le \theta_1$, and another report either changes nothing or makes her lose and get $0$.
If she loses by reporting truthfully, winning would cost her $\theta_2 \ge \theta_1$.
So truth-telling is optimal and the rule is strategy-proof.
Non-example: consider the first-price rule, where the winner pays her own report.
A bidder with value $\theta_1 = 10$ facing a report $\theta_2 = 4$ gets $0$ by reporting $10$ but $5$ by reporting $5$, so clause 1 fails.
In settings with money, the outcome is often split into an allocation and payments, and $u_i$ is quasilinear: value of the allocation minus payment.

## Explanations

### L1 human

Incentive compatibility means honesty is a best strategy.
The strong version asks this whatever the others report; the Bayesian version asks it only on average, when the others are honest.
