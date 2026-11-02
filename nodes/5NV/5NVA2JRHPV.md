---
tag: 5NVA2JRHPV
kind: concept
name: Primitive recursive function
msc: [03D20]
specializes: [KZSB5E471K]
sources:
  - url: https://en.wikipedia.org/wiki/Primitive_recursive_function
same_as:
  wikidata: Q1570472
  wikipedia: Primitive recursive function
---

## Summary

A primitive recursive function is a function on the [[natural numbers|0MWKJ44V5A]] built from zero, successor and projections by composition and primitive recursion.
Primitive recursion defines $f(n + 1)$ from $f(n)$, like a for-loop whose number of steps is fixed in advance.
Every primitive recursive function is total and [[computable|KZSB5E471K]], and most functions met in ordinary number theory are primitive recursive.
Not every total computable function is primitive recursive; the [[Ackermann function|N470JF7ZJX]] is the classical example.

## Explanations

### L1 human

Start with the simplest functions: the constant $0$, adding one, and picking one argument out of a list.
Then allow two ways of building new functions: plugging functions into each other, and defining a value at $n + 1$ from the value at $n$.
Addition comes from adding one repeatedly, multiplication from adding repeatedly, and powers from multiplying repeatedly.
Every function obtained this way can be computed by a program whose loops have a bound known before the loop starts.
