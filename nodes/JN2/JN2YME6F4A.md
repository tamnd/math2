---
tag: JN2YME6F4A
kind: statement
role: theorem
name: Little's law
msc: [60K25, 90B22]
uses: [P64V0HTE78, GTFRPF5J2K]
about: [P64V0HTE78]
sources:
  - url: https://en.wikipedia.org/wiki/Little's_law
same_as:
  wikidata: Q617388
  wikipedia: Little's law
---

## Statement

Consider a system, empty at time $0$, that customers enter at times $0 \le a_1 \le a_2 \le \cdots$ and leave at times $d_k \ge a_k$, with $a_k \to \infty$.
Let $W_k = d_k - a_k$ be the time customer $k$ spends in the system, let $A(t) = \#\set{k : a_k \le t}$, and let $L(t) = \#\set{k : a_k \le t < d_k}$ be the number in the system at time $t$.
Assume that the limits
$$\lambda = \lim_{t \to \infty} \frac{A(t)}{t} \quad \text{and} \quad W = \lim_{n \to \infty} \frac1n \sum_{k=1}^n W_k$$
exist and are finite.
Then the limit $L = \lim_{t \to \infty} \frac1t \int_0^t L(s)\, ds$ exists and
$$L = \lambda W.$$

## Remarks

The proof compares two ways of computing the total time spent in the system up to time $t$.
The integral $\int_0^t L(s)\, ds$ lies between the sum of the $W_k$ over customers who have left by time $t$ and the sum over customers who have arrived by time $t$.
Dividing by $t$, both bounds tend to $\lambda W$; the upper bound needs the fact that $W_n / a_n \to 0$, which follows from the two hypotheses.
Example: in the stable [[M/M/1 queue|GTFRPF5J2K]] with $\lambda = 3$ and $\mu = 4$, the mean number in the system is $L = 3$, so the mean time in the system is $W = L / \lambda = 1$.
The law needs no assumption on the arrival law, the service law, the number of servers or the order of service.

## Explanations

### L1 human

Average number of customers inside equals arrival rate times average time each one stays.
If $10$ people per minute enter a museum and each stays $30$ minutes, there are about $300$ people inside.
It is a piece of accounting, so it holds for almost any system with a stable long-run behaviour.

### L2 human

In [[queueing theory|P64V0HTE78]] one usually computes one of $L$ and $W$ from a model and gets the other one free.
For the M/M/1 queue, the stationary law gives $L = \rho/(1 - \rho)$, and Little's law gives $W = 1/(\mu - \lambda)$.
Applied to the waiting room alone, it links the mean queue length and the mean waiting time before service.
In the stochastic setting it holds for stationary systems with expectations in place of time averages.
