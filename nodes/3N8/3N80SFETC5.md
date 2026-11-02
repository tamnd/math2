---
tag: 3N80SFETC5
kind: definition
name: Forcing
msc: ["03E40", "03E35"]
defines: F2DTWW9HP7
uses: [0QV2JS9RJ3, WEDP73Y7GK, 0HE5WDQ9FJ]
sources:
  - url: https://en.wikipedia.org/wiki/Forcing_(mathematics)
---

## Definition

A *forcing notion* is a [[partial order|0QV2JS9RJ3]] $(P, \le)$ with a greatest element $1$.
Its elements are called *conditions*, and $q \le p$ is read "$q$ is stronger than $p$".

Let $M$ be a countable transitive model of [[ZFC|0HE5WDQ9FJ]] with $P \in M$.
A *$P$-name* is a set $\tau$ of pairs $(\sigma, p)$, where $\sigma$ is a $P$-name and $p \in P$; this is a definition by recursion on rank.
For a filter $G \subseteq P$, the *value* of a name is defined by recursion:
$$\tau^G = \set{\sigma^G : (\sigma, p) \in \tau \text{ for some } p \in G}.$$
For a [[generic filter|WEDP73Y7GK]] $G$ over $M$, the *forcing extension* is $M[G] = \set{\tau^G : \tau \in M \text{ is a } P\text{-name}}$.
Let $p \in P$, let $\varphi(x_1, \ldots, x_n)$ be a formula, and let $\tau_1, \ldots, \tau_n \in M$ be names.
The condition $p$ *forces* $\varphi(\tau_1, \ldots, \tau_n)$, written $p \Vdash \varphi(\tau_1, \ldots, \tau_n)$, if $M[G] \models \varphi(\tau_1^G, \ldots, \tau_n^G)$ for every generic $G$ over $M$ with $p \in G$.

## Remarks

The basic theorem of forcing says that $M[G]$ is a countable transitive model of ZFC, that $M \subseteq M[G]$ and $G \in M[G]$, and that $M$ and $M[G]$ have the same ordinals.
The forcing theorem says that a statement holds in $M[G]$ if and only if some $p \in G$ forces it.
It also says that the relation $\Vdash$ restricted to each formula is definable in $M$.
Example: *Cohen forcing* is the set of finite partial functions from $\omega$ to $\set{0, 1}$, ordered by reverse inclusion, with $1 = \emptyset$.
For a generic $G$, the union $\bigcup G$ is a function from $\omega$ to $\set{0, 1}$ that is not in $M$.
A non-example of a forcing notion is a partial order without a greatest element; this is a minor point, since one can add a new top element.
Some authors use preorders instead of partial orders, or write $p \le q$ for "$p$ is weaker", so the notation must be checked in each source.
