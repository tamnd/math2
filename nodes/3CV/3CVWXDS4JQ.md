---
tag: 3CVWXDS4JQ
kind: concept
name: Strassen algorithm
msc: [65F30, 68Q25, 15A69]
sources:
  - url: https://en.wikipedia.org/wiki/Strassen_algorithm
same_as:
  wikidata: Q728507
  wikipedia: Strassen algorithm
---

## Summary

The Strassen algorithm multiplies two $n \times n$ matrices with $O(n^{\log_2 7})$ arithmetic operations, where $\log_2 7 \approx 2.807$.
It rests on a way to multiply $2 \times 2$ matrices with $7$ multiplications instead of $8$, applied recursively to blocks.
Published by Volker Strassen in 1969, it was the first method faster than the usual $O(n^3)$ [[matrix multiplication|032Q9FB8MT]].
It started the search for the [[matrix multiplication exponent|X0G02CGQ5J]].

## Explanations

### L1 human

The schoolbook product of two $2 \times 2$ matrices uses $8$ multiplications of entries.
Strassen found clever sums and differences of entries so that $7$ products are enough, at the cost of more additions.
Because the entries can themselves be blocks, the trick can be applied again inside each block.
Saving one multiplication out of eight at every level adds up: for large matrices the total work grows like $n^{2.81}$ instead of $n^3$.
