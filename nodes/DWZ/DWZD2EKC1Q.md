---
tag: DWZD2EKC1Q
kind: example
name: Laplace transform of the error function
msc: [44A10, 33B20]
illustrates: [0V49JEZW06]
uses: [05XT5AVJBK, 1EG3DWPNZN, 0V3FZMVB4K, RDFYHS2Q55]
sources:
  - url: https://en.wikipedia.org/wiki/Error_function
---

## Example

Let $\operatorname{erf}(x) = \frac{2}{\sqrt{\pi}} \int_0^x e^{-u^2}\, du$ be the [[error function|1EG3DWPNZN]].
The [[Laplace transform|05XT5AVJBK]] of $f(t) = \operatorname{erf}(\sqrt{t})$ is
$$\mathcal{L}\{\operatorname{erf}(\sqrt{t})\}(s) = \frac{1}{s \sqrt{s + 1}} \quad (s > 0).$$
Check: $f(0) = 0$ and, for $t > 0$, $f'(t) = \frac{2}{\sqrt{\pi}} e^{-t} \cdot \frac{1}{2\sqrt{t}} = \frac{e^{-t}}{\sqrt{\pi t}}$.
By the [[transform of a power|RDFYHS2Q55]] with $\alpha = -1/2$ and the shift $s \mapsto s + 1$ caused by the factor $e^{-t}$,
$$\mathcal{L}\{f'\}(s) = \frac{1}{\sqrt{\pi}} \cdot \frac{\Gamma(1/2)}{\sqrt{s + 1}} = \frac{1}{\sqrt{s + 1}},$$
using $\Gamma(1/2) = \sqrt{\pi}$ for the [[gamma function|0V3FZMVB4K]].
Since $f(t) = \int_0^t f'(u)\, du$, its transform is that of $f'$ divided by $s$, which gives $1/(s\sqrt{s + 1})$.
The formula extends to $\operatorname{Re} s > 0$ with the principal square root.

## Explanations

### L1 human

The error function measures the area under the bell curve, and it appears in heat flow and probability.
Its transform, with argument $\sqrt{t}$, is a simple algebraic expression in $s$.
This is why Laplace transforms solve heat conduction problems: the hard function erf on the time side becomes a square root on the transform side.
