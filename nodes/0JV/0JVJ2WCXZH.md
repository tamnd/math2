---
tag: 0JVJ2WCXZH
kind: concept
name: Gaussian elimination
aliases: [row-reduction]
msc: [15A06, 65F05]
sources:
  - url: https://en.wikipedia.org/wiki/Gaussian_elimination
    locator: lead section
same_as:
  wikidata: Q2658
  wikipedia: Gaussian elimination
---

## Summary

Gaussian elimination is an algorithm that changes a matrix into a [[row echelon form|0VYCDGMJJJ]] by [[elementary row operations|04XWH28452]].
It works column by column, from left to right.
In each column, it chooses a nonzero entry as [[pivot|0J0BBCMJ5W]] and moves its row up.
Then it adds multiples of that row to the rows below, to make their entries in that column zero.
Applied to the [[augmented matrix|0T6MWGZSXA]] of a [[system of linear equations|0GT4WWGWH2]], it gives an equivalent system that [[back substitution|0ATFVE08MW]] solves.
For an $n \times n$ matrix, it uses on the order of $n^3$ arithmetic operations.

## Remarks

The algorithm also computes the [[rank|0ZC9YTXZRY]] of a matrix and, with a record of the row operations, its [[determinant|00KDZRW4C0]].
It also tests if a system is [[consistent|0X6V9B1V10]]: the system is inconsistent exactly when a row $(0, \dots, 0 \mid c)$ with $c \ne 0$ appears.
The method was known in China in the book *The Nine Chapters on the Mathematical Art*, long before Gauss.

## Explanations

### L1 human

Gaussian elimination is the method of solving equations by removing one unknown at a time.
We use the first equation to remove $x_1$ from all the other equations, then the second to remove $x_2$, and so on.
At the end, the last equation has the fewest unknowns, and we solve upwards.
