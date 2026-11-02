---
tag: 624XDXX8FN
kind: concept
name: Subshift of finite type
msc: [37B10]
specializes: [A1XE59ZHNM]
sources:
  - url: https://en.wikipedia.org/wiki/Subshift_of_finite_type
same_as:
  wikidata: Q7631990
  wikipedia: Subshift of finite type
---

## Summary

A subshift of finite type is a [[shift space|A1XE59ZHNM]] described by a finite list of forbidden words.
After a recoding of the symbols, every subshift of finite type becomes the set of bi-infinite walks on a finite [[directed graph|0KFYGSHHF5]].
These spaces are the basic models of [[symbolic dynamics|EWFWTSVY0B]].
Through [[Markov partitions|4VNHVDHTNN]] they also code hyperbolic smooth systems, so questions about such systems become questions about matrices.

## Explanations

### L1 human

Think of an infinite sequence of symbols, written in both directions.
A subshift of finite type allows every such sequence except those that contain some word from a fixed finite blacklist.
For example, take the symbols $0$ and $1$ and forbid the word $11$.
Then the allowed sequences are those in which two $1$s never stand next to each other.
Whether a sequence is allowed can always be checked by looking through a window of fixed width.
See the [[definition|M7RPDE39FM]].
