---
tag: 6TP0G4DKW2
kind: definition
name: Variogram
msc: [62M30, 62M40, 62H11]
defines: ZF8AA2JVKV
uses: [0QH5ENKZM1, 0477R9PYAE, 0WQNRCNY3M, 0KBFAWYRTE, 22735FGJV6]
sources:
  - url: https://en.wikipedia.org/wiki/Variogram
---

## Definition

Let $D = \R^d$ and let $(Z(s))_{s \in D}$ be a real random field with $E[Z(s)^2] < \infty$ for all $s$.
The field is *intrinsically stationary* if for every $h \in \R^d$:

1. $E[Z(s + h) - Z(s)] = 0$ for all $s$, and
2. $\operatorname{Var}(Z(s + h) - Z(s))$ does not depend on $s$.

For such a field the *variogram* is the function $2\gamma \colon \R^d \to [0, \infty)$ given by
$$2\gamma(h) = \operatorname{Var}(Z(s + h) - Z(s)) = E[(Z(s + h) - Z(s))^2],$$
and $\gamma$ is the *semivariogram*.

## Remarks

Every variogram satisfies $\gamma(0) = 0$ and $\gamma(-h) = \gamma(h)$.
It is conditionally negative definite: $\sum_{i,j} a_i a_j \gamma(s_i - s_j) \le 0$ whenever $\sum_i a_i = 0$.
If $Z$ is weakly stationary with [[covariance|0KBFAWYRTE]] function $C(h) = \operatorname{Cov}(Z(s + h), Z(s))$, then $\gamma(h) = C(0) - C(h)$.

Example: the standard [[Wiener process|22735FGJV6]] $(B(t))_{t \in \R}$, two-sided with $B(0) = 0$, has $B(t + h) - B(t)$ normal with mean $0$ and variance $\abs{h}$.
So it is intrinsically stationary with $2\gamma(h) = \abs{h}$, although its variance $\abs{t}$ is not constant in $t$.

Non-example: let $X$ be a standard normal random variable and $Z(s) = s^2 X$ on $\R$.
The increment $Z(s + h) - Z(s) = (2sh + h^2) X$ has mean $0$, but its variance $(2sh + h^2)^2$ depends on $s$, so clause 2 fails.
