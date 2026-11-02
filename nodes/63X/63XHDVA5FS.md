---
tag: 63XHDVA5FS
kind: concept
name: Kolmogorov epsilon-entropy
msc: [41A46, 46B50]
sources:
  - url: https://en.wikipedia.org/wiki/Covering_number
---

## Summary

Let $K$ be a [[totally bounded set|020Q06TYYH]] in a [[metric space|0VKD1TP7F3]].
Its Kolmogorov $\varepsilon$-entropy is the binary logarithm of the least number of pieces of diameter at most $2\varepsilon$ needed to cover $K$.
It measures how many bits are needed to describe an element of $K$ to accuracy $\varepsilon$.
Kolmogorov and Tikhomirov studied its growth as $\varepsilon \to 0$ for classes of smooth and analytic functions.
It gives lower bounds for every method of approximation or coding of the class, linear or not.

## Explanations

### L1 human

Suppose you must store any element of a set $K$, but only up to an error $\varepsilon$.
Cut $K$ into pieces so small that every piece has diameter at most $2\varepsilon$, and store only the label of the piece.
The fewest pieces that work is the covering number, and its logarithm in base $2$ is the number of bits you need.
For example, the interval $[0, 1]$ needs $\ceil{1/(2\varepsilon)}$ pieces, so its $\varepsilon$-entropy is about $\log_2(1/\varepsilon)$; a set of functions needs far more.
