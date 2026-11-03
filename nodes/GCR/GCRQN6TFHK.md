---
tag: GCRQN6TFHK
kind: statement
role: theorem
name: Johnson bound
msc: [94B65, 94B25]
uses: [TAE6K8NQ46, EP5HNGSXFA, K8ZHAQAK2B]
about: [TAE6K8NQ46]
sources:
  - url: https://en.wikipedia.org/wiki/Johnson_bound
same_as:
  wikidata: Q4351986
  wikipedia: Johnson bound
---

## Statement

Let $n \ge 1$, $d \ge 1$ and $0 \le w \le n$ be integers.
Let $A(n, d, w)$ be the largest number of words in $\set{0, 1}^n$ of [[Hamming weight|K8ZHAQAK2B]] exactly $w$ whose pairwise [[Hamming distances|EP5HNGSXFA]] are at least $d$.

1. If $1 \le w \le n$, then $A(n, d, w) \le \floor{\frac{n}{w} A(n - 1, d, w - 1)}$.
2. If $\delta$ is an integer with $1 \le \delta \le w$, then
$$A(n, 2\delta, w) \le \floor{\frac{n}{w} \floor{\frac{n - 1}{w - 1} \floor{\cdots \floor{\frac{n - w + \delta}{\delta}} \cdots}}}.$$

## Remarks

For part 1, take an optimal constant-weight code $C$ and count the pairs (codeword, position where it has a $1$) in two ways.
There are $\abs{C} w$ such pairs.
Fix a position, and delete it from the codewords that have a $1$ there.
This gives a code of length $n - 1$, weight $w - 1$ and distance at least $d$, so there are at most $A(n - 1, d, w - 1)$ such codewords.
Hence $\abs{C} w \le n A(n - 1, d, w - 1)$.
Part 2 follows by applying part 1 $w - \delta$ times and using $A(m, 2\delta, \delta) = \floor{m/\delta}$, since words of weight $\delta$ at distance at least $2\delta$ have disjoint supports.
Example: $A(7, 4, 3) \le \floor{\frac{7}{3} \cdot 3} = 7$.
The $7$ lines of the Fano plane, as words of weight $3$ in $\set{0,1}^7$, meet the bound: two lines share one point, so they are at distance $4$.
Distances between words of the same weight are even, which is why part 2 uses $d = 2\delta$.

## Explanations

### L1 human

Constant-weight codes are sets of words with the same number of ones that pairwise differ a lot.
The Johnson bound limits their size by a simple count: fix a position, look at the codewords with a one there, and repeat.
These bounds are useful in themselves, for example in the theory of block designs.

### L2 human

The bounds on $A(n, d, w)$ feed into bounds on unrestricted codes: Johnson used them to sharpen the Hamming bound, by counting words at distance $t + 1$ from the code.
A related Johnson bound in list decoding states that a Hamming ball of radius somewhat below the minimum distance contains only few codewords.
That form is the key step in the proof of the Elias–Bassalygo bound.
