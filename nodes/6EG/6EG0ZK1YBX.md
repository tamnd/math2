---
tag: 6EG0ZK1YBX
kind: concept
name: Indiscernible sequence
aliases: [indiscernibles, order-indiscernible-sequence, indiscernible-set, order-indiscernibles]
msc: ["03C30", "03C50"]
topics: [W9CHA4PD9H]
audience: grad
uses: [983GZBQYT4, HYJ10AF6RT, 0FRXBVVR03, 9V71Q3SD1G, DSQ17TNW1C, CGH8C8EA9N]
sources:
  - url: https://en.wikipedia.org/wiki/Indiscernibles
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Indiscernibles
    locator: Examples
  - book: isbn:9780387987606
    locator: Chapter 5
  - book: isbn:9780521763240
    locator: Chapter 5
---

## Summary

Let $\mathcal{M}$ be an $L$-[[structure|983GZBQYT4]], let $A \subseteq M$, and let $(I, <)$ be a [[linear order|0FRXBVVR03]].
A family $(a_i)_{i \in I}$ of elements of $M$ is an *indiscernible sequence over $A$* if, for every $n$, every $L$-[[formula|HYJ10AF6RT]] $\varphi(x_1, \dots, x_n)$ with parameters from $A$, and all $i_1 < \dots < i_n$ and $j_1 < \dots < j_n$ in $I$, we have $\mathcal{M} \models \varphi(a_{i_1}, \dots, a_{i_n})$ exactly when $\mathcal{M} \models \varphi(a_{j_1}, \dots, a_{j_n})$.
The family is an *indiscernible set over $A$* if the same holds for all tuples of pairwise distinct indices, with no condition on their order.
So no formula can tell two increasing tuples of the sequence apart, and for a set no formula can tell any two tuples of distinct members apart.
Indiscernibles are the raw material for models with many automorphisms and few types, and they are the main tool for passing between models of different sizes.
The formal definition is [[this definition|4016QKAHFB]].

## Motivation

A model of a theory can be large and complicated, and an arbitrary set of its elements carries no structure.
Ramsey's theorem says that every infinite colored structure has a large part on which the coloring is constant.
In model theory the colors are the truth values of formulas, and the constant part is an indiscernible sequence.
Such a sequence behaves like the index order $I$ itself: every order-preserving map of $I$ looks like a symmetry of the sequence.
Ehrenfeucht and Mostowski used this to build models whose automorphism groups contain the automorphism group of any chosen linear order.
Later the same idea gave Morley's proof of the categoricity theorem and the analysis of the number of models.

## Notation

The *type of the sequence*, or its *Ehrenfeucht-Mostowski type*, is the set of formulas $\varphi(x_1, \dots, x_n)$ that hold of every increasing $n$-tuple of the sequence, for all $n$.
It is often written $\Phi$ or $\operatorname{EM}((a_i)_{i \in I})$.
Many books say "indiscernible" for "order-indiscernible", and write "totally indiscernible" for an indiscernible set.
The members $a_i$ may also be tuples of a fixed finite length; every definition and result then holds with the same proofs.

## Remarks

### Examples

- An infinite [[basis|0KCQ9Y3QKA]] of a vector space is an indiscernible set, because every permutation of the basis extends to a linear automorphism; see [[this example|H7RFGN5RV7]].
- A [[transcendence basis|E45PA267S4]] of an algebraically closed field is an indiscernible set, because permutations of it extend to field automorphisms; see [[this example|8BDCM2MBV9]].
- A strictly increasing sequence in the rational order $(\Q, <)$ is an indiscernible sequence, because order-preserving maps between finite sets extend to automorphisms; see [[this example|KZASF579JE]].
- A constant family $a_i = b$ is indiscernible over every set, because every formula $\varphi(b, \dots, b)$ has one truth value.
- In an infinite set with no structure, every injective family is an indiscernible set, since a permutation of the set is an automorphism.

### Non-examples

- The sequence $0, 1, 2, \dots$ in $(\N, <)$ is not indiscernible: the formula $\exists y \, (y < x)$ is false at $0$ and true at $1$; see [[this example|1T221XPKPJ]].
- An increasing sequence in $(\Q, <)$ is not an indiscernible set: $x_1 < x_2$ holds of $(a_0, a_1)$ and fails for $(a_1, a_0)$.
- A basis $(e_n)$ of a vector space is not indiscernible over $A = \set{e_0}$: the formula $x = e_0$ is true at $e_0$ and false at $e_1$.

### Basic properties

- An order-indiscernible sequence with at least two members is constant or injective. If $a_i = a_j$ for one pair $i < j$, the formula $x_1 = x_2$ holds of every increasing pair.
- Every subfamily $(a_j)_{j \in J}$ with $J \subseteq I$ is again indiscernible over $A$, because its increasing tuples are increasing tuples of the original family.
- Indiscernibility is kept in every elementary extension, since an [[elementary embedding|CGH8C8EA9N]] keeps the truth of formulas.
- Suppose that for all increasing tuples $\bar{\imath}$ and $\bar{\jmath}$ of the same length some [[automorphism|DSQ17TNW1C]] of $\mathcal{M}$ fixes $A$ and maps $a_{\bar{\imath}}$ to $a_{\bar{\jmath}}$. Then the sequence is indiscernible over $A$.
- Increasing $n$-tuples of the sequence all have the same [[type|9V71Q3SD1G]] over $A$, and this is an equivalent form of the definition.
- Every theory with infinite models has indiscernible sequences of every order type; see the [[existence of indiscernibles|RG6D2FAS14]].

### History

Ehrenfeucht and Mostowski introduced indiscernible sequences in 1956, to build models with many automorphisms.
Morley used them in 1965 in his proof of the categoricity theorem.
Silver later found a closed unbounded class of indiscernibles for the [[constructible universe|6TF2JBTPPJ]], under a large cardinal hypothesis.

### Common errors

- The substructure generated by an indiscernible sequence need not be an elementary substructure. It is elementary when the theory is a [[Skolem theory|NKQY9NB955]].
- Indiscernibility over $\emptyset$ does not give indiscernibility over a larger set $A$. Each parameter in $A$ can separate the members.
- An indiscernible sequence is not an indiscernible set in general. The order of the indices matters, as in $(\Q, <)$.

## Explanations

### L1 human

Picture a row of identical twins standing in a line.
A question about two of them can only use their places in the line, such as "is this one to the left of that one?".
An indiscernible sequence is a row of elements like that.
In the rational numbers, the row $1, 2, 3, 4, \dots$ is an example: every true statement about $1$ and $2$ in terms of the order is also true about $3$ and $4$.
For an indiscernible set even the places do not matter, as for the members of a basis of a vector space.

### L2 human

We check that $a_n = n$ is an indiscernible sequence in $(\Q, <)$, for pairs.

1. Take $i_1 < i_2$ and $j_1 < j_2$ in $\N$, and a formula $\varphi(x_1, x_2)$ in the signature $\set{<}$.
2. Define $\sigma \colon \Q \to \Q$ to be linear on each of the intervals cut out by $i_1, i_2$, with $\sigma(i_1) = j_1$ and $\sigma(i_2) = j_2$, and a shift outside them.
3. The map $\sigma$ is an order-preserving bijection, so it is an automorphism of $(\Q, <)$.
4. Automorphisms preserve formulas, so $\varphi(i_1, i_2)$ holds exactly when $\varphi(j_1, j_2)$ holds.

The typical use is to transfer facts about one increasing tuple to all of them, and then to stretch the sequence by compactness.
The trap is to forget the order: $(1, 2)$ and $(2, 1)$ do not have the same type, so the sequence is not an indiscernible set.

### L3 human

An indiscernible sequence indexed by $I$ is a structure-preserving copy of the order $I$ inside a model, up to type.
The type $\Phi$ of the sequence is a blueprint: by compactness it gives, for each linear order $J$, a sequence indexed by $J$ with the same type, and in a Skolem theory it gives the [[Ehrenfeucht-Mostowski model|TSGB29FJM0]] generated by it.
In a [[stable theory|T7JW5QY6KR]] every indiscernible sequence is an indiscernible set, and this collapse is one way to state stability.
Replacing the order $I$ by trees, graphs or other structures gives [[generalized indiscernibles|RQS808ZC8T]], which detect the dividing lines of classification theory.
In set theory, Silver indiscernibles play the same role for the constructible universe $L$.
