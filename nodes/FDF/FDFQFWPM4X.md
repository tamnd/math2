---
tag: FDFQFWPM4X
kind: statement
role: theorem
name: Common modal axiom schemata
msc: ["03B45"]
topics: [SKY7AQFG1V]
audience: grad
uses: [6BQ71KQ6QT, YHGXV3SQDP, JS8W7PA6JK]
about: [XBCYFDPS2F, NGHWZ9Y7ZV]
proofs: [X8PAF0TD5W]
sources:
  - url: https://en.wikipedia.org/wiki/Kripke_semantics
    locator: Common modal axiom schemata
  - url: https://builds.openlogicproject.org/
    locator: Boxes and Diamonds
  - wikipedia: en:911960@r1374082003
    locator: Kripke semantics, section Semantics of modal logic > Correspondence and completeness > Common modal axiom schemata
    note: adopted
    mention: wikipedia://en/911960#WA4R
    sections: [Statement]
inventory: [XJNAXC8N0J]
---

## Statement

Let $\mathfrak{F} = (W, R)$ be a [[Kripke frame|6BQ71KQ6QT]], and write $\mathfrak{F} \models \varphi$ when $\varphi$ is valid on $\mathfrak{F}$.
Consider the axioms
$$\begin{aligned} \mathrm{K}&: \square(p \to q) \to (\square p \to \square q), & \mathrm{T}&: \square p \to p, & \mathrm{D}&: \square p \to \lozenge p, \\ \mathrm{B}&: p \to \square\lozenge p, & \mathrm{4}&: \square p \to \square\square p, & \mathrm{5}&: \lozenge p \to \square\lozenge p. \end{aligned}$$
Then $\mathfrak{F} \models \mathrm{K}$ for every frame, and for the other axioms the following equivalences hold, with the properties of the [[accessibility relation|YHGXV3SQDP]].

1. $\mathfrak{F} \models \mathrm{T}$ if and only if $R$ is reflexive.
2. $\mathfrak{F} \models \mathrm{D}$ if and only if $R$ is serial.
3. $\mathfrak{F} \models \mathrm{B}$ if and only if $R$ is symmetric.
4. $\mathfrak{F} \models \mathrm{4}$ if and only if $R$ is transitive.
5. $\mathfrak{F} \models \mathrm{5}$ if and only if $R$ is Euclidean.

So for a set $\Sigma \subseteq \set{\mathrm{T}, \mathrm{D}, \mathrm{B}, \mathrm{4}, \mathrm{5}}$, every theorem of the [[normal modal logic|JS8W7PA6JK]] $\mathsf{K}\Sigma$ is valid on every frame with the matching properties.
The proof is in [[the proof of the correspondences|X8PAF0TD5W]].

## Remarks

### Why each hypothesis is needed

1. The equivalences concern validity on a frame. In a single model the axiom can be true although the frame lacks the property. For example, axiom $\mathrm{4}$ is true in a model on a non-transitive frame with $V(p) = W$, see [[the axiom 4 example|NA6H3978PW]].
2. The equivalences are about the variable $p$ under all valuations; one fixed valuation is not enough to force the property.

### Consequences

1. The logic is named by its axioms: $\mathsf{KT} = \mathsf{T}$, $\mathsf{KD} = \mathsf{D}$, $\mathsf{K4}$, $\mathsf{KTB} = \mathsf{B}$, $\mathsf{KT4} = \mathsf{S4}$, $\mathsf{KT5} = \mathsf{S5}$, $\mathsf{KD45}$, and in general $\mathsf{K}\Sigma$.
2. Soundness: $\mathsf{T}$ is sound for reflexive frames, $\mathsf{S4}$ for preorders, $\mathsf{S5}$ for equivalence relations and $\mathsf{KD45}$ for serial, transitive, Euclidean frames. All four follow from [[soundness of normal modal logics|E87G6ZTMTN]].
3. Non-theorems: $\mathsf{T} \nvdash \mathrm{4}$, since a reflexive frame need not be transitive, see [[the reflexive non-transitive frame|EP284NG45P]].
4. With the [[completeness theorem|FXTCKYR3AQ]], each logic $\mathsf{K}\Sigma$ is exactly the set of formulas valid on the frames with the matching properties.

### Converse

Each item is an equivalence, so its converse is part of the statement.
The general converse question asks which first-order conditions are defined by modal formulas, and it has a negative answer.
Irreflexivity is not defined by any modal formula, and the McKinsey formula $\square\lozenge p \to \lozenge\square p$ defines no first-order condition.

### Generalizations

1. For $\mathrm{alt}_1$: $\lozenge p \to \square p$ is valid exactly when each world has at most one successor.
2. For the Geach axioms $\lozenge^k\square^l p \to \square^m\lozenge^n p$: the frame condition is that $w R^k v$ and $w R^m u$ imply some $x$ with $v R^l x$ and $u R^n x$.
3. All these are special cases of Sahlqvist's theorem, a topic of [[modal model theory|SPQVNPZDTB]].

## History

Kripke's paper of 1963 matched the logics $\mathsf{T}$, $\mathsf{S4}$, $\mathsf{B}$ and $\mathsf{S5}$ with reflexive, reflexive transitive, reflexive symmetric and equivalence relations.
The numerals in $\mathrm{4}$ and $\mathrm{5}$ come from Lewis's systems $\mathsf{S4}$ and $\mathsf{S5}$, of which these axioms are characteristic, and $\mathrm{D}$ stands for "deontic".
The letter $\mathrm{B}$ refers to Brouwer, see [[Brouwerian modal logic|2QPT4KCM0Q]].

## Explanations

### L1 human

Each axiom of necessity matches one rule about the arrows between worlds.
"What is necessary is true" matches "every world sees itself".
"What is necessary is necessarily necessary" matches "two arrows in a row can be replaced by one arrow".
"What is true is necessarily possible" matches "every arrow has an arrow back".
For example, take a frame where world 1 sees world 2 but world 2 does not see world 1.
On it, the third law fails at world 1 when the basic statement is true only at world 1.

### L2 human

We check axiom $\mathrm{5}$ on the frame $W = \set{a, b, c}$, $R = \set{(a,b), (a,c), (b,b), (b,c), (c,b), (c,c)}$.

1. The pairs of successors of $a$ are $b, c$; we need $b R c$ and $c R b$ and $b R b$ and $c R c$, which hold.
2. The successors of $b$ are $b, c$; again the four pairs hold.
3. The successors of $c$ are $b, c$; the same check applies.
4. So $R$ is Euclidean, and $\mathrm{5}$ is valid on the frame.
5. $R$ is not reflexive, since $(a, a) \notin R$, so with $V(p) = \set{b, c}$, the axiom $\mathrm{T}$ fails at $a$.

The typical use is to read off quickly which standard logic a frame belongs to.
A trap: the frame conditions are about the frame, and a single model can hide the failure of a condition.

### L3 human

Each correspondence is the case of one formula in a general phenomenon: frame validity of $\varphi$ is the second-order sentence $\forall P_1 \dots \forall P_n \forall x\, \mathrm{ST}_x(\varphi)$, see the [[standard translation|YW6YGBMVQY]].
For the five axioms, the second-order quantifiers can be removed by substituting the "minimal" valuation.
Examples are $P = R[x]$ for $\mathrm{T}$ and $\mathrm{4}$, or $P = \set{x}$ for $\mathrm{B}$.
This method, applied to a syntactic class of formulas, is the Sahlqvist algorithm, treated in [[modal model theory|SPQVNPZDTB]].
