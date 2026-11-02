---
tag: 88GQ3KHQ3Q
kind: definition
name: Meixner polynomials
msc: [33C45, 42C05]
defines: CEC3DESCFT
uses: [YZHM3HSM0F, 463X5V31D9]
sources:
  - url: https://en.wikipedia.org/wiki/Meixner_polynomials
---

## Definition

Let $\beta > 0$ and $0 < c < 1$ be real numbers, and let $n \ge 0$ be an integer.
Write $(a)_k$ for the [[Pochhammer symbol|YZHM3HSM0F]].
The *Meixner polynomial* of degree $n$ is
$$M_n(x; \beta, c) = \sum_{k=0}^{n} \frac{(-n)_k \, (-x)_k}{(\beta)_k \, k!} \left( 1 - \frac{1}{c} \right)^k,$$
that is, $M_n(x; \beta, c) = {}_2F_1\left( -n, -x; \beta; 1 - \frac{1}{c} \right)$, a terminating [[hypergeometric function|463X5V31D9]].

## Remarks

They are orthogonal on the nonnegative integers:
$$\sum_{x=0}^{\infty} \frac{(\beta)_x}{x!} c^x M_m(x; \beta, c) M_n(x; \beta, c) = \frac{c^{-n} \, n!}{(\beta)_n (1 - c)^\beta} \delta_{mn}.$$
Example: $M_1(x; \beta, c) = 1 - \frac{(1 - c) x}{\beta c}$.
Check: the weights sum to $(1 - c)^{-\beta}$, and their mean value of $x$ is $\frac{\beta c}{1 - c}$, so the weighted sum of $M_1$ is $(1 - c)^{-\beta} (1 - 1) = 0$.
Non-example: for $c \ge 1$ the clause $0 < c < 1$ fails, and the weights $\frac{(\beta)_x}{x!} c^x$ do not have a finite sum, so the orthogonality relation has no meaning.
Limit to Laguerre: $\lim_{c \to 1} M_n\left( \frac{x}{1 - c}; \alpha + 1, c \right) = \frac{L_n^{(\alpha)}(x)}{L_n^{(\alpha)}(0)}$.
