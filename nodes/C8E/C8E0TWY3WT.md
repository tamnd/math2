---
tag: C8E0TWY3WT
kind: concept
name: Liouville's equation
msc: [35J61, 53A05]
specializes: [RCNY89A4NY]
sources:
  - url: https://en.wikipedia.org/wiki/Liouville%27s_equation
same_as:
  wikidata: Q2184037
  wikipedia: Liouville's equation
---

## Summary

Liouville's equation is the [[semilinear|RCNY89A4NY]] elliptic equation $\Delta u + K e^{2u} = 0$ for a function $u$ of two real variables, with $K$ a constant.
It says that the metric $e^{2u}(dx^2 + dy^2)$ has constant [[Gaussian curvature|SQVQ5DQT6W]] $K$.
Joseph Liouville found its general local solution in terms of holomorphic functions.
Equations of this exponential type also appear in models of self-gravitating gases and of vortices.

## Explanations

### L1 human

Take a flat piece of the plane and rescale lengths by a factor $e^{u}$ that changes from point to point.
The rescaled surface can look curved, like a piece of a sphere, and its curvature depends on how $u$ varies.
Liouville's equation asks for the rescalings that give the same curvature everywhere.
For example, $u = \log\big(2/(1 + x^2 + y^2)\big)$ turns the plane into the round sphere of radius one with a point removed, which has curvature $1$.
