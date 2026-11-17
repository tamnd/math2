---
tag: ~e7c6fa0e
kind: concept
name: WKL0
msc: ["03B30", "03F35"]
topics: [BY8AAFN7C5]
audience: grad
uses: [~58b63877, DC60FYCSPM, W9VYJRBF9N]
sources:
  - url: https://en.wikipedia.org/wiki/Reverse_mathematics
    locator: Weak Kőnig's lemma WKL0
---

## Summary

$\mathsf{WKL}_0$ is the subsystem of [[second-order arithmetic|DC60FYCSPM]] whose axioms are those of [[RCA0|~58b63877]] together with weak König's lemma: every infinite binary tree has a path, as in its [[definition|~b501e994]].
It is the second of the big five systems of reverse mathematics.
It captures compactness arguments: many theorems that use the compactness of [[Cantor space|W9VYJRBF9N]] or of $[0, 1]$ are equivalent to it.

## Motivation

The computable sets satisfy $\mathsf{RCA}_0$, but many classical theorems fail there: a computable continuous function on $[0, 1]$ may have no computable point where it reaches its maximum.
The proofs of such theorems use compactness, often in the form of a path through an infinite tree.
Weak König's lemma is this compactness principle, and it adds no more strength than compactness needs.

## Notation

The system is $\mathsf{WKL}_0 = \mathsf{RCA}_0 + \mathrm{WKL}$, with $\mathrm{WKL}$ the sentence of weak König's lemma.

## Remarks

### Examples

- There is an [[ω-model of WKL0 whose sets are all low|~e8a57f1d]].
- The [[arithmetical sets|~46cb5771]] form an $\omega$-model of $\mathsf{WKL}_0$.
- The [[Heine-Borel theorem for $[0, 1]$|~ebb0edca]] is equivalent to $\mathsf{WKL}_0$ over $\mathsf{RCA}_0$.

### Non-examples

- The [[computable sets|~f2c0a555]] form a model of $\mathsf{RCA}_0$, but not of $\mathsf{WKL}_0$: a computable infinite binary tree can have no computable path.
- The [[sets computable from the halting set|~b9dd8ce0]] do not form a model of $\mathsf{WKL}_0$, by the same tree relativized to the halting set.

### Basic properties

- The $\omega$-models of $\mathsf{WKL}_0$ are the Turing ideals in which every infinite binary tree has a path.
- $\mathsf{WKL}_0$ does not prove arithmetical comprehension, since the low $\omega$-model omits the halting set.
- $\mathsf{WKL}_0$ is [[Π¹₁-conservative over RCA0|~d4bbed48]], and it is [[Π⁰₂-conservative over primitive recursive arithmetic|~de3d00df]].
- Over $\mathsf{RCA}_0$, $\mathsf{WKL}_0$ is equivalent to each of these: every continuous function on $[0, 1]$ is bounded; every continuous function on $[0, 1]$ attains its maximum; the Gödel completeness theorem for countable languages; the Brouwer fixed point theorem; the Hahn-Banach theorem for separable Banach spaces; every countable commutative ring has a prime ideal.

### History

Harvey Friedman introduced $\mathsf{WKL}_0$ in the 1970s.
Leo Harrington proved that it is $\Pi^1_1$-conservative over $\mathsf{RCA}_0$.
Stephen Simpson proposed it as a partial realization of Hilbert's program.

### Common errors

- Weak König's lemma is about binary trees. König's lemma for finitely branching trees, without a bound on the branching, is equivalent to $\mathsf{ACA}_0$.
- A path through a tree in a model need not be computable from the tree, and the model need not contain a given path; it contains some path.
- $\mathsf{WKL}_0$ is not stronger than $\mathsf{RCA}_0$ for arithmetic sentences: both prove the same $\Pi^1_1$ sentences.

## Explanations

### L1 human

$\mathsf{WKL}_0$ adds one principle to computable mathematics.
The principle says: if a tree of finite $0$-$1$ sequences never runs out, it has an infinite branch.
With it one can prove the theorems of analysis that use compactness, such as the fact that a continuous function on $[0, 1]$ is bounded.

### L2 human

To prove a compactness theorem in $\mathsf{WKL}_0$, build a binary tree whose paths code the objects one wants, and check that the tree is infinite.
For the reversal, build from a tree an instance of the theorem whose solutions compute paths.
A trap in the reversal is to use the set of nodes with infinitely many extensions, which needs $\mathsf{ACA}_0$.

### L3 human

A Turing degree computes a path through every infinite computable binary tree exactly when it is a PA degree, that is, when it computes a complete consistent extension of Peano arithmetic.
So the $\omega$-models of $\mathsf{WKL}_0$ are the Scott sets, which are also the standard systems of countable models of Peano arithmetic.
Weaker principles, such as weak weak König's lemma for trees of positive measure, link $\mathsf{WKL}_0$ to measure theory and algorithmic randomness.
