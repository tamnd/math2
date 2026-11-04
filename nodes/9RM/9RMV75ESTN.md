---
tag: 9RMV75ESTN
kind: proof
name: Proof of the order of the symmetric group
msc: [20B30]
proves: 0PCKBBMEXC
uses: [0RJMNEN3BJ, 0BQMWCNS8S, 0SEX9F9J5Z, 0CEBCS0E0E]
sources:
  - url: https://en.wikipedia.org/wiki/Permutation
    locator: Properties
---

## Proof

1. Let $n$ be a positive integer and let $X = \{1, 2, \dots, n\}$, a set with $n$ elements.
2. By the definition of the [[symmetric group|0RJMNEN3BJ]], $S_n = \operatorname{Sym}(X)$ is the set of all bijections from $X$ to $X$.
3. These bijections are exactly the [[permutations|0BQMWCNS8S]] of $X$.
4. By the [[number of permutations|0CEBCS0E0E]], $X$ has exactly $n!$ permutations.
5. The [[order|0SEX9F9J5Z]] of $S_n$ is the number of its elements. By steps 2 to 4, it is $n!$.

## Idea

The group $S_n$ is just the set of permutations of $n$ symbols with composition. So its order is the number of such permutations, which is $n!$ by a counting argument. The image of $1$ has $n$ choices, the image of $2$ then has $n - 1$ choices, and so on.
