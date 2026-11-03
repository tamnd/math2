---
tag: HV299DGBNZ
kind: definition
name: Bayesian game
msc: [91A27, 91A10]
defines: 2XQ7VWT8KJ
uses: [5MZTZRC3CZ, 00NBBSXRQS, 0990W5PN13, 0DVDCMA2DK, 0WQNRCNY3M, 745WYP9YJ0]
sources:
  - url: https://en.wikipedia.org/wiki/Bayesian_game
---

## Definition

A finite *Bayesian game* consists of:

1. a finite set $N = \set{1, \dots, n}$ of players;
2. for each player $i$, a finite set $A_i$ of actions; write $A = A_1 \times \cdots \times A_n$;
3. for each player $i$, a finite set $T_i$ of types; write $T = T_1 \times \cdots \times T_n$;
4. a [[prior|00NBBSXRQS]] [[probability distribution|0DVDCMA2DK]] $p$ on $T$, common to all players;
5. for each player $i$, a payoff function $u_i \colon A \times T \to \R$.

The game is played as follows.
A type profile $t \in T$ is drawn according to $p$, each player $i$ learns only her own type $t_i$, and the players choose actions simultaneously.
A (pure) strategy of player $i$ is a map $s_i \colon T_i \to A_i$.

## Remarks

A type $t_i$ with $p(t_i) > 0$ has the belief $p(t_{-i} \mid t_i)$ about the other types, given by [[conditional probability|0990W5PN13]].
A strategy profile $s$ is a *Bayesian Nash equilibrium* if for every player $i$ and every type $t_i$ with $p(t_i) > 0$, the action $s_i(t_i)$ maximizes the [[expected value|0WQNRCNY3M]]
$$\sum_{t_{-i}} p(t_{-i} \mid t_i) \, u_i\big(a_i, s_{-i}(t_{-i}), (t_i, t_{-i})\big)$$
over $a_i \in A_i$.
Suppose every type has positive probability.
Then this is a [[Nash equilibrium|745WYP9YJ0]] of the [[normal-form game|5MZTZRC3CZ]] whose strategies are the maps $s_i$, with ex ante expected payoffs.
Mixed strategies are defined in the same way, with $s_i(t_i)$ a probability distribution on $A_i$.

Example: take a sealed-bid first-price auction with two bidders.
Let $T_i$ be a finite set of values, $A_i$ a finite set of bids, and $p$ the joint distribution of values.
The payoff $u_i(a, t)$ is $t_i - a_i$ if $a_i$ is strictly the highest bid, $(t_i - a_i)/2$ if the two bids are equal, and $0$ otherwise.
All five clauses hold, so this is a Bayesian game.

Non-example: if the players hold beliefs about each other's types that cannot be derived from one common distribution $p$, clause 4 fails.
Such games with inconsistent beliefs are studied too, but they are not Bayesian games in the sense above.
