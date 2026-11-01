---
tag: 552AWX3QXN
kind: definition
name: Wiener process
msc: [60J65, 60G15]
defines: 22735FGJV6
uses: [0QH5ENKZM1, 05AQE0QR0D, 0GBJACNAP6]
sources:
  - url: https://en.wikipedia.org/wiki/Wiener_process
---

## Definition

Let $(\Omega, \mathcal{F}, P)$ be a probability space.
A *Wiener process*, or standard Brownian motion, is a real [[stochastic process|0QH5ENKZM1]] $(W_t)_{t \ge 0}$ such that:

1. $W_0 = 0$ almost surely.
2. For all $0 \le t_0 < t_1 < \dots < t_n$, the increments $W_{t_1} - W_{t_0}, \dots, W_{t_n} - W_{t_{n-1}}$ are [[independent|0GBJACNAP6]].
3. For all $0 \le s < t$, the increment $W_t - W_s$ has the [[normal distribution|05AQE0QR0D]] with mean $0$ and variance $t - s$.
4. Almost surely, the path $t \mapsto W_t$ is continuous.

## Remarks

Such a process exists; one construction takes the uniform limit of random series $\sum_k \xi_k \phi_k(t)$, with independent standard normal $\xi_k$ and suitable functions $\phi_k$ such as the Schauder functions.
The process $X_t = 2 W_t$ satisfies clauses 1, 2 and 4 but fails clause 3, since $X_t - X_s$ has variance $4(t - s)$.
Equivalently, $W$ is a centred [[Gaussian process|22WEM6RTW0]] with $E[W_s W_t] = \min(s, t)$ and continuous paths.
A process $W_t + \mu t$, or $\sigma W_t$, is called a Brownian motion with drift $\mu$ or with variance parameter $\sigma^2$.
A $d$-dimensional Wiener process is a vector of $d$ independent real Wiener processes.
