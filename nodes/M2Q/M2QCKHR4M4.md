---
tag: M2QCKHR4M4
kind: definition
name: Adams operations
msc: ["19L20", "55S25", "19E08"]
defines: KQP64TH307
uses: [E2KA3XP47F, 0ZNXZB4HNB, 0X5QVCF06N]
sources:
  - url: https://en.wikipedia.org/wiki/Adams_operation
---

## Definition

Let $R$ be a [[lambda-ring|E2KA3XP47F]] with operations $\lambda^n$, and let $\lambda_t(x) = \sum_{n \ge 0} \lambda^n(x) t^n$.
The *Adams operations* $\psi^k \colon R \to R$, for $k \ge 1$, are defined by the identity of power series
$$\sum_{k \ge 1} \psi^k(x) (-t)^k = -t \, \frac{\frac{d}{dt} \lambda_t(x)}{\lambda_t(x)}.$$
Equivalently, they are given recursively by Newton's formula
$$\psi^k(x) - \lambda^1(x) \psi^{k-1}(x) + \lambda^2(x) \psi^{k-2}(x) - \cdots + (-1)^{k-1} \lambda^{k-1}(x) \psi^1(x) + (-1)^k k \lambda^k(x) = 0.$$

## Remarks

So $\psi^1(x) = x$ and $\psi^2(x) = x^2 - 2 \lambda^2(x)$.
Newton's formula expresses the [[power sums|0ZNXZB4HNB]] through the [[elementary symmetric polynomials|0X5QVCF06N]]; if $x = \xi_1 + \cdots + \xi_r$ is a sum of line elements, then $\lambda^n(x) = e_n(\xi)$ and $\psi^k(x) = \xi_1^k + \cdots + \xi_r^k$.

In a lambda-ring the $\psi^k$ satisfy:

1. Each $\psi^k$ is a ring homomorphism.
2. $\psi^k \circ \psi^l = \psi^{kl}$.
3. $\psi^k(x) = x^k$ if $x$ is a line element, that is, $\lambda_t(x) = 1 + xt$.
4. $\psi^p(x) \equiv x^p \pmod{pR}$ for every prime $p$.

Example: in $\Z$ with $\lambda_t(m) = (1 + t)^m$, one gets $-t \cdot m (1 + t)^{-1} = \sum_{k \ge 1} m (-t)^k$, so $\psi^k(m) = m$ for all $k$.

Non-example: the map $x \mapsto x^2$ is not $\psi^2$ on $\Z$, since $2^2 = 4$ while $\psi^2(2) = 2$; squaring is not additive, while $\psi^2$ is.
