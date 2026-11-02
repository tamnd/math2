---
tag: KZSB5E471K
kind: concept
name: Computable function
msc: [03D20, 03D10]
specializes: [0EPAT51DXQ]
sources:
  - url: https://en.wikipedia.org/wiki/Computable_function
same_as:
  wikidata: Q1148456
  wikipedia: Computable function
---

## Summary

A computable function is a function on the natural numbers whose values can be calculated by an algorithm.
Formally, it is a partial function computed by a [[Turing machine|758EYCN27B]], and this class equals the class of partial [[general recursive functions|HBK5QHC1GC]].
Computable functions are the central objects of [[computability theory|X14Y880PN5]].
Some functions, such as the one that tells whether a program halts, are well defined but not computable.

## Explanations

### L1 human

A function is computable if there is a mechanical procedure that, given an input, eventually produces the output.
Addition, multiplication and the test "is $n$ prime?" are computable: there are clear step-by-step recipes for them.
A partial computable function may have no value at some inputs, because the procedure runs forever there.
The surprise of the 1930s was that some precisely defined functions have no such procedure at all.
