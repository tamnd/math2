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
Consider the following axioms.
$$\begin{aligned} \mathrm{K}&: \square(p \to q) \to (\square p \to \square q), & \mathrm{T}&: \square p \to p, & \mathrm{D}&: \square p \to \lozenge p, \\ \mathrm{B}&: p \to \square\lozenge p, & \mathrm{4}&: \square p \to \square\square p, & \mathrm{5}&: \lozenge p \to \square\lozenge p. \end{aligned}$$
Then $\mathfrak{F} \models \mathrm{K}$ for every frame, and the other axioms match properties of the [[accessibility relation|YHGXV3SQDP]] as follows.

1. $\mathfrak{F} \models \mathrm{T}$ if and only if $R$ is reflexive.
2. $\mathfrak{F} \models \mathrm{D}$ if and only if $R$ is serial.
3. $\mathfrak{F} \models \mathrm{B}$ if and only if $R$ is symmetric.
4. $\mathfrak{F} \models \mathrm{4}$ if and only if $R$ is transitive.
5. $\mathfrak{F} \models \mathrm{5}$ if and only if $R$ is Euclidean.

So for $\Sigma \subseteq \{ \mathrm{T}, \mathrm{D}, \mathrm{B}, \mathrm{4}, \mathrm{5} \}$, every theorem of the [[normal modal logic|JS8W7PA6JK]] $\mathsf{K}\Sigma$ is valid on every frame with the matching properties.
The proof is in [[the proof of the correspondences|X8PAF0TD5W]].

## Remarks

### Two cases by hand

Take the frame with $W = \{ 1, 2 \}$ and $R = \{ (1, 2), (2, 2) \}$, where world $1$ is irreflexive.
With $V(p) = \{ 2 \}$, the formula $\square p$ is true at $1$, since its only successor $2$ has $p$, while $p$ is false at $1$.
So $\mathrm{T}$ fails at $1$, and the missing loop at $1$ is exactly what the countermodel uses.

Now take $W = \{ 1, 2, 3 \}$ with $R = \{ (1, 2), (2, 3) \}$, which is not transitive since $(1, 3) \notin R$.
With $V(p) = \{ 2 \}$, the formula $\square p$ is true at $1$, and $\square p$ is false at $2$ because $3$ lacks $p$.
So $\square\square p$ is false at $1$, and $\mathrm{4}$ fails there.
Adding the pair $(1, 3)$ repairs the frame, and then $\mathrm{4}$ holds at every world.

### Frames, not models

The equivalences are about validity on a frame, under every valuation.
In a single model an axiom can be true although the frame lacks the property.
On the path $1 \to 2 \to 3$ above, the valuation $V(p) = W$ makes $\mathrm{4}$ true at every world, although the frame is not transitive; see [[the axiom 4 example|NA6H3978PW]].

### Names, soundness and non-theorems

The logics are named by their axioms: $\mathsf{T} = \mathsf{KT}$, $\mathsf{D} = \mathsf{KD}$, $\mathsf{B} = \mathsf{KTB}$, $\mathsf{S4} = \mathsf{KT4}$ and $\mathsf{S5} = \mathsf{KT5}$.
By [[soundness of normal modal logics|E87G6ZTMTN]], $\mathsf{T}$ is sound for reflexive frames, $\mathsf{S4}$ for preorders and $\mathsf{S5}$ for equivalence relations.
Likewise $\mathsf{KD45}$ is sound for serial, transitive and Euclidean frames.
A frame gives non-theorems too: $\mathsf{T} \nvdash \mathrm{4}$, since a reflexive frame need not be transitive; see [[the reflexive non-transitive frame|EP284NG45P]].
With the [[completeness theorem|FXTCKYR3AQ]], each $\mathsf{K}\Sigma$ is exactly the set of formulas valid on the frames with the matching properties.

### Which conditions are modal

Not every first-order condition on $R$ is defined by a modal formula.
Irreflexivity is defined by none.
In the other direction, the McKinsey formula $\square\lozenge p \to \lozenge\square p$ defines no first-order condition.
[[Modal correspondence theory|3RYBWYPJVD]] studies this question in general.

### More correspondences

The formula $\lozenge p \to \square p$ is valid exactly on the frames where each world has at most one successor.
The Geach axiom $\lozenge^k\square^l p \to \square^m\lozenge^n p$ is valid exactly when $w R^k v$ and $w R^m u$ imply some $x$ with $v R^l x$ and $u R^n x$.
All these are cases of [[Sahlqvist's theorem|S4SSDMETJM]].

## History

Kripke's paper of 1963 matched the logics $\mathsf{T}$, $\mathsf{S4}$, $\mathsf{B}$ and $\mathsf{S5}$ with reflexive, preorder, reflexive symmetric and equivalence relations.
The numerals in $\mathrm{4}$ and $\mathrm{5}$ come from Lewis's systems $\mathsf{S4}$ and $\mathsf{S5}$, and $\mathrm{D}$ stands for "deontic".
The letter $\mathrm{B}$ refers to Brouwer; see [[Brouwerian modal logic|2QPT4KCM0Q]].

## Explanations

### L1 human

Each axiom about necessity matches one rule about the arrows between worlds.
"What is necessary is true" matches "every world sees itself".
"What is necessary is necessarily necessary" matches "two arrows in a row can be replaced by one arrow".
"What is true is necessarily possible" matches "every arrow has an arrow back".
For example, let world 1 see world 2 while world 2 does not see world 1.
If a fact is true only at world 1, then at world 1 it is true but not necessarily possible.

### L2 human

We check $\mathrm{5}$ on the frame with $W = \{ a, b, c \}$ and the following relation.
$$R = \{ (a, b), (a, c), (b, b), (b, c), (c, b), (c, c) \}$$
Every world has the successor set $\{ b, c \}$.
The Euclidean property asks that any two successors $v, u$ of one world satisfy $v R u$.
Here this means $b R b$, $b R c$, $c R b$ and $c R c$, which all hold, so $\mathrm{5}$ is valid on the frame.
But $(a, a) \notin R$, so with $V(p) = \{ b, c \}$ the axiom $\mathrm{T}$ fails at $a$.
The typical use is to read off quickly which standard logics a frame validates.
Watch out: a single model can hide the failure of a frame condition, so a countermodel needs the right valuation.

### L3 human

Frame validity of $\varphi$ is the second-order sentence $\forall P_1 \dots \forall P_n \forall x\, \mathrm{ST}_x(\varphi)$, by the [[standard translation|YW6YGBMVQY]].
For the five axioms, the second-order quantifiers can be removed by substituting a minimal valuation.
Examples are $P = R[x]$ for $\mathrm{T}$ and $\mathrm{4}$, and $P = \{ x \}$ for $\mathrm{B}$.
This method, applied to a syntactic class of formulas, is the Sahlqvist algorithm, treated in [[modal model theory|SPQVNPZDTB]].
