---
tag: T88M6XTTRP
kind: concept
name: List decoding
msc: [94B35, 94B65]
sources:
  - url: https://en.wikipedia.org/wiki/List_decoding
same_as:
  wikidata: Q4437907
  wikipedia: List decoding
---

## Summary

List decoding relaxes the goal of decoding: instead of one codeword, the decoder outputs a short list of all codewords close to the received word.
A code is list decodable at radius $\rho$ when every Hamming ball of relative radius $\rho$ contains only few codewords.
This allows correction of more than half the [[minimum distance|M2X88AXM17]] many errors, which unique decoding cannot do.
For $q$-ary codes and $0 < \rho < 1 - 1/q$, every rate below $1 - H_q(\rho)$ is possible with constant list size, where $H_q$ is the [[$q$-ary entropy function|95CYGNRQQ6]].

## Explanations

### L1 human

With unique decoding, the decoder must commit to one answer, so it can only handle errors up to half the distance between codewords.
Beyond that, two codewords may be equally close, and the decoder cannot choose.
List decoding allows the answer "it is one of these few words".
For example, in a code where two codewords differ in $4$ places, a word in the middle at distance $2$ from both is ambiguous; a list decoder simply returns both.
Often other information, such as a checksum, then picks the right one.
