---
tag: 4XPHS45KSP
kind: statement
role: theorem
name: Heavy traffic approximation
msc: [60K25, 90B22, 60F17]
uses: [P64V0HTE78, GJT4VQ46KH, 0477R9PYAE, 0WQNRCNY3M, 0E99F51GVB]
about: [P64V0HTE78]
sources:
  - url: https://en.wikipedia.org/wiki/Heavy_traffic_approximation
same_as:
  wikidata: Q17022030
  wikipedia: Heavy traffic approximation
---

## Statement

For each $k = 1, 2, \ldots$, consider a G/G/1 queue with first-come first-served discipline.
Its interarrival times are independent copies of a random variable $T^{(k)}$.
Its service times are independent copies of a random variable $S^{(k)}$, independent of the interarrival times.
Let $\sigma_{a,k}^2$ and $\sigma_{s,k}^2$ be the [[variances|0477R9PYAE]] of $T^{(k)}$ and $S^{(k)}$, and let $\delta_k = \mathbb{E}[T^{(k)}] - \mathbb{E}[S^{(k)}]$.
Assume:

1. $\delta_k > 0$ for every $k$, and $\delta_k \to 0$.
2. $\sigma_{a,k}^2 \to \sigma_a^2$ and $\sigma_{s,k}^2 \to \sigma_s^2$, with $\sigma_a^2 + \sigma_s^2 > 0$.
3. The families $\set{(T^{(k)})^2}$ and $\set{(S^{(k)})^2}$ are uniformly integrable.

Let $W^{(k)}$ have the stationary law of the waiting time before service in the $k$-th queue.
Then, as $k \to \infty$,
$$\frac{2 \delta_k}{\sigma_a^2 + \sigma_s^2} \, W^{(k)}$$
converges in distribution to an [[exponential|0E99F51GVB]] random variable of mean $1$.

## Remarks

This is Kingman's heavy traffic theorem.
By the [[Lindley equation|GJT4VQ46KH]], $W^{(k)}$ has the law of the supremum of a random walk with increments $S^{(k)} - T^{(k)}$, whose drift $-\delta_k$ tends to $0$.
Rescaled, this random walk is close to a Brownian motion with drift $-\delta_k$ and variance $\sigma_a^2 + \sigma_s^2$ per unit time.
The supremum of a Brownian motion with drift $-\delta < 0$ and variance $\sigma^2$ is exponential with mean $\sigma^2 / (2\delta)$.
For example, take an M/M/1 queue with arrival rate $\lambda < 1$ and service rate $\mu = 1$.
The theorem predicts that $W$ is roughly exponential with mean $(1/\lambda^2 + 1) / (2(1/\lambda - 1))$.
This mean grows like $1/(1 - \lambda)$ as $\lambda \to 1$.
The exact stationary wait is $0$ with probability $1 - \lambda$ and otherwise exponential with mean $1/(1 - \lambda)$, which agrees in the limit.
Without the condition $\delta_k > 0$, the queue is not stable and has no stationary waiting time.
The same scaling at the level of processes gives diffusion approximations: the rescaled queue length process converges to a reflected Brownian motion.

## Explanations

### L1 human

When a server is almost always busy, waiting times become very long and hard to compute exactly.
The heavy traffic approximation says that in this regime the waiting time is approximately exponential.
Its mean depends only on the gap between arrival and service rates and on the variability of the two streams.
All other details of the distributions wash out.

### L2 human

Heavy traffic limits are the queueing analogue of the [[central limit theorem|0EPZC4Z1FC]]: only means and variances survive the scaling.
They justify [[Kingman's formula|8WT39NFCTP]] for the mean wait in a G/G/1 queue.
Their process-level versions, based on functional limit theorems such as [[Donsker's theorem|818832PMSV]], replace queueing networks by reflected Brownian motions, which are often easier to analyse and to optimise.
