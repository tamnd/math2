---
tag: PWHJZYBNEY
kind: definition
name: Signature
msc: [03C07, 03B10]
defines: WDVVEYD6AT
uses: [086QKPF0A6, 0EPAT51DXQ]
sources:
  - url: https://en.wikipedia.org/wiki/Signature_(logic)
---

## Definition

A *signature* $\sigma$ consists of:

1. a set $F$ of function symbols;
2. a set $R$ of relation symbols, disjoint from $F$;
3. an arity [[function|0EPAT51DXQ]] $\operatorname{ar} \colon F \cup R \to \N$ that gives the number of arguments of each symbol.

A function symbol of arity $0$ is a *constant symbol*.
The symbols of $\sigma$ are the non-logical symbols of a first-order language; the variables, connectives, quantifiers and equality are not part of $\sigma$.

## Remarks

The signature of rings is $\set{+, \cdot, -, 0, 1}$ with arities $2, 2, 1, 0, 0$; it has no relation symbols.
The signature of ordered sets has one relation symbol $<$ of arity $2$ and no function symbols.
The list "a binary operation $\cdot$ that is associative" is not a signature: associativity is an axiom, and a signature contains only symbols and their arities.
Some books list the constant symbols as a third set instead of treating them as functions of arity $0$.
In Mathlib a signature is `FirstOrder.Language`.
