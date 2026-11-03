---
tag: 5DYWS7DVQJ
kind: definition
name: Insertion sort
msc: [68P10, 68W40]
defines: XA3JEEDC59
uses: [MGKDQAM7K3]
sources:
  - url: https://en.wikipedia.org/wiki/Insertion_sort
---

## Definition

Let $(X, \le)$ be a totally ordered set.
Let $x \in X$ and let $s = (s_1, \dots, s_k)$ be a sorted sequence over $X$.
Let $j$ be the largest index in $\set{0, \dots, k}$ with $j = 0$ or $s_j \le x$.
The *insertion* of $x$ into $s$ is the sequence $(s_1, \dots, s_j, x, s_{j+1}, \dots, s_k)$.
*Insertion sort* is the [[sorting algorithm|MGKDQAM7K3]] that, on input $(a_1, \dots, a_n)$, starts with the empty sequence $s^{(0)}$.
For $i = 1, \dots, n$ it lets $s^{(i)}$ be the insertion of $a_i$ into $s^{(i-1)}$, and it returns $s^{(n)}$.

## Remarks

In the usual array version, $j$ is found by comparing $x$ with $s_k, s_{k-1}, \dots$ from the right and shifting each larger element one place.
The number of shifts equals the number of inversions of the input, the pairs $i < j$ with $a_i > a_j$.
So the running time is $\Theta(n + \mathrm{inv})$, where $\mathrm{inv}$ is the number of inversions; it is $\Theta(n^2)$ on the reversed list, which has $n(n-1)/2$ inversions.
Inserting after all equal elements makes the algorithm stable.

Example: on $(2, 3, 1)$ one gets $s^{(1)} = (2)$, $s^{(2)} = (2, 3)$ since $2 \le 3$, and $s^{(3)} = (1, 2, 3)$, since $j = 0$ for $x = 1$.

Non-example: appending each $a_i$ at the end of $s^{(i-1)}$ instead of at position $j + 1$ just copies the input, and $(2, 1)$ stays unsorted.
