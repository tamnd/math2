---
tag: EMVW7N54FE
kind: concept
name: Bode plot
msc: [93C80, 93C05]
sources:
  - url: https://en.wikipedia.org/wiki/Bode_plot
same_as:
  wikidata: Q245627
  wikipedia: Bode plot
---

## Summary

A Bode plot shows the [[frequency response|BMY8QZSD9H]] $G(i\omega)$ of a linear system as two graphs.
They show the gain in decibels and the phase over a logarithmic frequency axis.
On these scales a product of factors becomes a sum of graphs.
Each simple factor has a graph that is close to a few straight lines.
So the plot of a complicated [[transfer function|86JKV3TRFD]] can be sketched by hand.
It is used to read off [[gain and phase margins|J39ZSFW0YF]] and to design compensators.

## Explanations

### L1 human

A Bode plot is two pictures stacked on top of each other.
The top one shows how much the system amplifies a sine wave, the bottom one how much it delays it, both against the frequency of the wave.
Both axes for frequency and gain are logarithmic, so factors of ten are equal steps.
For $G(s) = 1/(s + 1)$ the gain is flat at $0$ decibels for low frequencies and falls by $20$ decibels for each factor of ten beyond $\omega = 1$.
