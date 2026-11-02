---
tag: 6V75QVQCX6
kind: definition
name: Robbins–Monro algorithm
msc: [62L20]
defines: CHHD44WDHJ
uses: [ZPCPW4W1Y9, 0DKRR22AEQ, 0WQNRCNY3M, 0QA1HBD9Z4]
sources:
  - url: https://en.wikipedia.org/wiki/Stochastic_approximation
    locator: Robbins–Monro algorithm
---

## Definition

Let $M \colon \R \to \R$ be an unknown function and let $\alpha \in \R$ be a target value.
Assume that at each $\theta \in \R$ one can observe a [[random variable|0DKRR22AEQ]] $N(\theta)$ with [[expectation|0WQNRCNY3M]] $E[N(\theta)] = M(\theta)$.
Let $(a_n)_{n \ge 1}$ be positive step sizes.
The *Robbins–Monro algorithm* is this [[stochastic approximation|ZPCPW4W1Y9]] scheme:
$$\theta_{n+1} = \theta_n - a_n \left( N_n - \alpha \right), \qquad n \ge 1.$$
Here $\theta_1$ is an initial guess.
Given the past, $N_n$ is an observation of $N(\theta_n)$, made independently of the earlier observations.
Its aim is a root $\theta^*$ of the equation $M(\theta) = \alpha$.

## Remarks

Robbins and Monro proved this convergence result in 1951.
Assume that $N(\theta)$ is uniformly bounded, $M$ is nondecreasing, $M'(\theta^*)$ exists and is positive, and the step sizes satisfy $\sum_n a_n = \infty$ and $\sum_n a_n^2 < \infty$.
Then $\theta_n \to \theta^*$ in $L^2$, and hence [[in probability|0QA1HBD9Z4]].

Example: let $N(\theta) = \theta - Z$ with $Z$ uniform on $[0, 2]$, so $M(\theta) = \theta - 1$, and let $\alpha = 0$ and $a_n = 1/n$.
The step sizes satisfy both conditions, since $\sum 1/n = \infty$ and $\sum 1/n^2 < \infty$, and the root is $\theta^* = 1$.
With fresh draws $Z_n$, the recursion is $\theta_{n+1} = \theta_n - \frac1n (\theta_n - Z_n)$, so $\theta_{n+1} = (Z_1 + \cdots + Z_n)/n$, the sample mean, which tends to $1$ by the law of large numbers.

Non-example: constant step sizes $a_n = c > 0$ violate $\sum a_n^2 < \infty$; in the example, $\theta_{n+1} = (1 - c) \theta_n + c Z_n$ for $0 < c < 1$ keeps fluctuating with conditional variance $c^2 \operatorname{Var}(Z) > 0$ at each step, so it does not converge.
