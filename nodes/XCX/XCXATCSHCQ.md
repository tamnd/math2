---
tag: XCXATCSHCQ
kind: definition
name: Quicksort
msc: [68P10, 68W40, 68W20]
defines: Q9B393M2AV
uses: [MGKDQAM7K3, G9NFJ55KCX, 0NANDX7V02]
sources:
  - url: https://en.wikipedia.org/wiki/Quicksort
---

## Definition

Let $(X, \le)$ be a totally ordered set, and fix a rule that chooses an index $k \in \set{1, \dots, n}$, the *pivot index*, for each sequence of length $n \ge 1$.
*Quicksort* is the [[sorting algorithm|MGKDQAM7K3]] defined recursively on $a = (a_1, \dots, a_n)$:

1. if $n \le 1$, return $a$;
2. otherwise let $x = a_k$ be the pivot, and let $L$ and $R$ be the subsequences of the $a_i$ with $i \ne k$ and $a_i < x$, respectively $a_i \ge x$;
3. return the quicksort of $L$, followed by $x$, followed by the quicksort of $R$.

In *randomized quicksort*, $k$ is chosen uniformly at random and independently at each call.

## Remarks

Both $L$ and $R$ have fewer than $n$ elements, so the recursion stops.
With the rule $k = 1$, a sorted input of $n$ elements gives $L$ empty at every step and $\binom{n}{2} = n(n-1)/2$ comparisons, the worst case.
For randomized quicksort on $n$ distinct elements, the expected number of comparisons is
$$2(n + 1) H_n - 4n = 2 n \ln n + O(n),$$
where $H_n$ is the $n$-th [[harmonic number|0NANDX7V02]].
For the proof, take the $i$-th and $j$-th smallest elements, with $i < j$.
They are compared exactly when one of them is the first pivot chosen among the $j - i + 1$ elements between them, which has probability $2/(j - i + 1)$.

Example: with $k = 1$ on $(2, 3, 1)$, the pivot is $2$, $L = (1)$ and $R = (3)$, and the output is $(1, 2, 3)$.

Non-example: suppose step 2 dropped the elements $a_i$ with $i \ne k$ and $a_i = x$.
Then the output on $(1, 1)$ would be $(1)$, which is not a rearrangement of the input.
