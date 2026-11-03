---
tag: VDT5VNVPCH
kind: problem
name: Orchard-planting problem
msc: [52C30, 52C10]
uses: [0AFNNTRTJE]
about: [0AFNNTRTJE]
sources:
  - url: https://en.wikipedia.org/wiki/Orchard-planting_problem
same_as:
  wikidata: Q7100169
  wikipedia: Orchard-planting problem
history:
  posed_by: "unknown; it is an old puzzle about planting trees in rows"
  first_stated: "19th century"
---

## Problem

Let $n \ge 3$ be an integer.
Let $S$ be a set of $n$ points in the real plane $\R^2$.
A *$3$-point line* of $S$ is a line that contains exactly $3$ points of $S$.
Let $t_3(n)$ be the largest number of $3$-point lines of a set of $n$ points in $\R^2$.
Determine $t_3(n)$ for every $n$.

## Remarks

Two distinct points lie on at most one common line, and a $3$-point line contains $3$ pairs of points.
Hence $t_3(n) \le \floor{n(n-1)/6}$.
Stefan Burr, Branko Grünbaum and Neil Sloane gave, in 1974, a construction based on cubic curves with
$$\floor{\frac{n(n-3)}{6}} + 1$$
$3$-point lines.
In 2013 Ben Green and Terence Tao proved that this number equals $t_3(n)$ for all sufficiently large $n$.
For $n = 4, 5, \dots, 14$ the values of $t_3(n)$ are $1, 2, 4, 6, 7, 10, 12, 16, 19, 22, 26$.
For example, $t_3(9) = 10$, and the formula above also gives $\floor{54/6} + 1 = 10$.

The problem is close to the [[Sylvester–Gallai theorem|T3GGJN70P2]], which concerns lines through exactly two of the points.

## Explanations

### L1 human

A gardener has $n$ trees and wants to plant them so that as many straight rows of exactly three trees as possible appear.
With $9$ trees one can make $10$ such rows.
Counting pairs of trees shows that one can never do much better than about $n^2/6$ rows.
For large $n$ the exact best number is now known, about $n^2/6 - n/2$.
