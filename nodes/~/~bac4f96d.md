---
tag: ~bac4f96d
kind: definition
name: Partition function
msc: [11P81]
defines: ~90906c74
uses: [~0091dfba]
sources:
  - url: https://en.wikipedia.org/wiki/Partition_function_(number_theory)
    locator: Definition and examples
---

## Definition

The partition function is the function $p : \mathbb{N} \to \mathbb{N}$ such that $p(n)$ is the number of [[partitions|~0091dfba]] of $n$.

## Remarks

The values for $n = 0, 1, \dots, 10$ are $1, 1, 2, 3, 5, 7, 11, 15, 22, 30, 42$.
The [[generating function for partitions|~4acf294a]] is $\sum_{n \ge 0} p(n) x^n = \prod_{k \ge 1} \frac{1}{1 - x^k}$.
The function grows faster than any polynomial and slower than any exponential $c^n$ with $c > 1$.

## Explanations

### L1 human

$p(n)$ counts the ways to write $n$ as a sum of positive integers in any order.
For example, $p(5) = 7$: $5$, $4+1$, $3+2$, $3+1+1$, $2+2+1$, $2+1+1+1$ and $1+1+1+1+1$.
