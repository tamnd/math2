---
tag: ~db2ea8fc
kind: definition
name: Cauchy product
msc: [40A05]
defines: ~3aedebf0
uses: [~6612f89e]
sources:
  - url: https://en.wikipedia.org/wiki/Cauchy_product
    locator: Cauchy product of two infinite series
---

## Definition

Let $\sum_{n=0}^{\infty} a_n$ and $\sum_{n=0}^{\infty} b_n$ be real [[series|~6612f89e]].
For each $n$, let $c_n = \sum_{k=0}^{n} a_k b_{n-k}$.
The series $\sum_{n=0}^{\infty} c_n$ is the Cauchy product of the two series.

## Remarks

The term $c_n$ collects all products $a_i b_j$ with $i + j = n$.
For power series, the Cauchy product of $\sum a_n x^n$ and $\sum b_n x^n$ is $\sum c_n x^n$. This is the rule for multiplying polynomials.
The Cauchy product of two convergent series need not converge. [[Mertens' theorem|~92c835ee]] gives a sufficient condition.

## Explanations

### L1 human

To multiply two series, multiply every term of one by every term of the other.
The Cauchy product groups these products by the sum of their indices.
