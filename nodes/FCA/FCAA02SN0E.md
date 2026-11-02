---
tag: FCAA02SN0E
kind: statement
role: theorem
name: Nikodym convergence theorem
msc: [28A33, 28A10]
uses: [N4KDT83V3S, NY6TYHRGMS, D7KB9HFCGZ]
about: [NY6TYHRGMS]
sources:
  - url: https://en.wikipedia.org/wiki/Vitali–Hahn–Saks_theorem
---

## Statement

Let $(X, \Sigma)$ be a [[measurable space|N4KDT83V3S]] and let $(\mu_n)_{n \ge 1}$ be a sequence of [[complex measures|NY6TYHRGMS]] on $\Sigma$.
Assume that for every $E \in \Sigma$ the limit $\mu(E) = \lim_{n \to \infty} \mu_n(E)$ exists in $\C$.
Then:

1. The $\mu_n$ are uniformly countably additive: for every sequence $E_1 \supseteq E_2 \supseteq \cdots$ in $\Sigma$ with $\bigcap_k E_k = \emptyset$, one has $\sup_n \abs{\mu_n(E_k)} \to 0$ as $k \to \infty$.
2. The set function $\mu$ is [[countably additive|D7KB9HFCGZ]], so it is a complex measure on $\Sigma$.

## Remarks

One proof reduces to the Vitali–Hahn–Saks theorem.
Put $\lambda = \sum_n 2^{-n} \abs{\mu_n} / (1 + \abs{\mu_n}(X))$, a finite measure.
Each $\mu_n$ is absolutely continuous with respect to $\lambda$, and the Vitali–Hahn–Saks theorem gives the conclusion.

Example: let $f_n$ be integrable functions on a measure space with $\int_E f_n$ convergent for every measurable $E$.
Then the limit $E \mapsto \lim_n \int_E f_n$ is again countably additive.

## Explanations

### L1 human

If a sequence of measures has a limit on each measurable set, the limit is a measure too.
This is surprising, because pointwise limits usually lose properties such as countable additivity.

### L2 human

The theorem is often stated together with the Nikodym boundedness theorem, which says that a family of complex measures bounded on each set is uniformly bounded.
Both are measure-theoretic forms of the uniform boundedness principle.
They are basic tools in the study of weak convergence in spaces of measures and in $L^1$.
