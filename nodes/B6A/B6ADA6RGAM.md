---
tag: B6ADA6RGAM
kind: definition
name: Sorting algorithm
msc: [68P10, 68W40]
defines: MGKDQAM7K3
uses: [9DMSG5HAQX, 0FRXBVVR03, 05RWFKVTJ7]
sources:
  - url: https://en.wikipedia.org/wiki/Sorting_algorithm
---

## Definition

Let $(X, \le)$ be a [[totally ordered set|0FRXBVVR03]].
A *sorting algorithm* for $X$ is an [[algorithm|9DMSG5HAQX]] whose inputs are finite sequences $(a_1, \dots, a_n)$ over $X$.
On each input it outputs a sequence $(a_{\sigma(1)}, \dots, a_{\sigma(n)})$ such that:

1. $\sigma$ is a [[permutation|05RWFKVTJ7]] of $\set{1, \dots, n}$;
2. $a_{\sigma(1)} \le a_{\sigma(2)} \le \cdots \le a_{\sigma(n)}$.

The algorithm is *stable* if moreover $\sigma(i) < \sigma(j)$ whenever $i < j$ and $a_{\sigma(i)} = a_{\sigma(j)}$.
It is a *comparison sort* if it accesses the elements only through tests of the form $a_i \le a_j$.

## Remarks

In practice one often sorts records by a key, and $\le$ is then a total preorder on records.
Stability matters only in that setting, or when equal elements can be told apart.

Example: on input $(3, 1, 2)$, the output $(1, 2, 3)$ is correct, with $\sigma = (2, 3, 1)$ in one-line notation, so $\sigma(1) = 2$, $\sigma(2) = 3$, $\sigma(3) = 1$.

Non-example: an algorithm that outputs $(1, 1, 2)$ on $(2, 1, 1, 3)$ fails clause 1, since its output is not a rearrangement of all four input elements.
An algorithm that outputs its input unchanged fails clause 2 on $(2, 1)$.
