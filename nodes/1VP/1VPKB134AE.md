---
tag: 1VPKB134AE
kind: definition
name: Law of comparative judgment
msc: [91C15, "91E30"]
defines: NE54WYCWBR
uses: [05AQE0QR0D, 0H8H7ZTHW2, 0PNRKMRC55]
sources:
  - url: https://en.wikipedia.org/wiki/Law_of_comparative_judgment
---

## Definition

Let stimuli $1, \dots, n$ evoke jointly normal [[random variables|0PNRKMRC55]] $X_1, \dots, X_n$, called discriminal processes.
Let $X_i$ have mean $\mu_i$ and standard deviation $\sigma_i > 0$, and let $\rho_{ij}$ be the correlation of $X_i$ and $X_j$.
Stimulus $i$ is judged greater than stimulus $j$ exactly when $X_i > X_j$.
Let $\Phi$ be the [[cumulative distribution function|0H8H7ZTHW2]] of the standard [[normal distribution|05AQE0QR0D]].
Let $s_{ij}^2 = \sigma_i^2 + \sigma_j^2 - 2\rho_{ij}\sigma_i\sigma_j$, and assume $s_{ij} > 0$.
The *law of comparative judgment* is the resulting formula
$$P(i \succ j) = P(X_i > X_j) = \Phi\left(\frac{\mu_i - \mu_j}{s_{ij}}\right).$$

## Remarks

The formula holds because $X_i - X_j$ is normal with mean $\mu_i - \mu_j$ and variance $\sigma_i^2 + \sigma_j^2 - 2\rho_{ij}\sigma_i\sigma_j$.
Case V, the most used case, assumes $\sigma_i = \sigma$ and $\rho_{ij} = 0$, so $P(i \succ j) = \Phi((\mu_i - \mu_j)/(\sigma\sqrt{2}))$.
Example: in Case V with $\sigma = 1/\sqrt{2}$, an observed proportion $0.8413$ gives $\mu_i - \mu_j \approx 1$.
Non-example: a model in which $i$ is judged greater than $j$ whenever $\mu_i > \mu_j$, without noise, is not of this form, since it gives only proportions $0$, $1/2$ and $1$.
The scale values are determined only up to a positive affine change, so they form an interval scale.
