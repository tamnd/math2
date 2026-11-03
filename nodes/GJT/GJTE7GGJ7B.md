---
tag: GJTE7GGJ7B
kind: statement
role: theorem
name: Comparison sort lower bound
msc: [68P10, 68Q25, 68W40]
uses: [MGKDQAM7K3, 8ZVN9X9WEC, 0D7EZ10V2R, 0KC0F51T6A, 05RWFKVTJ7]
about: [MGKDQAM7K3]
sources:
  - url: https://en.wikipedia.org/wiki/Comparison_sort
---

## Statement

Let $n \ge 1$, and let $\mathcal{A}$ be a deterministic comparison sort.
Then there is an input of $n$ distinct elements on which $\mathcal{A}$ performs at least $\ceil{\log_2 (n!)}$ comparisons.
Moreover, if the input is a uniformly random ordering of $n$ distinct elements, the expected number of comparisons of $\mathcal{A}$ is at least $\log_2 (n!)$.
Since $\log_2(n!) = n \log_2 n - n \log_2 e + O(\log n)$, both bounds are $\Omega(n \log n)$.

## Remarks

The proof models $\mathcal{A}$ on inputs of size $n$ as a [[decision tree|8ZVN9X9WEC]]: a [[binary tree|0D7EZ10V2R]] whose internal nodes are comparisons and whose leaves are outputs.
The $n!$ orderings of distinct elements need $n!$ different outputs, so the tree has at least $n!$ leaves.
A binary tree of height $h$ has at most $2^h$ leaves, so $h \ge \log_2(n!)$, and the height is the worst-case number of comparisons.
For the average, a binary tree with $L$ leaves has average leaf depth at least $\log_2 L$.
The estimate of $\log_2(n!)$ follows from [[Stirling's formula|0KC0F51T6A]].

Example: for $n = 3$, $\ceil{\log_2 6} = 3$, so no comparison sort sorts every list of $3$ distinct items with $2$ comparisons; $2$ comparisons give only $4$ possible outcomes, fewer than the $6$ orderings.
[[Merge sort|GNGVP9EE8Y]] uses $O(n \log n)$ comparisons, so the bound is optimal up to a constant factor.

The hypothesis that only comparisons are used is necessary.
Counting sort sorts $n$ integers in $\set{1, \dots, k}$ in $O(n + k)$ steps, which is $O(n)$ when $k = O(n)$, by using the values themselves as array indices.

## Explanations

### L1 human

Each comparison answers one yes-or-no question, so it can at most halve the number of possible orders still in play.
There are $n!$ possible orders of $n$ items, and halving $n!$ down to $1$ takes about $\log_2(n!)$ steps.
So any method that sorts by comparing pairs needs roughly $n \log_2 n$ comparisons.

### L2 human

This is the standard example of a lower bound in a restricted [[model of computation|YFHEG4GYHW]], the decision tree model.
It shows that merge sort and heapsort are asymptotically optimal among comparison sorts.
The average case of randomized [[quicksort|Q9B393M2AV]], about $1.39\, n \log_2 n$ comparisons, is within a constant factor of optimal.
The same counting argument shows that finding an element in a sorted list by comparisons needs about $\log_2 n$ steps, matching [[binary search|V67H7YCQ17]].
