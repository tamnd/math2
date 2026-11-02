---
tag: HBK5QHC1GC
kind: concept
name: General recursive function
msc: [03D20]
sources:
  - url: https://en.wikipedia.org/wiki/General_recursive_function
same_as:
  wikidata: Q284164
  wikipedia: General recursive function
---

## Summary

The general recursive functions, also called $\mu$-recursive functions, are the functions on the natural numbers obtained from the [[primitive recursive functions|5NVA2JRHPV]] by adding unbounded search.
The search operator $\mu$ returns the least number at which a given function takes the value $0$, and may run forever.
So the class contains partial functions, and the total ones among them are exactly the total [[computable functions|KZSB5E471K]].
This class was one of the first precise definitions of computability, and it agrees with computability by [[Turing machines|758EYCN27B]].

## Explanations

### L1 human

Primitive recursion is like a for-loop: the number of steps is known before the loop starts.
Unbounded search is like a while-loop: keep trying $y = 0, 1, 2, \ldots$ until a condition holds.
A while-loop may never stop, and then the function has no value at that input.
For example, searching for the least $y$ with $y^2 \ge x$ always stops and gives the rounded-up square root of $x$.
Adding this one tool to bounded loops gives every computable function.
