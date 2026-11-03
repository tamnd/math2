---
tag: T06A0Q0QNW
kind: definition
name: Watterson estimator
msc: [62P10, 92D10]
defines: XD14B1J3EQ
uses: [AVJWVXG5VZ, P2H42E2V2N, 0NANDX7V02, 0SSS6ERQ0S]
sources:
  - url: https://en.wikipedia.org/wiki/Watterson_estimator
---

## Definition

Let $n \ge 2$ DNA sequences be sampled from a population.
Let $S$ be the number of segregating sites among them, as in the [[infinite sites model|AVJWVXG5VZ]].
Let $a_n = \sum_{i=1}^{n-1} 1/i$ be the [[harmonic number|0NANDX7V02]] $H_{n-1}$.
The *Watterson estimator* of the scaled mutation rate $\theta$ is the [[estimator|0SSS6ERQ0S]]
$$\hat\theta_W = \frac{S}{a_n}.$$

## Remarks

Here $\theta = 4 N_e \mu$ for a diploid population of effective size $N_e$ with mutation rate $\mu$ per sequence per generation.
In the neutral model the genealogy is [[Kingman's coalescent|P2H42E2V2N]] in units of $2N_e$ generations.
Mutations fall on the tree at rate $\theta/2$ per unit length, and the expected total length is $2a_n$.
So $\operatorname{E}(S) = \theta a_n$, and $\hat\theta_W$ is unbiased.
Example: for $n = 4$ sequences with $S = 11$ segregating sites, $a_4 = 11/6$ and $\hat\theta_W = 6$.
Non-example: $S$ alone is not an unbiased estimator of $\theta$ for $n \ge 3$, since its mean is $\theta a_n \ne \theta$.
Since $a_n$ grows like $\log n$, larger samples improve the estimate only slowly.
