---
tag: F52PFPZ4H9
kind: definition
name: Stochastic difference equation
msc: [39A50, 62M10]
defines: WPYG78BSD5
uses: [0PNRKMRC55, 0QH5ENKZM1, YYNCJSR0PJ]
sources:
  - url: https://en.wikipedia.org/wiki/Autoregressive_model
---

## Definition

Let $(\Omega, \mathcal{F}, P)$ be a probability space, let $k, l \ge 1$, and let $(\xi_n)_{n \ge 1}$ be a sequence of [[random variables|0PNRKMRC55]] with values in $\R^l$.
For each $n \ge 0$ let $f_n \colon \R^k \times \R^l \to \R^k$ be a Borel [[measurable function|YYNCJSR0PJ]].
A *stochastic difference equation* is a recursion
$$X_{n+1} = f_n(X_n, \xi_{n+1}), \qquad n \ge 0,$$
together with an initial random variable $X_0$ with values in $\R^k$.
Its *solution* is the [[stochastic process|0QH5ENKZM1]] $(X_n)_{n \ge 0}$ defined recursively by these equations.

## Remarks

Example: the autoregressive equation of order $1$, $X_{n+1} = a X_n + \varepsilon_{n+1}$ with $a \in \R$ and independent identically distributed $\varepsilon_n$, is a stochastic difference equation with $f_n(x, e) = ax + e$.
Its solution is $X_n = a^n X_0 + \sum_{j=1}^{n} a^{n-j} \varepsilon_j$.

Non-example: $X_{n+1} = a X_n$ with a constant $X_0$ involves no random input, so it is a deterministic difference equation whose solution is a single sequence.

Higher-order equations, such as the autoregressive model of order $p$, $X_{n+1} = \sum_{i=1}^{p} a_i X_{n+1-i} + \varepsilon_{n+1}$, become first order on $\R^p$ by stacking $p$ consecutive values.
If $X_0, \xi_1, \xi_2, \dots$ are independent, the solution is a Markov chain.
It is time-homogeneous when $f_n$ does not depend on $n$ and the $\xi_n$ are identically distributed.
