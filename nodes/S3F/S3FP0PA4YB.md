---
tag: S3FP0PA4YB
kind: definition
name: Root locus
msc: [93B55, 93C05, 30C15]
defines: 69VWJKXK74
uses: [86JKV3TRFD, RYTSV821V8, 019MA1VTR2, 0CTE7A31XQ]
sources:
  - url: https://en.wikipedia.org/wiki/Root_locus_analysis
---

## Definition

Let $G = n/d$ be the open-loop [[transfer function|86JKV3TRFD]] of a single-input single-output system.
Here $n$ and $d$ are real polynomials with no common [[root|019MA1VTR2]] and $\deg n \le \deg d$.
For a real gain $K \ge 0$, close the unity negative feedback loop around $KG$.
Its [[closed-loop transfer function|RYTSV821V8]] is $KG/(1 + KG) = Kn/(d + Kn)$, with poles at the roots of $d + Kn$.
The *root locus* of $G$ is the following subset of the [[complex plane|0CTE7A31XQ]]:
$$\set{s \in \C : d(s) + K n(s) = 0 \text{ for some } K \ge 0}.$$
It is viewed as the union of the paths of the roots of $d + Kn$ as $K$ runs from $0$ to $\infty$.

## Remarks

At $K = 0$ the roots are the poles of $G$, the roots of $d$.
As $K \to \infty$, $\deg n$ of the paths tend to the zeros of $G$, the roots of $n$, and the other $\deg d - \deg n$ paths tend to infinity.
A point $s$ that is not a pole or zero of $G$ lies on the locus if and only if $G(s)$ is a negative real number.
Equivalently, $\arg G(s) = 180^\circ$ modulo $360^\circ$.

Example: for $G(s) = 1/(s(s + 2))$, the closed-loop poles are the roots of $s^2 + 2s + K$, namely $-1 \pm \sqrt{1 - K}$.
For $0 \le K \le 1$ they lie on the segment $[-2, 0]$.
For $K > 1$ they are $-1 \pm i\sqrt{K - 1}$, on the line $\operatorname{Re} s = -1$.
So the root locus is $[-2, 0]$ together with that line.

Non-example: the point $s = 1$ is not on this locus, since $s^2 + 2s + K = 3 + K > 0$ for all $K \ge 0$.
