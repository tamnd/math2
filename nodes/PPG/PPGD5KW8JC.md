---
tag: PPGD5KW8JC
kind: concept
name: Computable set
msc: [03D25, 03D20]
specializes: [0BJR9QR08E]
sources:
  - url: https://en.wikipedia.org/wiki/Computable_set
same_as:
  wikidata: Q877945
  wikipedia: Computable set
---

## Summary

A computable set, also called a recursive or decidable set, is a set of natural numbers for which an algorithm decides membership.
The algorithm must halt on every input and answer yes or no correctly.
Computable sets are exactly the sets whose characteristic function is a total [[computable function|KZSB5E471K]].
They are the bottom level of the hierarchies of complexity of sets in [[computability theory|X14Y880PN5]].

## Explanations

### L1 human

A set of numbers is computable if a program can always answer the question "is $n$ in the set?" in finitely many steps.
The even numbers and the prime numbers are computable sets.
The set of numbers of programs that halt is not computable, although a program can confirm membership when it holds.
Each finite set is computable, since a program can simply contain the list.
