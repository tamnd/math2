---
tag: HJVRBDQSGG
kind: concept
name: Fraïssé limit
aliases: [fraisse-limit, fraisse-class]
msc: ["03C15", "03C52"]
topics: [ZS8X8KS54R]
audience: grad
uses: [~41dc9926, XSCSX39GEZ, ~3b0d5f2d, ~7468669e, ~8123841a, 01TQB88H4C, 983GZBQYT4, A22K1X8GKD]
sources:
  - url: https://en.wikipedia.org/wiki/Fraïssé_limit
    locator: Fraïssé's theorem
  - book: isbn:9780521587136
same_as:
  wikidata: Q85850626
  wikipedia: Fraïssé limit
---

## Summary

A *Fraïssé class* is a nonempty class $\mathcal{K}$ of finitely generated [[structures|983GZBQYT4]], closed under isomorphism, with countably many isomorphism types, the hereditary property, the [[joint embedding property|~3b0d5f2d]] and the [[amalgamation property|XSCSX39GEZ]].
Its *Fraïssé limit* is the [[countable|01TQB88H4C]] [[ultrahomogeneous|~7468669e]] structure whose [[age|~41dc9926]] is $\mathcal{K}$.
[[Fraïssé's theorem|~8123841a]] says that the limit exists and is unique up to isomorphism.
The rational order is the limit of the finite linear orders, and the [[Rado graph|RMXR0FEF54]] is the limit of the finite graphs.
The limit is the most symmetric countable structure that contains every member of the class and nothing else of finite size.

## Motivation

Many central countable structures are characterized by a "richness" property: every finite configuration that could occur does occur, in every possible position.
Fraïssé limits make this precise and uniform.
One describes the finite pieces, checks amalgamation, and gets a unique countable structure for free.
The construction turns combinatorial facts about a class of finite objects into model-theoretic and group-theoretic facts about one countable object and its automorphism group.

## Notation

The limit of $\mathcal{K}$ is written $\operatorname{Flim}(\mathcal{K})$ in much of the literature on automorphism groups.
Some authors write "generic structure" or "universal homogeneous structure" for the same object.
The formal definition is [[this definition|HJBYFPJEQ1]].

## Remarks

### Examples

- $(\Q, <)$ is the limit of the finite linear orders; see [[this example|~4627e0e4]].
- The countable atomless Boolean algebra is the limit of the finite Boolean algebras; see [[this example|~efa643d7]].
- The algebraic closure of $\mathbb{F}_p$ is the limit of the finite fields of characteristic $p$; see [[this example|~7dcd06ac]].
- The Rado graph, and the [[Henson graphs|TZT25G2YB3]] as limits of the finite $K_n$-free graphs.
- A countably infinite set is the limit of the finite sets in the empty signature.

### Non-examples

- $(\Z, <)$ has the right age but is not ultrahomogeneous; see [[this non-example|~e359ec59]].
- The finite bipartite graphs have no Fraïssé limit, since they fail AP; see [[this non-example|~85a0ac66]].

### Basic properties

- The limit is universal for countable structures with age contained in $\mathcal{K}$: each of them embeds into it.
- In a finite relational signature, the theory of the limit is [[$\aleph_0$-categorical|A22K1X8GKD]] with quantifier elimination; see [[this theorem|~4c6933ec]].
- The automorphism group of the limit is a closed subgroup of $\operatorname{Sym}(\N)$ that acts transitively on copies of each member of $\mathcal{K}$.
- If $\mathcal{K}$ has strong amalgamation, the limit has no algebraicity: the pointwise stabilizer of a finite set has no other finite orbits.

### History

Roland Fraïssé introduced the construction in the early 1950s for relational structures.
Ehrenfeucht-Fraïssé games, from the same circle of ideas, are treated with the [[back-and-forth method|6F2DB4HTJR]].

### Common errors

- To call any countable structure with age $\mathcal{K}$ the limit. The limit must also be ultrahomogeneous.
- To forget AP. Without it there may be no ultrahomogeneous structure with the given age.
- To expect uncountable structures. The theorem is about countable limits.

## Explanations

### L1 human

Start with a collection of small pieces, such as all finite linear orders or all finite graphs.
The Fraïssé limit is one countable object into which every piece fits, and in which any two copies of the same piece look alike from the outside.
For finite linear orders the limit is $(\Q, <)$.
Every finite order sits inside $\Q$, and any order-preserving map between two finite subsets of $\Q$ extends to an order-preserving bijection of all of $\Q$.

### L2 human

We identify the limit of the class of finite sets with one unary predicate $P$.

1. HP and JEP are clear, and AP holds by gluing over the common part.
2. The limit $M$ must contain finite sets with any number of points in $P$ and outside $P$.
3. The age contains sets with $n$ points in $P$ and $n$ points outside, for every $n$, so both parts of $M$ are infinite.
4. A countable set split into two infinite parts is ultrahomogeneous, since a partial bijection respecting $P$ extends on each part.
5. So $M$ is a countable set split into two infinite parts.

The typical use is to recognize a well-known structure as the limit of a simple class.
A trap is to guess the limit from one or two examples without checking the extension property.

### L3 human

In a relational signature, the limit is the generic countable structure with age in $\mathcal{K}$: in the Polish space of such structures on $\N$, its isomorphism class is comeager.
Model-theoretic properties of the limit, such as stability or simplicity, are coded by the combinatorics of $\mathcal{K}$.
Its automorphism group is studied through the [[Kechris-Pestov-Todorcevic correspondence|~d7362f14]], the [[small index property|~22edb57f]] and the [[extension property for partial automorphisms|~6881f8c3]].
