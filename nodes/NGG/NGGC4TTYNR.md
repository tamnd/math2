---
tag: NGGC4TTYNR
kind: concept
name: Inverse tangent integral
msc: ["33B30", "33E20"]
sources:
  - url: https://en.wikipedia.org/wiki/Inverse_tangent_integral
same_as:
  wikidata: Q107524938
  wikipedia: Inverse tangent integral
---

## Summary

The inverse tangent integral $\operatorname{Ti}_2$ is the function $x \mapsto \int_0^x \frac{\arctan t}{t} \, dt$.
It is the analogue of the [[dilogarithm|G0X0NWSDB7]] built from the [[arctangent|0CE768XNVP]] instead of the logarithm.
For real $x$ it equals the imaginary part of $\operatorname{Li}_2(ix)$.
Its value at $1$ is Catalan's constant.

## Explanations

### L1 human

The dilogarithm can be written as an integral of $-\log(1 - t)/t$.
Replace the logarithm by the arctangent and you get the inverse tangent integral.
Its power series is $x - \frac{x^3}{9} + \frac{x^5}{25} - \cdots$, with odd powers and squared odd numbers in the denominators.
At $x = 1$ this gives $1 - \frac19 + \frac1{25} - \cdots = G \approx 0.91597$, Catalan's constant.
