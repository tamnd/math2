---
tag: 3TZW7W8N6A
kind: concept
name: Tarski's problems for free groups
aliases: [tarski-problems-on-free-groups]
msc: ["20E05", "03C60", "20F10"]
topics: [BAZT8JJ70S]
audience: research
uses: [~0757d1ee, 0KTW26C80J, P3B1V182N4, HWC687ES0Q]
sources:
  - url: https://en.wikipedia.org/wiki/Free_group
    locator: Tarski's problems
  - url: https://en.wikipedia.org/wiki/Elementary_equivalence
    locator: lead section
inventory: [VVYR0H9MW9]
---

## Summary

Tarski's problems for free groups are two questions about the [[elementary theory|~0757d1ee]] of the [[free groups|0KTW26C80J]] $F_n$ of finite rank $n \ge 2$.
The first question asks whether all these groups are [[elementarily equivalent|P3B1V182N4]], that is, whether they satisfy the same first-order sentences in the language of groups.
The second question asks whether their common theory is [[decidable|HWC687ES0Q]], that is, whether an algorithm can decide if a given sentence is true in $F_2$.
Both answers are yes, by the [[solution of Tarski's problems|~c44acebf]] of Sela and of Kharlampovich and Myasnikov.
The problems matter because they ask how much of the structure of a free group a first-order sentence can see.

## Motivation

The free groups $F_2, F_3, F_4, \ldots$ are not isomorphic, because the [[abelianization|0AQZV0905N]] of $F_n$ is $\mathbb{Z}^n$, and $\mathbb{Z}^m \not\cong \mathbb{Z}^n$ for $m \ne n$.
But the proof of this fact uses the set of all homomorphisms to $\mathbb{Z}$ or a count of generators, and a first-order sentence cannot talk about these things directly.
A first-order sentence can only use quantifiers over elements, the group operation, the inverse and the identity.
Many easy properties do not separate the groups: each $F_n$ with $n \ge 2$ is non-abelian, torsion-free, and has trivial centre.
So it is natural to ask whether any sentence at all separates $F_2$ from $F_3$.
The second question comes from logic: for many classes of structures, Tarski studied whether the true sentences can be listed by an algorithm.

## Notation

We write $F_n$ for the free group with basis $a_1, \ldots, a_n$, and $\operatorname{Th}(G)$ for the set of first-order sentences that are true in a group $G$.
We write $G \equiv H$ when $\operatorname{Th}(G) = \operatorname{Th}(H)$.
In this notation, the first question asks whether $F_m \equiv F_n$ for all $m, n \ge 2$.
Some authors call $\operatorname{Th}(F_2)$ the theory of the free group, or the theory of non-abelian free groups.

## Remarks

### The two questions

1. Elementary equivalence: is $F_m \equiv F_n$ for all $m, n \ge 2$?
2. Decidability: is there an algorithm that takes a sentence $\varphi$ and decides whether $F_2 \models \varphi$?

The second question depends on the first only for the choice of the group.
When the answer to the first question is yes, the second question is about one theory, the common theory of all $F_n$ with $n \ge 2$.

### Examples of partial answers

1. All $F_n$ with $n \ge 2$ satisfy the same universal sentences. A universal sentence that is true in a group is true in each subgroup. The group $F_n$ is a subgroup of $F_2$, and $F_2$ is a subgroup of $F_n$, so each group satisfies the universal sentences of the other.
2. The same argument with existential sentences works in the other direction. An existential sentence that is true in a subgroup is true in the larger group, so all $F_n$ with $n \ge 2$ satisfy the same existential sentences.
3. The sentence $\exists x \exists y \, (x y \ne y x)$ is true in each $F_n$ with $n \ge 2$, because $a_1 a_2$ and $a_2 a_1$ are different reduced words.

The full question is hard because a general sentence alternates the quantifiers $\forall$ and $\exists$ many times.

### Non-examples

1. The group $F_1 \cong \mathbb{Z}$ is not elementarily equivalent to $F_2$. The sentence $\forall x \forall y \, (x y = y x)$ is true in $F_1$ and false in $F_2$.
2. The free abelian groups $\mathbb{Z}^m$ and $\mathbb{Z}^n$ with $m \ne n$ are not elementarily equivalent. The quotient $\mathbb{Z}^n / 2\mathbb{Z}^n$ has $2^n$ elements, and a first-order sentence can say that there are exactly $2^n$ classes of elements modulo squares (in additive notation, modulo doubles).

These non-examples show that the answer for free groups is not a general fact about groups with $n$ generators.

### History

Alfred Tarski asked the two questions around 1945.
Partial results on equations over free groups came from Makanin and Razborov.
Zlil Sela, and independently Olga Kharlampovich and Alexei Myasnikov, gave positive answers in work that was published in 2006.
The details are in the node of the [[solution|~c44acebf]].

### Common errors

1. Elementary equivalence is not isomorphism. The groups $F_2$ and $F_3$ are elementarily equivalent, but they are not isomorphic.
2. The rank $1$ is not included. The group $F_1$ is abelian, so it is separated from $F_2$ by one sentence.
3. A sentence of first-order logic quantifies over elements only. A statement about all subgroups or all homomorphisms is not a first-order sentence of the language of groups.

## Explanations

### L1 human

A free group on two letters $a$ and $b$ contains all the words in $a$, $b$, $a^{-1}$ and $b^{-1}$, where we cancel a letter next to its inverse.
A free group on three letters contains more words, so it looks larger.
Tarski asked if a statement of a simple formal kind can see this difference.
The statements of this kind speak only about elements, products and equality, with "for all" and "there exists".
He also asked if a computer program can decide which of these statements are true.
More than sixty years later, mathematicians showed that no such statement sees the difference, and that such a program exists.

### L2 human

We check that $F_2$ and $F_3$ satisfy the same universal sentences.

1. Let $\varphi$ be a universal sentence, that is, $\varphi = \forall x_1 \cdots \forall x_k \, \theta$, where $\theta$ has no quantifiers.
2. Suppose that $G \models \varphi$ and that $H$ is a subgroup of $G$. Each tuple of elements of $H$ is a tuple of elements of $G$, and $\theta$ is evaluated in the same way in $H$ and in $G$. So $H \models \varphi$.
3. The subgroup of $F_3$ generated by $a_1$ and $a_2$ is free with basis $a_1, a_2$, so $F_3$ contains a copy of $F_2$.
4. The elements $a_1$, $a_2 a_1 a_2^{-1}$ and $a_2^2 a_1 a_2^{-2}$ of $F_2$ form the basis of a free subgroup, so $F_2$ contains a copy of $F_3$.
5. By step 2 in both directions, $F_2$ and $F_3$ satisfy the same universal sentences.

The typical use of this argument is to compare the universal theories of groups that embed in each other.
The trap is to apply it to a sentence that has both $\forall$ and $\exists$: step 2 fails for such sentences.

### L3 human

Tarski's problems are a test of how well first-order logic describes a group.
The free groups of rank at least $2$ turn out to share one theory, so first-order logic cannot see the rank.
The answer needs the theory of equations over free groups, where limit groups and Makanin-Razborov diagrams play the role of the varieties and their decompositions in algebraic geometry.
The same questions make sense for other classes, for example torsion-free hyperbolic groups, and Sela also studied them.
[[Szmielew's theorem|~efe20356]] on the theory of abelian groups is the abelian analogue, and the [[elementary theory of groups|~0757d1ee]] gives the setting of both results.
