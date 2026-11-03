---
tag: JP3SNC0V68
kind: concept
name: Church encoding
msc: [03B40, 68N18]
sources:
  - url: https://en.wikipedia.org/wiki/Church_encoding
same_as:
  wikidata: Q1089708
  wikipedia: Church encoding
---

## Summary

Church encoding represents data such as natural numbers and truth values by terms of the pure [[lambda calculus|BD756KR8FM]].
The number $n$ becomes the function that applies its first argument $n$ times to its second argument.
Arithmetic operations then become lambda terms, and computation becomes [[beta reduction|Y9B9CVY6SJ]].
It shows that the lambda calculus, which has only functions, can express all [[computable functions|KZSB5E471K]] on the natural numbers.

## Explanations

### L1 human

The lambda calculus has no built-in numbers, so one must build them out of functions.
Church's idea is to describe a number by what it does: the number $3$ is "do something three times".
So $3$ is the term that takes $f$ and $x$ and returns $f(f(f(x)))$.
Adding one means doing $f$ one more time, and multiplying means repeating a repetition.
Truth values work the same way: "true" picks the first of two options, and "false" picks the second.
