---
tag: HSSC2ZZWMY
kind: definition
name: Stochastic approximation
msc: [62L20]
defines: ZPCPW4W1Y9
uses: [0DKRR22AEQ, 0YAMJRK04E, 0QE8STGJH2]
sources:
  - url: https://en.wikipedia.org/wiki/Stochastic_approximation
---

## Definition

Let $h \colon \R^d \to \R^d$ be an unknown function.
Assume that at each point $\theta \in \R^d$ one can observe a [[random variable|0DKRR22AEQ]] whose mean is $h(\theta)$.
A *stochastic approximation algorithm* is a recursion
$$\theta_{n+1} = \theta_n + a_n Y_{n+1}, \qquad n \ge 0,$$
in which:

1. $\theta_0 \in \R^d$ is an initial point, possibly random.
2. $(a_n)_{n \ge 0}$ is a [[sequence|0QE8STGJH2]] of positive step sizes.
3. $Y_{n+1}$ is a noisy observation at $\theta_n$: with $\mathcal{F}_n = \sigma(\theta_0, Y_1, \dots, Y_n)$, the [[conditional expectation|0YAMJRK04E]] satisfies $E[Y_{n+1} \mid \mathcal{F}_n] = h(\theta_n)$.

The aim is that $\theta_n$ converges to a zero of $h$.

## Remarks

Example: let $Z_1, Z_2, \dots$ be independent with common mean $m$, and take $h(\theta) = m - \theta$, $Y_{n+1} = Z_{n+1} - \theta_n$ and $a_n = 1/(n+1)$, with $\theta_0 = 0$.
Then $E[Y_{n+1} \mid \mathcal{F}_n] = m - \theta_n$, and by induction $\theta_n = (Z_1 + \cdots + Z_n)/n$, the sample mean, which tends to the zero $m$ of $h$.

Non-example: the deterministic Newton iteration $\theta_{n+1} = \theta_n - h(\theta_n)/h'(\theta_n)$ is not a stochastic approximation algorithm, since it needs exact values of $h$ and $h'$ rather than noisy observations, so clause 3 fails.

The usual conditions on the step sizes are $\sum_n a_n = \infty$ and $\sum_n a_n^2 < \infty$.
The first condition lets the iterates travel any distance, and the second makes the accumulated noise $\sum_n a_n (Y_{n+1} - h(\theta_n))$ converge.
Writing the noise as a martingale difference sequence, the iterates follow, in the long run, the ordinary differential equation $\dot\theta = h(\theta)$.
