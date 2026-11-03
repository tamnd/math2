---
tag: KVPKPG0S08
kind: definition
name: Zero-order hold
msc: [93C57, 93C62]
defines: PQ5FJ334WR
uses: [0AJXYH4DDQ, 0V49JEZW06, 86JKV3TRFD]
sources:
  - url: https://en.wikipedia.org/wiki/Zero-order_hold
---

## Definition

Let $T > 0$ be a sampling period and let $(u_k)_{k \ge 0}$ be a sequence of real numbers.
The *zero-order hold* of $(u_k)$ with period $T$ is the function $u \colon [0, \infty) \to \R$ given by
$$u(t) = u_k \quad \text{for } kT \le t < (k + 1)T, \quad k = 0, 1, 2, \ldots.$$
The same definition applies to sequences of vectors in $\R^m$.

## Remarks

The output is a [[step function|0AJXYH4DDQ]] on each bounded interval, continuous from the right, with jumps only at the sampling instants $kT$.
Represent the sequence by the impulse train $\sum_k u_k\, \delta(t - kT)$.
Then the hold is the linear time-invariant system with impulse response equal to $1$ on $[0, T)$ and $0$ elsewhere.
Its [[transfer function|86JKV3TRFD]], the [[Laplace transform|0V49JEZW06]] of this impulse response, is
$$H(s) = \frac{1 - e^{-sT}}{s}.$$

Example: with $T = 1$ and $u_0 = 3$, $u_1 = 1$, $u_2 = 2$, the held signal is $u(t) = 3$ on $[0, 1)$, $1$ on $[1, 2)$ and $2$ on $[2, 3)$.

Non-example: the first-order hold, which joins the points $(kT, u_k)$ by straight line segments, is not a zero-order hold, since it is not constant on the intervals $[kT, (k+1)T)$.
