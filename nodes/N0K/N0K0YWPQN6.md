---
tag: N0K0YWPQN6
kind: statement
role: theorem
name: Vitali–Hahn–Saks theorem
msc: [28A33, 28A10]
uses: [PR11BZQQPG, 63Z1Q4FS23, NY6TYHRGMS, P0P21KDV6E]
about: [P0P21KDV6E]
sources:
  - url: https://en.wikipedia.org/wiki/Vitali–Hahn–Saks_theorem
same_as:
  wikidata: Q7936914
  wikipedia: Vitali–Hahn–Saks theorem
---

## Statement

Let $(X, \Sigma, \lambda)$ be a measure space with $\lambda$ a [[finite measure|63Z1Q4FS23]].
Let $(\mu_n)_{n \ge 1}$ be a sequence of [[complex measures|NY6TYHRGMS]] on $\Sigma$, each [[absolutely continuous|P0P21KDV6E]] with respect to $\lambda$.
Assume that for every $E \in \Sigma$ the limit $\mu(E) = \lim_{n \to \infty} \mu_n(E)$ exists in $\C$.
Then:

1. The $\mu_n$ are uniformly absolutely continuous with respect to $\lambda$: for every $\varepsilon > 0$ there is $\delta > 0$ such that $\lambda(E) < \delta$ implies $\abs{\mu_n(E)} < \varepsilon$ for all $n$.
2. The set function $\mu$ is a complex measure on $\Sigma$, and it is absolutely continuous with respect to $\lambda$.

## Remarks

A standard proof uses the Baire category theorem.
The measurable sets modulo $\lambda$-null sets form a complete metric space with distance $d(E, F) = \lambda(E \,\triangle\, F)$.
Each $\mu_n$ is continuous on this space, and a Baire argument on the sets where $\abs{\mu_n(E) - \mu_m(E)} \le \varepsilon$ for all $m, n \ge N$ gives the uniform bound.

Example: let $f_n \in L^1(\lambda)$ with $\int_E f_n \, d\lambda$ convergent for every $E$.
The theorem applied to $\mu_n = f_n \lambda$ shows that $(f_n)$ is uniformly integrable, which is a key step in the Dunford–Pettis theorem.

The hypothesis asks for convergence on every set of $\Sigma$.
Convergence on a generating family of sets, such as intervals, is not enough in general.

## Explanations

### L1 human

If a sequence of measures converges on every single set, then the limit is again a measure.
Moreover, the measures cannot concentrate mass on smaller and smaller sets at different speeds: they are controlled uniformly by the reference measure.

### L2 human

The theorem is the measure version of the uniform boundedness principle: pointwise convergence on a complete space forces a uniform estimate.
It is used to characterise weakly convergent and weakly compact sets in $L^1$.
The Nikodym convergence theorem is a version that needs no reference measure $\lambda$.
