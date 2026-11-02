---
tag: EB4N9RQR51
kind: concept
name: Basic hypergeometric series
msc: [33D15, 05A30]
specializes: [428M453CR2]
sources:
  - url: https://en.wikipedia.org/wiki/Basic_hypergeometric_series
same_as:
  wikidata: Q1062958
  wikipedia: Basic hypergeometric series
---

## Summary

A basic hypergeometric series, or $q$-hypergeometric series, is a power series $\sum_n c_n z^n$ in which the ratio $c_{n+1}/c_n$ is a rational function of $q^n$.
It is written ${}_r\phi_s(a_1, \dots, a_r; b_1, \dots, b_s; q, z)$ and is built from [[q-Pochhammer symbols|Y1X8ZZQ7VM]].
It is the [[q-analog|GFSDMJHHVA]] of the [[generalized hypergeometric series|VDBAW9PN88]], to which it tends as $q \to 1$ after a change of parameters.
Basic hypergeometric series contain the partition generating functions, the theta products and the $q$-orthogonal polynomials of the Askey scheme.

## Explanations

### L1 human

In an ordinary hypergeometric series, the ratio of two consecutive coefficients is a rational function of the index $n$.
In a basic hypergeometric series, the index $n$ appears only through the power $q^n$ of a fixed number $q$.
The simplest example is $\sum_{n \ge 0} \frac{z^n}{(1-q)(1-q^2)\cdots(1-q^n)}$, which equals $\prod_{k \ge 0} \frac{1}{1 - z q^k}$ for $\abs{q} < 1$ and $\abs{z} < 1$.
With $z = q$, it counts the partitions of each number, by the [[generating function for partitions|0578PA53VA]].
