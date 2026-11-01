---
tag: FV0E9GEPCD
kind: definition
name: Birth–death process
msc: [60J27, 60J80, 60K25]
defines: E8DAD7052E
uses: [TWQFE0FZZS, 02KYGSCTCN]
sources:
  - url: https://en.wikipedia.org/wiki/Birth–death_process
---

## Definition

Let $S = \set{0, 1, 2, \ldots}$, and let $(\lambda_n)_{n \ge 0}$ and $(\mu_n)_{n \ge 1}$ be nonnegative real numbers, with $\mu_0 = 0$.
Let $(X_t)_{t \ge 0}$ be a [[continuous-time Markov chain|TWQFE0FZZS]] on $S$ with generator matrix $Q = (q_{mn})$.
It is a *birth–death process* with birth rates $\lambda_n$ and death rates $\mu_n$ if
$$q_{n, n+1} = \lambda_n, \qquad q_{n, n-1} = \mu_n \ (n \ge 1), \qquad q_{nn} = -(\lambda_n + \mu_n),$$
and $q_{mn} = 0$ when $\abs{m - n} \ge 2$.
A finite version uses $S = \set{0, 1, \ldots, N}$ with $\lambda_N = 0$.

## Remarks

In state $n$ the process waits an exponential time of rate $\lambda_n + \mu_n$, then jumps to $n + 1$ with probability $\lambda_n / (\lambda_n + \mu_n)$ and to $n - 1$ otherwise.
Example: the Poisson process of rate $\lambda$ is the pure birth process with $\lambda_n = \lambda$ and $\mu_n = 0$ for all $n$; each row of $Q$ sums to $0$, as required.
Non-example: a chain on $S$ with $q_{n, n+2} > 0$ for some $n$ is not a birth–death process, because it jumps by two.
Suppose all $\lambda_n > 0$ and all $\mu_n > 0$ for $n \ge 1$, and the chain does not explode.
Then a [[stationary distribution|02KYGSCTCN]] exists if and only if
$$\sum_{n \ge 0} \frac{\lambda_0 \lambda_1 \cdots \lambda_{n-1}}{\mu_1 \mu_2 \cdots \mu_n} < \infty,$$
and then $\pi_n$ is proportional to the $n$-th term of this sum.
It follows from the balance equations $\pi_n \lambda_n = \pi_{n+1} \mu_{n+1}$.
