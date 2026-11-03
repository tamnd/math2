---
tag: ZKRS2QEJFX
kind: definition
name: Lindley equation
msc: [60K25, 90B22]
defines: GJT4VQ46KH
uses: [P64V0HTE78, 04VZE3FZXF]
sources:
  - url: https://en.wikipedia.org/wiki/Lindley_equation
---

## Definition

Consider a single-server queue with first-come first-served discipline, with customers numbered $n = 0, 1, 2, \ldots$.
Let $S_n \ge 0$ be the service time of customer $n$, and let $W_n$ be its waiting time before service.
Let $T_{n+1} \ge 0$ be the time between the arrivals of customers $n$ and $n+1$.
The *Lindley equation* is the recursion
$$W_{n+1} = \max(0, \; W_n + S_n - T_{n+1}), \qquad n \ge 0.$$

## Remarks

With $W_0 = 0$, $S_0 = 2$, $T_1 = 1$, $S_1 = 1$ and $T_2 = 3$, the recursion gives $W_1 = \max(0, 0 + 2 - 1) = 1$ and $W_2 = \max(0, 1 + 1 - 3) = 0$.
This matches the queue: customer $1$ arrives at time $1$, while customer $0$ is served until time $2$.
Customer $2$ arrives at time $4$, after customer $1$ has left at time $3$.
The recursion without the maximum, $W_{n+1} = W_n + S_n - T_{n+1}$, is not a Lindley equation; it can give negative waiting times.
Write $U_n = S_n - T_{n+1}$.
If $W_0 = 0$, then $W_n = \max(0, U_{n-1}, U_{n-1} + U_{n-2}, \ldots, U_{n-1} + \cdots + U_0)$.
If the $U_n$ are independent and identically distributed, $W_n$ has the same law as the maximum of the first $n+1$ partial sums $0, U_0, U_0 + U_1, \ldots$ of a [[random walk|04VZE3FZXF]].
So when $\mathbb{E}[U_0] < 0$, the law of $W_n$ converges to the law of the supremum of this random walk.
