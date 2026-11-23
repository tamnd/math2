---
tag: TVE4F04KME
kind: concept
name: Canonical model
msc: ["03B45"]
topics: [SKY7AQFG1V]
audience: grad
uses: [JS8W7PA6JK, NGHWZ9Y7ZV, VM8TQ70CVJ, SC0BSJ3GT6]
sources:
  - url: https://en.wikipedia.org/wiki/Kripke_semantics
    locator: Canonical models
  - url: https://builds.openlogicproject.org/
    locator: Boxes and Diamonds
---

## Summary

The canonical model of a modal logic is a Kripke model built from syntax alone: its worlds are complete, consistent descriptions, and one description sees another when the second contains everything that the first calls necessary.
It is the standard tool for proving that a logic is complete for a class of frames.

Here is the idea on one world.
Let $\Gamma$ be a maximal $\mathsf{K}$-[[consistent|VM8TQ70CVJ]] set that contains $\square p$ and $\lozenge q$.
A world $\Delta$ that $\Gamma$ sees must contain $p$, because $\square p \in \Gamma$.
A set $\Delta'$ with $\neg p \in \Delta'$ is therefore not a successor of $\Gamma$.
And since $\lozenge q \in \Gamma$, some successor must contain $q$: the set $\{ p, q \} \cup \{ \varphi : \square\varphi \in \Gamma \}$ is consistent, and any maximal consistent $\Delta$ above it is such a successor.

In general, let $\Lambda$ be a consistent [[normal modal logic|JS8W7PA6JK]].
Its canonical model $\mathfrak{M}^\Lambda = (W^\Lambda, R^\Lambda, V^\Lambda)$ is given by these three clauses:
$$W^\Lambda = \{ \Gamma : \Gamma \text{ maximal } \Lambda\text{-consistent} \}, \quad \Gamma R^\Lambda \Delta \iff \{ \varphi : \square\varphi \in \Gamma \} \subseteq \Delta, \quad V^\Lambda(p) = \{ \Gamma : p \in \Gamma \}.$$
The [[truth lemma|NM4CB7QAYT]] says that a formula is true at $\Gamma$ exactly when it belongs to $\Gamma$.
The pair $(W^\Lambda, R^\Lambda)$ is the canonical frame, and $\Lambda$ is called canonical when its canonical frame validates $\Lambda$.

## Motivation

To prove completeness for [[Kripke frames|NGHWZ9Y7ZV]], we must turn each non-theorem $\varphi$ into a model with a world where $\varphi$ fails.
Henkin's proof for first-order logic builds a structure from one maximal consistent set.
In modal logic one maximal consistent set describes only one world, and a countermodel needs many worlds at once.
So we take all maximal consistent sets together as the worlds, and we let the box formulas of each set decide which worlds it sees.

The construction is the same for every normal logic, and this is its strength.
The axioms of $\Lambda$ then show up as properties of $R^\Lambda$: axiom $\mathrm{T}$ makes it reflexive, and axiom $\mathrm{4}$ makes it transitive.
The [[completeness theorem for K to S5|FXTCKYR3AQ]] is proved in this way, and the [[finite model property|3NT8RCA6HE]] combines it with [[filtration|6ZZSHAKG5F]].

## Notation

We write $\mathfrak{F}^\Lambda = (W^\Lambda, R^\Lambda)$ for the canonical frame and $\mathfrak{M}^\Lambda$ for the canonical model, and we drop $\Lambda$ when the logic is fixed.
The set $\{ \varphi : \square\varphi \in \Gamma \}$ is often written $\square^{-1}\Gamma$, so that $\Gamma R^\Lambda \Delta$ means $\square^{-1}\Gamma \subseteq \Delta$.
An equivalent form, the box lemma of the [[truth lemma|NM4CB7QAYT]], says that $\Gamma R^\Lambda \Delta$ holds when $\lozenge\varphi \in \Gamma$ for every $\varphi \in \Delta$.
Some books write $\mathrm{MCS}_\Lambda$ for $W^\Lambda$ and call its members $\Lambda$-MCSs.

## Remarks

### How an axiom becomes a frame property

The typical computation reads one axiom inside a maximal consistent set.
Take $\Lambda = \mathsf{T}$, also written $\mathsf{KT}$, and let $\square\varphi \in \Gamma$.
The instance $\square\varphi \to \varphi$ of axiom $\mathrm{T}$ lies in $\Gamma$, and $\Gamma$ is closed under modus ponens, so $\varphi \in \Gamma$.
This gives $\square^{-1}\Gamma \subseteq \Gamma$, which says that $\Gamma R^{\mathsf{T}} \Gamma$.
So the canonical frame of $\mathsf{T}$ is reflexive.

Axiom $\mathrm{4}$ works in the same way.
If $\Gamma R \Delta R \Theta$ and $\square\varphi \in \Gamma$, then $\square\square\varphi \in \Gamma$ by axiom $\mathrm{4}$.
So $\square\varphi \in \Delta$ and then $\varphi \in \Theta$, which gives $\Gamma R \Theta$.
The [[proof of completeness|BJB500NW0P]] does the same for $\mathrm{D}$, $\mathrm{B}$ and $\mathrm{5}$, and the [[completeness theorem|FXTCKYR3AQ]] collects the results for $\mathsf{K}$, $\mathsf{T}$, $\mathsf{D}$, $\mathsf{K4}$, $\mathsf{S4}$, $\mathsf{B}$ and $\mathsf{S5}$.

### Three canonical models you can compute

For [[the verum logic|B464EAG58T]] $\mathsf{K} + \square\bot$, every world contains $\square\bot$.
A successor would then contain $\bot$, which no consistent set does, so the canonical relation is empty.

For [[the logic KD45 of belief|1CFMP9DEE6]], the three axioms $\mathrm{D}$, $\mathrm{4}$ and $\mathrm{5}$ act one at a time.
They make the canonical frame serial, transitive and Euclidean together, and completeness for that class follows with no new work.

For $\mathsf{K}$ itself, nothing needs checking: the canonical frame is a frame, and it refutes every non-theorem.
So $\mathsf{K}$ is complete for the class of all frames.

### When the method fails

The canonical frame of the provability logic $\mathsf{GL}$ is not conversely well-founded, so it does not validate $\mathsf{GL}$, as [[the GL example|E61769H6KG]] shows.
So $\mathsf{GL}$ is not canonical, even though it is complete for finite strict orders.
A [[Kripke incomplete|W67YJQTT50]] logic is the logic of no class of frames, so it cannot be canonical either.

The canonical model is also never small.
For each set $S$ of variables, the literals $p$ for $p \in S$ and $\neg p$ for $p \notin S$ form a consistent set, since a substitution of $\top$ and $\bot$ shows that no finite part is refutable.
With countably many variables this gives $2^{\aleph_0}$ different worlds.

### The lemmas you can use

Four facts carry every use of the canonical model, and the [[truth lemma page|NM4CB7QAYT]] states and proves them.
[[Lindenbaum's lemma|SC0BSJ3GT6]] extends every $\Lambda$-consistent set to a maximal one.
The existence lemma says that if $\lozenge\varphi \in \Gamma$, then some $\Delta$ with $\Gamma R^\Lambda \Delta$ contains $\varphi$.
The truth lemma says that $\mathfrak{M}^\Lambda, \Gamma \models \varphi$ exactly when $\varphi \in \Gamma$.
Together they give the canonical model theorem: every $\Lambda$-consistent set is true at some world of $\mathfrak{M}^\Lambda$.

### Watch out

The first slip is to define the relation by inclusion, $\Gamma \subseteq \Delta$.
Two different maximal consistent sets are never included in each other, so this relation is the identity, and it is wrong for $\mathsf{K}$.
The correct condition moves one box inward: $\square\varphi \in \Gamma$ gives $\varphi \in \Delta$.

The second slip is to think that completeness needs canonicity.
$\mathsf{GL}$ is complete but not canonical, and its completeness is proved with finite models instead.

The third slip is to forget maximality.
For a consistent set that is not maximal, $p \notin \Gamma$ does not give $\neg p \in \Gamma$, and the truth lemma fails.

### History

Henkin's completeness proof for first-order logic of 1949 built models from maximal consistent sets.
Lemmon and Scott developed canonical models for normal modal logics in the 1960s, and their treatment appeared in the Lemmon notes of 1977, edited by Segerberg.
Segerberg's An Essay in Classical Modal Logic of 1971 applied canonical models and filtration to many logics.

### Try it

First, show that the canonical frame of $\mathsf{D}$ is serial.
Necessitation puts $\square\top$ in every $\Gamma$, axiom $\mathrm{D}$ gives $\lozenge\top \in \Gamma$, and the existence lemma gives a successor that contains $\top$.

Second, let $\Gamma$ contain $\square(p \wedge q)$ and let $\Gamma R \Delta$.
Is $q \in \Delta$?
Yes: $p \wedge q \in \Delta$ by the definition of $R$, and a maximal consistent set that contains a conjunction contains each conjunct.

## Explanations

### L1 human

A canonical model is a model built out of descriptions.
Each world is a complete description: for every statement it says yes or no, and it never contradicts the logic.
One world sees another when everything that the first calls "necessary" is true in the second.
For example, if world $A$ says "necessarily it rains", then every world that $A$ sees says "it rains".
Then each description is true exactly at its own world, so every statement that the logic cannot prove is false somewhere.

### L2 human

We use the canonical model to show that $\mathsf{K}$ does not prove $\square p \to p$.
The set $\{ \square p, \neg p \}$ is $\mathsf{K}$-consistent, because the one-world model with no arrows and $p$ false makes both true.
Lindenbaum's lemma extends it to a maximal consistent set $\Gamma$.
By the truth lemma, $\square p$ is true and $p$ is false at $\Gamma$ in $\mathfrak{M}^{\mathsf{K}}$, so $\square p \to p$ fails there.
Notice that $\Gamma$ does not see itself: $p \in \square^{-1}\Gamma$ but $p \notin \Gamma$.
This is the typical use: a non-theorem becomes a consistent set, and the canonical model turns the set into a world.
Watch out: the canonical model of $\mathsf{S5}$ is not universal.
It is an equivalence relation with many classes, and each class is a universal model.

### L3 human

Algebraically, the canonical frame is the ultrafilter frame of the Lindenbaum algebra of $\Lambda$, and the truth lemma is the Jónsson-Tarski representation of that Boolean algebra with an operator.
A logic is canonical when its variety of modal algebras is closed under canonical extensions.
[[Sahlqvist's theorem|S4SSDMETJM]] gives a large syntactic class of canonical logics, and [[general and descriptive frames|6W9MEGN982]] explain what the canonical frame forgets.
Restricted to a finite set of formulas, the same construction gives a finite model, which links canonical models to [[filtration|6ZZSHAKG5F]] and to the [[completeness of GL|1DMFNR7FZT]] by finite models.
