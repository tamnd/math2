---
tag: PGXZJ2YWVJ
kind: concept
name: MacCormack method
msc: [65M06, 35L65]
specializes: [X7HYEBA5SA]
sources:
  - url: https://en.wikipedia.org/wiki/MacCormack_method
same_as:
  wikidata: Q6721779
  wikipedia: MacCormack method
---

## Summary

The MacCormack method is an explicit second-order [[finite difference|X7HYEBA5SA]] scheme for hyperbolic [[conservation laws|8RA7AMWSAF]].
It makes a predictor step with forward differences and then a corrector step with backward differences.
For linear equations it coincides with the [[Lax–Wendroff method|YHZ9BCNDRZ]].
For nonlinear systems it is simpler to program, because it needs no Jacobian of the flux.
It was introduced for problems of computational fluid dynamics, such as compressible flow.

## Explanations

### L1 human

The method first makes a rough prediction of the next time level, looking one grid point ahead.
It then corrects this prediction, looking one grid point back, and averages the result with the old value.
Alternating the two directions cancels the leading errors of each one-sided difference.
The result is second-order accurate, like a centred scheme, while each step uses only simple one-sided differences.
