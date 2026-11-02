---
tag: NC26CE0Y8B
kind: concept
name: Sweedler notation
msc: [16T15, 16T05]
sources:
  - url: https://en.wikipedia.org/wiki/Coalgebra
---

## Summary

Sweedler notation is a shorthand for the comultiplication of a [[coalgebra|A06RA8KB0T]]: one writes $\Delta(c) = \sum c_{(1)} \otimes c_{(2)}$, or even $c_{(1)} \otimes c_{(2)}$, without naming the terms of the sum.
Coassociativity lets one write iterated coproducts as $c_{(1)} \otimes c_{(2)} \otimes c_{(3)}$ without brackets.
It is named after Moss Sweedler and is the standard notation for computations with [[Hopf algebras|7XFYP0N84H]] and [[comodules|7WEM2E6RTV]].

## Explanations

### L1 human

The coproduct of an element is a sum of pairs, but the pairs are rarely worth naming one by one.
Sweedler notation writes a typical pair as $c_{(1)} \otimes c_{(2)}$ and lets the summation stay implicit.
With it, the counit law reads $\varepsilon(c_{(1)}) c_{(2)} = c$, and the antipode law reads $S(c_{(1)}) c_{(2)} = \varepsilon(c) 1$.
The symbols $c_{(1)}$ and $c_{(2)}$ are not elements on their own; they only make sense inside expressions that are linear in each of them.
