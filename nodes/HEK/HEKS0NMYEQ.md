---
tag: HEKS0NMYEQ
kind: definition
name: Exponential sum
msc: [11L03, 11L07]
defines: 97PBMQCPPM
uses: [07GJV36896]
sources:
  - url: https://en.wikipedia.org/wiki/Exponential_sum
---

## Definition

For a real number $x$, write $e(x) = e^{2\pi i x}$, where $e^{z}$ is the [[complex exponential|07GJV36896]].
Let $A$ be a finite set of integers, and let $f \colon A \to \R$ be a function.
The *exponential sum* of $f$ over $A$ is the complex number
$$S = \sum_{n \in A} e(f(n)).$$
Most often $A$ is an interval $\set{n \in \Z : M < n \le M + N}$.

## Remarks

Each term has absolute value $1$, so $\abs{S} \le \#A$; this is the trivial bound.
Example: for $f(n) = n\alpha$ with $\alpha \in \R \setminus \Z$ and $A = \set{1, \dots, N}$, the sum is geometric and
$$\abs{S} = \abs{\frac{e(N\alpha) - 1}{e(\alpha) - 1}} \le \frac{1}{\abs{\sin \pi \alpha}},$$
a bound independent of $N$.
Non-example: $\sum_{n=1}^{N} 2^n$ is a sum of values of an exponential function, but it is not an exponential sum in this sense.
Its terms have absolute value larger than $1$, so they are not of the form $e(f(n))$ with $f$ real.
When $f$ is a polynomial, $S$ is called a Weyl sum.
Sums with weights, $\sum_{n \in A} a_n e(f(n))$ with complex $a_n$, are also called exponential sums.
