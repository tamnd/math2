---
tag: GNSMVY7G0G
kind: definition
name: Expected shortfall
msc: [91G70, 62P05]
defines: KKVCHFGA14
uses: [C063APG9NT, 0WQNRCNY3M, 0PNRKMRC55, 05AQE0QR0D]
sources:
  - url: https://en.wikipedia.org/wiki/Expected_shortfall
---

## Definition

Let $L$ be an integrable [[random variable|0PNRKMRC55]], the loss of a portfolio, and let $\alpha \in (0, 1)$.
The *expected shortfall* of $L$ at level $\alpha$ is
$$\mathrm{ES}_\alpha(L) = \frac{1}{1 - \alpha} \int_\alpha^1 \mathrm{VaR}_u(L) \, du,$$
where $\mathrm{VaR}_u$ is the [[value at risk|C063APG9NT]] at level $u$.

## Remarks

If the distribution function of $L$ is continuous, then $\mathrm{ES}_\alpha(L) = E[L \mid L \ge \mathrm{VaR}_\alpha(L)]$, a conditional [[expected value|0WQNRCNY3M]].
Always $\mathrm{ES}_\alpha(L) \ge \mathrm{VaR}_\alpha(L)$, since $u \mapsto \mathrm{VaR}_u(L)$ is nondecreasing.
Example: if $L$ is standard [[normal|05AQE0QR0D]], then $\mathrm{ES}_\alpha(L) = \varphi(\Phi^{-1}(\alpha)) / (1 - \alpha)$, where $\varphi$ and $\Phi$ are its density and distribution function; for $\alpha = 0.99$ this is about $2.67$, against a VaR of about $2.33$.
Non-example: if $L$ is not integrable, for instance if $P(L > x) = 1/x$ for $x \ge 1$, then $\mathrm{ES}_\alpha(L) = \infty$ and the definition gives no finite value.
For discrete $L$ the formula $E[L \mid L \ge \mathrm{VaR}_\alpha(L)]$ can differ from $\mathrm{ES}_\alpha(L)$, and only the integral form is subadditive in general.
