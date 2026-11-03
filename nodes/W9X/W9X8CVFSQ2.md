---
tag: W9X8CVFSQ2
kind: concept
name: Hill equation
msc: [92C45, 92C40]
sources:
  - url: https://en.wikipedia.org/wiki/Hill_equation_(biochemistry)
same_as:
  wikidata: Q2554020
  wikipedia: Hill equation (biochemistry)
---

## Summary

The Hill equation gives the fraction of a receptor or protein that is bound by a ligand as a sigmoid function of the ligand concentration.
It was proposed by Archibald Hill in 1910 to describe the binding of oxygen to haemoglobin.
Its exponent, the Hill coefficient, measures cooperativity: values above $1$ mean that binding of one ligand makes further binding easier.
Hill functions are the standard way to write activation and repression in models of gene regulation.

## Explanations

### L1 human

A protein with several binding sites can be partly or fully loaded with ligand.
If the sites help each other, the protein switches from mostly empty to mostly full over a narrow range of concentration.
The Hill equation captures this with one number $n$: for $n = 1$ the curve rises gently, and for large $n$ it looks almost like a step.
For example, with $n = 4$ and half-saturation at $1$, the bound fraction is about $0.06$ at concentration $0.5$ and about $0.94$ at concentration $2$.
