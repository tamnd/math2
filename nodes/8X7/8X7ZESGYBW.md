---
tag: 8X7ZESGYBW
kind: definition
name: Khinchin integral
msc: [26A39]
defines: Q1TV4F608D
uses: [4W31MKE01V, ZT6F4C2YHK, 0P27W9RW0G]
sources:
  - url: https://en.wikipedia.org/wiki/Khinchin_integral
---

## Definition

Let $a < b$ be real numbers.
Let $F \colon [a, b] \to \R$ be a function and let $E \subseteq [a, b]$.
The function $F$ is *absolutely continuous on $E$* if the following holds.
For every $\varepsilon > 0$ there is $\delta > 0$ such that for every finite family of non-overlapping intervals $[a_1, b_1], \dots, [a_n, b_n]$ with all endpoints in $E$,
$$\sum_{k=1}^{n} (b_k - a_k) < \delta \quad \text{implies} \quad \sum_{k=1}^{n} \abs{F(b_k) - F(a_k)} < \varepsilon.$$
The function $F$ is *generalized absolutely continuous*, or ACG, on $[a, b]$ if two conditions hold.
First, $F$ is [[continuous|0P27W9RW0G]] on $[a, b]$.
Second, $[a, b]$ is a countable union of sets on each of which $F$ is absolutely continuous.
Let $f \colon [a, b] \to \R$ be a function.
It is *Khinchin integrable* if some ACG function $F$ on $[a, b]$ has [[approximate derivative|4W31MKE01V]] equal to $f(x)$ at almost every $x \in [a, b]$.
The *Khinchin integral* of $f$ is then $\int_a^b f = F(b) - F(a)$.

## Remarks

The integral is well defined: two ACG functions with the same approximate derivative almost everywhere differ by a constant.

Example: let $f$ be Lebesgue integrable on $[a, b]$.
Then $F(x) = \int_a^x f$ is [[absolutely continuous|ZT6F4C2YHK]] on all of $[a, b]$, hence ACG, and $F' = f$ almost everywhere.
So the Khinchin and Lebesgue integrals of $f$ agree.

Non-example of a primitive: the [[Cantor function|NPBYYK63FE]] $c$ is continuous and $c'(x) = 0$ for almost every $x$, but $c$ is not ACG.
If it were, the uniqueness above would force $c$ to be constant, while $c(1) - c(0) = 1$.
