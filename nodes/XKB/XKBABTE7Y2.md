---
tag: XKBABTE7Y2
kind: definition
name: Exchangeable random variables
msc: [60G09]
defines: 4MR4YJS1ZD
uses: [0PNRKMRC55, 0DR81R1F2B, 05RWFKVTJ7, 00MRN0FARV]
sources:
  - url: https://en.wikipedia.org/wiki/Exchangeable_random_variables
---

## Definition

Let $(\Omega, \mathcal{F}, P)$ be a probability space and let $(S, \mathcal{S})$ be a measurable space.
Let $X_1, \dots, X_n$ be [[random variables|0PNRKMRC55]] on $\Omega$ with values in $S$.
The finite sequence $(X_1, \dots, X_n)$ is *exchangeable* if for every [[permutation|05RWFKVTJ7]] $\sigma$ of $\set{1, \dots, n}$ the random vector $(X_{\sigma(1)}, \dots, X_{\sigma(n)})$ has the same [[joint distribution|0DR81R1F2B]] as $(X_1, \dots, X_n)$.
An infinite sequence $X_1, X_2, \dots$ is *exchangeable* if $(X_1, \dots, X_n)$ is exchangeable for every $n \ge 1$.

## Remarks

Equivalently, an infinite sequence is exchangeable if its joint law on $S^{\N}$ is invariant under every permutation of $\N$ that moves only finitely many indices.
Example: if $X_1, X_2, \dots$ are [[i.i.d.|00MRN0FARV]], the joint law of $(X_1, \dots, X_n)$ is the product $\mu^{\otimes n}$ of the common law $\mu$, and a product of equal factors does not change when the factors are permuted.
Another example: in the [[Pólya urn model|DHPXDFEEMF]], the sequence of colours drawn is exchangeable but not independent.
Non-example: let $Y$ be a [[Bernoulli|0386Y0Z7Y7]] variable with parameter $\frac{1}{2}$, and let $X_1 = Y$ and $X_2 = 2Y$.
Then $P((X_1, X_2) = (1, 2)) = \frac{1}{2}$ but $P((X_2, X_1) = (1, 2)) = 0$, so the transposition of $1$ and $2$ changes the law.
Each $X_i$ of an exchangeable sequence has the same law, and each pair $(X_i, X_j)$ with $i \ne j$ has the same joint law.
