---
tag: ~c5dccb2a
kind: statement
role: theorem
name: Criterion for finite axiomatizability
aliases: [basic-elementary-class-criterion]
msc: ["03C52", "03C07"]
topics: [AY09KYSW81]
audience: ug2
about: [~8205aea8, MEC3ZMC4F1]
uses: [~8205aea8, MEC3ZMC4F1, 1NR3HAWG9D, 92SWXST1ZM]
sources:
  - url: https://en.wikipedia.org/wiki/Elementary_class
    locator: A basic elementary class
  - book: isbn:9780387987606
    locator: Chapter 2
---

## Statement

Let $L$ be a signature.

1. A class $K$ of $L$-structures is a basic [[elementary class|MEC3ZMC4F1]] if and only if both $K$ and its complement, the class of $L$-structures not in $K$, are elementary classes.
2. If an $L$-[[theory|92SWXST1ZM]] $T$ is [[finitely axiomatizable|~8205aea8]], then some finite subset $T_0 \subseteq T$ has $\operatorname{Mod}(T_0) = \operatorname{Mod}(T)$.

## Remarks

### Why each hypothesis is needed

- In part 1, elementarity of $K$ alone is not enough: infinite sets form an elementary class that is not basic, and its complement, the finite sets, is not elementary.
- The argument uses the [[compactness theorem|1NR3HAWG9D]], so the statement is about first-order logic. In second-order logic part 2 fails: the class of infinite sets is defined by one second-order sentence, yet no finite subset of $\set{\lambda_n : n \ge 2}$ defines it.

### Consequences

- The theories of fields of characteristic $0$ and of [[algebraically closed fields|~a0f7620d]] are not finitely axiomatizable: in each case every finite subset of the usual axioms has a model outside the class.
- The class $K_+$ of fields of positive characteristic is not elementary. Otherwise the complement of the class $K_0$ of fields of characteristic $0$, which is the union of $K_+$ and the class of non-fields, would be elementary, and $K_0$ would be basic by part 1.
- [[Peano arithmetic|M5WNB181T7]] is not finitely axiomatizable; part 2 shows that it suffices to rule out the finite subsets of the induction schema.

### Converse

Part 2 has an obvious converse: a theory with a finite subset that has the same models is finitely axiomatizable.
Part 1 is an equivalence.

### Generalizations

- A theory $T$ is finitely axiomatizable over a theory $T'$ when $\operatorname{Mod}(T) = \operatorname{Mod}(T' \cup F)$ for a finite $F$; the same proof gives the analogue of both parts relative to $\operatorname{Mod}(T')$.
- In topological terms, the basic elementary classes correspond to the clopen subsets of the space of complete theories, and the elementary classes to the closed subsets.

## History

The criterion is a standard consequence of the compactness theorem and appears in the textbooks; we do not attribute it to a single author.

## Explanations

### L1 human

Suppose a class and the rest of the world can each be described by a list of axioms.
The two lists together are contradictory, and by compactness a finite part of them is already contradictory.
That finite part of the first list describes the class by itself.

### L2 human

We apply part 2 to the theory $T_\infty$ of infinite sets.

1. Suppose $T_\infty$ were finitely axiomatizable.
2. By part 2, some finite $T_0 \subseteq T_\infty$ has the same models, and $T_0 \subseteq \set{\lambda_2, \dots, \lambda_N}$ for some $N$.
3. A set with $N$ elements is a model of $T_0$ and not of $T_\infty$, a contradiction.

The typical use of part 2 is to reduce a question about all finite sets of sentences to a question about finite subsets of a given axiomatization.
A trap is to use part 1 with the complement taken inside a smaller class, such as fields, without adding the axioms of that class.
