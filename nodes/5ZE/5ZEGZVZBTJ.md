---
tag: 5ZEGZVZBTJ
kind: definition
name: Bayes factor
msc: [62F15, 62F03]
defines: NSBYE143KS
uses: [05FSTXM92W, 00NBBSXRQS, 0NM6E9VW04]
sources:
  - url: https://en.wikipedia.org/wiki/Bayes_factor
    locator: Definition
---

## Definition

Let $M_0$ and $M_1$ be two models for data $x$.
For $i = 0, 1$, model $M_i$ has a parameter $\theta_i \in \Theta_i$, a density or mass function $f_i(x \mid \theta_i)$ and a proper [[prior|00NBBSXRQS]] $\pi_i$ on $\Theta_i$.
The *marginal likelihood* of $M_i$ is
$$m_i(x) = \int_{\Theta_i} f_i(x \mid \theta_i) \, \pi_i(d\theta_i).$$
If $m_0(x) > 0$, the *Bayes factor* of $M_1$ against $M_0$ is
$$B_{10}(x) = \frac{m_1(x)}{m_0(x)}.$$

## Remarks

By [[Bayes' theorem|0NM6E9VW04]], with prior model probabilities $P(M_0), P(M_1) > 0$, the posterior odds are
$$\frac{P(M_1 \mid x)}{P(M_0 \mid x)} = B_{10}(x) \cdot \frac{P(M_1)}{P(M_0)}.$$
If both models are simple, that is each $\Theta_i$ is a single point, then $B_{10}$ is the [[likelihood|05FSTXM92W]] ratio.
Example: let $M_0$ say that a coin is fair and $M_1$ that its chance $p$ of heads is uniform on $[0, 1]$, and observe two heads in two tosses.
Then $m_0 = 1/4$ and $m_1 = \int_0^1 p^2 \, dp = 1/3$, so $B_{10} = 4/3$.
Non-example: with an improper prior $\pi_1$, the integral $m_1(x)$ is defined only up to an arbitrary constant factor, so the ratio is not a well-defined Bayes factor.
