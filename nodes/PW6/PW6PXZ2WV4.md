---
tag: PW6PXZ2WV4
kind: concept
name: Conditional mutual information
msc: [94A17]
sources:
  - url: https://en.wikipedia.org/wiki/Conditional_mutual_information
same_as:
  wikidata: Q5159269
  wikipedia: Conditional mutual information
---

## Summary

The conditional mutual information $I(X; Y \mid Z)$ measures how much information $X$ and $Y$ share once a third random variable $Z$ is known.
It is the average over the values $z$ of $Z$ of the [[mutual information|A83CYGDXFG]] of $X$ and $Y$ under the conditional law given $Z = z$.
It is non-negative, and it is zero exactly when $X$ and $Y$ are [[conditionally independent|0THJ7416DX]] given $Z$.
It gives the chain rule $I(X; Y, Z) = I(X; Z) + I(X; Y \mid Z)$, which underlies the [[data processing inequality|BGH1T3HKPV]].

## Explanations

### L1 human

Two quantities can be related only through a third one.
For example, the reading of two thermometers in the same room both depend on the room temperature.
Once the temperature is known, the two readings may tell nothing more about each other.
Conditional mutual information measures what the two still share after the third quantity is known.
It can be smaller or larger than the plain mutual information: for two independent fair bits $X, Y$ and $Z = X + Y \bmod 2$, one has $I(X; Y) = 0$ but $I(X; Y \mid Z) = 1$ bit.
