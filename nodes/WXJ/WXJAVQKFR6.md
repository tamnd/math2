---
tag: WXJAVQKFR6
kind: problem
name: Euler's thirty-six officers problem
msc: [05B15]
uses: [KHD2QMNR7R]
about: [H6TN6BADVY]
sources:
  - url: https://en.wikipedia.org/wiki/Mutually_orthogonal_Latin_squares
history:
  posed_by: "Leonhard Euler"
  first_stated: "1782"
---

## Problem

Thirty-six officers come from six regiments, with one officer of each of six ranks in each regiment.
Arrange them in a $6 \times 6$ square with two conditions.
Each row and each column contains exactly one officer of each regiment and exactly one officer of each rank.

## Remarks

Writing the regiment and the rank of the officer in each cell gives two Latin squares of order $6$.
The arrangement asked for exists if and only if these two squares are [[orthogonal|KHD2QMNR7R]].
So the problem asks for a pair of orthogonal Latin squares of order $6$.
Euler posed the problem in 1782 and believed it had no solution.
Gaston Tarry proved in 1901, by a case analysis, that there is no solution.
Euler also conjectured that no orthogonal pair exists for any order $n \equiv 2 \pmod 4$.
Bose, Shrikhande and Parker disproved this around 1959 to 1960: an orthogonal pair of order $n$ exists for every $n$ except $2$ and $6$.

## Explanations

### L1 human

The puzzle is a two-colour Sudoku without boxes: every row and column must show each regiment once and each rank once.
For $25$ officers in a $5 \times 5$ square the analogous puzzle has a solution, but for $36$ officers it has none.
It is surprising that $6$ fails while $10$, $14$ and every larger order work.
