---
tag: 6G24FVAKZX
kind: concept
name: Luby transform code
msc: [94B60, 68P30]
sources:
  - url: https://en.wikipedia.org/wiki/Luby_transform_code
same_as:
  wikidata: Q13563306
  wikipedia: Luby transform code
---

## Summary

A Luby transform (LT) code is a rateless erasure code, or fountain code.
From $k$ input symbols the encoder can produce an unlimited stream of output symbols.
Each is the bitwise XOR of a random set of input symbols.
The size of each set is drawn from a degree distribution.
The receiver recovers the input from any slightly more than $k$ output symbols, with high probability.
Decoding is the peeling process, that is [[belief propagation|Q6GZN4JWJP]] on the [[binary erasure channel|ESYMTB37YG]].
Luby introduced LT codes in 2002, together with the robust soliton degree distribution that makes them efficient.

## Explanations

### L1 human

Think of a fountain that sprays drops, each drop a mixture of a few input packets.
A receiver collects any drops it catches, in any order, and stops once it has a few more than the number of input packets.
It decodes by finding a drop made of a single packet, which reveals that packet, then removing that packet from all other drops, and repeating.
For example, with inputs $x_1, x_2, x_3$ and received drops $x_1$, $x_1 \oplus x_2$ and $x_2 \oplus x_3$, one finds $x_1$, then $x_2$, then $x_3$.
No feedback is needed about which drops were lost, which suits broadcast to many receivers.
