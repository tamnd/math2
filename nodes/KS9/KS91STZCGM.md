---
tag: KS91STZCGM
kind: statement
role: proposition
name: Gibbs sampling
msc: [65C05, 65C40, 60J22]
uses: [ZGNBR2SPZ0, 0ZN9EZTEM6, 0F462493EA, 0KRH5157WP, CTGN6CK1ZS, B1E1ES1BYD]
about: [ZGNBR2SPZ0]
sources:
  - url: https://en.wikipedia.org/wiki/Gibbs_sampling
same_as:
  wikidata: Q1191905
  wikipedia: Gibbs sampling
---

## Statement

Let $S = S_1 \times \cdots \times S_d$ be a product of countable sets, and let $\pi$ be a probability distribution on $S$.
For $x \in S$ and $1 \le i \le d$, write $x_{-i}$ for $x$ with its $i$-th coordinate removed, and let $Z_i(x) = \sum_{z \in S, \, z_{-i} = x_{-i}} \pi(z)$.
Let $K_i$ be the [[transition matrix|0F462493EA]] on $S$ with
$$K_i(x,y) = \frac{\pi(y)}{Z_i(x)} \quad \text{if } y_{-i} = x_{-i} \text{ and } Z_i(x) > 0,$$
$K_i(x,y) = 0$ for the other $y$ when $Z_i(x) > 0$, and $K_i(x, \cdot) = \delta_x$ when $Z_i(x) = 0$.
So $K_i$ redraws the $i$-th coordinate from its [[conditional distribution|0ZN9EZTEM6]] under $\pi$ given the others.
Then:

1. each $K_i$ satisfies [[detailed balance|CTGN6CK1ZS]] with respect to $\pi$, that is, $\pi(x) K_i(x,y) = \pi(y) K_i(y,x)$ for all $x, y \in S$;
2. $\pi$ is a [[stationary distribution|0KRH5157WP]] of the systematic-scan Gibbs sampler $K_1 K_2 \cdots K_d$ and of the random-scan Gibbs sampler $\frac{1}{d} \sum_{i=1}^{d} K_i$.

## Remarks

For clause 1, if $y_{-i} = x_{-i}$ and $Z_i(x) > 0$, then $Z_i(y) = Z_i(x)$ and both sides equal $\pi(x) \pi(y) / Z_i(x)$.
If $Z_i(x) = 0$ then $\pi(x) = \pi(y) = 0$ for all such $y$, and in all other cases both sides are $0$.
Summing detailed balance over $x$ gives $\pi K_i = \pi$, and clause 2 follows because a product or an average of kernels that fix $\pi$ also fixes $\pi$.
The same argument works for densities on $\R^d$, with sums replaced by integrals.
Stationarity alone does not give convergence of the chain to $\pi$.
If $S$ is finite and $\pi(x) > 0$ for every $x$, every entry of $K_1 \cdots K_d$ is positive, so the chain is irreducible and aperiodic and converges to $\pi$ by the [[convergence theorem|B1E1ES1BYD]].
Without positivity this can fail: for $\pi$ uniform on $\set{(0,0), (1,1)} \subset \set{0,1}^2$, each $K_i$ fixes every state of positive mass, so the chain never moves.

## Explanations

### L1 human

Gibbs sampling draws random samples from a joint distribution of many variables when sampling them all at once is hard.
It updates one variable at a time, drawing it from its distribution given the current values of all the others.
Repeating these simple updates builds a random walk through the space.
The result says that this walk leaves the target distribution unchanged.
So, when the walk mixes well, the visited states are samples from the target.

### L2 human

Gibbs sampling is the [[Markov chain Monte Carlo|ZGNBR2SPZ0]] method of choice when the full conditional distributions are easy to sample.
This is the case in many Bayesian hierarchical models with conjugate priors and in lattice models such as the Ising model.
Each update is a Metropolis–Hastings step whose proposal is the full conditional, so its acceptance probability is always $1$.
The systematic-scan sampler is in general not reversible, though each $K_i$ is; the random-scan sampler is reversible.
Strong dependence between coordinates slows mixing, since moves along single coordinates then make little progress; blocking several coordinates together is the usual remedy.
