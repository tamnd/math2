---
tag: Q3VCF5R06B
kind: example
name: M/G/1 queue
msc: [60K25, 90B22]
illustrates: [N1DRDHVHN4]
uses: [2P6TYP0RBZ, 0G48PYM96Q, 0XB9GQTN9G, JN2YME6F4A]
sources:
  - url: https://en.wikipedia.org/wiki/M/G/1_queue
same_as:
  wikidata: Q3916814
  wikipedia: M/G/1 queue
---

## Example

In the M/G/1 queue, in [[Kendall's notation|9HTFATQNJ2]], customers arrive as a Poisson process of rate $\lambda > 0$.
One server serves them in order of arrival.
The service times $S_1, S_2, \dots$ are independent with a common general law of mean $\mathbb{E}[S] > 0$, and independent of the arrivals.
Let $\rho = \lambda \mathbb{E}[S]$.

The number of customers is not a Markov process in continuous time, because the remaining service time matters.
It becomes a [[Markov chain|0G48PYM96Q]] when observed just after departures.
Let $Q_n$ be the number left behind by the $n$-th departing customer.
Let $A_{n+1}$ be the number of arrivals during the service of customer $n + 1$.
Then
$$Q_{n+1} = \max(Q_n - 1, 0) + A_{n+1},$$
where the $A_n$ are independent with $P(A_n = k) = \mathbb{E}\big[e^{-\lambda S} (\lambda S)^k / k!\big]$, a mixed [[Poisson distribution|0XB9GQTN9G]], and mean $\mathbb{E}[A_n] = \rho$.
This chain is positive recurrent if and only if $\rho < 1$, and then the long-run fraction of time the server is busy is $\rho$.
If moreover $\mathbb{E}[S^2] < \infty$, the [[Pollaczek–Khinchine formula|N1DRDHVHN4]] gives the mean waiting time in the queue, $W_q = \lambda \mathbb{E}[S^2] / (2(1 - \rho))$.

For deterministic service $S = 1/\mu$ (the M/D/1 queue), $\mathbb{E}[S^2] = 1/\mu^2$ and $W_q = \rho / (2\mu(1 - \rho))$.
For exponential service of rate $\mu$ (the M/M/1 queue), $\mathbb{E}[S^2] = 2/\mu^2$ and $W_q = \rho / (\mu(1 - \rho))$, twice as much.
So at the same load, exponential service times double the mean wait compared with constant ones.

## Explanations

### L1 human

Customers arrive at random at a single counter, but the service times can follow any pattern, from always the same to wildly variable.
Looking at the queue just when a customer leaves gives a simple step-by-step rule for the queue length.
The mean wait depends not only on the average service time but also on its spread: more variable service means longer waits.
