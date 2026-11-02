---
tag: PZGNRA2DAY
kind: definition
name: Power of a test
msc: [62F03]
defines: 4RJSN0QARD
uses: [087P03NEND, 0R41PVFA39]
sources:
  - url: https://en.wikipedia.org/wiki/Power_(statistics)
---

## Definition

Let $X$ be data whose law $P_\theta$ depends on $\theta \in \Theta$, and consider a [[hypothesis test|087P03NEND]] of $H_0 \colon \theta \in \Theta_0$ against $H_1 \colon \theta \in \Theta_1$.
Let the test reject $H_0$ when $X$ lies in a rejection region $R$.
The *power function* of the test is $\pi(\theta) = P_\theta(X \in R)$ for $\theta \in \Theta$.
The *power* of the test at $\theta \in \Theta_1$ is $\pi(\theta)$.

## Remarks

For $\theta \in \Theta_1$, the power is $1 - \beta(\theta)$, where $\beta(\theta)$ is the probability of a [[type II error|0R41PVFA39]].
For $\theta \in \Theta_0$, the value $\pi(\theta)$ is the probability of a type I error, and $\sup_{\theta \in \Theta_0} \pi(\theta)$ is the size of the test.
For a randomized test $\varphi$ with values in $[0, 1]$, the power function is $\pi(\theta) = E_\theta[\varphi(X)]$.
Example: let $X \sim \mathcal{N}(\theta, 1)$, $H_0 \colon \theta = 0$, $H_1 \colon \theta > 0$, and $R = \set{x > 1.645}$.
Then $\pi(\theta) = 1 - \Phi(1.645 - \theta)$, where $\Phi$ is the standard normal distribution function; so $\pi(0) \approx 0.05$ and $\pi(2) \approx 0.64$.
Non-example: $\pi(0) \approx 0.05$ is not a power in this example, since $0 \notin \Theta_1$; it is the size.
