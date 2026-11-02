---
tag: A0K9EZRM7E
kind: concept
name: Polymorphism of a relation
msc: [08A40, 08A02]
sources:
  - url: https://en.wikipedia.org/wiki/Clone_(algebra)
---

## Summary

An operation $f \colon A^n \to A$ is a polymorphism of a relation $R \subseteq A^m$ when applying $f$ coordinatewise to tuples of $R$ always gives a tuple of $R$.
One also says that $f$ preserves $R$, or that $R$ is invariant under $f$.
The polymorphisms of a set of relations form a [[clone|PTKR703G6A]], and this links operations to relations through a Galois connection.
Polymorphisms are the main tool of the algebraic approach to constraint satisfaction problems.

## Explanations

### L1 human

Write the tuples of a relation as the rows of a table, and pick $n$ rows.
Apply $f$ to each column of the chosen rows, and you get a new row.
The operation $f$ is a polymorphism if this new row is always again in the table.
For example, the operation $\min$ on $\R$ is a polymorphism of the order $\le$: if $a \le b$ and $c \le d$, then $\min(a, c) \le \min(b, d)$.
