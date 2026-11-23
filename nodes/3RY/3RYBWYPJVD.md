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

Take the modal formula $\square p \to p$ and a frame $(W, R)$.
If every world sees itself, then $\square p$ at $w$ forces $p$ at $w$, so the formula is valid.
If some $w$ does not see itself, make $p$ true everywhere except at $w$; then $\square p$ holds at $w$ and $p$ fails.
So $\square p \to p$ is valid on a frame exactly when the first-order sentence $\forall x \, R(x, x)$ is true in it.

Correspondence theory asks this question for every modal formula: which [[first-order|086QKPF0A6]] condition on $R$, if any, says the same as validity of the formula.
It works because validity quantifies over all valuations, and for many formulas one valuation, the smallest one that makes the antecedent true, already decides everything.
The theory matters because frame conditions link the axioms of a modal logic to the relational structures that the axioms describe.

Students slip on the difference between frames and models.
A frame condition matches validity under every valuation, and it says nothing about truth in one fixed model.

## Motivation

The axioms of the familiar modal logics correspond to simple properties of the accessibility relation.
These facts explain why the logics $\mathsf{T}$, $\mathsf{S4}$ and [[S5|VC3A2VWXND]] are complete for frames with these properties.
A general theory should say which formulas behave in this way, and why some formulas do not.

The difficulty lies in the shape of frame validity.
Let $p_1, \ldots, p_n$ be the variables of $\varphi$.
By the [[standard translation|YW6YGBMVQY]], $\mathfrak{F} \models \varphi$ is the following statement.
$$\mathfrak{F} \models \forall P_1 \cdots \forall P_n \, \forall x \, \mathrm{ST}_x(\varphi)$$
This is a universal monadic [[second-order|G6X7SZSNC5]] sentence.
So every modal formula defines a $\Pi^1_1$ class of frames, and the question is when the second-order quantifiers can be removed.

## Notation

A Kripke frame is a pair $\mathfrak{F} = (W, R)$ of a nonempty set and a binary relation; see [[Kripke semantics|NGHWZ9Y7ZV]].
We write $\mathfrak{F} \models \varphi$ when $\varphi$ is true at every world under every valuation.
We write $\mathfrak{F}, w \models \varphi$ when $\varphi$ is true at $w$ under every valuation, and $\mathfrak{M}, w \models \varphi$ for truth in a model.
$\mathrm{Fr}(\varphi)$ denotes the class of frames that validate $\varphi$, and $\varphi$ *defines* a class $\mathsf{K}$ when $\mathrm{Fr}(\varphi) = \mathsf{K}$.
The formula $\varphi$ *corresponds* to a first-order sentence $\alpha$ in the language with one binary symbol $R$ when $\mathfrak{F} \models \varphi$ if and only if $\mathfrak{F} \models \alpha$, for every frame.
It *locally corresponds* to $\alpha(x)$ when $\mathfrak{F}, w \models \varphi$ if and only if $\mathfrak{F} \models \alpha[w]$, for every frame and world.

## Remarks

### A catalog of correspondents

Each line below is checked in the same way as the reflexivity example of the Summary.
See [[common modal axiom schemata|FDFQFWPM4X]] for the axiom names.

1. $\square p \to \square \square p$ corresponds to transitivity, and $p \to \square \lozenge p$ to symmetry.
2. $\lozenge \top$ corresponds to seriality $\forall x \, \exists y \, R(x, y)$.
3. $\square \square p \to \square p$ corresponds to density; see [[the density axiom corresponds to density|TBVXHH00GQ]].
4. $\lozenge \square p \to \square \lozenge p$ corresponds to confluence; see [[the axiom .2 corresponds to confluence|SD4F3G0EPR]].
5. $\lozenge p \to \square p$ corresponds to $\forall x \, \forall y \, \forall z \, (R(x, y) \wedge R(x, z) \to y = z)$.

All these formulas are Sahlqvist formulas, and [[Sahlqvist's theorem|S4SSDMETJM]] computes their correspondents by one algorithm.

### Worked example: at most one successor

We check line 5 of the catalog.
Suppose each world has at most one successor, and let $w \models \lozenge p$.
Then some successor $v$ of $w$ has $p$, and every successor of $w$ equals $v$, so $w \models \square p$.
Conversely, suppose $w R y$ and $w R z$ with $y \neq z$.
Make $p$ true at $y$ only.
Then $w \models \lozenge p$ through $y$, and $w \not\models \square p$ because $p$ fails at $z$.

### Worked example: a formula without variables

The formula $\lozenge \top$ contains no variable, so the valuation plays no role.
A world satisfies it exactly when it has a successor.
So $\mathfrak{F} \models \lozenge \top$ if and only if $\forall x \, \exists y \, R(x, y)$, and this holds locally too, with $\exists y \, R(x, y)$.

### What has no correspondent, and what is not definable

Löb's formula $\square(\square p \to p) \to \square p$ has no first-order correspondent; see [[Löb's formula is not first-order definable|RVTJNF5HMF]].
Its frames are the transitive frames with no infinite path $x_0 R x_1 R x_2 R \cdots$.
The McKinsey formula $\square \lozenge p \to \lozenge \square p$ has no first-order correspondent either; see [[the McKinsey formula|4N4ZNWZRE2]].

In the other direction, irreflexivity is first-order but defined by no modal formula.
The two-cycle maps onto a single reflexive point by a bounded morphism, and so does the successor chain in [[this example|T3YJ84YDV4]].
Validity is preserved by bounded morphic images, so any formula valid on all irreflexive frames is valid on the loop, which is not irreflexive.

### The rules you can use

1. Every class $\mathrm{Fr}(\varphi)$ is closed under generated subframes, bounded morphic images and disjoint unions, and it reflects ultrafilter extensions.
2. A first-order class of frames with these closure properties is modally definable, by the [[Goldblatt-Thomason theorem|GX5E3GNRCS]].
3. Every Sahlqvist formula has a local first-order correspondent, and it can be computed.
4. If $\varphi$ has a first-order correspondent, then $\mathrm{Fr}(\varphi)$ is closed under elementary equivalence, so under ultraproducts and elementary substructures.
   The McKinsey formula fails the last condition, and this is how one proves that it has no correspondent.

### History

Correspondences for single axioms were known from the completeness theory of the 1960s.
Henrik Sahlqvist gave a general class of formulas with first-order correspondents in 1975.
In the same year, Robert Goldblatt and Steven Thomason characterized the modally definable first-order classes of frames.
Johan van Benthem developed correspondence theory as a subject in his 1976 dissertation "Modal correspondence theory".

### Watch out

A frame condition is not a condition on one model.
In the model with one world $a$, no successors, and $p$ true at $a$, the formula $\square p \to p$ is true at $a$.
The frame is not reflexive, and the valuation that makes $p$ false at $a$ refutes the formula.

### Try it

Find the frame condition of $\lozenge \square p \to p$.
Answer: symmetry.
Substituting $\neg p$ for $p$ in $p \to \square \lozenge p$ and contraposing gives $\lozenge \square \neg p \to \neg p$, and a frame validates a formula exactly when it validates all its substitution instances.

Find the frame condition of $\square p \to \lozenge p$.
Answer: seriality, since a world without successors makes $\square p$ true and $\lozenge p$ false.

## Explanations

### L1 human

A modal axiom is a rule about statements such as "it is necessary that".
A frame is a picture of points with arrows between them.
Correspondence theory finds, for each rule, the shape of the pictures in which the rule always holds.
For example, "what is necessary is true" holds in every picture exactly when every point has an arrow to itself.
Some rules match no shape that can be described with "for all points" and "there is a point".

### L2 human

The typical use is in completeness proofs.
One shows that the canonical frame of a logic has the property that its axioms correspond to.
For $\mathsf{K4}$, if $\square \varphi \in \Gamma$ and $\Gamma R \Delta R \Theta$ in the canonical frame, then $\square \square \varphi \in \Gamma$, so $\square \varphi \in \Delta$ and $\varphi \in \Theta$.
So the canonical frame is transitive, and $\mathsf{K4}$ is complete for transitive frames.
Watch out: the refuting valuations in correspondence arguments are chosen for the frame, so the arguments say nothing about one fixed model.

### L3 human

The standard translation places modal logic inside monadic second-order logic on frames and inside first-order logic on models.
Correspondence theory studies the gap between the two: when a $\Pi^1_1$ condition collapses to a first-order one.
Sahlqvist's theorem and the algorithms SQEMA and ALBA give syntactic sufficient conditions, and Chagrova showed that first-order definability of a modal formula is undecidable.
Algebraically, correspondence is linked to canonicity through duality, and Fine's theorem says that a logic complete for a first-order class of frames is canonical.
The same questions arise for intuitionistic logic and for extended modal languages, where nominals make many more conditions definable.
