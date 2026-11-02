---
tag: WN6M8B3ZKB
kind: concept
name: Series in Banach spaces
msc: [40A05, 46B15]
sources:
  - url: https://en.wikipedia.org/wiki/Absolute_convergence
---

## Summary

A series $\sum x_n$ of vectors in a [[Banach space|06GZ956657]] converges when its partial sums converge in norm.
It converges absolutely when the real series $\sum \norm{x_n}$ converges.
[[Absolute convergence implies convergence|082MGNWNA8]], because the space is complete.
In infinite dimensions the converse fails more sharply than in $\R$: there are series that converge after every rearrangement but not absolutely.
Series of this kind are used everywhere in analysis, for example in the Neumann series $\sum T^n$ for an operator $T$ of norm less than $1$.

## Explanations

### L1 human

A series of vectors is added term by term, like a series of numbers, and one asks whether the partial sums approach a vector.
The size of a vector is its norm, so convergence means that the norm of the difference between the partial sums and the limit tends to $0$.
If the sizes $\norm{x_n}$ add up to a finite number, the series converges, just as for numbers.
For example, in the space $\ell^2$ of square-summable sequences, with $e_n$ the $n$-th unit vector, the series $e_1 + e_2/2 + e_3/3 + \cdots$ can converge even though $1 + 1/2 + 1/3 + \cdots$ diverges.
