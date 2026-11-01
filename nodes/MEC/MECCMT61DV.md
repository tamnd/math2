---
tag: MECCMT61DV
kind: definition
name: Markov chain Monte Carlo
msc: [65C05, 60J22, 65C40]
defines: ZGNBR2SPZ0
uses: [033TJBZDG0, 0F462493EA, 0KRH5157WP, CTGN6CK1ZS, MKHF449E22, B1E1ES1BYD, 04VZE3FZXF]
sources:
  - url: https://en.wikipedia.org/wiki/Markov_chain_Monte_Carlo
---

## Definition

Let $S$ be a countable set, let $\pi$ be a probability distribution on $S$, and let $f \colon S \to \R$ be bounded.
A *Markov chain Monte Carlo method* for estimating $\pi(f) = \sum_{x \in S} f(x) \pi(x)$ consists of:

1. a [[transition matrix|0F462493EA]] $P$ on $S$ such that $\pi$ is a [[stationary distribution|0KRH5157WP]] of $P$ and the chain with transition matrix $P$ is irreducible;
2. a [[Markov chain|033TJBZDG0]] $(X_k)_{k \ge 0}$ with transition matrix $P$, simulated from some starting state;
3. the estimator $\hat{\pi}_n(f) = \frac{1}{n} \sum_{k=1}^{n} f(X_k)$, computed for a large $n$.

## Remarks

By the ergodic theorem for irreducible chains with a stationary distribution, $\hat{\pi}_n(f) \to \pi(f)$ almost surely as $n \to \infty$, for every starting state.
The usual way to obtain clause 1 is to impose [[detailed balance|CTGN6CK1ZS]] for $\pi$, as the [[Metropolis–Hastings algorithm|MKHF449E22]] does.
In practice the first steps, the burn-in, are often discarded, and if the chain is also aperiodic then the law of $X_k$ tends to $\pi$ by the [[convergence theorem|B1E1ES1BYD]].
Example: on $S = \Z$ with $\pi(x) \propto e^{-x^2}$, propose $x \pm 1$ with probability $1/2$ each and accept with probability $\min(1, \pi(y)/\pi(x))$.
This chain is irreducible and satisfies detailed balance for $\pi$.
Non-example: the simple [[random walk|04VZE3FZXF]] on the path $\set{1, \ldots, m}$, which moves to a uniform neighbour, has stationary law proportional to the degrees.
So its averages estimate expectations under that law, not under the uniform law, and it fails clause 1 for uniform $\pi$ when $m \ge 3$.
