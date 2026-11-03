---
tag: NZMKB1EXDG
kind: concept
name: Universal code
msc: [94A45, 94A29, 68P30]
specializes: [GNB3T6TD0M]
sources:
  - url: https://en.wikipedia.org/wiki/Universal_code_(data_compression)
same_as:
  wikidata: Q4176366
  wikipedia: Universal code (data compression)
---

## Summary

A universal code for the integers is a prefix code for the positive integers that is good for every decreasing probability distribution at once.
Its expected codeword length is at most a constant times the larger of $1$ and the entropy, whatever the distribution.
The only condition is that small numbers are at least as likely as large ones.
Elias gamma and Elias delta codes are standard examples.
Such codes are used to write lengths and counts when their distribution is unknown.

## Explanations

### L1 human

Suppose you must send a positive whole number but do not know in advance how large it tends to be.
Writing it in binary is not enough, because the receiver does not know where the number ends.
The Elias gamma code first writes as many zeros as the binary form has digits after the first, then the binary form.
So $5 = 101_2$ becomes $00101$, and the receiver counts the zeros to know how many digits follow.
