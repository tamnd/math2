---
tag: 8J77QFAEQT
kind: problem
name: Multi-armed bandit
msc: [62L05, 90C40, 68W27]
uses: [0WQNRCNY3M, 0DVDCMA2DK]
about: [WCNHWTJXYD]
sources:
  - url: https://en.wikipedia.org/wiki/Multi-armed_bandit
same_as:
  wikidata: Q2882343
  wikipedia: Multi-armed bandit
history:
  posed_by: "Herbert Robbins"
  first_stated: "1952"
  notes: "Robbins formulated it in his paper on the sequential design of experiments; related allocation questions appear earlier in work of William R. Thompson (1933)."
---

## Problem

Let $K \ge 2$ and let $\nu_1, \dots, \nu_K$ be [[probability distributions|0DVDCMA2DK]] on $\R$ with finite means $\mu_1, \dots, \mu_K$, unknown to the player.
At each time $t = 1, 2, \dots, T$, the player chooses an arm $I_t \in \set{1, \dots, K}$, possibly at random, as a function of the past choices and rewards.
The player then receives a reward $X_t$ drawn from $\nu_{I_t}$, independently of the past given $I_t$.
Let $\mu^* = \max_i \mu_i$.
The *regret* of a strategy after $T$ rounds is
$$R_T = T \mu^* - \mathbb{E}\Big[\sum_{t=1}^{T} X_t\Big].$$
The problem asks for strategies whose regret grows as slowly as possible in $T$, uniformly over a given class of reward distributions.

## Remarks

The difficulty is the trade-off between exploration, trying arms to learn their means, and exploitation, playing the arm that looks best so far.
Always playing the arm with the best empirical mean can lock onto a bad arm forever, and then the regret grows linearly in $T$.
For Bernoulli rewards and similar families, Lai and Robbins showed in 1985 a lower bound.
Every strategy that is good for all parameter values has regret at least of order $\log T$, and they gave strategies that attain this order.
Index strategies such as the upper confidence bound rule UCB1 achieve regret $O(\log T)$ for rewards in $[0, 1]$ with a constant that depends on the gaps $\mu^* - \mu_i$.
In the Bayesian version with discounted rewards and independent arms, an optimal strategy is given by the Gittins index rule.

## Explanations

### L1 human

A gambler faces a row of slot machines, each paying out at its own unknown average rate.
Every pull of a lever both earns money and teaches something about that machine.
Pulling only the machine that looks best so far may miss a better one; trying machines too often wastes pulls on bad ones.
The multi-armed bandit problem asks how to balance these two needs, and it models clinical trials, online advertising and adaptive routing.
