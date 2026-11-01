---
tag: B6Y8PEY72W
kind: statement
role: theorem
name: Dieudonné's theorem on paracompact Hausdorff spaces
msc: [54D20, 54D15]
uses: [8R29G6NG9Q, 0S1FJ8VEX9, 0NSR9V8TED, DZ297MMGV8]
about: [8R29G6NG9Q, 0NSR9V8TED]
sources:
  - url: https://en.wikipedia.org/wiki/Paracompact_space
---

## Statement

Let $X$ be a [[paracompact|8R29G6NG9Q]] [[Hausdorff space|0S1FJ8VEX9]].
Then $X$ is [[normal|0NSR9V8TED]].
That is, for any two disjoint closed sets $A, B \subseteq X$, there are disjoint open sets $U \supseteq A$ and $V \supseteq B$.

## Remarks

The proof has two steps of the same shape.
First, $X$ is [[regular|03HMJASQBQ]]: for a closed set $C$ and a point $x \notin C$, cover $C$ by open sets whose closures miss $x$, and add $X \setminus C$.
Take a [[locally finite|DZ297MMGV8]] open refinement.
The union of the closures of the members that meet $C$ is closed, by local finiteness, and it misses $x$.
The second step repeats this argument with a closed set in place of the point $x$, using regularity.

Example at work: every [[compact|0TVJZYB6SH]] Hausdorff space is paracompact, so it is normal.

The Hausdorff hypothesis cannot be dropped.
Take $X = \set{a, b, c}$ with open sets $\emptyset$, $\set{a}$, $\set{a, b}$, $\set{a, c}$ and $X$.
It is finite, so paracompact.
The closed sets $\set{b}$ and $\set{c}$ are disjoint, but every open set containing either of them contains $a$.

## Explanations

### L1 human

A normal space is one where two disjoint closed sets can be put in disjoint open boxes.
Dieudonné's theorem says that paracompactness plus the Hausdorff condition already gives this.
It extends the classical fact that compact Hausdorff spaces are normal.

### L2 human

Normality is what makes [[Urysohn's lemma|01EY3VR7ZD]] work.
So on a paracompact Hausdorff space, there are many continuous real functions.
This is the first step toward partitions of unity subordinate to an open cover.
In fact, a Hausdorff space is paracompact if and only if every open cover has a subordinate partition of unity.
