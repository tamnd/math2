---
tag: WS6GCG3YF8
kind: concept
name: Propagation of uncertainty
msc: [65G99, 62P99]
sources:
  - url: https://en.wikipedia.org/wiki/Propagation_of_uncertainty
same_as:
  wikidata: Q1364905
  wikipedia: Propagation of uncertainty
---

## Summary

Propagation of uncertainty computes how the uncertainties of input quantities carry over to a quantity computed from them.
Inputs are modelled as random variables with known means, [[variances|0477R9PYAE]] and [[covariances|0KBFAWYRTE]].
For a smooth function one usually linearizes it at the means.
The output covariance is then $J \Sigma J^{T}$, where $J$ is the [[Jacobian matrix|047NDTEPCV]] and $\Sigma$ the input covariance matrix.
It is the standard tool for error bars in experimental science; for guaranteed bounds one uses [[interval arithmetic|QPKKTE1ZY0]] instead.

## Explanations

### L1 human

Every measurement comes with an uncertainty, such as $2.00 \pm 0.01$ m.
If one computes an area or a speed from measured values, the result is uncertain too, and one wants to know by how much.
For a sum of two independent measurements, the standard deviations combine like the sides of a right triangle: $\sigma^2 = \sigma_1^2 + \sigma_2^2$.
For a product, the relative uncertainties combine in the same way.
For example, a rectangle measured as $2.00 \pm 0.02$ by $3.00 \pm 0.03$ has area $6.00$ with relative uncertainty about $\sqrt{0.01^2 + 0.01^2} \approx 1.4\%$, so about $\pm 0.08$.
