---
tag: 51GRFQ4WY6
kind: concept
name: Rademacher functions
msc: [42C10, 60G50]
sources:
  - url: https://en.wikipedia.org/wiki/Rademacher_system
same_as:
  wikidata: Q2125570
  wikipedia: Rademacher system
---

## Summary

The Rademacher functions $r_1, r_2, \dots$ on $[0, 1)$ are square waves that record the binary digits of a point.
The value $r_k(t)$ is $1$ or $-1$ according as the $k$-th binary digit of $t$ is $0$ or $1$.
They form an orthonormal system in $L^2([0, 1))$ which is not complete.
For [[Lebesgue measure|2Z2QVWZ262]] they are independent random signs, so they model coin tossing inside analysis.
Their finite products are the [[Walsh functions|F12A5QKW8Z]].

## Explanations

### L1 human

Split $[0, 1)$ into halves and put $+1$ on the left half and $-1$ on the right: that is $r_1$.
Split into quarters and alternate $+1, -1, +1, -1$: that is $r_2$.
Each next function flips twice as fast.
If one picks $t$ at random, the values $r_1(t), r_2(t), \dots$ behave like fair coin tosses, one for each binary digit of $t$.
