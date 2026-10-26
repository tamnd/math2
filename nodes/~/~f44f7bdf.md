---
tag: ~f44f7bdf
kind: statement
role: proposition
name: Order of a permutation is the lcm of its cycle lengths
msc: [20B30]
uses: [~aab6149a, ~47dae8e0, ~b576f7df]
sources:
  - url: https://en.wikipedia.org/wiki/Permutation
    locator: Order of a permutation
---

## Statement

Let $\sigma \in S_n$, and let $\sigma = c_1 c_2 \cdots c_r$ be its decomposition into disjoint cycles of lengths $k_1, \dots, k_r$.
Then the [[order|~aabf2e22]] of $\sigma$ is $\operatorname{lcm}(k_1, \dots, k_r)$.

## Remarks

A $k$-cycle has order $k$.
The disjoint cycles commute, so $\sigma^m = c_1^m \cdots c_r^m$, and this is the identity exactly when each $c_i^m$ is the identity.
For example, $(1\ 2)(3\ 4\ 5)$ has order $6$.

## Explanations

### L1 human

A permutation returns to the identity when each of its cycles is back at the start.
A cycle of length $k$ is back at the start after each multiple of $k$ steps.
So you need the first common multiple of all the cycle lengths.
