---
tag: PJNAENVPFG
kind: definition
name: Gompertz–Makeham law of mortality
msc: [91G05, 91D20, 62P05]
defines: AVM4TXEM3W
uses: [Y959NKQ3XW, QTM1HZM53Q, 0J0FCWV32D]
sources:
  - url: https://en.wikipedia.org/wiki/Gompertz–Makeham_law_of_mortality
---

## Definition

Let $\alpha > 0$, $\beta > 0$ and $\lambda \ge 0$ be real numbers.
A nonnegative random lifetime $T$ follows the *Gompertz–Makeham law of mortality* with these parameters if its [[hazard function|Y959NKQ3XW]] is
$$\mu(x) = \alpha e^{\beta x} + \lambda \qquad (x \ge 0).$$
When $\lambda = 0$ this is the *Gompertz law*.

## Remarks

Integrating the hazard gives the [[survival function|QTM1HZM53Q]]
$$S(x) = P(T > x) = \exp\left(-\lambda x - \frac{\alpha}{\beta}\left(e^{\beta x} - 1\right)\right).$$
Check: $-\frac{d}{dx} \ln S(x) = \lambda + \alpha e^{\beta x} = \mu(x)$ and $S(0) = 1$.
Example: $\alpha = 10^{-4}$, $\beta = 0.085$, $\lambda = 5 \cdot 10^{-4}$ gives a hazard whose ageing part doubles every $\ln 2 / 0.085 \approx 8.2$ years.
Non-example: the constant hazard $\mu(x) = \lambda$ of an exponential lifetime is not of this form, since it needs $\alpha = 0$, which clause $\alpha > 0$ excludes.
The ageing part grows by the factor $e^\beta$ per year of age.
