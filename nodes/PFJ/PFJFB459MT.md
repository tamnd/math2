---
tag: PFJFB459MT
kind: definition
name: Horvitz–Thompson estimator
msc: [62D05]
defines: QED889GZDE
uses: [0TTNRP5PFQ, 0DCT0QZVQ1, Y0PTCJBPEA]
sources:
  - url: https://en.wikipedia.org/wiki/Horvitz–Thompson_estimator
---

## Definition

Let $U = \set{1, \dots, N}$ be a finite population, and let $y_1, \dots, y_N$ be fixed real values attached to the units.
Let $S \subseteq U$ be a random sample drawn by a sampling design, and let $\pi_i = P(i \in S)$ be the inclusion probability of unit $i$.
Assume $\pi_i > 0$ for every $i \in U$.
The *Horvitz–Thompson estimator* of the population total $Y = \sum_{i=1}^N y_i$ is the [[estimator|0TTNRP5PFQ]]
$$\hat{Y}_{HT} = \sum_{i \in S} \frac{y_i}{\pi_i}.$$
The Horvitz–Thompson estimator of the population mean $Y/N$ is $\hat{Y}_{HT}/N$.

## Remarks

The estimator is unbiased: write $\hat{Y}_{HT} = \sum_{i=1}^N \frac{y_i}{\pi_i} \mathbf{1}[i \in S]$, and take the [[expected value|0DCT0QZVQ1]], using $E(\mathbf{1}[i \in S]) = \pi_i$, to get $E(\hat{Y}_{HT}) = Y$.

Example: in a [[simple random sample|Y0PTCJBPEA]] of size $n$ drawn without replacement, every unit has $\pi_i = n/N$.
Then $\hat{Y}_{HT} = \frac{N}{n}\sum_{i \in S} y_i = N \bar{y}$, where $\bar{y}$ is the sample mean.

Non-example: let some unit $j$ have $\pi_j = 0$.
Then it never appears in the sample, so no estimator built from the sample can be unbiased for every choice of $y_j$.
The condition $\pi_i > 0$ fails, and the definition does not apply.

With the joint inclusion probabilities $\pi_{ij} = P(i \in S, j \in S)$ and $\pi_{ii} = \pi_i$, the variance is
$$\operatorname{Var}(\hat{Y}_{HT}) = \sum_{i=1}^N \sum_{j=1}^N (\pi_{ij} - \pi_i \pi_j) \frac{y_i}{\pi_i} \frac{y_j}{\pi_j}.$$
