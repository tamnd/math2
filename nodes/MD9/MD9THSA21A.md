---
tag: MD9THSA21A
kind: concept
name: Pseudorandom generator
msc: [68Q87, 68Q10, 68W20]
sources:
  - url: https://en.wikipedia.org/wiki/Pseudorandom_generator
same_as:
  wikidata: Q7255474
  wikipedia: Pseudorandom generator
---

## Summary

A pseudorandom generator stretches a short uniformly random seed into a long string that no efficient test can tell apart from a uniformly random string.
In complexity theory the tests are [[Boolean circuits|SQXNFGVADX]] of bounded size, or algorithms of bounded running time.
Derandomization is the use of such generators to replace the random bits of an algorithm, which turns randomised algorithms into deterministic ones.
Good enough generators, with seed length logarithmic in the output length, would give $\mathrm{BPP} = \mathrm{P}$.

## Explanations

### L1 human

A randomised algorithm uses many coin flips, but perhaps it does not need truly random ones: it only needs bits that look random to it.
A pseudorandom generator produces such bits from a short seed.
If the seed has only $O(\log n)$ bits, a deterministic algorithm can try all polynomially many seeds and take the majority answer.
This turns a randomised polynomial-time algorithm into a deterministic one.
The [[pseudorandom number generators|C5FG6ARWVV]] of programming libraries are a practical relative of this idea, without proved guarantees.
