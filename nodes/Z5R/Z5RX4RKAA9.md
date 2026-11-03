---
tag: Z5RX4RKAA9
kind: statement
role: theorem
name: Limiting proportion of derangements
msc: [05A05, 05A16]
uses: [0TH61JR04G, 03WY4HHMT1, 03RSJXF728]
sources:
  - url: https://github.com/mitchkeller/applied-combinatorics/blob/ebd95d6bd59e23c633c65cf560bcb93efa912aae/source/s_inclusion-exclusion_derangements.ptx#L81
    locator: source/s_inclusion-exclusion_derangements.ptx:81
---

## Statement

For each positive integer $n$, let $d_n$ be the [[number of derangements|03WY4HHMT1]] of the set $\{1,\dots,n\}$, that is, the number of [[derangements|0TH61JR04G]] of that set.
Then the ratio $d_n/n!$ converges as $n \to \infty$, and
$$\lim_{n\to\infty} \frac{d_n}{n!} = \frac{1}{e}.$$

Since $n!$ is the number of all permutations of the set, this says that the proportion of permutations without a fixed point tends to $1/e$.

## Remarks

The limit follows from the [[formula for the number of derangements|03RSJXF728]]. It gives $d_n/n!$ as a partial sum of the series for $e^{-1}$.
