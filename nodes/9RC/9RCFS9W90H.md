---
tag: 9RCFS9W90H
kind: concept
name: Paraproduct
msc: [42B25, 42B20, 35S50]
sources:
  - url: https://en.wikipedia.org/wiki/Paraproduct
same_as:
  wikidata: Q17096244
  wikipedia: Paraproduct
---

## Summary

A paraproduct is the part of a product $fg$ in which the high frequencies of $f$ are multiplied by the low frequencies of $g$.
Using the [[Littlewood–Paley decomposition|D1PAT0K446]], every product splits as $fg = \Pi_g f + \Pi_f g + R(f, g)$, two paraproducts and a remainder in which both factors have comparable frequencies.
Paraproducts are bilinear operators that behave much better than the full product in many function spaces.
They appear in Bony's paradifferential calculus for nonlinear PDE and in the T(1) theorem, where they are the model non-convolution Calderón–Zygmund operators.

## Explanations

### L1 human

When two functions are multiplied, their frequencies interact.
If $f$ oscillates fast and $g$ varies slowly, the product $fg$ oscillates at about the same frequencies as $f$, with an amplitude modulated by $g$.
The paraproduct $\Pi_g f$ collects exactly these interactions, frequency band by frequency band.
For example, if $g$ is a constant $c$, then the paraproduct $\Pi_g f$ is just $c f$.
