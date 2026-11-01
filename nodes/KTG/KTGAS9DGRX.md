---
tag: KTGAS9DGRX
kind: problem
name: Class number problem
msc: [11R29, 11R11]
uses: [7SV4WA92SM, KTKK9B1X41, SBDSYA037Q]
about: [KTKK9B1X41, 7SV4WA92SM]
sources:
  - url: https://en.wikipedia.org/wiki/Class_number_problem
history:
  posed_by: "Carl Friedrich Gauss"
  first_stated: "1801"
---

## Problem

For each positive integer $h$, determine the complete list of imaginary [[quadratic fields|7SV4WA92SM]] $\Q(\sqrt{-d})$, with $d$ a positive squarefree integer, whose [[class number|KTKK9B1X41]] equals $h$.

## Remarks

The problem goes back to Gauss, who stated it in the language of [[binary quadratic forms|SBDSYA037Q]].
It has three parts: show that the class number tends to infinity as $d \to \infty$, so that each list is finite; make this effective; and compute the lists.

Status:
the class number of $\Q(\sqrt{-d})$ tends to infinity with $d$ (Heilbronn), but this proof gives no effective bound.
The case $h = 1$ is the [[Stark–Heegner theorem|KZTFH832H0]], with nine fields, and the case $h = 2$ was solved by Baker and by Stark.
Goldfeld, combined with the theorem of Gross and Zagier, gave an effective lower bound for the class number, which reduces each $h$ to a finite computation.
Watkins completed the lists for all $h \le 100$.

The analogue for real quadratic fields is open: it is not known whether infinitely many real quadratic fields have class number $1$.

## Explanations

### L1 human

The class number of a number field measures how badly unique factorisation fails in its integers.
The problem asks, for each value of the class number, which imaginary quadratic fields have it.
For class number $1$ the answer is nine fields; for larger class numbers the lists are known up to $100$ by computer-assisted proofs.
