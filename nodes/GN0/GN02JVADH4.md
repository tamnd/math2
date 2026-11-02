---
tag: GN02JVADH4
kind: definition
name: Stratified sampling
msc: [62D05]
defines: PNMT15BB91
uses: [08QMKTWF9T, Y0PTCJBPEA, 0GQ938GDE0]
sources:
  - url: https://en.wikipedia.org/wiki/Stratified_sampling
---

## Definition

Let $U$ be a finite population of $N$ units, and let $U_1, \dots, U_H$ be a [[partition|08QMKTWF9T]] of $U$ into nonempty strata of sizes $N_1, \dots, N_H$.
Choose sample sizes $n_1, \dots, n_H$ with $1 \le n_h \le N_h$.
*Stratified (simple random) sampling* with these sizes draws, for each $h$, a [[simple random sample|Y0PTCJBPEA]] $S_h$ of size $n_h$ from $U_h$.
The $H$ draws are [[independent|0GQ938GDE0]].
The sample is $S = S_1 \cup \cdots \cup S_H$.

## Remarks

For values $y_i$ attached to the units, the stratified estimator of the population mean is $\bar y_{st} = \sum_{h=1}^{H} \frac{N_h}{N} \bar y_h$, where $\bar y_h$ is the sample mean in $S_h$.
It is unbiased, with variance $\sum_h \big(\frac{N_h}{N}\big)^2 \big(1 - \frac{n_h}{N_h}\big) \frac{S_h^2}{n_h}$, where $S_h^2$ is the population variance of the $y_i$ in $U_h$ with divisor $N_h - 1$.
*Proportional allocation* takes $n_h$ proportional to $N_h$.
*Neyman allocation* takes $n_h$ proportional to $N_h S_h$, which minimizes the variance for a fixed total $n = \sum_h n_h$.

Example: $U = \set{1, 2, 3, 4}$ with strata $U_1 = \set{1, 2}$ and $U_2 = \set{3, 4}$, and $n_1 = n_2 = 1$.
The possible samples are $\set{1, 3}$, $\set{1, 4}$, $\set{2, 3}$ and $\set{2, 4}$, each with probability $1/4$.

Non-example: a simple random sample of size $2$ from the whole of $U$.
It can be $\set{1, 2}$, with no unit from $U_2$, so it is not a stratified sample with $n_1 = n_2 = 1$.
