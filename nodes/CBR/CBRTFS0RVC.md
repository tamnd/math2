---
tag: CBRTFS0RVC
kind: statement
role: theorem
name: Entropic uncertainty principle
msc: ["42A38", "94A17", "81S07"]
uses: [DPVM34ADZV, SASP14MA1Z, FFM7Y61KRT, HPZHRZ0502]
about: [DPVM34ADZV]
sources:
  - url: https://en.wikipedia.org/wiki/Entropic_uncertainty
same_as:
  wikidata: Q5380783
  wikipedia: Entropic uncertainty
---

## Statement

Let $f \in L^2(\R)$ with $\norm{f}_2 = 1$, and let $\hat f$ be its Fourier transform on $L^2(\R)$, normalized so that $\hat f(\xi) = \int_\R f(x) e^{-2\pi i x \xi}\, dx$ for integrable $f$.
For a probability density $p$ on $\R$, let $H(p) = -\int_\R p(x) \log p(x)\, dx$ be its differential entropy, with the natural logarithm.
Suppose that the integrals defining $H(\abs{f}^2)$ and $H(\abs{\hat f}^2)$ converge absolutely.
Then
$$H(\abs{f}^2) + H(\abs{\hat f}^2) \ge \log \frac{e}{2}.$$
Equality holds when $f$ is a Gaussian $f(x) = (2a)^{1/4} e^{-\pi a x^2}$ with $a > 0$.

## Remarks

By the [[Plancherel theorem|HPZHRZ0502]], $\abs{\hat f}^2$ is also a probability density, so both entropies make sense.
The proof differentiates the [[Babenko–Beckner inequality|FFM7Y61KRT]] $\norm{\hat f}_q \le A_p \norm{f}_p$ with respect to $p$ at $p = 2$.
At $p = 2$ both sides are equal to $1$, so the derivative of the difference has a sign, and that sign is the entropy inequality.
I. I. Hirschman proved a weaker constant and conjectured this one; W. Beckner's sharp constant in the Hausdorff–Young inequality gave the conjecture.

On $\R^n$ the bound is $n \log \frac{e}{2}$.

The inequality implies the Heisenberg inequality.
For a density $p$ with variance $\sigma^2$, the entropy satisfies $H(p) \le \frac12 \log(2\pi e \sigma^2)$, with equality for normal densities.
Inserting this for $\abs{f}^2$ and $\abs{\hat f}^2$ gives $\sigma_x^2 \sigma_\xi^2 \ge 1/(16\pi^2)$.

## Explanations

### L1 human

Entropy measures how spread out a probability distribution is.
The theorem says that the spread of $\abs{f}^2$ and the spread of $\abs{\hat f}^2$, measured by entropy, cannot both be small.
Their sum is at least the number $\log(e/2)$, and Gaussians reach this bound.

### L2 human

Entropy is a finer measure of spread than variance: a density can have infinite variance and still finite entropy.
So this form of the uncertainty principle is stronger than the Heisenberg inequality, which it implies.
It is the model for entropic uncertainty relations in quantum information, where the Fourier transform is replaced by a pair of measurements in two bases.
