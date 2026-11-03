---
tag: 6PQD1SEX62
kind: definition
name: Rate–distortion function
msc: [94A34, 94A17]
defines: 4JN2Z9DH4Y
uses: [PFJER4FMJ5, A83CYGDXFG, 0ZN9EZTEM6, 0WQNRCNY3M, 0D6J4B671D, GW25TGD33J]
sources:
  - url: https://en.wikipedia.org/wiki/Rate%E2%80%93distortion_theory
---

## Definition

Let $\mathcal{X}$ and $\hat{\mathcal{X}}$ be finite sets, let $p$ be a [[probability mass function|0D6J4B671D]] on $\mathcal{X}$, and let $d \colon \mathcal{X} \times \hat{\mathcal{X}} \to [0, \infty)$ be a distortion measure.
Let $X$ be a random variable with law $p$.
For a [[conditional distribution|0ZN9EZTEM6]] $q(\hat{x} \mid x)$ of a random variable $\hat{X}$ with values in $\hat{\mathcal{X}}$ given $X$, let $I(X; \hat{X})$ be the [[mutual information|A83CYGDXFG]] in bits.
Put $D_{\min} = \sum_{x} p(x) \min_{\hat{x}} d(x, \hat{x})$.
The *rate–distortion function* of $(p, d)$ is the function on $[D_{\min}, \infty)$ given by
$$R(D) = \min \set{ I(X; \hat{X}) : q \text{ such that } \mathbb{E}\, d(X, \hat{X}) \le D }.$$

## Remarks

The minimum exists, since the allowed $q$ form a non-empty compact set and $I(X; \hat{X})$ is continuous in $q$.
The function $R$ is non-increasing and convex.
By Shannon's rate–distortion theorem, $R(D)$ equals the operational rate–distortion function of [[rate–distortion theory|PFJER4FMJ5]] for i.i.d. sources with law $p$.

Example: let $p$ be Bernoulli with $p(1) = r \le 1/2$, with $\hat{\mathcal{X}} = \set{0, 1}$ and Hamming distortion.
Then $R(D) = h(r) - h(D)$ for $0 \le D \le r$ and $R(D) = 0$ for $D \ge r$, where $h$ is the [[binary entropy function|GW25TGD33J]].
At $D = r$ the constant reproduction $\hat{X} = 0$ has [[expected|0WQNRCNY3M]] distortion $r$ and $I(X; \hat{X}) = 0$, which matches $R(r) = 0$.
Non-example: the map $D \mapsto h(r) - h(D)$ is not the rate–distortion function on all of $[0, 1/2]$ when $r < 1/2$, since it is negative for $r < D \le 1/2$.
For a Gaussian source of variance $\sigma^2$ with squared-error distortion, the analogous formula is $R(D) = \frac{1}{2} \log_2 (\sigma^2 / D)$ for $0 < D \le \sigma^2$.
