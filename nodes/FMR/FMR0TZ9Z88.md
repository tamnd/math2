---
tag: FMR0TZ9Z88
kind: statement
role: theorem
name: Zero–one principle for sorting networks
msc: [68P10, 68Q06]
uses: [G854V12EC7, 0FRXBVVR03, 0A7KV2WB7A]
about: [G854V12EC7]
sources:
  - url: https://en.wikipedia.org/wiki/Sorting_network
    locator: Zero-one principle
---

## Statement

Let $N$ be a comparator network on $n$ wires, as in the definition of a [[sorting network|G854V12EC7]].
If $N$ sorts every input in $\set{0,1}^n$, then $N$ sorts every input in $X^n$ for every [[totally ordered set|0FRXBVVR03]] $X$.

## Remarks

The key fact is that comparators commute with [[monotone maps|0A7KV2WB7A]]: if $g \colon X \to Y$ is non-decreasing, then $\min(g(a), g(b)) = g(\min(a, b))$ and the same for $\max$, so $N(g(x)) = g(N(x))$ entrywise.
Suppose $N$ fails on some $x \in X^n$, so the output $y = N(x)$ has $y_k > y_{k+1}$ for some $k$.
Let $g(t) = 1$ if $t \ge y_k$ and $g(t) = 0$ otherwise; $g$ is non-decreasing.
Then $N(g(x)) = g(y)$ has a $1$ at position $k$ and a $0$ at position $k+1$, so $N$ fails on the $0$-$1$ input $g(x)$.
So to verify a network on $n$ wires it suffices to test $2^n$ inputs instead of all $n!$ orderings.
For example, $[1,2], [2,3]$ fails on the $0$-$1$ input $(1, 1, 0)$, which it maps to $(1, 0, 1)$, and this matches its failure on $(3, 2, 1)$.

## Explanations

### L1 human

To check that a network of compare-and-swap boxes sorts all lists of numbers, it is enough to check lists of zeros and ones.
The reason is that a comparator does the same thing whether it sees numbers or just the information "big" or "small".

### L2 human

The principle is the standard tool for proving that constructions such as Batcher's odd–even mergesort and the bitonic sorter are correct.
It also helps computer searches for optimal small networks, since it reduces the test set to $2^n$ inputs, and further to the $2^n - n - 1$ inputs that are not already sorted.
It holds only for comparator networks, whose operations are data-independent; it says nothing about general sorting algorithms.
