---
tag: TJPNYW7J8E
kind: concept
name: Catastrophic cancellation
msc: [65G50]
sources:
  - url: https://en.wikipedia.org/wiki/Catastrophic_cancellation
same_as:
  wikidata: Q104589774
  wikipedia: Catastrophic cancellation
---

## Summary

Catastrophic cancellation is the large loss of relative accuracy when one subtracts two nearly equal numbers that are only known approximately.
The leading digits cancel, and what is left is dominated by the errors of the inputs.
The subtraction itself is often exact in [[floating-point arithmetic|RTKRSC3KPH]]; the damage comes from earlier [[round-off errors|CPN6SD3BTV]].
It is the most common cause of numerically unstable formulas, and it is avoided by rewriting formulas, for example $\sqrt{x+1} - \sqrt{x} = 1/(\sqrt{x+1} + \sqrt{x})$.

## Explanations

### L1 human

Suppose two lengths are measured as $1.2341$ m and $1.2259$ m, each to the nearest tenth of a millimetre.
Their difference $0.0082$ m has only two significant digits, although each length had five.
If one first rounds both lengths to three digits, both become $1.23$ and the difference becomes $0$, a $100\%$ error.
Subtracting close numbers throws away the digits that agree and keeps the digits that carry the error.
