---
tag: H5CW67CCST
kind: definition
name: Many-one reduction
msc: [03D30]
defines: JTAH37JTHD
uses: [KZSB5E471K, PPGD5KW8JC, TN9G24VABN]
sources:
  - url: https://en.wikipedia.org/wiki/Many-one_reduction
---

## Definition

Let $A$ and $B$ be subsets of $\N$.
A *many-one reduction* from $A$ to $B$ is a total [[computable function|KZSB5E471K]] $f \colon \N \to \N$ such that for every $x \in \N$,
$$x \in A \iff f(x) \in B.$$
The set $A$ is *many-one reducible* to $B$, written $A \le_m B$, if such an $f$ exists.
The sets $A$ and $B$ are *many-one equivalent*, written $A \equiv_m B$, if $A \le_m B$ and $B \le_m A$.

## Remarks

Example: let $E$ be the set of even numbers and let $f(x) = 0$ for even $x$ and $f(x) = 1$ for odd $x$.
Then $f$ is total and computable, and $x \in E$ holds exactly when $f(x) \in \set{0}$, so $E \le_m \set{0}$.

Non-example: the empty set is not many-one reducible to $\N$.
For any $f$, the point $0 \notin \emptyset$ would need $f(0) \notin \N$, which is impossible.

The relation $\le_m$ is reflexive and transitive.
If $A \le_m B$ and $B$ is a [[computable set|PPGD5KW8JC]], then $A$ is computable.
If $A \le_m B$ and $B$ is [[computably enumerable|TN9G24VABN]], then $A$ is computably enumerable.
