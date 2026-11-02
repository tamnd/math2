---
tag: TBSBNJFD2P
kind: example
name: Crown
msc: [06A07]
instance_of: [0QV2JS9RJ3]
illustrates: [JC4J24MF93]
uses: [W8DZ5KGGHN, 1P4830BH6Z]
sources:
  - url: https://en.wikipedia.org/wiki/Crown_graph
---

## Example

Let $n \ge 3$.
The crown $S_n$ is the [[partially ordered set|0QV2JS9RJ3]] on $2n$ elements $a_1, \ldots, a_n, b_1, \ldots, b_n$ whose only strict relations are $a_i < b_j$ for all $i \ne j$.
It is also called the standard example of dimension $n$, because its [[order dimension|JC4J24MF93]] is $n$.
Some authors use the name crown for a different poset of height $2$, whose comparability graph is a cycle of length $2n$.

Lower bound.
For each $i$, the elements $a_i$ and $b_i$ are incomparable, so a realizer needs a [[linear extension|W8DZ5KGGHN]] $L$ with $b_i$ before $a_i$.
Suppose one linear extension $L$ has $b_i$ before $a_i$ and $b_j$ before $a_j$ with $i \ne j$.
Since $a_i < b_j$ and $a_j < b_i$, $L$ would contain the cycle $a_i, b_j, a_j, b_i, a_i$, which is impossible.
So each linear extension reverses at most one pair, and at least $n$ linear extensions are needed.

Upper bound.
For each $i$, let $L_i$ be the following order.
First come the $a_j$ with $j \ne i$, in increasing order of $j$, then $b_i$, then $a_i$.
Last come the $b_j$ with $j \ne i$, in increasing order of $j$.
Each $L_i$ is a linear extension, and every incomparable pair appears in both relative orders among $L_1, \ldots, L_n$, so these $n$ orders form a realizer.

## Remarks

The [[comparability graph|1P4830BH6Z]] of $S_n$ is the crown graph: the complete bipartite graph $K_{n,n}$ with a perfect matching removed.
The crown $S_n$ has height $2$ and width $n$, so it shows that the dimension of a poset of height $2$ can be as large as one likes.

## Explanations

### L1 human

Draw $n$ points in a bottom row and $n$ points in a top row.
Join each bottom point to every top point except the one just above it.
This poset needs $n$ different total orders to describe it exactly, because each total order can account for only one missing link.
