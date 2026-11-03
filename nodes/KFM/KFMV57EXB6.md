---
tag: KFMV57EXB6
kind: concept
name: Patch test
msc: [74S05, 65N30]
sources:
  - url: https://en.wikipedia.org/wiki/Patch_test_(finite_elements)
same_as:
  wikidata: Q2056643
  wikipedia: Patch test (finite elements)
---

## Summary

The patch test is a numerical check of a finite element: a small patch of elements must reproduce exactly any displacement field of constant strain.
Bruce Irons introduced it for elements whose trial functions are not continuous across element boundaries, where the usual convergence theory does not apply.
Passing the test is a practical check of consistency, and failing it signals that the element cannot converge to the right solution in general.
It is used in the [[finite element method in structural mechanics|CGYM9VZC39]] to validate new elements.

## Explanations

### L1 human

As a mesh is refined, the strain inside each tiny element is nearly constant.
So a good element must at least get constant strain exactly right.
The patch test takes a few elements, often with distorted shapes, prescribes boundary displacements that come from a uniform stretch, and checks the computed answer.
If the computed strain is the same uniform stretch everywhere in the patch, the element passes.
Standard linear triangles, for example, pass, because a linear displacement field lies in their trial space.
