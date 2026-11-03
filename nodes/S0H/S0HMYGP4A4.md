---
tag: S0HMYGP4A4
kind: definition
name: Affine term structure model
msc: [91G30, 60H10]
defines: WCZEBMCV1F
uses: [7TZ87AS1MW, Y99MCTGZHZ, 22735FGJV6, 0TTDGTEFMN]
sources:
  - url: https://en.wikipedia.org/wiki/Affine_term_structure_model
---

## Definition

Let $X$ be a process in $\R^n$ that solves a [[stochastic differential equation|Y99MCTGZHZ]] driven by a [[Brownian motion|22735FGJV6]] under a risk-neutral measure $Q$.
Let the short rate be $r_t = \delta_0 + \delta \cdot X_t$ with $\delta_0 \in \R$ and $\delta \in \R^n$.
Let $P(t, T)$ be the zero-coupon bond price, the [[conditional expectation|0TTDGTEFMN]] of $\exp(-\int_t^T r_s \, ds)$ given the information at time $t$.
The model is an *affine term structure model* if there are deterministic functions $A$ and $B = (B_1, \dots, B_n)$ with
$$P(t, T) = \exp\big( A(t, T) - B(t, T) \cdot X_t \big) \quad \text{for all } 0 \le t \le T.$$

## Remarks

Example: in the Vasicek model, with $n = 1$ and $X = r$, one has $B(t, T) = (1 - e^{-a(T - t)}) / a$, so the model is affine.
The [[short-rate model|7TZ87AS1MW]] $dr_t = \mu(r_t) \, dt + \sigma(r_t) \, dW_t$ is affine whenever $\mu(r)$ and $\sigma(r)^2$ are affine functions of $r$; then $A$ and $B$ solve Riccati equations.
Non-example: the Black–Karasinski model, in which $\ln r_t$ is an Ornstein–Uhlenbeck process, is not affine: its squared volatility is proportional to $r^2$ and its drift contains $r \ln r$.
The yields $-\ln P(t, T) / (T - t)$ are then affine in $X_t$ as well.
