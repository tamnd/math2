---
tag: K3KADGATHA
kind: concept
name: Van Wijngaarden transformation
msc: [65B10, 40A25]
specializes: [B1S2XJPGYD]
sources:
  - url: https://en.wikipedia.org/wiki/Van_Wijngaarden_transformation
same_as:
  wikidata: Q7913772
  wikipedia: Van Wijngaarden transformation
---

## Summary

The van Wijngaarden transformation accelerates an [[alternating series|0QED0GPYKY]] by averaging its partial sums again and again.
Each new row of the table holds the means of neighbouring entries of the row above.
It is a variant of the [[Euler transform|WT0HACKQV7]] that is easy to carry out by hand or by machine.

## Explanations

### L1 human

The partial sums of an alternating series jump above and below the sum.
The average of two consecutive partial sums lies between them and is usually much closer to the sum.
Averaging the averages improves the values again.
For the Leibniz series $1 - \frac13 + \frac15 - \cdots = \frac{\pi}{4}$, three rounds of averaging of the first four partial sums give about $0.7905$, against $0.7854$ for $\frac{\pi}{4}$ and $0.7238$ for the fourth partial sum.
