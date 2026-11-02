---
tag: 1AKKDC17M2
kind: definition
name: Equational theory
msc: [08B05, 03C05]
defines: F1M51B4MDG
uses: [PKD440G2XW, 6D3WA7N2W4]
sources:
  - url: https://en.wikipedia.org/wiki/Equational_logic
---

## Definition

Let $\sigma$ be a signature with only function symbols and let $X$ be a countably infinite set of variables.
For a class $\mathcal{K}$ of algebras of signature $\sigma$, the *equational theory* of $\mathcal{K}$ is the set
$$\operatorname{Id}(\mathcal{K}) = \set{s \approx t : s, t \text{ terms over } \sigma \text{ and } X, \ \mathcal{K} \models s \approx t}$$
of all [[identities|PKD440G2XW]] satisfied by $\mathcal{K}$.
A set $\Sigma$ of identities over $\sigma$ and $X$ is an *equational theory* if $\Sigma = \operatorname{Id}(\mathcal{K})$ for some class $\mathcal{K}$.

## Remarks

Every equational theory contains $t \approx t$ for every [[term|6D3WA7N2W4]] $t$, is closed under symmetry and transitivity, under applying an operation symbol to identities, and under substitution of terms for variables.
By Birkhoff's completeness theorem, these closure properties characterise equational theories.
For a set $\Sigma$ of identities, the equational theory of the class of all algebras satisfying $\Sigma$ is the set of consequences of $\Sigma$.

Example: for $\mathcal{K}$ the class of all commutative semigroups, $\operatorname{Id}(\mathcal{K})$ contains $x(yz) \approx (zy)x$, since both sides equal $xyz$ in every commutative semigroup.

Non-example: the set $\set{x y \approx y x}$ is not an equational theory.
Every set of the form $\operatorname{Id}(\mathcal{K})$ contains the identity $x \approx x$, which is not in this set.
