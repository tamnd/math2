---
tag: 8CKDVESXT6
kind: statement
role: theorem
name: Lévy's characterization of Brownian motion
msc: [60J65, 60G44]
uses: [ZWJ9G89W3T, ZBYC3MFW89, 552AWX3QXN, HNK1Y62G7V, YRNFE016FF]
about: [22735FGJV6, XC2YPC2BSW]
sources:
  - url: https://en.wikipedia.org/wiki/Wiener_process
---

## Statement

Let $(\Omega, \mathcal{F}, P)$ be a probability space with a [[filtration|HNK1Y62G7V]] $(\mathcal{F}_t)_{t \ge 0}$.
Let $(X_t)_{t \ge 0}$ be a real [[adapted|YRNFE016FF]] process with continuous paths and $X_0 = 0$.
Assume that $(X_t)$ and $(X_t^2 - t)$ are both [[local martingales|ZWJ9G89W3T]].
Then $(X_t)$ is a [[Wiener process|552AWX3QXN]], and for all $0 \le s < t$ the increment $X_t - X_s$ is independent of $\mathcal{F}_s$.

## Remarks

The second hypothesis says that the [[quadratic variation|ZBYC3MFW89]] of $X$ is $[X]_t = t$.
For a fixed $u \in \R$, Itô's formula shows that $Z_t = \exp(i u X_t + u^2 t / 2)$ is a local martingale; it is bounded on bounded time intervals, hence a martingale.
So $E[\exp(i u (X_t - X_s)) \mid \mathcal{F}_s] = \exp(-u^2 (t - s)/2)$, which identifies the conditional law of the increment as normal with mean $0$ and variance $t - s$.
Continuity is necessary: for a Poisson process $N$ of rate $1$, both $N_t - t$ and $(N_t - t)^2 - t$ are martingales, but $N_t - t$ is not a Wiener process.
In dimension $d$, a continuous process $X$ with $X_0 = 0$ is a $d$-dimensional Wiener process if each $X^i$ and each $X^i X^j - \delta_{ij} t$ is a local martingale.

## Explanations

### L1 human

Brownian motion is the only continuous fair game whose squared size grows on average exactly like time.
Nothing about normal distributions or independence has to be assumed: they come for free.
So these two martingale properties pin down Brownian motion completely.

### L2 human

The theorem is the standard way to recognise a Brownian motion inside stochastic calculus.
It gives the Dambis–Dubins–Schwarz theorem: a continuous local martingale $M$ with $[M]_\infty = \infty$ is a time-changed Brownian motion, $M_t = B_{[M]_t}$.
It is also a step in the proof of the [[Girsanov theorem|Z76HD1BZ29]], and it shows that $\int_0^t \sgn(W_s) \, dW_s$ is a Wiener process, which is used with [[Tanaka's formula|GEM0ERJ5ZB]].
