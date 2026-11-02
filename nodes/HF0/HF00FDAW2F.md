---
tag: HF00FDAW2F
kind: definition
name: Ultrafilter on a Boolean algebra
msc: ["06E05", "03G05"]
defines: CQM84EW10G
uses: [0XADJKM699, Z15FXM9WM1]
sources:
  - url: https://en.wikipedia.org/wiki/Ultrafilter
---

## Definition

Let $B$ be a [[Boolean algebra|0XADJKM699]] with order $\le$.
A *filter* of $B$ is a subset $F \subseteq B$ such that $1 \in F$, $a \wedge b \in F$ for all $a, b \in F$, and $b \in F$ whenever $a \in F$ and $a \le b$.
It is *proper* if $0 \notin F$.
An *ultrafilter* of $B$ is a proper filter $U$ such that for every proper filter $F$ with $U \subseteq F$, one has $F = U$.

## Remarks

The filters of $B$ are the nonempty [[order filters|Z15FXM9WM1]] of $B$ seen as a lattice.
For a proper filter $U$, these are equivalent.
(a) $U$ is an ultrafilter.
(b) For every $a \in B$, exactly one of $a$ and $\neg a$ lies in $U$.
(c) $U$ is prime: $a \vee b \in U$ implies $a \in U$ or $b \in U$.
Ultrafilters $U$ correspond to homomorphisms $\chi \colon B \to \set{0, 1}$, by $U = \chi^{-1}(1)$.

Example: in the power set of a set $X$, for $x \in X$, the family $\set{A \subseteq X : x \in A}$ is an ultrafilter.
It is a proper filter, and for each $A$, either $x \in A$ or $x \in X \setminus A$.

Non-example: in the power set of $\set{1, 2}$, the family $F = \set{\set{1, 2}}$ is a proper filter but not an ultrafilter.
It contains neither $\set{1}$ nor its complement $\set{2}$, and it lies in the larger proper filter $\set{\set{1}, \set{1, 2}}$.
