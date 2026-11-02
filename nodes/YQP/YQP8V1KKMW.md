---
tag: YQP8V1KKMW
kind: concept
name: Hahn series
msc: ["13F25", "12J10"]
sources:
  - url: https://en.wikipedia.org/wiki/Hahn_series
same_as:
  wikidata: Q5638887
  wikipedia: Hahn series
---

## Summary

A Hahn series is a formal sum $\sum_\gamma a_\gamma t^\gamma$ with coefficients in a field and exponents in a [[linearly ordered group|P2E8BNYC7B]].
Its set of exponents must be [[well-ordered|01CGSJ0GNQ]].
Hahn series generalise [[formal power series|033WGN00BF]] and [[formal Laurent series|YZWYF7DXTW]] to exponents that may be fractions, reals, or elements of any ordered abelian group.
They form a field with a natural [[valuation|B85T5VKR3M]], and these fields are a main source of examples of valued and ordered fields.

## Explanations

### L1 human

A Laurent series in $t$ uses integer powers, starting from some lowest power and going up.
A Hahn series allows any exponents from an ordered group, like $t^{1/2}$ or $t^{\sqrt{2}}$, as long as each nonempty set of exponents used has a smallest element.
For example $t^{1/2} + t^{2/3} + t^{3/4} + \cdots$ is a Hahn series with rational exponents.
The rule about smallest elements is exactly what makes products of two such series well defined.
