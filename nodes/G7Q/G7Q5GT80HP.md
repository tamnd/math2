---
tag: G7Q5GT80HP
kind: proof
name: Proof of the sum of independent normal random variables by characteristic functions
msc: ["60E05"]
proves: 0NXGPJWNFN
uses: [07RXBVTVZB, 0MYDNRT7PP, 0NS0TDA4E2, 02JGYG0T7M, 0T8BYAFEXX, 0E9502NT92, 0WM7DJCM6G]
sources:
  - url: https://en.wikipedia.org/wiki/Sum_of_normally_distributed_random_variables
    locator: Proof using characteristic functions
---

## Proof

We compute the characteristic function of $X + Y$ and recognise it.

1. For a real random variable $Z$, let $\varphi_Z(t) = E[e^{itZ}]$ be its [[characteristic function|0MYDNRT7PP]], for $t \in \R$.
2. By the [[characteristic function of the normal distribution|0NS0TDA4E2]], $\varphi_X(t) = \exp\left(i \mu_1 t - \tfrac12 \sigma_1^2 t^2\right)$ and $\varphi_Y(t) = \exp\left(i \mu_2 t - \tfrac12 \sigma_2^2 t^2\right)$.
3. $X$ and $Y$ are [[independent|0E9502NT92]]. By the [[characteristic function of a sum of independent random variables|02JGYG0T7M]], $\varphi_{X+Y}(t) = \varphi_X(t) \, \varphi_Y(t)$ for each $t$.
4. By the [[product of exponentials|0WM7DJCM6G]], $\varphi_{X+Y}(t) = \exp\left(i (\mu_1 + \mu_2) t - \tfrac12 (\sigma_1^2 + \sigma_2^2) t^2\right)$.
5. Let $\mu = \mu_1 + \mu_2$ and $\sigma^2 = \sigma_1^2 + \sigma_2^2$. Then $\sigma^2 > 0$, so the [[normal distribution|07RXBVTVZB]] $\mathcal{N}(\mu, \sigma^2)$ is defined. Let $W \sim \mathcal{N}(\mu, \sigma^2)$.
6. By the characteristic function of the normal distribution, $\varphi_W(t) = \exp\left(i \mu t - \tfrac12 \sigma^2 t^2\right)$. By step 4, $\varphi_W(t) = \varphi_{X+Y}(t)$ for all $t \in \R$.
7. By the theorem that [[the characteristic function determines the distribution|0T8BYAFEXX]], $X + Y$ and $W$ have the same law.
8. Hence $X + Y \sim \mathcal{N}(\mu_1 + \mu_2, \, \sigma_1^2 + \sigma_2^2)$.

## Idea

For independent variables, characteristic functions multiply. The characteristic function of a normal law is the exponential of a quadratic in $t$. So in a product the means add and the variances add. Since a characteristic function fixes the law, the sum is normal.
