---
tag: JJH68RANFH
kind: concept
name: Low-density parity-check code
msc: [94B05, 94B35]
specializes: [E85KREWV60]
sources:
  - url: https://en.wikipedia.org/wiki/Low-density_parity-check_code
same_as:
  wikidata: Q187444
  wikipedia: Low-density parity-check code
---

## Summary

A low-density parity-check (LDPC) code is a [[linear code|E85KREWV60]] defined by a [[parity-check matrix|Y4JB44WWFG]] with very few nonzero entries in each row and each column.
The sparse matrix is best seen as a [[Tanner graph|GTDMNAMPD9]], and [[belief propagation decoding|Q6GZN4JWJP]] on this graph runs in time linear in the length.
Gallager introduced these codes in the early 1960s, and they were rediscovered in the 1990s.
Well-designed LDPC codes come very close to [[channel capacity|J7MZ2XQP9M]] and are used in Wi-Fi, digital television and 5G.

## Explanations

### L1 human

Each parity check of an LDPC code involves only a handful of bits, and each bit takes part in only a handful of checks.
So when a bit is uncertain, only a few checks speak about it, and each check can be evaluated quickly.
The decoder lets bits and checks exchange opinions many times, and the local opinions spread into a global decision.
For example, label the $6$ edges of a complete graph on $4$ vertices as bits.
Ask that the bits on the $3$ edges at each vertex sum to $0$ modulo $2$.
Then each check involves $3$ bits and each bit lies in $2$ checks.
