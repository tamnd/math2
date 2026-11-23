---
tag: E87G6ZTMTN
kind: statement
role: theorem
name: Soundness of normal modal logics
msc: ["03B45"]
topics: [SKY7AQFG1V]
audience: grad
uses: [JS8W7PA6JK, 6BQ71KQ6QT, 4A84VHDTHV]
about: [D1TJYZZDCY, NGHWZ9Y7ZV]
proofs: [V4J6AXX5DF]
sources:
  - url: https://en.wikipedia.org/wiki/Kripke_semantics
    locator: Correspondence and completeness
  - url: https://builds.openlogicproject.org/
    locator: Boxes and Diamonds
---

## Statement

Let $\mathsf{C}$ be a class of [[Kripke frames|6BQ71KQ6QT]], and let $\operatorname{Log}(\mathsf{C})$ be the set of modal formulas valid on every frame of $\mathsf{C}$.

1. $\operatorname{Log}(\mathsf{C})$ is a [[normal modal logic|JS8W7PA6JK]].
2. Let $\Gamma$ be a set of formulas, each valid on every frame of $\mathsf{C}$. Then every theorem of $\mathsf{K}\Gamma$ is valid on every frame of $\mathsf{C}$.

In particular, every theorem of $\mathsf{K}$ is valid on every frame.
The proof is in [[the proof of soundness|V4J6AXX5DF]].

## Remarks

### What soundness is for

Soundness is the tool for showing that a formula is not provable.
To show $\mathsf{K}\Gamma \nvdash \varphi$, we find a frame on which every formula of $\Gamma$ is valid, and a model on it with a world where $\varphi$ is false.
For instance, $\mathsf{K}$ is consistent, since $\bot$ is false on the frame with one world.
With [[common modal axiom schemata|FDFQFWPM4X]], the logics $\mathsf{T}$, $\mathsf{S4}$ and $\mathsf{S5}$ are sound for reflexive frames, for preorders and for equivalence relations.

### Why frames and not models

The hypothesis is validity on frames, and truth in one model is not enough.
The formulas true in one model need not be closed under uniform substitution; see [[the axiom 4 example|NA6H3978PW]].
Truth at some worlds is not enough either, since necessitation fails for it.
If $p$ is true at $w$ and false at a successor of $w$, then $p$ holds at $w$ while $\square p$ does not.

### The converse is completeness

The converse says that every formula valid on all frames of $\mathsf{C}$ is a theorem of $\mathsf{K}\Gamma$.
It holds for the logics of [[the completeness theorem|FXTCKYR3AQ]].
It fails for some normal logics, which are [[Kripke incomplete|W67YJQTT50]].

### Other forms of soundness

The same proof gives soundness for local consequence.
If $\Delta \vdash_{\mathsf{K}\Gamma} \varphi$, then $\varphi$ is true at every world of a $\mathsf{C}$-model where all of $\Delta$ is true.
Soundness also holds for normal [[neighborhood frames|CN7HK9K1B6]] and for [[general frames|GGG7BB78JB]], by the same induction.

## History

Soundness for the relational semantics is part of Kripke's paper of 1963, where it is the easy half of each completeness theorem.

## Explanations

### L1 human

Soundness says that the rules of a modal logic never lead from true laws to false ones.
If the starting laws hold at every world of some kind of model, then everything we derive also holds there.
For example, "if necessarily $p$ and necessarily $q$, then necessarily $p$ and $q$" holds at every world of every frame.

### L2 human

We use soundness to show $\mathsf{K} \nvdash \square p \to p$.

1. Take the frame with $W = \{ w \}$ and $R = \varnothing$, and take $V(p) = \varnothing$.
2. $\square p$ is true at $w$, since $w$ has no successors.
3. $p$ is false at $w$, so $\square p \to p$ is false at $w$.
4. By soundness, every theorem of $\mathsf{K}$ is true at $w$, so $\square p \to p$ is not a theorem.

The typical use is exactly this: a countermodel shows that a formula is not provable.
Watch out: the countermodel must lie on a frame that validates every axiom of the logic, not only the axioms a proof seems to need.

### L3 human

Soundness says that $\operatorname{Log}$ sends classes of frames to normal logics.
This is one half of a Galois connection between classes of frames and normal logics.
The other half sends a logic $\Lambda$ to the class of frames that validate it.
The logics fixed by the connection are the Kripke complete ones.
