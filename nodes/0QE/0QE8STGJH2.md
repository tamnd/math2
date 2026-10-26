---
tag: 0QE8STGJH2
kind: definition
name: Sequence
msc: [40A05]
defines: 0G9EKM0E15
sources:
  - url: https://en.wikipedia.org/wiki/Sequence
    locator: Formal definition and basic properties
---

## Definition

Let $X$ be a set.
A sequence in $X$ is a function $a \colon \mathbb{N} \to X$, where $\mathbb{N} = \{0, 1, 2, \dots\}$.
The value $a(n)$ is the $n$-th term of the sequence, and we write it as $a_n$.
We write the sequence as $(a_n)_{n \in \mathbb{N}}$, or as $(a_n)$ when the index set is clear.

## Remarks

Many texts start the index at $1$, and they use a function on $\{1, 2, 3, \dots\}$. The theory does not change.
The terms of a sequence can repeat. For example, $(1, 0, 1, 0, \dots)$ is the sequence with $a_n = 1$ for even $n$ and $a_n = 0$ for odd $n$.
A sequence of real numbers is a [[real sequence|0CTV783HYT]].

## Explanations

### L1 human

A sequence is an infinite list $a_0, a_1, a_2, \dots$ of elements of a set.
The order matters, and the same element can occur more than once.
For example, the squares $0, 1, 4, 9, 16, \dots$ form the sequence $a_n = n^2$.
