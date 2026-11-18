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

### Why each hypothesis is needed

1. Validity on frames cannot be replaced by validity in a model. The set of formulas valid in one model need not be closed under uniform substitution, see [[the axiom 4 example|NA6H3978PW]].
2. The axioms in $\Gamma$ must be valid on the frames, not only true at some worlds. Otherwise necessitation fails, since $p$ can be true at $w$ while $\square p$ is false there.

### Consequences

1. To show $\mathsf{K}\Gamma \nvdash \varphi$, it suffices to find a frame on which $\Gamma$ is valid and a model on it with a world where $\varphi$ fails.
2. $\mathsf{K}$ is consistent, since $\bot$ is not valid on the one-world frame.
3. With [[common modal axiom schemata|FDFQFWPM4X]], the logics $\mathsf{T}$, $\mathsf{S4}$ and $\mathsf{S5}$ are sound for reflexive frames, preorders and equivalence relations.

### Converse

The converse, that every formula valid on all frames of $\mathsf{C}$ is a theorem of $\mathsf{K}\Gamma$, is completeness.
It holds for the logics of [[the completeness theorem|FXTCKYR3AQ]], and it fails for some normal logics, which are Kripke incomplete.

### Generalizations

1. The same proof gives soundness for local consequence. If $\Delta \vdash_{\mathsf{K}\Gamma} \varphi$, then $\varphi$ is true at every world of a $\mathsf{C}$-model where all of $\Delta$ is true.
2. Soundness also holds for normal neighbourhood frames and for general frames, with the same induction.

## History

Soundness for the relational semantics is part of Kripke's paper of 1963; it is the easy half of each of his completeness theorems.

## Explanations

### L1 human

Soundness says that the rules of a modal logic never lead from true laws to false ones.
If the starting laws hold in every world of some kind of model, then everything we derive also holds there.
For example, the law "if necessarily $p$ and necessarily $q$, then necessarily ($p$ and $q$)" holds at every world of every frame.

### L2 human

We use soundness to show $\mathsf{K} \nvdash \square p \to p$.

1. Take the frame $W = \set{w}$ with $R = \emptyset$.
2. Take $V(p) = \emptyset$.
3. $\square p$ is true at $w$, since $w$ has no successors.
4. $p$ is false at $w$, so $\square p \to p$ fails at $w$.
5. By soundness, every theorem of $\mathsf{K}$ is true at $w$, so $\square p \to p$ is not a theorem.

The typical use is exactly this: a countermodel shows that a formula is not provable.
A trap: the countermodel must be on a frame that validates all axioms of the logic, not only those the proof seems to need.

### L3 human

Soundness is the statement that $\operatorname{Log}$ maps classes of frames to normal logics.
This is the first half of a Galois connection between classes of frames and normal logics.
The other half sends a logic $\Lambda$ to the class of frames that validate it.
The logics fixed by the connection are the Kripke complete ones.
