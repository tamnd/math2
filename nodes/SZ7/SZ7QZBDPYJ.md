---
tag: SZ7QZBDPYJ
kind: definition
name: Cross-validation
msc: [62G09, 62J05]
defines: HA1KJ3B9DX
uses: [3BTG6VVCGZ, 0TTNRP5PFQ]
sources:
  - url: https://en.wikipedia.org/wiki/Cross-validation_(statistics)
---

## Definition

Let $(x_1, y_1), \dots, (x_n, y_n)$ be data, and let a fitting rule map any subset $S$ of the data to a prediction function $\hat f_S$.
Let $\ell(y, \hat y) \ge 0$ be a [[loss function|3BTG6VVCGZ]].
Let $K$ be an integer with $2 \le K \le n$, and let $F_1, \dots, F_K$ be a partition of $\set{1, \dots, n}$ into nonempty folds.
For each $k$, let $\hat f^{(-k)}$ be the prediction function fitted on the data with indices outside $F_k$.
The *$K$-fold cross-validation estimate* of the prediction error is
$$\mathrm{CV} = \frac{1}{n} \sum_{k=1}^{K} \sum_{i \in F_k} \ell\big(y_i, \hat f^{(-k)}(x_i)\big).$$

## Remarks

The case $K = n$, with one observation per fold, is *leave-one-out* cross-validation.
To choose a tuning parameter, one computes $\mathrm{CV}$ for each candidate value and keeps a value with the smallest $\mathrm{CV}$.
Example: for least squares with $\ell(y, \hat y) = (y - \hat y)^2$, leave-one-out has a closed form.
It equals $\frac{1}{n} \sum_i \big((y_i - \hat y_i)/(1 - h_{ii})\big)^2$, where $\hat y_i$ is the full fit and $h_{ii}$ the $i$-th diagonal entry of the hat matrix.
Non-example: the training error $\frac{1}{n} \sum_i \ell(y_i, \hat f(x_i))$ with $\hat f$ fitted on all data is not cross-validation.
Each $y_i$ is predicted by a function that used it, so the error is biased downwards.
