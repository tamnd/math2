---
tag: 5CSCTKRTB2
kind: definition
name: Regular variation
msc: [26A12, "40E05"]
defines: MFM9ZXWMHA
uses: [YYNCJSR0PJ, EHJ7D5CRZS]
sources:
  - url: https://en.wikipedia.org/wiki/Slowly_varying_function
---

## Definition

Let $f \colon (0, \infty) \to (0, \infty)$ be a [[measurable function|YYNCJSR0PJ]].
The function $f$ is *regularly varying* (at infinity) if for every real $a > 0$ the limit
$$g(a) = \lim_{x \to \infty} \frac{f(ax)}{f(x)}$$
exists and satisfies $0 < g(a) < \infty$.

## Remarks

For such $f$ there is a real number $\rho$ with $g(a) = a^\rho$ for all $a > 0$; this is Karamata's characterization theorem.
The number $\rho$ is the *index* of $f$.
Equivalently, $f(x) = x^\rho L(x)$ where $L$ is a [[slowly varying function|EHJ7D5CRZS]].
The regularly varying functions of index $0$ are exactly the slowly varying functions.

Example: $f(x) = x^2 \log(e + x)$ is regularly varying of index $2$.
Indeed $f(ax)/f(x) = a^2 \cdot \log(e + ax)/\log(e + x)$, and the second factor tends to $1$.

Non-example: $f(x) = e^x$ is not regularly varying.
For $a = 2$ the ratio $f(2x)/f(x) = e^x$ tends to $\infty$, so the limit is not finite.
