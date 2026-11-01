---
tag: R5JTGHBMGE
kind: definition
name: Stochastic ordering
msc: ["60E15"]
defines: HJPPRZ29YE
uses: [0PNRKMRC55, 0H8H7ZTHW2, HTR7J0W66V, 0WQNRCNY3M, 0X60VE98HN]
sources:
  - url: https://en.wikipedia.org/wiki/Stochastic_ordering
---

## Definition

Let $X$ and $Y$ be real [[random variables|0PNRKMRC55]], not necessarily on the same probability space.
$X$ is *smaller than $Y$ in the usual stochastic order*, written $X \le_{\mathrm{st}} Y$, if
$$P(X > t) \le P(Y > t) \qquad \text{for all } t \in \R.$$

## Remarks

In terms of [[distribution functions|0H8H7ZTHW2]], $X \le_{\mathrm{st}} Y$ means $F_X(t) \ge F_Y(t)$ for all $t$.
It is equivalent to $E[u(X)] \le E[u(Y)]$ for every nondecreasing function $u \colon \R \to \R$ for which both [[expectations|0WQNRCNY3M]] exist.
It is also equivalent to the existence of a [[coupling|HTR7J0W66V]] $(X', Y')$ with $X'$ distributed as $X$, $Y'$ distributed as $Y$ and $X' \le Y'$ almost surely.
One can take $X' = F_X^{-1}(U)$ and $Y' = F_Y^{-1}(U)$ for $U$ uniform on $(0, 1)$, where $F^{-1}$ is the [[quantile function|0X60VE98HN]].
The relation depends only on the laws, and it is a partial order on the probability measures on $\R$.
If $X \le_{\mathrm{st}} Y$ and $E[X] = E[Y]$ is finite, then $X$ and $Y$ have the same law.
Example: if $X$ is exponential with rate $\lambda$ and $Y$ is exponential with rate $\lambda' \le \lambda$, then $P(X > t) = e^{-\lambda t} \le e^{-\lambda' t} = P(Y > t)$ for $t \ge 0$, and both sides are $1$ for $t < 0$; so $X \le_{\mathrm{st}} Y$.
Non-example: if $X$ is normal with mean $0$ and variance $1$ and $Y$ is normal with mean $0$ and variance $4$, then $P(X > 1) < P(Y > 1)$ but $P(X > -1) > P(Y > -1)$, so neither $X \le_{\mathrm{st}} Y$ nor $Y \le_{\mathrm{st}} X$.
The name stochastic ordering also covers other orders, such as the convex order ($E[u(X)] \le E[u(Y)]$ for convex $u$) and the hazard rate and likelihood ratio orders.
