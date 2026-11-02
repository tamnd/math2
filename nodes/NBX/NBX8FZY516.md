---
tag: NBX8FZY516
kind: concept
name: Independent component analysis
msc: [62H25, 94A12]
sources:
  - url: https://en.wikipedia.org/wiki/Independent_component_analysis
same_as:
  wikidata: Q1259145
  wikipedia: Independent component analysis
---

## Summary

Independent component analysis recovers hidden source signals from observed linear mixtures of them, assuming the sources are statistically independent.
Unlike [[principal component analysis|ABXD13M340]], which only makes the new variables uncorrelated, it asks for full [[independence|0GQ938GDE0]].
This is possible only when at most one source is Gaussian.
It is a standard tool for blind source separation in signal processing.

## Explanations

### L1 human

At a party, two microphones each record a different mix of two people talking.
Independent component analysis tries to unmix the recordings into the two separate voices, without knowing how they were mixed.
The key assumption is that what one person says does not depend on what the other says.
The voices come back only up to order and volume: the method cannot tell which voice is "first" or how loud it really was.
