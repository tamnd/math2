---
tag: T3RS1TAM7C
kind: definition
name: Bitonic sorter
msc: [68P10, 68Q06, 68W10]
defines: RP5A709FVZ
uses: [G854V12EC7, 0G9EKM0E15]
sources:
  - url: https://en.wikipedia.org/wiki/Bitonic_sorter
---

## Definition

A finite [[sequence|0G9EKM0E15]] $x_1, \dots, x_n$ of real numbers is *bitonic* if some cyclic shift of it is first non-decreasing and then non-increasing.
Let $i < j$.
The comparator $[i:j]$ puts the minimum of the entries in positions $i$ and $j$ in position $i$ and the maximum in position $j$.
The reversed comparator puts the maximum in position $i$ and the minimum in position $j$.
Let $n = 2^k$ with $k \ge 1$.

1. The *half-cleaner* $H_n$ is the layer of the $n/2$ comparators $[i : i + n/2]$ for $1 \le i \le n/2$.
2. The *bitonic merger* $B_n$ is defined by $B_2 = H_2$. For $n \ge 4$, $B_n$ applies $H_n$ and then $B_{n/2}$ to each half in parallel.
3. The *bitonic sorter* $T_n$ is defined by $T_2 = B_2$. For $n \ge 4$, $T_n$ applies $T_{n/2}$ to the first half. In parallel it applies $T_{n/2}$ with every comparator reversed to the second half. Then it applies $B_n$.

## Remarks

Let the input of $H_n$ be bitonic.
Then both halves of the output are bitonic, and every entry of the first half is at most every entry of the second half.
By induction $B_n$ sorts every bitonic input, and $T_n$ sorts every input, so $T_n$ is a [[sorting network|G854V12EC7]].
It has depth $k(k+1)/2$ and $n k (k+1)/4$ comparators.

Example: $(1, 4, 6, 5, 3, 2, 0, 0)$ is bitonic, since it rises to $6$ and then falls.
The half-cleaner $H_8$ compares positions $(1,5), (2,6), (3,7), (4,8)$ and gives $(1, 2, 0, 0, 3, 4, 6, 5)$.
Both halves are bitonic, and every entry of $(1, 2, 0, 0)$ is at most every entry of $(3, 4, 6, 5)$.

Non-example: $(1, 3, 2, 4)$ is not bitonic, because read cyclically it has two peaks, $3$ and $4$, so no cyclic shift of it rises and then falls.
The merger $B_4$, made of $[1:3], [2:4]$ and then $[1:2], [3:4]$, leaves it unsorted: the first layer changes nothing and the second gives $(1, 3, 2, 4)$ again.

Variants replace the reversed comparators by a different wiring of the first merging layer, comparing position $i$ with position $n + 1 - i$.
