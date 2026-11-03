---
tag: TW55PBYQ3E
kind: concept
name: Jukes–Cantor model
msc: [92D15, 60J27]
specializes: [5G0AKZ8SXJ]
sources:
  - url: https://en.wikipedia.org/wiki/Models_of_DNA_evolution
---

## Summary

The Jukes–Cantor model is the simplest [[model of DNA evolution|5G0AKZ8SXJ]].
Every nucleotide changes into each of the three others at the same rate, and the four nucleotides are equally frequent at equilibrium.
Its transition probabilities have a closed form, which gives the Jukes–Cantor distance between two aligned DNA sequences.

## Explanations

### L1 human

Picture each position of a DNA sequence as a four-sided die that is re-rolled at random times.
Under the Jukes–Cantor model every outcome of a re-roll is equally likely, so no change is preferred.
After a long time the letter at a position is any of the four with probability $1/4$, whatever it was at the start.
If two sequences differ at $30\%$ of positions, the model estimates about $0.38$ substitutions per position.
This is more than $0.30$, because some changes are hidden by later changes at the same position.
