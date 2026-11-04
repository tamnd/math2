---
kind: statement
msc:
- 05A15
- 05C05
name: Generating function of binary trees by leaves
role: theorem
sources:
- locator: source/s_recurrence_rubots.ptx:64
  url: https://github.com/mitchkeller/applied-combinatorics/blob/ebd95d6bd59e23c633c65cf560bcb93efa912aae/source/s_recurrence_rubots.ptx#L64
tag: ~bded895a
uses:
- 0PHAC833JF
- 092DRBFKMG
---

## Statement

Let $c_n$ be the number of rooted, unlabeled, ordered binary trees with $n$ leaves, for $n \ge 1$. Here each node that is not a leaf has exactly two children, in a fixed left to right order.

Then the [[generating function|0PHAC833JF]] $C(x) = \sum_{n \ge 1} c_n x^n$ is
$$C(x) = \frac{1 - \sqrt{1 - 4x}}{2} = \sum_{n=1}^{\infty} \frac{1}{n} \binom{2n-2}{n-1} x^n.$$

## Remarks

So $c_n = \frac{1}{n}\binom{2n-2}{n-1}$, which is the [[Catalan number|092DRBFKMG]] $C_{n-1}$.
Example: $c_1 = 1$, $c_2 = 1$, $c_3 = 2$, $c_4 = 5$.
Splitting a tree at the root gives $C(x) = x + C(x)^2$, and the square root form is the root of this quadratic that vanishes at $x = 0$.
