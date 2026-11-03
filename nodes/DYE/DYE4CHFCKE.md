---
tag: DYE4CHFCKE
kind: definition
name: Threshold model of collective behavior
msc: [91D30, 91D10]
defines: 6QC26Z29WJ
uses: [0H8H7ZTHW2, 00C0BR7D7H]
sources:
  - url: https://en.wikipedia.org/wiki/Threshold_model
---

## Definition

Let a population consist of $N \ge 1$ individuals, and let individual $k$ have a *threshold* $\theta_k \in [0, 1]$.
Let $F(r) = \frac{1}{N}\#\set{k : \theta_k \le r}$ be the [[cumulative distribution function|0H8H7ZTHW2]] of the thresholds.
In the *threshold model*, let $r_t \in [0, 1]$ be the share of individuals acting at time $t$.
It evolves by
$$r_0 = 0, \qquad r_{t+1} = F(r_t),$$
that is, individual $k$ acts at time $t + 1$ exactly when $r_t \ge \theta_k$.
The *equilibrium outcome* is the limit $r^* = \lim_{t \to \infty} r_t$.

## Remarks

The sequence $r_t$ is nondecreasing because $F$ is.
It takes values in the finite set $\set{0, 1/N, \dots, 1}$, so it becomes constant after at most $N$ steps.
The limit $r^*$ is the least fixed point of $F$.
Example: $N = 100$ and $\theta_k = (k-1)/100$ for $k = 1, \dots, 100$.
Then $F(r) = \min(1, \floor{100 r}/100 + 1/100)$, so $r_t = t/100$ until $r_{100} = 1$, and everyone acts.
Non-example of a cascade: replacing $\theta_2 = 1/100$ by $2/100$ gives $F(0) = F(1/100) = 1/100$, so $r^* = 1/100$.
In the network version, individuals are vertices of a [[graph|00C0BR7D7H]] and compare $\theta_k$ with the share of their own neighbours who act.
