---
tag: ZMCBQ0M082
kind: definition
name: Hilbert–Schmidt integral operator
msc: [47G10, 47B10, 45P05]
defines: CB5G212Q03
uses: [P15VQS5DJ9, SASP14MA1Z, WWMWX7AD4V]
sources:
  - url: https://en.wikipedia.org/wiki/Hilbert%E2%80%93Schmidt_integral_operator
---

## Definition

Let $(X, \mu)$ be a $\sigma$-finite [[measure space|P15VQS5DJ9]], and let $L^2(X)$ be the [[$L^2$ space|SASP14MA1Z]] of $\mu$.
Let $K \colon X \times X \to \C$ be a measurable function with
$$\int_X \int_X \abs{K(x, y)}^2 \, d\mu(x) \, d\mu(y) < \infty.$$
The *Hilbert–Schmidt integral operator* with kernel $K$ is the operator $T_K \colon L^2(X) \to L^2(X)$ given by
$$(T_K f)(x) = \int_X K(x, y) \, f(y) \, d\mu(y).$$

## Remarks

The operator is well defined: for almost every $x$, $K(x, \cdot) \in L^2(X)$, and the Cauchy–Schwarz inequality gives $\norm{T_K f} \le \norm{K}_{L^2(X \times X)} \norm{f}$.
Its Hilbert–Schmidt norm $\left(\sum_n \norm{T_K e_n}^2\right)^{1/2}$, for any orthonormal basis $(e_n)$, equals $\norm{K}_{L^2(X \times X)}$.

Example: on $X = [0, 1]$ with Lebesgue measure, $K(x, y) = \min(x, y)$ satisfies $\int_0^1 \int_0^1 \min(x, y)^2 \, dx \, dy = 1/6 < \infty$, so $T_K$ is a Hilbert–Schmidt integral operator.

Non-example: on $[0, 1]$, $K(x, y) = \abs{x - y}^{-1/2}$ fails the condition, since $\int_0^1 \int_0^1 \abs{x - y}^{-1} \, dx \, dy = \infty$.
Its operator is still bounded and compact on $L^2[0, 1]$, but it is not a Hilbert–Schmidt operator.

Kernels with the condition above are the [[square-integrable kernels|WWMWX7AD4V]].
