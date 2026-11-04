---
tag: 39VH4PBYYT
kind: proof
name: Proof of the formula for the mean of the normal distribution
msc: ["60E05"]
proves: 09PR1V6RWR
uses: [07RXBVTVZB, 027JF1FBB0, 04YG690N5V, 01ZWX875AT, 0DCT0QZVQ1, 0D37QFPEZE, 0XYAFCN0PT, 0RXX2PT1MQ, 0EX9GFJ0B3, 0VCTBJMEJF]
sources:
  - url: https://en.wikipedia.org/wiki/Normal_distribution
    locator: Moments
---

## Proof

We substitute $x = \mu + \sigma z$ and use that $z \varphi(z)$ is an odd function.

1. Let $\mu \in \R$, $\sigma^2 > 0$, and $\sigma = \sqrt{\sigma^2} > 0$. Let $X$ have the [[normal distribution|07RXBVTVZB]] $\mathcal{N}(\mu, \sigma^2)$.
2. Let $f = \varphi_{\mu, \sigma^2}$ and $\varphi = \varphi_{0,1}$ be the [[normal densities|027JF1FBB0]]. By definition, $f$ is a [[probability density function|04YG690N5V]] of $X$.
3. By the [[law of the unconscious statistician|01ZWX875AT]], $X$ is integrable if $\int_{\R} \abs{x} f(x) \, dx < \infty$. In that case $E[X] = \int_{\R} x f(x) \, dx$.
4. For a continuous function $h \ge 0$ on $\R$, the integral $\int_\R h \, dx$ is the limit of $\int_{a}^{b} h \, dx$ as $a \to -\infty$ and $b \to \infty$. So we may compute with [[improper integrals|0VCTBJMEJF]].
5. For all real $z$, $\sigma f(\mu + \sigma z) = \varphi(z)$. So, for continuous $g$ and $R > 0$, [[substitution|0D37QFPEZE]] with $x = \mu + \sigma z$ gives
$$\int_{\mu - \sigma R}^{\mu + \sigma R} g(x) f(x) \, dx = \int_{-R}^{R} g(\mu + \sigma z) \, \varphi(z) \, dz.$$
6. By the [[chain rule|0RXX2PT1MQ]] and [[the derivative of the exponential function|0EX9GFJ0B3]], the function $-\varphi$ has derivative $z \varphi(z)$.
7. By the [[fundamental theorem of calculus|0XYAFCN0PT]], $\int_0^R z \varphi(z) \, dz = \varphi(0) - \varphi(R) \le \varphi(0) = 1/\sqrt{2\pi}$.
8. The function $\abs{z} \varphi(z)$ is even. So $\int_{-R}^{R} \abs{z} \varphi(z) \, dz = 2 \int_0^R z \varphi(z) \, dz \le 2/\sqrt{2\pi}$.
9. Since $\varphi$ is the density of $\mathcal{N}(0, 1)$, its integral over $\R$ is $1$. So $\int_{-R}^R \varphi(z) \, dz \le 1$.
10. By step 5 with $g(x) = \abs{x}$ and $\abs{\mu + \sigma z} \le \abs{\mu} + \sigma \abs{z}$, we get $\int_{\mu - \sigma R}^{\mu + \sigma R} \abs{x} f(x) \, dx \le \abs{\mu} + 2\sigma/\sqrt{2\pi}$.
11. This bound does not depend on $R$. By steps 3 and 4, $\int_\R \abs{x} f(x) \, dx < \infty$, so $X$ is integrable.
12. Write $x f(x)$ as the difference of its positive part and its negative part. Both parts are continuous, nonnegative and at most $\abs{x} f(x)$.
13. Applying step 4 to each part gives $E[X] = \lim_{R \to \infty} \int_{\mu - \sigma R}^{\mu + \sigma R} x f(x) \, dx$.
14. By step 5 with $g(x) = x$, the integral in step 13 equals $\mu \int_{-R}^{R} \varphi(z) \, dz + \sigma \int_{-R}^{R} z \varphi(z) \, dz$.
15. The function $z \varphi(z)$ is odd. Substituting $z = -u$ on $[-R, 0]$ shows that $\int_{-R}^{0} z \varphi(z) \, dz = -\int_0^R u \varphi(u) \, du$. So $\int_{-R}^{R} z \varphi(z) \, dz = 0$.
16. As $R \to \infty$, $\int_{-R}^{R} \varphi(z) \, dz \to 1$ by step 9.
17. By steps 13 to 16, the [[expected value|0DCT0QZVQ1]] is $E[X] = \mu \cdot 1 + \sigma \cdot 0 = \mu$. This is the stated integral.

## Idea

The substitution $x = \mu + \sigma z$ reduces everything to the standard normal density $\varphi$. The integral of $\varphi$ is $1$, and the integral of $z \varphi(z)$ is $0$ because the function is odd. What is left is $\mu$.
