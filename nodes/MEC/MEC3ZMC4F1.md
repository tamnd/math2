---
tag: MEC3ZMC4F1
kind: concept
name: Elementary class
msc: ["03C52", "03C07"]
topics: [AY09KYSW81]
audience: ug2
uses: [MVCH6N9SNW, 92SWXST1ZM, 983GZBQYT4, P3B1V182N4, X9HV9C6X4F, 1NR3HAWG9D]
sources:
  - url: https://en.wikipedia.org/wiki/Elementary_class
    locator: Definition; Examples
  - book: isbn:9780387987606
    locator: Chapter 2
same_as:
  wikidata: Q1327762
  wikipedia: Elementary class
---

## Summary

An elementary class is the class $\operatorname{Mod}(T)$ of all [[models|MVCH6N9SNW]] of a first-order [[theory|92SWXST1ZM]] $T$ in a fixed signature.
When $T$ can be taken to be one sentence, or equivalently a finite set, the class is a *basic elementary class*.
Groups, rings, fields of characteristic $0$ and dense linear orders are elementary classes.
An elementary class is closed under isomorphism, [[elementary equivalence|P3B1V182N4]] and ultraproducts.
By the [[compactness theorem|1NR3HAWG9D]], many natural classes, such as finite sets, torsion groups, well-orders and connected graphs, are not elementary.

## Motivation

A mathematician defines a class of structures by axioms: groups, fields, orders, graphs.
The question is which classes can be defined by first-order axioms, and how many axioms they need.
The answer tells us which tools of model theory apply to the class.
The compactness theorem, the Löwenheim-Skolem theorems and ultraproducts work for elementary classes, and they fail for classes that are not elementary.

## Notation

Some books write $\mathrm{EC}$ for the basic elementary classes and $\mathrm{EC}_\Delta$ for the elementary classes; other books say "axiomatizable" and "finitely axiomatizable" class.
The class of models of $T$ is $\operatorname{Mod}(T)$, and the smallest elementary class that contains a class $K$ is $\operatorname{Mod}(\operatorname{Th}(K))$, built from the [[theory of $K$|X9HV9C6X4F]].
Universal classes, quasivarieties and varieties are elementary classes whose axioms have special shapes.

## Remarks

### Examples

- Fields of characteristic $0$ form an elementary class that is not basic; see [[this example|XB3DB1KW29]].
- Groups form a basic elementary class, in either of two signatures; see [[this example|Q3G2XKD8HR]].
- Algebraically closed fields form an elementary class that is not basic; see [[this non-example|2ZTTR9VZ4P]].
- Infinite sets, in the empty signature, form an elementary class that is not basic.

### Non-examples

- Finite sets, torsion groups, well-orders, connected graphs, Archimedean ordered fields and simple groups; see [[this non-example|T1S9T0RKHJ]].
- [[Finite groups|3J825EJ81F]].
- Fields of positive characteristic: an ultraproduct of the fields $\mathbb{F}_p$ over a nonprincipal ultrafilter on the primes has characteristic $0$.

### Basic properties

- $K$ is elementary if and only if $K = \operatorname{Mod}(\operatorname{Th}(K))$.
- The intersection of elementary classes $\operatorname{Mod}(T_i)$ is $\operatorname{Mod}(\bigcup_i T_i)$, and the union of two basic elementary classes $\operatorname{Mod}(\sigma)$, $\operatorname{Mod}(\tau)$ is $\operatorname{Mod}(\sigma \lor \tau)$.
- An elementary class is closed under [[ultraproducts|AX9Q86GB8M]], by [[Łoś's theorem|AGYBSTD7BG]].
- A class $K$ is elementary if and only if it is closed under elementary equivalence and ultraproducts.
- $K$ is basic elementary if and only if both $K$ and its complement are elementary; see [[the criterion|9XKWFMVKJD]].
- The complement of an elementary class need not be elementary: infinite sets form one, finite sets do not.

### History

Birkhoff's theorem of 1935 characterized the varieties, the classes defined by equations, as the classes closed under homomorphic images, substructures and products.
This was an early result of the same kind as the closure properties above.

### Common errors

- To think that a class defined by one natural property is elementary. Torsion groups are defined by "every element has finite order", which is not first-order.
- To forget the signature. Groups can be taken as $\set{\cdot}$-structures or as $\set{\cdot, {}^{-1}, e}$-structures, and the axioms and their shape depend on this choice.
- To think that elementary classes are closed under substructures. Fields form an elementary class, and $\Z$ is a substructure of $\Q$ in the signature of rings.

## Explanations

### L1 human

Pick a list of first-order axioms, such as the group axioms.
The elementary class of the list is everything that satisfies all of them.
First-order axioms may quantify over elements but not over sets of elements or over natural numbers.
So "every element has finite order" cannot be written as one first-order axiom, and torsion groups are not an elementary class.

### L2 human

We show that the class of finite sets, in the empty signature, is not elementary.

1. Suppose $T$ has exactly the finite sets as models.
2. Let $\lambda_n$ say "there are at least $n$ elements". Each finite subset of $T \cup \set{\lambda_n : n \ge 2}$ has a model, a large finite set.
3. By the compactness theorem, $T \cup \set{\lambda_n : n \ge 2}$ has a model. It is infinite and satisfies $T$, a contradiction.

The typical use of the concept is as the class to which compactness and Löwenheim-Skolem apply.
A trap is to prove non-elementarity of a class by finding one model of a candidate theory outside it; one must rule out every theory.

### L3 human

The closure of elementary classes under ultraproducts and elementary equivalence gives a purely algebraic description, and the Keisler-Shelah theorem replaces elementary equivalence by isomorphic ultrapowers; see the sub-area on [[ultraproducts|HZG1YP26AB]].
Preservation theorems relate closure properties to the shape of axioms, for example closure under substructures to universal axioms; see the sub-area on [[preservation theorems|JYJHB4YBAH]].
Abstract elementary classes, defined by Shelah's axioms on a class with a strong substructure relation, extend the theory to classes that are not elementary.
