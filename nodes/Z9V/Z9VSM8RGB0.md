---
tag: Z9VSM8RGB0
kind: definition
name: Short-rate model
msc: [91G30, 60H10]
defines: 7TZ87AS1MW
uses: [Y99MCTGZHZ, 22735FGJV6, 858BHBY2BD, 0TTDGTEFMN, HNK1Y62G7V]
sources:
  - url: https://en.wikipedia.org/wiki/Short-rate_model
---

## Definition

Let $W$ be a [[Brownian motion|22735FGJV6]] under a probability measure $Q$, with its [[filtration|HNK1Y62G7V]] $(\mathcal{F}_t)$.
Let $\mu$ and $\sigma$ be functions of $(t, r)$ such that the equation below has a unique solution.
A *short-rate model* is a [[stochastic differential equation|Y99MCTGZHZ]]
$$dr_t = \mu(t, r_t) \, dt + \sigma(t, r_t) \, dW_t$$
for the short rate $r$, where $Q$ is taken as the [[risk-neutral measure|858BHBY2BD]].
The price at time $t$ of the zero-coupon bond paying $1$ at time $T \ge t$ is defined as the [[conditional expectation|0TTDGTEFMN]]
$$P(t, T) = E_Q\left[ \exp\left( -\int_t^T r_s \, ds \right) \Bigm| \mathcal{F}_t \right].$$

## Remarks

Example: $\mu = 0$ and $\sigma = 0$ give the constant rate $r_t = r_0$, and then $P(t, T) = e^{-r_0 (T - t)}$.
Example: $\mu(t, r) = a(b - r)$ and $\sigma(t, r) = \sigma$ give the Vasicek model.
Non-example: a model given by the dynamics of the whole forward curve $T \mapsto f(t, T)$, as in the Heath–Jarrow–Morton framework, is not of this form in general.
There the short rate alone need not be a Markov process.
The yield of the bond is $-\ln P(t, T) / (T - t)$, and the instantaneous forward rate is $f(t, T) = -\partial_T \ln P(t, T)$.
