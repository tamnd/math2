---
tag: V5CKNFP3HC
kind: statement
role: theorem
name: Fraïssé's theorem
aliases: [fraisse-theorem, fraisses-theorem]
msc: ["03C15", "03C52"]
topics: [ZS8X8KS54R]
audience: grad
about: [HJVRBDQSGG, 5FKW715RGJ, XSCSX39GEZ, H8VM37SSAX]
uses: [5FKW715RGJ, HBE89GZ79M, XSCSX39GEZ, 2KBFZ1MPMW, 59FQ5Q2B8R, H8VM37SSAX, CZFGSN4JNE, 01TQB88H4C, WDVVEYD6AT, A22K1X8GKD]
sources:
  - url: https://en.wikipedia.org/wiki/Fraïssé_limit
    locator: Fraïssé's theorem
  - book: isbn:9780521587136
---

## Statement

Let $L$ be a countable [[signature|WDVVEYD6AT]], and let $\mathcal{K}$ be a nonempty class of finitely generated $L$-structures, closed under isomorphism.
Suppose that $\mathcal{K}$ has at most countably many isomorphism types, the hereditary property, the [[joint embedding property|59FQ5Q2B8R]] and the [[amalgamation property|XSCSX39GEZ]].
Then there is a [[countable|01TQB88H4C]] [[ultrahomogeneous|H8VM37SSAX]] $L$-structure $M$ whose [[age|5FKW715RGJ]] is $\mathcal{K}$.
It is unique up to isomorphism, and it is called the [[Fraïssé limit|HJVRBDQSGG]] of $\mathcal{K}$.

Conversely, if $M$ is a countable ultrahomogeneous $L$-structure, then $\operatorname{Age}(M)$ is nonempty, has at most countably many isomorphism types, and has the hereditary, joint embedding and amalgamation properties.

## Remarks

### Why each hypothesis is needed

- Hereditary property: the even-size finite linear orders have JEP and AP but are not an age; see [[this non-example|VDQCA78MNQ]].
- Joint embedding: the class of finite fields has HP and AP within each characteristic, but no single structure has it as age; see [[this non-example|8DQKEDXM8S]].
- Amalgamation: the finite bipartite graphs have HP and JEP, and they are the age of a countable graph, but of no ultrahomogeneous one; see [[this non-example|7YEX9F1V8D]].
- Countably many types: with unary predicates $P_i$ for $i \in \N$, the one-point structures already have $2^{\aleph_0}$ types, and a countable structure realizes only countably many.

### Consequences

- $(\Q, <)$ is the limit of the finite linear orders.
- The [[Rado graph|RMXR0FEF54]] is the limit of the finite graphs, and the [[Henson graph|TZT25G2YB3]] $G_n$ is the limit of the finite $K_n$-free graphs.
- The countable atomless Boolean algebra is the limit of the finite Boolean algebras; see [[this example|4GCVG943HX]].
- The algebraic closure of $\mathbb{F}_p$ is the limit of the finite fields of characteristic $p$; see [[this example|ZE2D07G8XQ]].
- In a finite relational signature, the limit has an [[$\aleph_0$-categorical|A22K1X8GKD]] theory with quantifier elimination, by [[this theorem|ZRWJZK78MD]].

### Converse

The converse is part of the statement, so ultrahomogeneous countable structures and classes with the four properties correspond one to one, through the age.

### Generalizations

- Metric Fraïssé theory replaces finite structures by finite metric spaces; the limit of the finite rational metric spaces is the rational Urysohn space, whose completion is the [[Urysohn universal space|R1H00F1668]].
- Hrushovski amalgamation restricts the embeddings to self-sufficient ones; see [[generic structures|933BFNKPXF]].
- Projective Fraïssé theory reverses the arrows and uses quotient maps instead of embeddings.

## History

Roland Fraïssé proved the theorem for relational structures in the early 1950s.
It is the source of the term "Fraïssé limit".

## Explanations

### L1 human

Fraïssé's theorem tells when a list of finite shapes is exactly the list of finite pieces of a single, maximally symmetric countable object.
Three rules are needed: pieces of shapes are shapes, any two shapes fit together, and two shapes sharing a part fit together along that part.
When the rules hold, there is exactly one such object.

### L2 human

We check the hypotheses for finite graphs.

1. Countably many types: there are finitely many graphs on $\set{1, \dots, n}$ for each $n$.
2. HP: an induced subgraph of a finite graph is a finite graph.
3. JEP: take the disjoint union.
4. AP: take the free amalgam over the common part.

So the theorem gives a unique countable ultrahomogeneous graph containing every finite graph: the Rado graph.
A trap is to skip AP; it is the hypothesis that fails most often in practice.

### L3 human

The proof builds the limit as the union of a chain of members of $\mathcal{K}$, meeting countably many amalgamation tasks one at a time.
Uniqueness is a back-and-forth argument.
The theorem identifies countable ultrahomogeneous structures with Fraïssé classes, and this lets properties of the automorphism group, such as extreme amenability or the small index property, be read off from the class.
