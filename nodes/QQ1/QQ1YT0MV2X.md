---
tag: QQ1YT0MV2X
kind: concept
name: Method of matched asymptotic expansions
msc: ["34E05", "34E15"]
sources:
  - url: https://en.wikipedia.org/wiki/Method_of_matched_asymptotic_expansions
same_as:
  wikidata: Q17098224
  wikipedia: Method of matched asymptotic expansions
---

## Summary

The method of matched asymptotic expansions builds approximate solutions of [[singularly perturbed|G6J21TGRMM]] problems.
It uses one expansion away from the thin layers where the solution changes fast, and another expansion inside each layer, in a stretched variable.
The two are joined by requiring that they agree in an intermediate region.
It is a standard tool for [[boundary layers|YCFPD0GE5G]] in fluid dynamics and for many problems in applied mathematics.

## Explanations

### L1 human

Imagine a solution that is smooth almost everywhere but has a steep cliff near one end.
One formula describes the flat part well, and a zoomed-in formula describes the cliff well.
Matching makes the two formulas agree where the cliff meets the flat part.
Adding them and removing the shared part gives one formula that is good everywhere.
For $\varepsilon y'' + y' + y = 0$, $y(0) = 0$, $y(1) = 1$, this gives $y \approx e^{1 - x} - e^{1 - x/\varepsilon}$.
