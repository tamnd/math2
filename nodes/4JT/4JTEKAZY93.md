---
tag: 4JTEKAZY93
kind: proof
name: Proof of term-by-term differentiation
msc: [40A30, 26A24]
proves: 0TJ8QBJX5K
uses: [0MRE6XRE5V, 0M0TKFRX2A, 0HXEX0DPRA, 0K0H5E3Z5N, 0CS42KEM5C]
sources:
  - url: https://dec41.user.srcf.net/notes/IB_M/analysis_ii_thm_proof.pdf
    locator: Section 1, Uniform convergence
---

## Proof

We apply the theorem on sequences of differentiable functions to the partial sums.

1. Let $a < b$, and let $f_n$ and $x_0$ be as in the statement. Let $s_N = \sum_{n=0}^{N} f_n$ be the partial sums of the [[series|0MRE6XRE5V]] $\sum f_n$.
2. Each $s_N$ is differentiable on $[a, b]$, with $s_N' = \sum_{n=0}^{N} f_n'$. This follows from [[linearity of differentiation|0M0TKFRX2A]] and induction on $N$.
3. At the endpoints, the derivatives are [[one-sided|0HXEX0DPRA]]. The proof of linearity applies to one-sided limits in the same way, since a sum of difference quotients is the difference quotient of the sum.
4. By hypothesis, $\sum_n f_n(x_0)$ converges. So the sequence $(s_N(x_0))$ converges, by the definition of a [[convergent series|0K0H5E3Z5N]].
5. By hypothesis, $\sum_n f_n'$ converges uniformly on $[a, b]$. By step 2, this means that $(s_N')$ converges uniformly on $[a, b]$ to the function $g = \sum_{n=0}^{\infty} f_n'$.
6. By steps 2, 4 and 5, the [[theorem on uniform convergence of derivatives|0CS42KEM5C]] applies to $(s_N)$.
7. It gives that $(s_N)$ converges uniformly on $[a, b]$ to a differentiable function $s$, with $s' = g$.
8. By the definition of a series of functions, step 7 says that $\sum f_n$ converges uniformly on $[a, b]$ with sum $s$. So the sum is differentiable, and
$$\Big( \sum_{n=0}^{\infty} f_n \Big)' = s' = g = \sum_{n=0}^{\infty} f_n'.$$

## Idea

A series of functions is the sequence of its partial sums. Finite sums can be differentiated term by term. So the result for sequences, applied to the partial sums, gives the result for series.
