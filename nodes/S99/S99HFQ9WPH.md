---
tag: S99HFQ9WPH
kind: definition
name: Conjugate prior
msc: [62F15]
defines: EHY450Q5CW
uses: [Q0DXKAQXE1, 00NBBSXRQS, 0KJ7ZS8AJA, 05FSTXM92W, 0PP5ZAJPP7]
sources:
  - url: https://en.wikipedia.org/wiki/Conjugate_prior
---

## Definition

Let $\set{f(\cdot \mid \theta) : \theta \in \Theta}$ be a [[parametric model|Q0DXKAQXE1]] given by densities or mass functions, with [[likelihood|05FSTXM92W]] $L(\theta \mid x) = f(x \mid \theta)$.
Let $\mathcal{C}$ be a family of probability distributions on $\Theta$.
The family $\mathcal{C}$ is *conjugate* for the model if the following holds for every [[prior|00NBBSXRQS]] $\pi \in \mathcal{C}$.
For every observation $x$ with $0 < \int_\Theta f(x \mid \theta) \, \pi(d\theta) < \infty$, the [[posterior|0KJ7ZS8AJA]] $\pi(\cdot \mid x)$ belongs to $\mathcal{C}$.
A *conjugate prior* is a member of such a family, usually a family indexed by finitely many hyperparameters.

## Remarks

Example: for $k$ successes in $n$ Bernoulli trials with chance $p \in (0, 1)$, the [[beta distributions|0PP5ZAJPP7]] form a conjugate family.
Indeed, with prior density proportional to $p^{a - 1}(1 - p)^{b - 1}$, the posterior density is proportional to $p^{a + k - 1}(1 - p)^{b + n - k - 1}$, so the posterior is $\mathrm{Beta}(a + k, b + n - k)$.
Non-example: for a Poisson observation $x$ with rate $\lambda > 0$, the log-normal family is not conjugate.
The posterior density is proportional to $\lambda^{x} e^{-\lambda}$ times a log-normal density, and the factor $e^{-\lambda}$ cannot be written in log-normal form.
The gamma family is conjugate for the Poisson rate: a $\mathrm{Gamma}(\alpha, \beta)$ prior, with rate $\beta$, gives the posterior $\mathrm{Gamma}(\alpha + x, \beta + 1)$.
The family of all distributions on $\Theta$ is conjugate, because every posterior is a distribution on $\Theta$; so the notion is useful only for small families.
