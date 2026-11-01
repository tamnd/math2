---
tag: TAE6K8NQ46
kind: concept
name: Error-correcting code
msc: [94B25, 94B05]
sources:
  - url: https://en.wikipedia.org/wiki/Error_correction_code
same_as:
  wikidata: Q55611017
  wikipedia: Error correction code
---

## Summary

An error-correcting code is a set of words of fixed length, the codewords, chosen far apart from each other in Hamming distance.
A message is sent as a codeword; if a few symbols are corrupted on the way, the receiver still finds the nearest codeword.
A code whose codewords are at distance at least $2t + 1$ from each other corrects any $t$ errors.
Codes link combinatorics with algebra: good codes come from [[block designs|4JCSS2Z1BA]], [[Hadamard matrices|J0N4J606X0]] and finite fields.
The node [[error-correcting code|X122TKFP9G]] gives the precise definition.

## Explanations

### L1 human

Suppose you send one bit, but noise may flip it.
Send it three times instead: $000$ for $0$ and $111$ for $1$.
If the receiver gets $010$, the most likely message is $0$, since only one bit had to flip.
This is the repetition code; it corrects one error at the price of sending three times as much.
Better codes, such as the Hamming code, correct errors at a much lower price.
