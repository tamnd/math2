---
tag: VYADGX4G3E
kind: definition
name: Stackelberg competition
msc: [91A65, 91B54, 91A18]
defines: FZVHQ1Q686
uses: [S5HGX1PNZR, 4Y8AF9H9HA, HE8K9M4EXN]
sources:
  - url: https://en.wikipedia.org/wiki/Stackelberg_competition
---

## Definition

Let two firms produce one homogeneous good, with inverse demand $P \colon \R_+ \to \R_+$ and cost functions $C_1, C_2 \colon \R_+ \to \R_+$, and profits $\pi_i(q_1, q_2) = P(q_1 + q_2) q_i - C_i(q_i)$ as in [[Cournot competition|S5HGX1PNZR]].
The *Stackelberg game* is the [[extensive-form game|4Y8AF9H9HA]] with perfect information in which:

1. firm $1$, the leader, chooses $q_1 \ge 0$;
2. firm $2$, the follower, observes $q_1$ and chooses $q_2 \ge 0$;
3. the payoffs are $\pi_1(q_1, q_2)$ and $\pi_2(q_1, q_2)$.

A *Stackelberg equilibrium* is a [[subgame perfect equilibrium|HE8K9M4EXN]] of this game.
It consists of a quantity $q_1^*$ and a strategy $q_2 = R(q_1)$ of the follower such that:

- $R(q_1)$ maximizes $\pi_2(q_1, \cdot)$ for every $q_1 \ge 0$;
- $q_1^*$ maximizes $\pi_1(q_1, R(q_1))$ over $q_1 \ge 0$.

## Remarks

Example: $P(Q) = \max(a - Q, 0)$ and $C_i(q) = c q$ with $0 \le c < a$.
The follower's best response is $R(q_1) = (a - c - q_1)/2$ for $q_1 \le a - c$.
The leader then maximizes $(a - q_1 - R(q_1) - c) q_1 = \frac{(a - c - q_1) q_1}{2}$, which gives $q_1^* = (a - c)/2$ and $q_2^* = (a - c)/4$.
The leader earns $(a - c)^2 / 8$, more than its Cournot profit $(a - c)^2 / 9$.

Non-example: the Cournot pair $q_1 = q_2 = (a - c)/3$ is not a Stackelberg outcome.
The follower's reply is indeed optimal, but the leader, anticipating $R$, gains by raising $q_1$ to $(a - c)/2$.

A strategy of the follower must give a reply to every $q_1$, not only to $q_1^*$; this is what makes the equilibrium subgame perfect.
The same leader–follower structure, applied to general games, gives Stackelberg games in bilevel optimization.
