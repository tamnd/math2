---
tag: JSYH3DHCN7
kind: definition
name: Muller's ratchet
msc: [92D15, 92D10]
defines: VY3VCNBBC4
uses: [SR4F169EKF, 0XB9GQTN9G, AFJ02FJ1KR]
sources:
  - url: https://en.wikipedia.org/wiki/Muller%27s_ratchet
---

## Definition

Let an asexual population of $N$ haploid individuals reproduce as in the [[Wright–Fisher model|SR4F169EKF]], with no recombination.
Each individual carries a number $k \ge 0$ of deleterious mutations and has fitness $(1 - s)^k$ for a fixed $s \in (0, 1)$.
At each birth the offspring receives a number of new mutations with the [[Poisson distribution|0XB9GQTN9G]] of mean $U > 0$.
Mutations are never lost by back mutation.
Let $k_{\min}(t)$ be the least number of mutations carried by an individual in generation $t$; the individuals with $k = k_{\min}(t)$ form the *least-loaded class*.

1. A *click* of the ratchet is a generation $t$ with $k_{\min}(t) > k_{\min}(t - 1)$, that is, a loss of the least-loaded class.
2. *Muller's ratchet* is the process $t \mapsto k_{\min}(t)$, which is nondecreasing and increases by clicks.

## Remarks

The process is nondecreasing because an offspring has at least as many mutations as its parent.
Example: in the infinite population limit the distribution of $k$ settles to the Poisson distribution with mean $U/s$.
So the least-loaded class has size about $N e^{-U/s}$.
When this number is small, [[genetic drift|AFJ02FJ1KR]] soon removes it and the ratchet clicks often.
Non-example: with back mutation or recombination, the least-loaded class can be rebuilt.
Then $k_{\min}$ can decrease, and the process of clause 2 is no longer irreversible.
