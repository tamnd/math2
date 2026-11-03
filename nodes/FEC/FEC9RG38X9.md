---
tag: FEC9RG38X9
kind: concept
name: Aliasing
msc: [94A20, 94A12, 42A38]
sources:
  - url: https://en.wikipedia.org/wiki/Aliasing
same_as:
  wikidata: Q868732
  wikipedia: Aliasing
---

## Summary

Aliasing is the effect by which different signals give the same samples, so that after sampling one cannot tell them apart.
When a signal is sampled at rate $f_s$, a frequency $\xi$ cannot be distinguished from the frequencies $\xi + k f_s$ with $k \in \Z$.
High frequencies then show up in the samples as false low frequencies.
Sampling above the [[Nyquist rate|AXKCWXE77N]] of a [[band-limited|P3T104G564]] signal avoids aliasing.
See the [[definition|AJPKH8XY3G]].

## Explanations

### L1 human

In films, a spinning wheel sometimes seems to turn slowly or even backwards.
The camera takes pictures at a fixed rate, and the wheel turns almost a full spoke between pictures, so the eye sees only a small step.
The same thing happens with any sampled signal.
A cosine at $7$ hertz sampled $10$ times per second gives exactly the same samples as a cosine at $3$ hertz.
Engineers therefore filter out high frequencies before sampling, so that no such false copies appear.
