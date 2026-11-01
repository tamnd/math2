---
tag: GTFRPF5J2K
kind: example
name: M/M/1 queue
msc: [60K25, 60J27, 90B22]
instance_of: [E8DAD7052E]
sources:
  - url: https://en.wikipedia.org/wiki/M/M/1_queue
same_as:
  wikidata: Q2736426
  wikipedia: M/M/1 queue
---

## Example

Let $\lambda > 0$ and $\mu > 0$.
In the M/M/1 queue of [[queueing theory|P64V0HTE78]], customers arrive as a Poisson process of rate $\lambda$ and there is one server.
Service times are independent [[exponential|0E99F51GVB]] random variables of rate $\mu$.
The number $Q(t)$ of customers in the system is a [[birth–death process|E8DAD7052E]] on $\set{0, 1, 2, \ldots}$.
Its birth rates are $\lambda_n = \lambda$ for $n \ge 0$ and its death rates are $\mu_n = \mu$ for $n \ge 1$.
This holds because the exponential law has no memory.
At each moment, the time to the next arrival and the remaining service time are again exponential, of rates $\lambda$ and $\mu$.

Let $\rho = \lambda / \mu$.
The balance equations $\pi_n \lambda = \pi_{n+1} \mu$ give $\pi_n = \rho^n \pi_0$.
So a [[stationary distribution|02KYGSCTCN]] exists if and only if $\rho < 1$, and then
$$\pi_n = (1 - \rho) \rho^n, \qquad n \ge 0,$$
a geometric law.
The mean number in the system is $L = \sum_n n \pi_n = \rho / (1 - \rho)$.
By [[Little's law|JN2YME6F4A]], the mean time in the system is $W = L / \lambda = 1/(\mu - \lambda)$.
If $\rho \ge 1$ the queue has no stationary distribution: it is null recurrent for $\rho = 1$ and transient for $\rho > 1$.

## Explanations

### L1 human

One clerk serves customers who arrive at random, at $\lambda$ per hour on average, and serves $\mu$ per hour on average when busy.
If $\lambda = 3$ and $\mu = 4$, the clerk is busy three quarters of the time, there are $3$ customers in the system on average, and each spends $1$ hour there on average.
As $\lambda$ comes close to $\mu$, the average line grows without bound.
