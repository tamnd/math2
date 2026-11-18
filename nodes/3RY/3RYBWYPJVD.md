---
tag: 3RYBWYPJVD
kind: concept
name: Modal correspondence theory
msc: ["03B45", "03C95"]
topics: [SPQVNPZDTB]
audience: grad
uses: [NGHWZ9Y7ZV, YW6YGBMVQY, 086QKPF0A6, G6X7SZSNC5, FDFQFWPM4X]
sources:
  - url: https://en.wikipedia.org/wiki/Kripke_semantics
    locator: Correspondence and completeness
  - url: https://en.wikipedia.org/wiki/Sahlqvist_formula
    locator: Definition
  - url: https://en.wikipedia.org/wiki/Standard_translation
    locator: Definition
  - url: https://builds.openlogicproject.org/
    locator: Modal Logic
---

## Summary

A Kripke frame is a pair $\mathfrak{F} = (W, R)$ of a nonempty set and a binary relation, and $\mathfrak{F} \models \varphi$ means that $\varphi$ is true at every world under every valuation; see [[Kripke semantics|NGHWZ9Y7ZV]].
A modal formula $\varphi$ *defines* a class $\mathsf{K}$ of frames if, for every frame $\mathfrak{F}$, $\mathfrak{F} \models \varphi$ holds exactly when $\mathfrak{F} \in \mathsf{K}$.
The formula $\varphi$ *corresponds* to a [[first-order|086QKPF0A6]] sentence $\alpha$ in the language with one binary symbol $R$ when $\mathfrak{F} \models \varphi$ if and only if $\mathfrak{F} \models \alpha$, for every frame.
It *locally corresponds* to $\alpha(x)$ when $\mathfrak{F}, w \models \varphi$ under all valuations if and only if $\mathfrak{F} \models \alpha[w]$, for every frame and world.
Modal correspondence theory studies which modal formulas have first-order correspondents, how to compute them, and which classes of frames are modally definable.
It matters because frame conditions are the bridge between axioms of modal logics and the relational structures that the axioms describe.

## Motivation

The axioms of the familiar modal logics correspond to simple properties of the accessibility relation: $\square p \to p$ to reflexivity, $\square p \to \square \square p$ to transitivity.
These facts explain why the logics $\mathsf{T}$, $\mathsf{S4}$ and [[S5|VC3A2VWXND]] are complete for the frames with these properties.
A general theory should say which formulas behave in this way, and why some formulas do not.
The source of the difficulty is the shape of frame validity.
By the [[standard translation|YW6YGBMVQY]], $\mathfrak{F} \models \varphi$ says
$$\mathfrak{F} \models \forall P_1 \cdots \forall P_n \, \forall x \, \mathrm{ST}_x(\varphi),$$
where $p_1, \ldots, p_n$ are the variables of $\varphi$.
This is a universal monadic [[second-order|G6X7SZSNC5]] sentence, so every modal formula defines a $\Pi^1_1$ class of frames, and the question is when the second-order quantifiers can be removed.

## Notation

We write $\mathfrak{F} \models \varphi$ for frame validity, $\mathfrak{F}, w \models \varphi$ for validity at $w$ under all valuations, and $\mathfrak{M}, w \models \varphi$ for truth in a model.
$\mathrm{Fr}(\varphi)$ denotes the class of frames that validate $\varphi$.
Many texts write $\Diamond$ for $\lozenge$ and $\Box$ for $\square$.

## Remarks

### Examples

1. $\square p \to p$ corresponds to reflexivity $\forall x \, R(x, x)$, and $\square p \to \square \square p$ to transitivity; see [[common modal axiom schemata|FDFQFWPM4X]].
2. $p \to \square \lozenge p$ corresponds to symmetry, and $\lozenge \top$ to seriality $\forall x \, \exists y \, R(x, y)$.
3. $\square \square p \to \square p$ corresponds to density; see [[the density axiom corresponds to density|TBVXHH00GQ]].
4. $\lozenge \square p \to \square \lozenge p$ corresponds to confluence; see [[the axiom .2 corresponds to confluence|SD4F3G0EPR]].
5. $\lozenge p \to \square p$ corresponds to $\forall x \, \forall y \, \forall z \, (R(x, y) \wedge R(x, z) \to y = z)$, so each world has at most one successor.
6. All these formulas are Sahlqvist formulas, and [[Sahlqvist's theorem|S4SSDMETJM]] computes their correspondents by one algorithm.

### Non-examples

1. Löb's formula $\square(\square p \to p) \to \square p$ has no first-order correspondent; see [[Löb's formula is not first-order definable|RVTJNF5HMF]]. Its frame condition includes converse well-foundedness.
2. The McKinsey formula $\square \lozenge p \to \lozenge \square p$ has no first-order correspondent; see [[the McKinsey formula|4N4ZNWZRE2]].
3. Grzegorczyk's formula $\square(\square(p \to \square p) \to p) \to p$ defines the partial orders without infinite strictly ascending chains, which is not a first-order class; see [[Grzegorczyk logic|2Q8E4GQF3B]].
4. Irreflexivity is a first-order property that no modal formula defines, since it is not preserved by bounded morphic images; see [[bisimulation invariance|TKFFTAX30E]].

### Basic properties

1. Every modal formula defines a class of frames that is closed under generated subframes, bounded morphic images and disjoint unions, and that reflects ultrafilter extensions.
2. Conversely, a first-order class of frames with these closure properties is modally definable, by the [[Goldblatt-Thomason theorem|GX5E3GNRCS]].
3. Every Sahlqvist formula has a local first-order correspondent, which can be computed; see [[Sahlqvist's theorem|S4SSDMETJM]].
4. If $\varphi$ has a first-order correspondent, then $\mathrm{Fr}(\varphi)$ is closed under elementary equivalence, and so under ultraproducts and elementary substructures. The [[McKinsey formula|4N4ZNWZRE2]] fails the last condition, and this is how one proves that it has no correspondent.
5. Correspondence on frames and truth in models differ. In the model on one world $a$ without successors and with $p$ true, $\square p \to p$ is true, though the frame is not reflexive.

### History

Correspondence results for single axioms were known from the completeness theory of the 1960s.
Henrik Sahlqvist gave a general class of formulas with first-order correspondents in 1975.
Johan van Benthem developed correspondence theory as a subject in his 1976 dissertation "Modal correspondence theory".
Goldblatt and Thomason characterized the modally definable elementary classes in 1975.

### Common errors

1. Reading frame correspondence as a statement about models. A frame condition is equivalent to validity under all valuations, not to truth under one valuation.
2. Assuming that every modal formula is first-order on frames. Löb's and McKinsey's formulas are the standard counterexamples.
3. Assuming that every first-order frame property is modally definable. Irreflexivity and antisymmetry are not.

## Explanations

### L1 human

A modal axiom is a rule about statements such as "it is necessary that".
A frame is a picture of points with arrows between them.
Correspondence theory finds, for each rule, the shape of the pictures in which the rule is always true.
For example, "what is necessary is true" holds in every picture exactly when every point has an arrow to itself.
Some rules match no simple shape that can be described with "for all points" and "there is a point".

### L2 human

We find the frame condition of $\lozenge \top$.

1. $\mathfrak{F}, w \models \lozenge \top$ means that some $v$ has $w R v$, since $\top$ is true everywhere.
2. The formula has no variables, so the valuation plays no role.
3. So $\mathfrak{F} \models \lozenge \top$ if and only if every world has a successor, that is, $\forall x \, \exists y \, R(x, y)$.
4. Now take $\square p \to p$. If $R$ is reflexive and $w \models \square p$, then $w R w$ gives $w \models p$.
5. If $w R w$ fails, put $p$ true everywhere except at $w$. Then $w \models \square p$ and $w \not\models p$.

The typical use is in completeness proofs: one shows that the canonical frame of a logic has the property that its axioms correspond to.
A trap: step 5 needs a valuation chosen for the frame, so the argument says nothing about one fixed model.

### L3 human

The standard translation places modal logic inside monadic second-order logic on frames and inside first-order logic on models.
Correspondence theory studies the gap between the two: when a $\Pi^1_1$ condition collapses to a first-order one.
Sahlqvist's theorem and the algorithms SQEMA and ALBA give syntactic sufficient conditions, and Chagrova showed that first-order definability of a modal formula is undecidable.
Algebraically, correspondence is linked to canonicity through duality, and Fine's theorem says that a logic complete for a first-order class of frames is canonical.
The same questions arise for intuitionistic logic, where intermediate axioms correspond to conditions on partial orders, and for extended modal languages, where nominals make many more conditions definable.
