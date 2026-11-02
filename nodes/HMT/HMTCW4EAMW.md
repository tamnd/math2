---
tag: HMTCW4EAMW
kind: definition
name: Inversion of rational transforms by partial fractions
msc: [44A10, 26C15]
defines: 1P6TBEPHQH
uses: [0WCZH4AFMT, 030VFEREKG, 05XT5AVJBK, 0JRW4X1MDC, CD35MSBNE7]
sources:
  - url: https://en.wikipedia.org/wiki/Partial_fraction_decomposition
---

## Definition

Let $P$ and $Q$ be complex polynomials with $Q \ne 0$ and $\deg P < \deg Q$, and let $F = P/Q$ be the [[rational function|0WCZH4AFMT]].
Let $a_1, \ldots, a_r$ be the distinct roots of $Q$, with multiplicities $m_1, \ldots, m_r$.
The [[partial fraction decomposition|030VFEREKG]] writes $F$ uniquely as
$$F(s) = \sum_{j=1}^{r} \sum_{k=1}^{m_j} \frac{c_{j k}}{(s - a_j)^k}$$
with complex constants $c_{j k}$.
*Inversion by partial fractions* is the computation of the [[inverse Laplace transform|0JRW4X1MDC]] of $F$ as
$$f(t) = \sum_{j=1}^{r} \sum_{k=1}^{m_j} c_{j k} \, \frac{t^{k-1}}{(k-1)!} \, e^{a_j t}, \qquad t \ge 0.$$
It rests on the identity $\mathcal{L}\{t^{k-1} e^{a t}/(k-1)!\}(s) = 1/(s - a)^k$ for $\operatorname{Re} s > \operatorname{Re} a$.

## Remarks

The identity follows from $\mathcal{L}\{t^{k-1}\}(s) = (k-1)!/s^k$ and the [[frequency shift theorem|CD35MSBNE7]].
Example: $F(s) = \frac{s + 3}{(s + 1)(s + 2)} = \frac{2}{s + 1} - \frac{1}{s + 2}$, so $f(t) = 2 e^{-t} - e^{-2t}$; check $f(0) = 1 = \lim_{s \to \infty} s F(s)$.
Non-example: $F(s) = s/(s + 1)$ has $\deg P = \deg Q$, so the method does not apply as stated.
Indeed $F(s) \to 1$ as $s \to \infty$, while the Laplace transform of a function [[tends to $0$ at infinity|N2JFN9VHD9]]; here $F = 1 - 1/(s+1)$ is the transform of the distribution $\delta - e^{-t}$.
For real $P$ and $Q$, the complex roots come in conjugate pairs, and the two terms of a simple pair combine into $e^{\alpha t}(A \cos \beta t + B \sin \beta t)$.
The coefficients of simple roots are quickly found with the [[Heaviside cover-up method|SRQ5P3077W]].
