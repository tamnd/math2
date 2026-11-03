---
tag: 7S2A6ERJJ9
kind: definition
name: Cournot competition
msc: [91B54, 91A10, 91A80]
defines: S5HGX1PNZR
uses: [5MZTZRC3CZ, 745WYP9YJ0]
sources:
  - url: https://en.wikipedia.org/wiki/Cournot_competition
---

## Definition

Let $n \ge 2$ firms produce one homogeneous good.
Let $P \colon \R_+ \to \R_+$ be the inverse demand function, so that $P(Q)$ is the market price when the total quantity is $Q$.
Let $C_i \colon \R_+ \to \R_+$ be the cost function of firm $i$.
The *Cournot game* is the [[normal-form game|5MZTZRC3CZ]] in which:

1. each firm $i$ chooses a quantity $q_i \ge 0$, all at the same time;
2. the payoff of firm $i$ is its profit $\pi_i(q_1, \dots, q_n) = P(q_1 + \cdots + q_n) \, q_i - C_i(q_i)$.

A *Cournot equilibrium* is a [[Nash equilibrium|745WYP9YJ0]] $(q_1^*, \dots, q_n^*)$ of this game: for each $i$ and each $q_i \ge 0$, $\pi_i(q_i^*, q_{-i}^*) \ge \pi_i(q_i, q_{-i}^*)$.

## Remarks

Example: $n = 2$, $P(Q) = \max(a - Q, 0)$ and $C_i(q) = c q$ with $0 \le c < a$.
For $q_j < a - c$, the best response of firm $i$ to $q_j$ maximizes $(a - q_i - q_j - c) q_i$, which gives $q_i = (a - c - q_j)/2$.
The two best responses meet at $q_1^* = q_2^* = (a - c)/3$, with price $(a + 2c)/3$.
With $n$ identical firms, the symmetric equilibrium is $q_i^* = (a - c)/(n + 1)$, and the price $(a + n c)/(n + 1)$ tends to marginal cost $c$ as $n \to \infty$.

Non-example: in the same market, $q_1 = q_2 = (a - c)/4$, the split of the monopoly quantity, is not a Cournot equilibrium.
Firm $1$'s best response to $q_2 = (a - c)/4$ is $3(a - c)/8 \ne (a - c)/4$.

When firms choose prices instead of quantities, the model becomes [[Bertrand competition|YA9SSGCKY3]], and when one firm moves first it becomes [[Stackelberg competition|FZVHQ1Q686]].
