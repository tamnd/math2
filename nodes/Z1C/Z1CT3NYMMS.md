---
tag: Z1CT3NYMMS
kind: definition
name: Ruin theory
msc: [91G05, 60G55, 60K10]
defines: YSXZZ1HQR5
uses: [0QH5ENKZM1, 0PNRKMRC55]
sources:
  - url: https://en.wikipedia.org/wiki/Ruin_theory
---

## Definition

Let $u \ge 0$ be an initial capital and let $c > 0$ be a premium rate.
Let $(S_t)_{t \ge 0}$ be a [[stochastic process|0QH5ENKZM1]] with $S_0 = 0$ and nondecreasing paths, the total claims paid up to time $t$.
The *surplus process* is $U_t = u + c t - S_t$.
The *time of ruin* is $\tau = \inf\set{ t \ge 0 : U_t < 0 }$, with $\inf \emptyset = \infty$.
The *probability of ruin* is $\psi(u) = P(\tau < \infty)$, and the probability of ruin before a horizon $T$ is $\psi(u, T) = P(\tau \le T)$.
Ruin theory is the study of $\tau$, $\psi$ and related quantities.

## Remarks

Example: if claims never occur, $S_t = 0$, then $U_t = u + ct \ge 0$ for all $t$ and $\psi(u) = 0$.
Example: in the Cramér–Lundberg model, with exponential claims of mean $\mu$ and premium $c = (1 + \theta) \lambda \mu$, one has $\psi(u) = \frac{1}{1 + \theta} \exp\left( - \frac{\theta u}{(1 + \theta) \mu} \right)$.
Non-example: a surplus observed only at the end of each year gives a discrete-time model.
Its ruin probability can be smaller than $\psi(u)$, since dips below zero within a year are not seen.
The function $\psi$ is nonincreasing in $u$, because more capital can only delay ruin.
