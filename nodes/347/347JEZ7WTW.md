---
tag: 347JEZ7WTW
kind: definition
name: Slowly varying function
msc: [26A12, "40E05"]
defines: EHJ7D5CRZS
uses: [YYNCJSR0PJ]
sources:
  - url: https://en.wikipedia.org/wiki/Slowly_varying_function
---

## Definition

Let $L \colon (0, \infty) \to (0, \infty)$ be a [[measurable function|YYNCJSR0PJ]].
The function $L$ is *slowly varying* (at infinity) if for every real $a > 0$
$$\lim_{x \to \infty} \frac{L(ax)}{L(x)} = 1.$$

## Remarks

Example: $L(x) = \log(e + x)$ is slowly varying.
For fixed $a > 0$ and large $x$, $\log(e + ax) = \log x + \log a + o(1)$ and $\log(e + x) = \log x + o(1)$, so the ratio tends to $1$.
Every positive measurable function with a positive finite limit at infinity is slowly varying.

Non-example: $L(x) = x^\rho$ with $\rho \ne 0$ is not slowly varying, because $L(ax)/L(x) = a^\rho \ne 1$ for $a \ne 1$.

The uniform convergence theorem says that the limit is uniform for $a$ in each compact subset of $(0, \infty)$.
In the language of regular variation, slowly varying functions are the regularly varying functions of index $0$.
