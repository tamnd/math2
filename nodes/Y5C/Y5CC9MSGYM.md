---
tag: Y5CC9MSGYM
kind: definition
name: Function of exponential order
msc: [44A10]
defines: TKZAV3KR86
uses: [0XHDTE5YMZ, 0RMVS7RXZX]
sources:
  - url: https://en.wikipedia.org/wiki/Laplace_transform
---

## Definition

Let $f \colon [0, \infty) \to \C$ be a [[function|0XHDTE5YMZ]] and let $a \in \R$.
The function $f$ is *of exponential order $a$* if there are constants $M > 0$ and $T \ge 0$ such that
$$\abs{f(t)} \le M e^{at} \quad \text{for all } t \ge T,$$
where $e^{at}$ is the [[exponential function|0RMVS7RXZX]].
The function $f$ is *of exponential order* if it is of exponential order $a$ for some real $a$.

## Remarks

Example: $f(t) = t^n$ with $n \in \N$ is of exponential order $1$, since $e^t \ge t^n / n!$ for $t \ge 0$ by the power series of $e^t$; so $\abs{f(t)} \le n!\, e^t$ with $T = 0$.
In fact $t^n$ is of exponential order $a$ for every $a > 0$.
Non-example: $f(t) = e^{t^2}$ is not of exponential order, since $e^{t^2}/e^{at} = e^{t(t - a)} \to \infty$ for every real $a$.
A bounded function, such as $\sin t$, is of exponential order $0$.
Some books require the bound for all $t \ge 0$ ($T = 0$); for functions that are bounded on bounded intervals the two versions agree, after enlarging $M$.
