---
tag: RX4CVSSRRJ
kind: example
name: Dirichlet distribution
msc: ["60E05", "62E15", 62F15]
instance_of: [0DVDCMA2DK]
uses: [0H5SYBSED9, 0B80PAQD3C, 0EW824Z7G2]
sources:
  - url: https://en.wikipedia.org/wiki/Dirichlet_distribution
same_as:
  wikidata: Q981016
  wikipedia: Dirichlet distribution
---

## Example

Let $K \ge 2$ and $\alpha_1, \dots, \alpha_K > 0$, and let $\alpha_0 = \alpha_1 + \dots + \alpha_K$.
The *Dirichlet distribution* $\operatorname{Dir}(\alpha_1, \dots, \alpha_K)$ is the law of a random vector $(X_1, \dots, X_K)$ in the open simplex $\set{x \in \R^K : x_i > 0, \ x_1 + \dots + x_K = 1}$.
The vector $(X_1, \dots, X_{K-1})$ has the density
$$f(x_1, \dots, x_{K-1}) = \frac{\Gamma(\alpha_0)}{\Gamma(\alpha_1) \cdots \Gamma(\alpha_K)} \prod_{i=1}^K x_i^{\alpha_i - 1}$$
on the set where all $x_i > 0$ and $x_1 + \dots + x_{K-1} < 1$, with $x_K = 1 - x_1 - \dots - x_{K-1}$; here $\Gamma$ is the [[gamma function|0H5SYBSED9]].
A construction: if $Y_1, \dots, Y_K$ are independent and $Y_i$ has the [[gamma distribution|0B80PAQD3C]] with shape $\alpha_i$ and scale $1$, then $(Y_1, \dots, Y_K) / (Y_1 + \dots + Y_K)$ has law $\operatorname{Dir}(\alpha_1, \dots, \alpha_K)$.
Check for $K = 2$: the density becomes $\frac{\Gamma(\alpha_1 + \alpha_2)}{\Gamma(\alpha_1)\Gamma(\alpha_2)} x^{\alpha_1 - 1} (1 - x)^{\alpha_2 - 1}$ on $(0, 1)$, so $X_1$ has the [[beta distribution|0EW824Z7G2]] with parameters $\alpha_1, \alpha_2$.
The means are $E[X_i] = \alpha_i / \alpha_0$ and the variances are $\operatorname{Var}(X_i) = \frac{\alpha_i (\alpha_0 - \alpha_i)}{\alpha_0^2 (\alpha_0 + 1)}$.

## Remarks

If all $\alpha_i = 1$, the density is constant, so the law is uniform on the simplex.
The Dirichlet law is the conjugate prior of the multinomial law: with prior $\operatorname{Dir}(\alpha_1, \dots, \alpha_K)$ for the cell probabilities and observed counts $n_1, \dots, n_K$, the posterior is $\operatorname{Dir}(\alpha_1 + n_1, \dots, \alpha_K + n_K)$.
It is the finite-dimensional building block of the [[Dirichlet process|XT4SWG6J7N]].

## Explanations

### L1 human

The Dirichlet distribution is a law on random probability vectors: lists of $K$ positive numbers that add up to $1$.
It is used to model an unknown die with $K$ faces, before the die has been thrown.
Large parameters concentrate the vector near the mean $(\alpha_1, \dots, \alpha_K)/\alpha_0$, and small parameters push it towards the corners of the simplex.
For two categories it is the beta distribution.
