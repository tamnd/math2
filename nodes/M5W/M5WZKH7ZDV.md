---
tag: M5WZKH7ZDV
kind: example
name: Ideal chain
msc: [82D60, 60G50]
instance_of: [04VZE3FZXF]
uses: [04VZE3FZXF, 0EPZC4Z1FC, 05AQE0QR0D]
sources:
  - url: https://en.wikipedia.org/wiki/Ideal_chain
same_as:
  wikidata: Q1453564
  wikipedia: Ideal chain
---

## Example

An *ideal chain*, or freely jointed chain, models a polymer of $N$ segments of fixed length $b > 0$ whose directions are independent.
Let $u_1, \dots, u_N$ be independent random unit vectors in $\R^3$, each uniformly distributed on the unit sphere.
The end-to-end vector is $R = b \sum_{i=1}^N u_i$, so the chain is a [[random walk|04VZE3FZXF]] in $\R^3$ with steps of length $b$.
Check of the mean square size: $\mathbb{E}[u_i] = 0$ and $\mathbb{E}[u_i \cdot u_j] = 0$ for $i \ne j$ by independence, while $u_i \cdot u_i = 1$.
So $\mathbb{E}[R] = 0$ and
$$\mathbb{E}\big[\abs{R}^2\big] = b^2 \sum_{i, j} \mathbb{E}[u_i \cdot u_j] = N b^2.$$
The typical size $\sqrt{N} b$ is much smaller than the contour length $N b$.

## Remarks

Each coordinate of $u_i$ has mean $0$ and variance $1/3$.
By the [[central limit theorem|0EPZC4Z1FC]], for large $N$ the vector $R$ is close to a [[normal distribution|05AQE0QR0D]] with density
$$P(R) = \Big( \frac{3}{2 \pi N b^2} \Big)^{3/2} \exp\Big( -\frac{3 \abs{R}^2}{2 N b^2} \Big).$$
At temperature $T$ the entropy $k_B \ln P(R)$ gives the free energy $F(R) = \frac{3 k_B T}{2 N b^2} \abs{R}^2$ up to a constant.
So an ideal chain behaves as a spring of stiffness $3 k_B T / (N b^2)$, of purely entropic origin.
The model ignores the fact that two segments cannot overlap; a real chain in a good solvent is better described by a [[self-avoiding walk|E2BVEB570S]].

## Explanations

### L1 human

Think of a polymer as a chain of short rigid sticks joined by perfectly loose hinges.
Each stick points in a random direction, independently of the others, so the chain is a random walk in space.
After $N$ sticks the two ends are typically about $\sqrt{N}$ stick lengths apart, not $N$.
For a chain of $10000$ sticks, the ends are typically only about $100$ stick lengths apart.
Pulling the ends apart reduces the number of possible shapes, and this is why rubber pulls back when stretched.
