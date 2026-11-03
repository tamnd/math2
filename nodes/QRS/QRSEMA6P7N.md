---
tag: QRSEMA6P7N
kind: definition
name: Jump diffusion model
msc: [91G20, 60J76, 60H10]
defines: 8BZZW063X4
uses: [22735FGJV6, 0MTNR28K60, D48DR46B97, 8NT5CFG2ZR]
sources:
  - url: https://en.wikipedia.org/wiki/Jump_diffusion
---

## Definition

On one probability space, let $W$ be a [[Brownian motion|22735FGJV6]] and let $N$ be a [[Poisson process|0MTNR28K60]] on $[0, \infty)$ with intensity $\lambda > 0$.
Let $Y_1, Y_2, \dots$ be independent and identically distributed random variables with $Y_i > 0$.
Assume that $W$, $N$ and $(Y_i)$ are independent, and let $\mu \in \R$ and $\sigma > 0$.
The *jump diffusion model* (of Merton type) for an asset price $S$ is
$$S_t = S_0 \exp\left( \left(\mu - \tfrac{1}{2}\sigma^2\right) t + \sigma W_t \right) \prod_{i=1}^{N_t} Y_i, \qquad S_0 > 0.$$
At the $i$-th jump time of $N$ the price is multiplied by $Y_i$.

## Remarks

Equivalently, $S$ solves $dS_t = S_{t-} \left( \mu \, dt + \sigma \, dW_t + dJ_t \right)$ with the compound Poisson process $J_t = \sum_{i=1}^{N_t} (Y_i - 1)$.
The log-price $\ln S_t$ is a [[Lévy process|8NT5CFG2ZR]] with finitely many jumps on each bounded time interval.
Example: Merton's model takes $\ln Y_i$ normal with mean $m$ and variance $\delta^2$; then, given $N_t = n$, $\ln S_t$ is normal.
Non-example: if $Y_i = 1$ for all $i$, the jumps have size zero and $S$ is a [[geometric Brownian motion|D48DR46B97]].
Another choice, due to Kou, takes $\ln Y_i$ with a double exponential law.
