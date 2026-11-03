---
tag: DXERNSJH8B
kind: definition
name: Value at risk
msc: [91G70, 62P05]
defines: C063APG9NT
uses: [0PNRKMRC55, 0H8H7ZTHW2, 0X60VE98HN, 05AQE0QR0D]
sources:
  - url: https://en.wikipedia.org/wiki/Value_at_risk
---

## Definition

Let $L$ be a [[random variable|0PNRKMRC55]], the loss of a portfolio over a fixed horizon, with [[distribution function|0H8H7ZTHW2]] $F_L$.
Let $\alpha \in (0, 1)$ be the confidence level.
The *value at risk* of $L$ at level $\alpha$ is
$$\mathrm{VaR}_\alpha(L) = \inf\set{ \ell \in \R : P(L > \ell) \le 1 - \alpha } = \inf\set{ \ell \in \R : F_L(\ell) \ge \alpha }.$$

## Remarks

So $\mathrm{VaR}_\alpha(L) = F_L^{-1}(\alpha)$ is the lower $\alpha$-[[quantile|0X60VE98HN]] of $L$.
Example: if $L$ has the [[normal distribution|05AQE0QR0D]] with mean $\mu$ and standard deviation $s$, then $\mathrm{VaR}_\alpha(L) = \mu + s \Phi^{-1}(\alpha)$, where $\Phi$ is the standard normal distribution function; for $\alpha = 0.99$ this is about $\mu + 2.33 s$.
Non-example of subadditivity: let $L_1, L_2$ be independent, each equal to $100$ with probability $0.04$ and to $0$ otherwise.
Then $\mathrm{VaR}_{0.95}(L_i) = 0$, but $P(L_1 + L_2 > 0) = 1 - 0.96^2 = 0.0784 > 0.05$, so $\mathrm{VaR}_{0.95}(L_1 + L_2) = 100 > 0 + 0$.
Some texts work with the profit $X = -L$ and define $\mathrm{VaR}_\alpha(X) = \mathrm{VaR}_\alpha(-X)$ with the same meaning.
