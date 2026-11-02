---
tag: TN9G24VABN
kind: concept
name: Computably enumerable set
msc: [03D25]
specializes: [0BJR9QR08E]
sources:
  - url: https://en.wikipedia.org/wiki/Computably_enumerable_set
same_as:
  wikidata: Q676835
  wikipedia: Computably enumerable set
---

## Summary

A computably enumerable set, also called recursively enumerable or semidecidable, is a set of natural numbers whose elements can be listed by an algorithm.
Equivalently, some algorithm halts exactly on the elements of the set.
Every [[computable set|PPGD5KW8JC]] is computably enumerable, but the halting set is computably enumerable and not computable.
These sets are the $\Sigma^0_1$ sets of the [[arithmetical hierarchy|7CVJCQKY41]] and are studied through their [[Turing degrees|P5N2ND3VCG]].

## Explanations

### L1 human

A set is computably enumerable if a program can print its elements one by one, possibly forever and in any order.
If a number is in the set, you will see it printed after some time.
If it is not in the set, you may wait forever without learning this.
For example, the numbers of programs that halt can be listed by running all programs in parallel and printing each one when it stops.
