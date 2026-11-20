---
tag: A22K1X8GKD
kind: concept
name: Omega-categorical theory
aliases: [countably-categorical-theory, omega-categorical, omega-categorical-theories, omega-categoricity, aleph-zero-categorical-theory]
msc: ["03C35", "03C15"]
topics: [6XEXRME4C1]
audience: research
uses: [1JJCGNX240, 655K8Y7VS8, 01TQB88H4C, 9V71Q3SD1G, 1513J40TKA, 0K1SCPBNKJ, 0YQPZB5Q1G]
sources:
  - url: https://en.wikipedia.org/wiki/Omega-categorical_theory
  - url: https://en.wikipedia.org/wiki/Omega-categorical_theory
    locator: Examples
  - book: isbn:9780387987606
  - book: isbn:9780521587136
same_as:
  wikidata: Q7089964
  wikipedia: Omega-categorical theory
inventory: [1FGM3P0KN0]
---

## Summary

A [[complete theory|655K8Y7VS8]] $T$ in a countable signature, with infinite models, is *$\omega$-categorical* if it has exactly one [[countably infinite|01TQB88H4C]] model up to isomorphism.
It is the case $\kappa = \aleph_0$ of [[$\kappa$-categoricity|1JJCGNX240]].
By the [[Ryll-Nardzewski theorem|1513J40TKA]], $T$ is $\omega$-categorical exactly when it has finitely many complete $n$-[[types|9V71Q3SD1G]] for each $n$.
Equivalently, the [[automorphism group|0K1SCPBNKJ]] of its countable model has finitely many [[orbits|0YQPZB5Q1G]] on $n$-tuples for each $n$.
The rational order, the random graph and infinite vector spaces over a finite field are the standard examples.

## Motivation

For countable models, categoricity has an exact description by counting types, which is not available in uncountable cardinals.
Such theories are complete by the Łoś-Vaught test, and their countable model is highly symmetric.
They connect model theory with permutation groups and with finite combinatorics, since the countable model is often the limit of a class of finite structures.

## Notation

The names $\aleph_0$-categorical, $\omega$-categorical and countably categorical are used for the same notion.
For the countable model $M$, the group $\Aut(M)$ acts on $M^n$, and the condition is that this action has finitely many orbits.

## Remarks

### Examples

- The theory of [[infinite sets|KFWXHKBHYT]] in the empty signature.
- The [[theory of dense linear orders without endpoints|2W4S2H4VYA]].
- The theory of the [[Rado graph|RMXR0FEF54]], given by the extension axioms.
- Infinite vector spaces over a fixed finite field, and atomless Boolean algebras.
- An [[equivalence relation with infinitely many infinite classes|~2f97a8b0]].

### Non-examples

- $\mathrm{ACF}_0$, with one countable model of each transcendence degree $0, 1, \dots, \aleph_0$.
- The theory of $(\Z, <)$; see [[this non-example|~9769b292]].
- Nonzero vector spaces over $\Q$; see [[this example|~187e3871]].
- [[Ehrenfeucht's theory|~51f2568c]], with exactly three countable models.

### Basic properties

- The equivalent conditions of the [[Ryll-Nardzewski theorem|1513J40TKA]]: finitely many types, finitely many formulas in $n$ variables up to equivalence, all types isolated, finitely many orbits.
- Every model is atomic, and the countable model is prime, saturated and homogeneous.
- Adding finitely many constants, or passing to a reduct, keeps the property.
- An $\omega$-categorical theory need not be [[finitely axiomatizable|JR6XPJ7X56]]. The theory of infinite sets is not: every finite subset of it has finite models, while the full theory does not.

### History

Erwin Engeler, Czesław Ryll-Nardzewski and Lars Svenonius found the characterization by types independently in 1959.
Gregory Cherlin, Leo Harrington and Alistair Lachlan showed in 1985 that an $\omega$-categorical, $\omega$-stable theory is not finitely axiomatizable; Boris Zilber had proved this for totally categorical theories.
Later work describes the $\omega$-categorical structures that are approximated by finite substructures, the smoothly approximable structures.

### Common errors

- $\omega$-categorical is not the same as categorical in every cardinal. The rational order is $\omega$-categorical and not $\aleph_1$-categorical.
- For a theory not assumed complete, a unique countable model does not give completeness when there are finite models. The theory of nonempty sets has one countably infinite model, and it is not complete.
- The condition counts types over the empty set. Over a countable model, an $\omega$-categorical theory can have $2^{\aleph_0}$ types, as the rational order does.

## Explanations

### L1 human

A theory is $\omega$-categorical when it describes exactly one countable world, up to renaming.
The rational numbers with their order are the standard case: every countable dense order without endpoints is a copy of them.
Such worlds are very symmetric: any two finite lists of points that look alike can be swapped by a symmetry.

### L2 human

We test the property for the theory of $(\Z, <)$ by counting $2$-types.

1. For each $k$, the pairs $(a, b)$ with exactly $k$ elements strictly between $a < b$ have one type, and different $k$ give different types.
2. So $S_2(T)$ is infinite, and the theory is not $\omega$-categorical, by the Ryll-Nardzewski theorem.
3. Indeed, $\Z$ and $\Z + \Z$ are non-isomorphic countable models.

The typical use is an orbit count in a known countable structure.
A trap is to count orbits of the automorphism group on single elements only; the condition is for every $n$.

### L3 human

An $\omega$-categorical structure is determined by its automorphism group, as a topological group, up to bi-interpretability.
These groups are the closed oligomorphic subgroups of the symmetric group of a countable set, and they form a meeting point of model theory and permutation group theory.
