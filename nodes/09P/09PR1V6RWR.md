---
tag: 09PR1V6RWR
kind: statement
role: proposition
name: Mean of the normal distribution
msc: ["60E05"]
uses: [07RXBVTVZB, 0DCT0QZVQ1, 027JF1FBB0]
sources:
  - url: https://en.wikipedia.org/wiki/Normal_distribution
    locator: Moments
---

## Statement

Let $\mu \in \mathbb{R}$, let $\sigma^2 > 0$ and let $X$ have the [[normal distribution|07RXBVTVZB]] $\mathcal{N}(\mu, \sigma^2)$. Then $X$ is integrable and
$$E[X] = \int_{-\infty}^{\infty} x \, \frac{1}{\sqrt{2\pi\sigma^2}} e^{-(x - \mu)^2/(2\sigma^2)} \, dx = \mu.$$

## Remarks

Proof: substitute $x = \mu + \sigma z$ with $\sigma = \sqrt{\sigma^2}$. The integral becomes $\mu \int \varphi(z) \, dz + \sigma \int z \varphi(z) \, dz$, where $\varphi$ is the [[standard normal density|027JF1FBB0]].
The first integral is $1$. The second is $0$, because $z \varphi(z)$ is an odd integrable function.
So the parameter $\mu$ is the mean. It is also the median and the mode, because the density is symmetric about $\mu$ and has its maximum there.

## Explanations

### L1 human

The bell curve of $\mathcal{N}(\mu, \sigma^2)$ is symmetric about $\mu$, so its average is $\mu$.
