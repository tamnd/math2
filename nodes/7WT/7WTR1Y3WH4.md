---
tag: 7WTR1Y3WH4
kind: definition
name: Saturated model
msc: ["03C50"]
topics: [Z772KEC9BY]
audience: grad
defines: RMTZ5J64FX
uses: [9V71Q3SD1G, MVCH6N9SNW, 0EBACQFAZW, 0G0ASKNA6Z]
sources:
  - url: https://en.wikipedia.org/wiki/Saturated_model
    locator: Definition
  - book: isbn:9780387987606
    locator: Chapter 4
---

## Definition

Let $L$ be a signature, let $M$ be an $L$-structure, and let $\kappa$ be an infinite [[cardinal|0EBACQFAZW]].
The structure $M$ is *$\kappa$-saturated* if the following holds for every set $A$ of elements of $M$ with $\abs{A} < \kappa$.
Every complete $1$-[[type|9V71Q3SD1G]] over $A$ is realized in $M$.
The structure $M$ is *saturated* if it is infinite and $\abs{M}$-saturated, where $\abs{M}$ is the [[cardinality|0G0ASKNA6Z]] of its domain.

## Notation

One writes $\omega$-saturated for $\aleph_0$-saturated.
Here a type over $A$ means a type of the theory $\operatorname{Th}_A(\mathcal{M})$ in the language $L_A$, so its formulas may use the elements of $A$ as parameters.

## Remarks

The main page of the idea is [[saturated model|RMTZ5J64FX]].
A $\kappa$-saturated structure also realizes every complete $n$-type over fewer than $\kappa$ parameters, for every $n \ge 1$.

Example: $(\Q, <)$ is saturated.
A complete $1$-type over a finite set $A \subseteq \Q$ says where $x$ lies relative to the elements of $A$.
Either $x$ equals some $a \in A$, or $x$ lies in one of the open intervals cut out by $A$, including the two unbounded ones.
Each of these intervals contains a rational number, so the type is realized.

Non-example: the field $\overline{\Q}$ of algebraic numbers is a model of the theory of algebraically closed fields of characteristic $0$, but it is not $\aleph_0$-saturated.
The set $\set{f(x) \ne 0 : f \in \Z[x], f \ne 0}$ is consistent with its theory over $A = \emptyset$, as $\C$ shows, and it extends to a complete type.
No element of $\overline{\Q}$ realizes it, since every algebraic number is a root of a nonzero integer polynomial.

Every structure has a $\kappa$-saturated elementary extension for each $\kappa$; see [[existence of saturated models|~b797b7c8]].
Saturated models of the same complete theory and the same cardinality are isomorphic; see [[uniqueness of saturated models|~a2cbf168]].

## Explanations

### L1 human

A structure is saturated when every consistent description of an element, written with fewer parameters than the structure has elements, is met by an element of the structure.

### L2 human

To check that a structure $\mathcal{M}$ is $\kappa$-saturated, follow these steps.

1. Take a parameter set $A$ with $\abs{A} < \kappa$.
2. Describe all complete $1$-types over $A$, usually with quantifier elimination.
3. Find an element of $\mathcal{M}$ that realizes each of them.

The trap is to check only the types over finite sets: that gives $\aleph_0$-saturation, which is weaker than saturation for an uncountable structure.
