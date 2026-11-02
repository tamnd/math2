---
tag: MZZ56W92DY
kind: definition
name: Mittag-Leffler function
msc: ["33E12", "26A33"]
defines: 12G9M694YG
uses: [0H5SYBSED9, 0MZB06ST2B, 0G4F0XB9X2]
sources:
  - url: https://en.wikipedia.org/wiki/Mittag-Leffler_function
---

## Definition

Let $\alpha, \beta \in \C$ with $\operatorname{Re} \alpha > 0$, and let $\Gamma$ be the [[gamma function|0H5SYBSED9]], with the convention $1/\Gamma(-m) = 0$ for $m = 0, 1, 2, \ldots$.
The *two-parameter Mittag-Leffler function* is the [[power series|0MZB06ST2B]]
$$E_{\alpha, \beta}(z) = \sum_{k=0}^{\infty} \frac{z^k}{\Gamma(\alpha k + \beta)}, \qquad z \in \C.$$
The *Mittag-Leffler function* is $E_\alpha = E_{\alpha, 1}$.

## Remarks

The series has infinite radius of convergence, because $\Gamma(\alpha k + \beta)$ grows faster than any power of $k$ when $\operatorname{Re} \alpha > 0$, so $E_{\alpha, \beta}$ is an [[entire function|0G4F0XB9X2]].

Example: for $\alpha = \beta = 1$, $\Gamma(k + 1) = k!$, so $E_{1,1}(z) = e^z$.
Also $E_2(z) = \sum_k \frac{z^k}{(2k)!} = \cosh \sqrt{z}$, and $E_{1/2}(z) = e^{z^2} \operatorname{erfc}(-z)$.

Non-example: for $\alpha = 0$ and $\beta = 1$ the series is $\sum_k z^k$, which is not entire; it converges only for $\abs{z} < 1$, so the condition $\operatorname{Re} \alpha > 0$ cannot be dropped.

Laplace transform: for $\operatorname{Re} s$ large enough,
$$\int_0^\infty e^{-st} \, t^{\beta - 1} E_{\alpha, \beta}(\lambda t^\alpha) \, dt = \frac{s^{\alpha - \beta}}{s^\alpha - \lambda},$$
which follows by integrating the series term by term.
