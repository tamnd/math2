---
tag: D4DJXF8Q6S
kind: example
name: Ehrenfest model
msc: [60J10, 82C03]
instance_of: [0G48PYM96Q]
uses: [0G48PYM96Q, 0KRH5157WP, CTGN6CK1ZS, 0WCWA1KT3M]
sources:
  - url: https://en.wikipedia.org/wiki/Ehrenfest_model
same_as:
  wikidata: Q3318105
  wikipedia: Ehrenfest model
---

## Example

Let $N \ge 1$ balls be distributed between two urns.
At each step one of the $N$ balls is chosen uniformly at random and moved to the other urn.
Let $X_n$ be the number of balls in the first urn after $n$ steps.
Then $(X_n)$ is a [[Markov chain|0G48PYM96Q]] on $\set{0, 1, \dots, N}$ with transition probabilities
$$P(k, k - 1) = \frac{k}{N}, \qquad P(k, k + 1) = \frac{N - k}{N}.$$
This is the *Ehrenfest model*, introduced by Paul and Tatiana Ehrenfest in 1907.

Check that the [[binomial distribution|0WCWA1KT3M]] $\pi(k) = \binom{N}{k} 2^{-N}$ is a [[stationary distribution|0KRH5157WP]].
It satisfies [[detailed balance|CTGN6CK1ZS]]: $\pi(k) P(k, k + 1) = \binom{N}{k} \frac{N - k}{N} 2^{-N} = \binom{N}{k + 1} \frac{k + 1}{N} 2^{-N} = \pi(k + 1) P(k + 1, k)$.
Summing detailed balance over $k$ gives $\sum_k \pi(k) P(k, j) = \pi(j)$ for every $j$.

## Remarks

The chain is irreducible with period $2$, since $X_n$ changes parity at each step.
The drift toward the middle is linear: $\mathbb{E}[X_{n+1} - \frac N2 \mid X_n] = (1 - \frac2N)(X_n - \frac N2)$, so the mean approaches $N/2$ exponentially fast.
By Kac's formula for an irreducible chain, the expected return time to a state $k$ is $1/\pi(k)$.
So the chain started with all balls in one urn returns there after $2^N$ steps on average.
For even $N$, it returns to the balanced state $N/2$ after about $\sqrt{\pi N / 2}$ steps on average.
For $N$ of the order of the number of molecules in a gas, $2^N$ is far beyond any physical time, which reconciles the observed irreversibility with recurrence.

## Explanations

### L1 human

Imagine two dogs and $N$ fleas; at each moment one flea, chosen at random, jumps from its dog to the other.
Most of the time each dog carries about half the fleas.
If all fleas start on one dog, they quickly spread out, and the chance that they all come back to the same dog is tiny.
The model shows how a system can drift to equilibrium and still, in principle, return to its starting state.
