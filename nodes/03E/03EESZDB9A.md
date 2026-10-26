---
tag: 03EESZDB9A
kind: statement
role: proposition
name: Variance of the normal distribution
msc: ["60E05"]
uses: [07RXBVTVZB, 007QED3E0Y, 09PR1V6RWR, 0KVQ9D86BM, 04CYN5G6RY]
sources:
  - url: https://en.wikipedia.org/wiki/Normal_distribution
    locator: Moments
---

## Statement

Let $\mu \in \mathbb{R}$, let $\sigma^2 > 0$ and let $X$ have the [[normal distribution|07RXBVTVZB]] $\mathcal{N}(\mu, \sigma^2)$. Then
$$\operatorname{Var}(X) = \sigma^2.$$

## Remarks

Proof: $Z = (X - \mu)/\sigma$ has the law $\mathcal{N}(0, 1)$, where $\sigma = \sqrt{\sigma^2}$. Integration by parts gives $E[Z^2] = \int z^2 \varphi(z) \, dz = \int \varphi(z) \, dz = 1$.
Since $E[Z] = 0$ by the [[mean of the normal distribution|09PR1V6RWR]], $\operatorname{Var}(Z) = 1$. The [[scaling|0KVQ9D86BM]] and [[translation|04CYN5G6RY]] rules then give $\operatorname{Var}(X) = \sigma^2 \operatorname{Var}(Z) = \sigma^2$.
So the two parameters of $\mathcal{N}(\mu, \sigma^2)$ are its mean and its variance.

## Explanations

### L1 human

The second parameter of the normal distribution is exactly its variance. So $\sigma$ is the standard deviation, the typical distance of a value from the center.
