---
tag: QGNCCJ125J
kind: definition
name: Generic filter
msc: ["03E40"]
defines: WEDP73Y7GK
uses: [0QV2JS9RJ3]
sources:
  - url: https://en.wikipedia.org/wiki/Generic_filter
---

## Definition

Let $(P, \le)$ be a [[partial order|0QV2JS9RJ3]], and let $M$ be a set or class.
A subset $D \subseteq P$ is *dense* if for every $p \in P$ there is $q \in D$ with $q \le p$.
A subset $G \subseteq P$ is a *filter* if:

1. $G$ is nonempty.
2. If $p \in G$ and $p \le q$, then $q \in G$.
3. If $p, q \in G$, then there is $r \in G$ with $r \le p$ and $r \le q$.

A filter $G$ is *generic over $M$*, or *$M$-generic*, if $G \cap D \neq \emptyset$ for every dense set $D \subseteq P$ with $D \in M$.

## Remarks

If $P$ has a least element $0$, then $G = P$ is generic over every $M$: each dense set $D$ contains some $q \le 0$, so $0 \in D$.
Non-example: let $P$ be the set of finite partial functions from $\omega$ to $\set{0, 1}$, ordered by reverse inclusion.
Let $M$ be a transitive model of ZFC with $P \in M$, and let $G \in M$ be a filter.
The set $D = P \setminus G$ is in $M$, and it is dense.
Given $p$, pick $n \notin \operatorname{dom} p$, and extend $p$ at $n$ by a value that disagrees with $\bigcup G$ at $n$, or by any value if $\bigcup G$ is undefined at $n$.
So $G \cap D = \emptyset$, and $G$ is not generic over $M$.
If $M$ is countable, the Rasiowa–Sikorski lemma gives, for each $p \in P$, a generic filter over $M$ that contains $p$.
Some authors also allow open dense sets or maximal antichains in the definition; these give the same notion of genericity.
