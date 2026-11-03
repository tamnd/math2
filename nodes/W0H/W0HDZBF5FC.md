---
tag: W0HDZBF5FC
kind: concept
name: Quine–McCluskey algorithm
msc: [94C11, "06E30", 68W40]
sources:
  - url: https://en.wikipedia.org/wiki/Quine%E2%80%93McCluskey_algorithm
same_as:
  wikidata: Q621409
  wikipedia: Quine–McCluskey algorithm
---

## Summary

The Quine–McCluskey algorithm finds a shortest [[disjunctive normal form|0GVDFAY4KW]] of a [[Boolean function|0X05GS525E]].
The function is given by the list of inputs where it is true.
It first finds all prime implicants by merging terms that differ in one variable.
Then it chooses a smallest set of prime implicants that covers every true input.
It is the tabular, mechanical counterpart of the [[Karnaugh map|TS1B16HX5K]] and works for any number of variables.
Its running time grows exponentially with the number of variables, as expected for the NP-hard problem of [[logic optimization|WXSPR8HPJA]].

## Explanations

### L1 human

Write each input where the function is true as a string of bits, such as $011$.
If two strings differ in one place, the function does not care about that variable there, so merge them into one string with a dash, such as $0{-}1$.
Keep merging until nothing more can be merged; what is left are the prime implicants.
Finally choose as few of them as possible so that every true input is covered.
