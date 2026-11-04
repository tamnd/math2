---
tag: VKP5HGD7TV
kind: proof
name: Proof of the formula for the moment-generating function of the normal distribution
msc: ["60E10"]
proves: 0B1G4E21G7
uses: [0NNRNGKMFM, 07RXBVTVZB, 027JF1FBB0, 04YG690N5V, 01ZWX875AT, 0D37QFPEZE, 0E8HNVBCSP, 0VCTBJMEJF]
sources:
  - url: https://en.wikipedia.org/wiki/Normal_distribution
    locator: Moment- and cumulant-generating functions
---

## Proof

We substitute $x = \mu + \sigma z$ and complete the square in the exponent.

1. Let $\mu \in \R$, $\sigma^2 > 0$, and $\sigma = \sqrt{\sigma^2} > 0$. Let $X \sim \mathcal{N}(\mu, \sigma^2)$ be [[normal|07RXBVTVZB]], and fix $t \in \R$.
2. Let $f = \varphi_{\mu, \sigma^2}$ and $\varphi = \varphi_{0,1}$ be the [[normal densities|027JF1FBB0]]. By definition, $f$ is a [[probability density function|04YG690N5V]] of $X$.
3. By the [[law of the unconscious statistician|01ZWX875AT]], if $\int_\R e^{tx} f(x) \, dx < \infty$, then $e^{tX}$ is integrable and $E[e^{tX}]$ equals this integral.
4. The integrand is continuous and positive. So the integral is the limit of $\int_{\mu - \sigma R}^{\mu + \sigma R} e^{tx} f(x) \, dx$ as $R \to \infty$, an [[improper integral|0VCTBJMEJF]].
5. For all real $z$, $\sigma f(\mu + \sigma z) = \varphi(z)$. [[Substitution|0D37QFPEZE]] with $x = \mu + \sigma z$ gives
$$\int_{\mu - \sigma R}^{\mu + \sigma R} e^{tx} f(x) \, dx = \int_{-R}^{R} e^{t\mu + t\sigma z} \varphi(z) \, dz.$$
6. Completing the square gives $t\sigma z - z^2/2 = \sigma^2 t^2/2 - (z - \sigma t)^2/2$.
7. By step 6 and the [[exponential of a sum|0E8HNVBCSP]], $e^{t\mu + t\sigma z} \varphi(z) = e^{\mu t + \sigma^2 t^2/2} \, \varphi(z - \sigma t)$.
8. Substitution with $u = z - \sigma t$ gives $\int_{-R}^{R} \varphi(z - \sigma t) \, dz = \int_{-R - \sigma t}^{R - \sigma t} \varphi(u) \, du$.
9. Since $\varphi$ is the density of $\mathcal{N}(0, 1)$, its integral over $\R$ is $1$. So the integral in step 8 tends to $1$ as $R \to \infty$.
10. By steps 4, 5, 7 and 9, $\int_\R e^{tx} f(x) \, dx = e^{\mu t + \sigma^2 t^2/2} < \infty$.
11. By step 3, the [[moment-generating function|0NNRNGKMFM]] is $M_X(t) = E[e^{tX}] = \exp\left(\mu t + \tfrac{1}{2}\sigma^2 t^2\right)$.

## Idea

Multiplying the standard normal density by $e^{sz}$ shifts the centre of the Gaussian bell to $s$ and multiplies it by $e^{s^2/2}$. This is completing the square. The shifted bell still has total mass $1$.
