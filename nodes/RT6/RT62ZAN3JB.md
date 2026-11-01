---
tag: RT62ZAN3JB
kind: definition
name: Equidistribution modulo one
msc: [11K06, 11J71]
defines: XM6DH57BWY
uses: [08GR54CKEA, 05M5SWSZZD]
sources:
  - url: https://en.wikipedia.org/wiki/Equidistributed_sequence
---

## Definition

For a real number $x$, let $\{x\} = x - \floor{x}$ be its fractional part, where $\floor{x}$ is the [[floor|08GR54CKEA]] of $x$.
A sequence $(x_n)_{n \ge 1}$ of real numbers is *equidistributed modulo one* if for all real $a, b$ with $0 \le a < b \le 1$,
$$\lim_{N \to \infty} \frac{\#\set{n : 1 \le n \le N, \ \{x_n\} \in [a, b)}}{N} = b - a.$$

## Remarks

Example: for irrational $\alpha$, the sequence $x_n = n\alpha$ is equidistributed modulo one; this is the [[equidistribution theorem|NCCGNTBEYV]].
Non-example: $x_n = n/2$ has $\{x_n\} \in \set{0, 1/2}$, so for $[a, b) = [0.1, 0.4)$ the count is $0$ for every $N$, and the limit $0$ differs from $0.3$.
Weyl's criterion gives an equivalent form: the sequence is equidistributed modulo one if and only if
$$\lim_{N \to \infty} \frac{1}{N} \sum_{n=1}^{N} e^{2\pi i h x_n} = 0$$
for every nonzero integer $h$.
Another equivalent form: $\frac{1}{N} \sum_{n=1}^{N} f(\{x_n\}) \to \int_0^1 f(t)\,dt$ for every continuous function $f$ on $[0, 1]$ with $f(0) = f(1)$.
Some authors also say *uniformly distributed modulo one*.
