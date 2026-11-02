---
tag: VP1N9S4J4F
kind: definition
name: Algebraic stack
msc: [14A20, 18F20]
defines: VNX79CRH90
uses: [5A35TYZD02, MTV9TFKF3X, EXKGG9X6J0, 1DZMT4S9FB]
sources:
  - url: https://en.wikipedia.org/wiki/Algebraic_stack
---

## Definition

Let $S$ be a [[scheme|5A35TYZD02]], and let $\mathcal{C}$ be the category of schemes over $S$ with the fppf topology.
An *algebraic stack* over $S$ is a category $\mathcal{X}$ with a functor $p \colon \mathcal{X} \to \mathcal{C}$ such that:

1. $\mathcal{X}$ is a stack in groupoids over $\mathcal{C}$: every fibre category is a groupoid, and objects and morphisms glue along fppf coverings.
2. The diagonal $\mathcal{X} \to \mathcal{X} \times_{\mathcal{C}} \mathcal{X}$ is representable by [[algebraic spaces|MTV9TFKF3X]].
3. There are an $S$-scheme $U$ and a 1-morphism from $U$ to $\mathcal{X}$ that is surjective and [[smooth|EXKGG9X6J0]].

In clause 3, a scheme $U$ is seen as the stack of $S$-schemes over $U$.
Clause 2 makes this 1-morphism representable by algebraic spaces, so surjective and smooth make sense.

## Remarks

Let $k$ be a field and $G$ a finite group, seen as a constant group scheme over $k$.
The classifying stack $BG$, whose objects over $T$ are $G$-torsors over $T$, is an algebraic stack.
The map $\operatorname{Spec} k \to BG$ given by the trivial torsor is surjective and étale, hence smooth.
Every algebraic space is an algebraic stack whose fibre categories have only identity morphisms.
A functor that fails the sheaf condition, such as the constant presheaf with value $\set{0, 1}$, fails clause 1.
If in clause 3 the map can be chosen étale, the stack is called a Deligne–Mumford stack.
This is the definition of the Stacks Project; some authors also require the diagonal to be quasi-compact and separated.
