---
tag: PFJER4FMJ5
kind: concept
name: Rate–distortion theory
msc: [94A34, 94A29]
sources:
  - url: https://en.wikipedia.org/wiki/Rate%E2%80%93distortion_theory
same_as:
  wikidata: Q843483
  wikipedia: Rate–distortion theory
---

## Summary

Rate–distortion theory is the part of information theory that studies lossy compression.
It asks for the least number of bits per source symbol that allows a reconstruction within a given average distortion.
Shannon showed that this least rate is given by a minimum of mutual information, the rate–distortion function.
The theory underlies the design of audio, image and video coders.

## Explanations

### L1 human

A photograph does not need to be stored exactly: a small error is invisible.
Allowing errors saves bits, and the question is how many.
For a fair coin flip stored with a bit error rate of $10\%$, about $0.53$ bits per flip suffice instead of $1$.
Rate–distortion theory gives this trade-off between file size and quality for any source and any way of measuring error.
