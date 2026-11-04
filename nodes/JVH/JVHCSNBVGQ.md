---
tag: JVHCSNBVGQ
kind: proof
name: Proof of the comparison test
msc: [40A05]
proves: 04Z5G0THN6
uses: [0MX1HZBBXJ, 0NB643K60Q]
sources:
  - url: https://en.wikipedia.org/wiki/Direct_comparison_test
---

## Proof

1. Let $A_N = \sum_{n=0}^{N} a_n$ and $B_N = \sum_{n=0}^{N} b_n$ be the [[partial sums|0NB643K60Q]]. Since $a_n \le b_n$ for every $n$, we have $A_N \le B_N$ for every $N$.
2. Assume that $\sum b_n$ converges, with sum $B$. Since $b_n \ge 0$, the [[criterion for nonnegative series|0MX1HZBBXJ]] gives $B = \sup_N B_N$. So $B_N \le B$ for all $N$.
3. By steps 1 and 2, $A_N \le B$ for all $N$. So the partial sums of $\sum a_n$ are bounded above.
4. Since $a_n \ge 0$, the same criterion shows that $\sum a_n$ converges, with sum $\sup_N A_N$.
5. By step 3, $B$ is an upper bound of the $A_N$. So $\sum a_n = \sup_N A_N \le B = \sum b_n$.
6. Now assume that $\sum a_n$ diverges. If $\sum b_n$ converged, then $\sum a_n$ would converge by steps 2 to 4. So $\sum b_n$ diverges.

## Idea

The partial sums of the smaller series stay below those of the larger one. For nonnegative terms, convergence means bounded partial sums, so a bound for the larger series is also a bound for the smaller one.
