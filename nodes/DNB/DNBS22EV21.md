---
tag: DNBS22EV21
kind: definition
name: Dedekind–MacNeille completion
msc: [06B23, 06A06]
defines: DKH4933HMQ
uses: [0QV2JS9RJ3, 0S60DVMVPN, D7A0ZGZT5S, 0G3RRM41X9, 0GSZ7B0CGR]
sources:
  - url: https://en.wikipedia.org/wiki/Dedekind%E2%80%93MacNeille_completion
---

## Definition

Let $(P, \le)$ be a [[partially ordered set|0QV2JS9RJ3]].
For $A \subseteq P$, let $A^u$ be the set of [[upper bounds|0S60DVMVPN]] of $A$ in $P$ and $A^l$ the set of lower bounds of $A$ in $P$.
The *Dedekind–MacNeille completion* of $P$ is the set
$$\operatorname{DM}(P) = \set{A \subseteq P : (A^u)^l = A},$$
ordered by inclusion, together with the map $\iota \colon P \to \operatorname{DM}(P)$, $\iota(x) = \set{y \in P : y \le x}$.

## Remarks

$\operatorname{DM}(P)$ is a [[complete lattice|D7A0ZGZT5S]], whose meets are intersections, and $\iota$ is an order embedding: $x \le y$ if and only if $\iota(x) \subseteq \iota(y)$.
The image of $\iota$ is join-dense and meet-dense: each element of $\operatorname{DM}(P)$ is a supremum and an infimum of elements of $\iota(P)$.
These properties characterize $\operatorname{DM}(P)$ up to isomorphism, and it embeds in every complete lattice that contains $P$ as an ordered subset.
Example: for $P = \Q$, the sets $A = (A^u)^l$ are $\varnothing$, $\Q$, and the sets $\set{q \in \Q : q \le r}$ for $r \in \R$.
So $\operatorname{DM}(\Q)$ is the [[extended real line|0GSZ7B0CGR]], and its proper nonempty elements are closely related to [[Dedekind cuts|0G3RRM41X9]].
Non-example: in $\Q$, the set $A = \set{q \in \Q : q < 0}$ is not in $\operatorname{DM}(\Q)$, because $A^u$ is the set of nonnegative rationals and $(A^u)^l = \set{q : q \le 0} \ne A$.
