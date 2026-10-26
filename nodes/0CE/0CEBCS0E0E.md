---
tag: 0CEBCS0E0E
kind: statement
role: theorem
name: Number of permutations
msc: [05A05]
uses: [05099E1NMJ, 0WFCGVMRRC, 0BQMWCNS8S]
sources:
  - url: https://en.wikipedia.org/wiki/Permutation
    locator: Permutations of totally ordered sets
---

## Statement

Let $X$ be a finite set with $|X| = n$.
Then the number of [[permutations|0BQMWCNS8S]] of $X$ is $n!$.

## Remarks

For $n = 3$ there are $3! = 6$ permutations of $\{1, 2, 3\}$: $123$, $132$, $213$, $231$, $312$ and $321$.
The count follows from the [[rule of product|0VPK4X73Q0]]. The image of the first element has $n$ choices, the image of the second has $n - 1$ choices, and so on.
It is the case $k = n$ of the [[number of injections|0X0N833FF8]].

## Explanations

### L1 human

To arrange $n$ different objects in a row, you have $n$ choices for the first place, then $n - 1$ for the second, and so on.
The product of these numbers is $n!$.
