---
tag: 7XQBJ52RA1
kind: definition
name: Algebraic structure
msc: [08A05, 08A62]
defines: QJGPT2W0FT
uses: [WDVVEYD6AT, 983GZBQYT4, EJ8YJVM9BW]
sources:
  - url: https://en.wikipedia.org/wiki/Algebraic_structure
---

## Definition

Let $\sigma$ be a [[signature|WDVVEYD6AT]] whose symbols are all function symbols, each with an arity $n \ge 0$.
An *algebraic structure* of signature $\sigma$, or $\sigma$-algebra, is a pair $\mathbf{A} = (A, (f^{\mathbf{A}})_{f \in \sigma})$ such that:

1. $A$ is a nonempty set, the universe of $\mathbf{A}$;
2. for each symbol $f \in \sigma$ of arity $n$, $f^{\mathbf{A}} \colon A^n \to A$ is an $n$-ary [[finitary operation|EJ8YJVM9BW]] on $A$.

An operation of arity $0$ is identified with an element of $A$, a constant.
So a $\sigma$-algebra is the same as a [[structure|983GZBQYT4]] for the purely functional signature $\sigma$.

## Remarks

Example: $(\Z, +, -, 0)$ is an algebraic structure of signature $(2, 1, 0)$.
Addition is a map $\Z^2 \to \Z$, negation is a map $\Z \to \Z$, and $0 \in \Z$ is a constant.

Non-example: $(\N, +, -, 0)$ with $-$ the map $x \mapsto -x$ is not an algebraic structure, because $-1 \notin \N$, so clause 2 fails for the unary symbol.

A *class* of algebras, such as the class of groups, is given by a signature together with axioms that the operations must satisfy.
The axioms are not part of the definition of an algebraic structure.
Some authors allow the empty set as universe when $\sigma$ has no constants.
