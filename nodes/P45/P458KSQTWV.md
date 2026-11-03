---
tag: P458KSQTWV
kind: concept
name: BSSN formalism
msc: ["83C05", "83-08", "65M06"]
sources:
  - url: https://en.wikipedia.org/wiki/BSSN_formalism
same_as:
  wikidata: Q3748129
  wikipedia: BSSN formalism
---

## Summary

The BSSN formalism, named after Baumgarte, Shapiro, Shibata and Nakamura, is a reformulation of the evolution equations of the [[ADM formalism|CFAFAPV7HB]].
It splits the spatial metric into a conformal factor and a conformal metric of unit determinant.
It splits the extrinsic curvature into its trace and trace-free part, and it adds three conformal connection functions as new variables.
Unlike the ADM evolution equations, the resulting system is strongly hyperbolic for common gauge choices, and it gives stable long-time simulations.
Together with the moving puncture gauge, it is one of the standard methods of [[numerical relativity|HQ2CRGCNCG]] for black hole binaries.

## Explanations

### L1 human

The Einstein equations can be written in many equivalent ways, but on a computer some ways blow up quickly because of small errors.
The BSSN variables rearrange the same information so that the errors stay under control.
The size of space at each point is stored in one variable, its shape in another, and the rate of expansion in a third.
With this bookkeeping, computer simulations of two black holes that orbit and merge became possible.
