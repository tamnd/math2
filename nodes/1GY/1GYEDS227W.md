---
tag: 1GYEDS227W
kind: definition
name: Model theory
msc: [03C07, 03C98]
topics: [AY09KYSW81]
audience: ug2
defines: HFTBG5PMXC
uses: [92SWXST1ZM, MVCH6N9SNW, 983GZBQYT4, 086QKPF0A6]
sources:
  - url: https://en.wikipedia.org/wiki/Model_theory
    locator: Basic model-theoretic concepts
  - book: isbn:9780387987606
    locator: Chapter 1
---

## Definition

Model theory is the part of mathematical logic whose objects are the following.

1. Formal languages, most often the language of [[first-order logic|086QKPF0A6]] over a signature.
2. [[Theories|92SWXST1ZM]], that is, sets of sentences of such a language.
3. [[Structures|983GZBQYT4]] for the signature, and the relation of truth between structures and sentences, in particular the [[models|MVCH6N9SNW]] of theories.

It studies the classes of models of theories and the sets definable in structures.

## Remarks

Example: the statement that every field elementarily equivalent to $\C$ is algebraically closed of characteristic $0$ is a result of model theory.
It concerns the class of models of the complete theory $\mathrm{Th}(\C)$.

Non-example: the computation of the homology of a sphere is not a result of model theory, because it concerns no formal language and no relation of truth.

Classical model theory works with first-order logic; other parts study [[infinitary logic|PQG7VAZ1R2]], finite structures or [[second-order logic|G6X7SZSNC5]].

## Explanations

### L1 human

Model theory is the study of mathematical structures through the sentences that are true in them.
It sits between logic and algebra: its theorems are about formulas, and its applications are often about fields, groups and orders.

### L2 human

We check that the transfer of a statement from $\C$ to $\overline{\Q}$ is a result of model theory.

1. The statement "every polynomial $x^2 - a$ has a root" is the first-order sentence $\forall a \, \exists x \, (x \cdot x = a)$.
2. It is true in $\C$.
3. The fields $\C$ and $\overline{\Q}$ are elementarily equivalent, so the sentence is true in $\overline{\Q}$.

The argument uses a formal language, structures and the relation of truth, which are the objects listed in the definition.
A trap is to call every result about structures model theory; the method must go through formulas and their truth.
