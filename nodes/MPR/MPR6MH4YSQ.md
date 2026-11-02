---
tag: MPR6MH4YSQ
kind: concept
name: Height of a poset
msc: [06A07]
sources:
  - url: https://en.wikipedia.org/wiki/Graded_poset
---

## Summary

The height of a [[partially ordered set|0QV2JS9RJ3]] is the largest number of elements of a [[chain|0S8FE7ZMFM]] in it.
It is the number of elements in the longest sequence of elements each strictly above the previous one.
By [[Mirsky's theorem|5VPXR3RDF1]], for a finite poset it is also the least number of antichains that cover the poset.

## Explanations

### L1 human

Draw a poset with smaller elements lower down.
The height counts the elements on the tallest path that only goes upward.
In the divisors of $12$ ordered by divisibility, the path $1, 2, 4, 12$ has $4$ elements, and no chain is longer, so the height is $4$.
An antichain has height $1$.
