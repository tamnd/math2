---
tag: 8YTFTSRRFS
kind: definition
name: Binary search
msc: [68P10, 68W40]
defines: V67H7YCQ17
uses: [9DMSG5HAQX, 0FRXBVVR03]
sources:
  - url: https://en.wikipedia.org/wiki/Binary_search
---

## Definition

Let $(X, \le)$ be a [[totally ordered set|0FRXBVVR03]], let $a_1 \le a_2 \le \cdots \le a_n$ be a sorted array over $X$, and let $t \in X$ be a target.
*Binary search* is the [[algorithm|9DMSG5HAQX]] that keeps two indices $\ell$ and $r$, starting with $\ell = 1$ and $r = n$, and repeats the following:

1. if $\ell > r$, stop and report that $t$ does not occur;
2. otherwise let $m = \floor{(\ell + r)/2}$;
3. if $a_m = t$, stop and return $m$; if $a_m < t$, set $\ell = m + 1$; if $a_m > t$, set $r = m - 1$.

## Remarks

The invariant is: if $t$ occurs in the array, then it occurs among $a_\ell, \dots, a_r$.
It holds at the start, and step 3 keeps it because the array is sorted.
The length $r - \ell + 1$ of the range drops from $s$ to at most $\floor{s/2}$ at each round, so there are at most $\floor{\log_2 n} + 1$ rounds.

Example: for $(1, 3, 5, 7, 9, 11)$ and $t = 9$: $m = 3$ and $a_3 = 5 < 9$, so $\ell = 4$; then $m = 5$ and $a_5 = 9$, so the search returns $5$.

Non-example: take the unsorted array $(5, 1, 3)$ and $t = 5$.
The first round finds $a_2 = 1 < 5$ and sets $\ell = 3$.
The second finds $a_3 = 3 < 5$, and the search wrongly reports that $5$ does not occur.
So the hypothesis that the array is sorted is needed.
