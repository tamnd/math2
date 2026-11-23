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

We define the system $\mathsf{WKL}_0$, which is $\mathsf{RCA}_0$ together with the statement that every infinite binary tree has an infinite path.

We work in the language $L_2$ with the codes of the [[definition of second-order arithmetic|Y92NXGEQBD]], so that a finite sequence of numbers is coded by a number.
Let $2^{<\mathbb{N}}$ be the set of codes of finite sequences with entries $0$ and $1$, and write $\lvert \sigma \rvert$ for the length of $\sigma$.
A *binary tree* is a set $T \subseteq 2^{<\mathbb{N}}$ such that every initial segment of an element of $T$ is in $T$.
The tree $T$ is *infinite* when for every $m$ there is $\sigma \in T$ with code at least $m$.
A *path* through $T$ is a function $f \colon \mathbb{N} \to \{0, 1\}$ with $f {\restriction} n \in T$ for every $n$, where $f {\restriction} n = \langle f(0), \ldots, f(n - 1) \rangle$.

*Weak König's lemma* is the sentence
$$\forall T\, \big(T \text{ is an infinite binary tree} \to \exists f\, (f \text{ is a path through } T)\big).$$
$\mathsf{WKL}_0$ is the subsystem of second-order arithmetic whose axioms are those of [[RCA0|DNXCKXZZ08]] together with weak König's lemma.

## Notation

We write $\mathrm{WKL}$ for the sentence and $\mathsf{WKL}_0 = \mathsf{RCA}_0 + \mathrm{WKL}$ for the system.
Some books spell the name Kőnig, after Dénes Kőnig, and write $2^{<\omega}$ for $2^{<\mathbb{N}}$.

## Remarks

Each condition has a job.
Closure under initial segments makes $T$ a tree, so that a path is a way of reading the tree from the root upward.
The bound to entries $0$ and $1$ is what makes the lemma weak: each node has at most two children, and over $\mathsf{RCA}_0$ this gives a much weaker principle than [[König's lemma for finitely branching trees|3P2J5NWCM1]].
Infinity is the hypothesis that the lemma turns into a path.

The definition of "infinite" by codes agrees with the more natural one by lengths.
There are only $2^n$ binary sequences of length $n$, so a tree with elements of arbitrarily large code has elements of arbitrarily large length, and closure under initial segments then gives an element of every length.
$\mathsf{RCA}_0$ proves this equivalence.

For a small example, the set of 0-1 sequences with no two adjacent entries equal to $1$ is an infinite binary tree.
Removing the last entry cannot create two adjacent ones, and the all-zero sequence of each length belongs to it, so the constant function $0$ is a path.

For a case that fails a condition, take $\{ \langle \rangle, \langle 0 \rangle, \langle 0, 0 \rangle, \langle 1 \rangle \}$.
It is a binary tree, but it is finite, so weak König's lemma says nothing about it, and indeed it has no path.
The set $\{ \langle \rangle, \langle 0, 0 \rangle \}$ fails in another way: it is not a tree, since $\langle 0 \rangle$ is missing.

The concept of [[WKL0|7W9EG02T79]] explains what the system proves and which models it has.

## Explanations

### L1 human

A binary tree grows sequences of $0$s and $1$s one digit at a time, and some branches stop.
Weak König's lemma says that if the tree never runs out, then some branch goes on forever.
For example, if the rule is "never write two $1$s in a row", the branch $0, 0, 0, \ldots$ goes on forever.
$\mathsf{WKL}_0$ adds this principle to computable mathematics.

### L2 human

Weak König's lemma is a compactness principle for [[Cantor space|W9VYJRBF9N]].
To prove that something exists in $\mathsf{WKL}_0$, we describe it by finite conditions, collect the finite sequences that satisfy the conditions up to their length into a tree, and check that the tree is infinite.
For the rule "at most one $1$", the tree has the $n + 1$ sequences of length $n$ with at most one $1$, so it is infinite, and a path exists.
Watch out: the tree must be a set of the model, given by $\Delta^0_1$ comprehension.
A tree defined with an unbounded quantifier, such as "the nodes that have extensions of every length", need not exist in $\mathsf{RCA}_0$, and then the lemma cannot be applied to it.
