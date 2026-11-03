---
tag: AXKCWXE77N
kind: concept
name: Nyquist rate
msc: [94A20, 94A12, 42A38]
sources:
  - url: https://en.wikipedia.org/wiki/Nyquist_rate
same_as:
  wikidata: Q6273772
  wikipedia: Nyquist rate
---

## Summary

The Nyquist rate of a [[band-limited|P3T104G564]] signal is twice its highest frequency.
It is the sampling rate above which the [[sampling theorem|BMXDMHRXBG]] guarantees that the samples determine the signal.
Sampling more slowly than the Nyquist rate can cause [[aliasing|FEC9RG38X9]].
See the [[definition|AJ3RC25YV3]].

## Explanations

### L1 human

A signal with no frequencies above $B$ hertz cannot wiggle faster than about $B$ times per second.
To capture each wiggle you need at least two samples per cycle, one near the top and one near the bottom.
So the signal needs about $2B$ samples per second, and $2B$ is its Nyquist rate.
For example, audio that contains frequencies up to $20\,000$ hertz has Nyquist rate $40\,000$ samples per second, which is why CDs use $44\,100$.
