---
tag: Q8CTDCZH01
kind: concept
name: Minimal model program
msc: ["14E30"]
sources:
  - url: https://en.wikipedia.org/wiki/Minimal_model_program
same_as:
  wikidata: Q6865325
  wikipedia: Minimal model program
---

## Summary

The minimal model program, or MMP, is a strategy for finding a simplest variety in each birational class of projective varieties.
It modifies a variety step by step, by contractions and flips, so as to make the [[canonical bundle|W05VYY4HBR]] [[nef|RZ66X0NAM5]].
It ends either with a minimal model or with a Mori fibre space, a fibration whose general fibres are Fano varieties.
For surfaces it is the classical process of contracting $(-1)$-curves; in dimension $3$ it was carried out by Mori and others.

## Explanations

### L1 human

Many different varieties have the same function field, because one can always blow up points to make a variety more complicated.
The program runs this backwards: it looks for curves on which the canonical bundle is negative and removes them.
For a surface, it repeatedly contracts curves that look like a projective line with self-intersection $-1$.
When no such curves are left, either the canonical bundle is nef and the surface is minimal, or the surface is $\mathbb{P}^2$ or fibred in projective lines over a curve.
