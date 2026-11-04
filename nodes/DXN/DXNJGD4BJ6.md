---
tag: DXNJGD4BJ6
kind: proof
name: Proof of the formula for the variance of the normal distribution
msc: ["60E05"]
proves: 03EESZDB9A
uses: [07RXBVTVZB, 027JF1FBB0, 04YG690N5V, 007QED3E0Y, 09PR1V6RWR, 01ZWX875AT, 0D37QFPEZE, 08Y1BBQTK9, 0RXX2PT1MQ, 0EX9GFJ0B3, 06JZGMYTYD, 0VCTBJMEJF]
sources:
  - url: https://en.wikipedia.org/wiki/Normal_distribution
    locator: Moments
---

## Proof

We substitute $x = \mu + \sigma z$ and integrate by parts.

1. Let $\mu \in \R$, $\sigma^2 > 0$, and $\sigma = \sqrt{\sigma^2} > 0$. Let $X$ have the [[normal distribution|07RXBVTVZB]] $\mathcal{N}(\mu, \sigma^2)$.
2. Let $f = \varphi_{\mu, \sigma^2}$ and $\varphi = \varphi_{0,1}$ be the [[normal densities|027JF1FBB0]]. By definition, $f$ is a [[probability density function|04YG690N5V]] of $X$.
3. By the [[mean of the normal distribution|09PR1V6RWR]], $X$ is integrable with $E[X] = \mu$. So by definition the [[variance|007QED3E0Y]] is $\operatorname{Var}(X) = E[(X - \mu)^2]$.
4. By the [[law of the unconscious statistician|01ZWX875AT]], if $\int_\R (x - \mu)^2 f(x) \, dx < \infty$, then $E[(X - \mu)^2]$ equals this integral.
5. The integrand in step 4 is continuous and nonnegative. So the integral is the limit of $\int_{\mu - \sigma R}^{\mu + \sigma R} (x - \mu)^2 f(x) \, dx$ as $R \to \infty$, an [[improper integral|0VCTBJMEJF]].
6. For all real $z$, $\sigma f(\mu + \sigma z) = \varphi(z)$. [[Substitution|0D37QFPEZE]] with $x = \mu + \sigma z$ gives
$$\int_{\mu - \sigma R}^{\mu + \sigma R} (x - \mu)^2 f(x) \, dx = \sigma^2 \int_{-R}^{R} z^2 \varphi(z) \, dz.$$
7. By the [[chain rule|0RXX2PT1MQ]] and [[the derivative of the exponential function|0EX9GFJ0B3]], $\varphi'(z) = -z \varphi(z)$.
8. [[Integration by parts|08Y1BBQTK9]] with $u(z) = z$ and $v(z) = -\varphi(z)$, so that $v'(z) = z \varphi(z)$, gives
$$\int_{-R}^{R} z^2 \varphi(z) \, dz = \big[-z \varphi(z)\big]_{-R}^{R} + \int_{-R}^{R} \varphi(z) \, dz = -2R\varphi(R) + \int_{-R}^{R} \varphi(z) \, dz.$$
9. By the [[power series of the exponential function|06JZGMYTYD]], $e^{y} \ge y$ for $y \ge 0$. With $y = R^2/2$, this gives $R \varphi(R) \le 2/(R\sqrt{2\pi})$ for $R > 0$.
10. So $R \varphi(R) \to 0$ as $R \to \infty$.
11. Since $\varphi$ is the density of $\mathcal{N}(0, 1)$, $\int_{-R}^{R} \varphi(z) \, dz \to 1$ as $R \to \infty$.
12. By steps 8, 10 and 11, $\int_{-R}^{R} z^2 \varphi(z) \, dz \to 1$.
13. By steps 5, 6 and 12, the integral in step 4 is finite and equals $\sigma^2 \cdot 1$.
14. By steps 3 and 4, $\operatorname{Var}(X) = \sigma^2$.

## Idea

After the substitution $x = \mu + \sigma z$, the variance is $\sigma^2$ times $\int z^2 \varphi(z) \, dz$. Since $\varphi' = -z\varphi$, integration by parts turns this integral into $\int \varphi = 1$.
