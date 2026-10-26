---
tag: 03GP7KMBYM
kind: definition
name: Absolutely convergent improper integral
msc: [40A10]
defines: 0F9VKJPWCA
uses: [0VCTBJMEJF]
sources:
  - url: https://en.wikipedia.org/wiki/Improper_integral
    locator: Improper Riemann integrals and Lebesgue integrals
---

## Definition

Let $f \colon [a, \infty) \to \mathbb{R}$ be Riemann integrable on $[a, b]$ for each $b > a$.
The [[improper integral|0VCTBJMEJF]] $\int_a^\infty f(x) \, dx$ converges absolutely if $\int_a^\infty |f(x)| \, dx$ converges.

## Remarks

An absolutely convergent improper integral converges. The proof uses $0 \le f + |f| \le 2|f|$ and the [[comparison test|0FR1BDKK10]].
The converse fails. The [[Dirichlet integral|0GZNSHMG4Q]] $\int_0^\infty \frac{\sin x}{x} \, dx$ converges, but not absolutely.
A function on $[a, \infty)$ whose improper integral converges absolutely is Lebesgue integrable there. The two integrals agree.

## Explanations

### L1 human

An improper integral converges absolutely when the area between the graph and the axis is finite, with all parts counted as positive.
This is the analogue of absolute convergence of series.
