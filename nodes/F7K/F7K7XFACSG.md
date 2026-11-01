---
tag: F7K7XFACSG
kind: statement
role: theorem
name: Cauchy–Davenport theorem
msc: [11P70, 11B13]
uses: [XNBN31HQWB, 03VFZ2WETT, 01826KMG2H]
about: [XNBN31HQWB]
sources:
  - url: https://en.wikipedia.org/wiki/Restricted_sumset
---

## Statement

Let $p$ be a [[prime number|01826KMG2H]], and let $A$ and $B$ be nonempty subsets of the [[integers modulo $p$|03VFZ2WETT]], $\Z/p\Z$.
Then the [[sumset|XNBN31HQWB]] $A + B$ satisfies
$$\abs{A + B} \ge \min(p, \ \abs{A} + \abs{B} - 1).$$

## Remarks

One proof is by induction on $\abs{B}$.
It replaces $(A, B)$ by $(A \cup (B + e), \ B \cap (A - e))$ for a suitable $e$, which keeps $\abs{A} + \abs{B}$ and does not enlarge the sumset.
Another proof uses the [[combinatorial Nullstellensatz|9ZW7BCJMDT]] with a polynomial that vanishes on a too small set $C \supseteq A + B$.
The bound is sharp: for $A = \set{0, 1, \dots, k-1}$ and $B = \set{0, 1, \dots, l-1}$ with $k + l - 1 \le p$, the sumset is $\set{0, \dots, k + l - 2}$.
The hypothesis that $p$ is prime is needed.
In $\Z/4\Z$, take $A = B = \set{0, 2}$; then $A + B = \set{0, 2}$ has $2$ elements, while $\min(4, 3) = 3$.

## Explanations

### L1 human

Work with numbers modulo a prime $p$, on a clock with $p$ hours.
Add every element of a set $A$ to every element of a set $B$.
You get at least $\abs{A} + \abs{B} - 1$ different results, unless you already get all $p$ of them.
So sums modulo a prime cannot bunch up too much.

### L2 human

The Cauchy–Davenport theorem is the analogue for $\Z/p\Z$ of the easy bound $\abs{A + B} \ge \abs{A} + \abs{B} - 1$ for sets of integers.
Over composite moduli, subgroups give smaller sumsets, and Kneser's theorem describes this.
The Dias da Silva–Hamidoune theorem bounds the set of sums of two distinct elements of $A$ by $\min(p, 2\abs{A} - 3)$, as conjectured by Erdős and Heilbronn.
