---
tag: NJ3APQ8BHH
kind: concept
name: Residue field
msc: [13H99, 13B30]
specializes: [04C5ZBG1WT]
sources:
  - url: https://en.wikipedia.org/wiki/Residue_field
same_as:
  wikidata: Q7315530
  wikipedia: Residue field
---

## Summary

The residue field of a [[local ring|MZ02BKPHJA]] $R$ with maximal ideal $\mathfrak m$ is the [[quotient ring|0076HWHGHQ]] $R/\mathfrak m$, which is a [[field|04C5ZBG1WT]].
More generally, the residue field of any [[commutative ring|0310REJJY8]] at a [[prime ideal|00MHHZ9SNE]] $\mathfrak p$ is the residue field of the [[localization|X6JD4AG973]] $R_{\mathfrak p}$.
It is the field of "values at a point", and many invariants of local rings, such as the [[cotangent space|Z1CGB483J6]], are vector spaces over it.

## Explanations

### L1 human

Reducing modulo the maximal ideal throws away everything except the "value at the point".
For the ring $\Z_{(p)}$ of fractions with denominators prime to $p$, reducing modulo $p$ gives the field $\Z/p\Z$ with $p$ elements.
For the power series ring $k[\![x]\!]$, it keeps only the constant term, so the residue field is $k$.
The [[definition|8ST7CTZ2DE]] gives the construction.
