---
tag: Y4S52CZ9YJ
kind: definition
name: Genetic drift
msc: [92D15, 92D10]
defines: AFJ02FJ1KR
uses: [CCN582E2C4, 0DKRR22AEQ, 0DCT0QZVQ1, 007QED3E0Y]
sources:
  - url: https://en.wikipedia.org/wiki/Genetic_drift
---

## Definition

Consider a population of finite size in which the allele frequency $p_t$ of an allele $A$ in generation $t$ is a [[random variable|0DKRR22AEQ]].
Assume that the gene copies of generation $t + 1$ are a random sample of offspring of the gene copies of generation $t$.
*Genetic drift* is the random part of the change $p_{t+1} - p_t$ that comes from this sampling.
In a model without selection, mutation or migration, $E[p_{t+1} \mid p_t] = p_t$, and all of the change is drift.

## Remarks

The size of drift is measured by the [[variance|007QED3E0Y]] $\operatorname{Var}(p_{t+1} \mid p_t)$.
Example: in the [[Wright–Fisher model|SR4F169EKF]] with $2N$ gene copies, $2N p_{t+1}$ is binomial with parameters $2N$ and $p_t$.
Hence the [[expected value|0DCT0QZVQ1]] is $E[p_{t+1} \mid p_t] = p_t$ and $\operatorname{Var}(p_{t+1} \mid p_t) = p_t (1 - p_t) / (2N)$.
For $N = 50$ and $p_t = 1/2$, the standard deviation of $p_{t+1}$ is $\sqrt{0.25/100} = 0.05$.

Non-example: in a deterministic model of selection, such as $p_{t+1} = p_t (1 + s) / (1 + s p_t)$ with $s > 0$, the change is not random, so there is no drift.

Drift lowers the expected heterozygosity $H_t = 2 p_t (1 - p_t)$.
In the Wright–Fisher model, $E[H_{t+1} \mid p_t] = (1 - 1/(2N)) H_t$.
So variation is lost at rate about $1/(2N)$ per generation, and eventually an allele is fixed.
