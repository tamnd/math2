---
tag: NG2QE06MP1
kind: definition
name: Survival function
msc: [62N05, 62N01, "60E05"]
defines: QTM1HZM53Q
uses: [0PNRKMRC55, 0H8H7ZTHW2, 0E99F51GVB]
sources:
  - url: https://en.wikipedia.org/wiki/Survival_function
---

## Definition

Let $T$ be a [[random variable|0PNRKMRC55]] with values in $[0, \infty)$, and let $F$ be its [[cumulative distribution function|0H8H7ZTHW2]].
The *survival function* of $T$ is the function $S \colon [0, \infty) \to [0, 1]$ given by
$$S(t) = P(T > t) = 1 - F(t).$$

## Remarks

The function $S$ is nonincreasing and right-continuous, and $S(t) \to 0$ as $t \to \infty$.
If $T$ has a density $f$, then $S(t) = \int_t^\infty f(u) \, du$ and $f = -S'$ wherever $f$ is continuous.
The mean of $T$ is $E[T] = \int_0^\infty S(t) \, dt$.
Some authors use $P(T \ge t)$ instead; the two agree at every $t$ with $P(T = t) = 0$.

Example: if $T$ has the [[exponential distribution|0E99F51GVB]] with rate $\lambda > 0$, then $S(t) = e^{-\lambda t}$.
Indeed $P(T > t) = \int_t^\infty \lambda e^{-\lambda u} \, du = e^{-\lambda t}$, and $\int_0^\infty e^{-\lambda t} \, dt = 1/\lambda$ is the mean.

Non-example: the function $G(t) = e^{-t} \cos^2 t$ takes values in $[0, 1]$, has $G(0) = 1$ and tends to $0$, but it is not a survival function.
It satisfies $G(\pi/2) = 0 < e^{-\pi} = G(\pi)$, so it is not nonincreasing, while $P(T > t)$ can only decrease as $t$ grows.
