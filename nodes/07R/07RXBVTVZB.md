---
tag: 07RXBVTVZB
kind: definition
name: Normal distribution
msc: ["60E05"]
defines: 05AQE0QR0D
uses: [04YG690N5V, 099SXAG014, 027JF1FBB0]
sources:
  - url: https://en.wikipedia.org/wiki/Normal_distribution
    locator: General normal distribution
---

## Definition

Let $\mu \in \mathbb{R}$ and $\sigma^2 > 0$.
The normal distribution with mean $\mu$ and variance $\sigma^2$, written $\mathcal{N}(\mu, \sigma^2)$, is the distribution on $\mathbb{R}$ with the [[probability density function|04YG690N5V]]
$$\varphi_{\mu, \sigma^2}(x) = \frac{1}{\sqrt{2\pi\sigma^2}} \exp\left(-\frac{(x - \mu)^2}{2\sigma^2}\right), \quad x \in \mathbb{R}.$$
The standard normal distribution is $\mathcal{N}(0, 1)$.

## Remarks

The function $\varphi_{\mu, \sigma^2}$ is the [[density of the normal distribution|027JF1FBB0]].
Some authors, and the library Mathlib, also allow $\sigma^2 = 0$. Then $\mathcal{N}(\mu, 0)$ is the [[Dirac measure|099SXAG014]] $\delta_\mu$.
If $X \sim \mathcal{N}(\mu, \sigma^2)$ and $a \ne 0$, $b$ are real, then $aX + b \sim \mathcal{N}(a\mu + b, a^2 \sigma^2)$. In particular, $(X - \mu)/\sigma \sim \mathcal{N}(0, 1)$.
The cumulative distribution function of $\mathcal{N}(0, 1)$ is written $\Phi$. It has no formula with elementary functions.

## Explanations

### L1 human

The normal distribution is the famous bell curve. It is symmetric about the mean $\mu$, and $\sigma$ measures its width.
Heights of people and errors of measurement are often close to normal.
