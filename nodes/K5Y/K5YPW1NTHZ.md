---
tag: K5YPW1NTHZ
kind: definition
name: WKL0
msc: ["03B30", "03F35"]
topics: [BY8AAFN7C5]
audience: grad
defines: 7W9EG02T79
uses: [DNXCKXZZ08, XQENB067R3, Y92NXGEQBD]
sources:
  - url: https://en.wikipedia.org/wiki/Reverse_mathematics
    locator: Weak Kőnig's lemma WKL0
  - url: https://en.wikipedia.org/wiki/K%C5%91nig%27s_lemma
    locator: Computability aspects
---

## Definition

Work in the language $L_2$ with the codes of the [[definition of second-order arithmetic|Y92NXGEQBD]].
A *binary tree* is a set $T \subseteq 2^{<\N}$ such that every initial segment of an element of $T$ is in $T$.
$T$ is *infinite* when for every $m$ there is $\sigma \in T$ with code at least $m$.
A *path* through $T$ is a function $f \colon \N \to \set{0, 1}$ with $f {\restriction} n \in T$ for every $n$, where $f {\restriction} n$ is the sequence $\langle f(0), \ldots, f(n - 1) \rangle$.

*Weak König's lemma* is the sentence: every infinite binary tree has a path.
$\mathsf{WKL}_0$ is the subsystem of second-order arithmetic whose axioms are those of [[RCA0|DNXCKXZZ08]] together with weak König's lemma.

## Notation

The sentence is written $\mathrm{WKL}$, and the system $\mathsf{WKL}_0 = \mathsf{RCA}_0 + \mathrm{WKL}$.
Some texts spell the name as Kőnig, after Dénes Kőnig.

## Remarks

In $\mathsf{RCA}_0$, a binary tree is infinite exactly when it has an element of every length, since there are only $2^n$ binary sequences of length $n$.

Example: the full binary tree $2^{<\N}$ is infinite, and every function $f \colon \N \to \set{0, 1}$ is a path through it.

Example: the set of binary sequences with no two adjacent entries equal to $1$ is an infinite binary tree; the constant function $0$ is one of its paths.

Non-example: the set $\set{\langle \rangle, \langle 0 \rangle, \langle 0, 0 \rangle, \langle 1 \rangle}$ is a binary tree, but it is finite, so weak König's lemma says nothing about it.

## Explanations

### L1 human

A binary tree is a way to grow sequences of $0$s and $1$s one digit at a time, where some branches can stop.
Weak König's lemma says: if the tree never runs out, then there is an infinite branch.
$\mathsf{WKL}_0$ adds this principle to computable mathematics.

### L2 human

Weak König's lemma is a compactness principle for Cantor space.
It is the usual tool for proving that something exists in $\mathsf{WKL}_0$: one builds a tree whose paths are the wanted objects, and checks that the tree is infinite.
A trap is to apply it to a tree that is not a set in the model, such as a tree defined with an unbounded quantifier.
