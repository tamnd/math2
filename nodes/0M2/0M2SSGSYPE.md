---
tag: 0M2SSGSYPE
kind: statement
role: theorem
name: Cayley's formula
msc: [05C30]
uses: [0MJ0JS72DZ]
sources:
  - url: https://en.wikipedia.org/wiki/Cayley's_formula
    locator: lead section
same_as:
  wikidata: Q859176
  wikipedia: "Cayley's formula"
---

## Statement

Let $n \ge 2$ be an integer.
Then the number of [[trees|0MJ0JS72DZ]] with vertex set $\{1, 2, \dots, n\}$ is $n^{n-2}$.

## Remarks

The trees are labelled: two trees are the same only if they have the same edge set. Thus the formula counts the [[spanning trees|0FQ5B8S1ZC]] of $K_n$.
For $n = 3$ there are $3$ trees, and for $n = 4$ there are $16$.
A proof uses the [[Prüfer sequence|09PV9JSY6E]], a bijection between these trees and the sequences of length $n - 2$ over $\{1, \dots, n\}$.

## History

Carl Wilhelm Borchardt found the formula in 1860.
Arthur Cayley extended it in 1889, and the formula has his name.

## Explanations

### L1 human

Label $n$ points with the numbers $1$ to $n$ and count the ways to connect them by a tree.
For $4$ points there are $4^2 = 16$ ways: $12$ paths and $4$ stars.
