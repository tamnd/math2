---
tag: EZ011FT3GT
kind: concept
name: Lattice of normal modal logics
msc: ["03B45", "06B20"]
topics: [SPQVNPZDTB]
audience: research
uses: [C3RZY20ETK, NGHWZ9Y7ZV, D7A0ZGZT5S, DE0GD8BM4M, G989VP2NGP, 5083DHSK82]
sources:
  - url: https://en.wikipedia.org/wiki/Normal_modal_logic
    locator: Common normal modal logics
  - url: https://en.wikipedia.org/wiki/Kripke_semantics
    locator: Correspondence and completeness
  - url: https://builds.openlogicproject.org/
    locator: Modal Logic
---

## Summary

The normal modal logics, ordered by inclusion, form one large lattice, and many questions about modal logic become questions about where a logic sits in it.
At the bottom is $\mathsf{K}$, at the top is the inconsistent logic, and just below the top there are exactly two logics, those of a reflexive point and of an irreflexive point.

A *normal modal logic* is a set $L$ of formulas of the basic [[modal language|C3RZY20ETK]] that contains all tautologies and the axiom $\square(p \to q) \to (\square p \to \square q)$, and that is closed under modus ponens, [[necessitation|G989VP2NGP]] and [[uniform substitution|DE0GD8BM4M]].
For a normal logic $L$, the set $\mathrm{NExt}(L)$ of normal logics that contain $L$, ordered by inclusion, is a [[complete lattice|D7A0ZGZT5S]].
The meet of a family is its intersection, and the join $L_1 \oplus L_2$ is the smallest normal logic that contains both.
The *lattice of normal modal logics* is $\mathrm{NExt}(\mathsf{K})$.

## Motivation

Each logic studied on its own, such as $\mathsf{S4}$ or the provability logic $\mathsf{GL}$, is one point of $\mathrm{NExt}(\mathsf{K})$.
Questions about all logics at once need the global view: how many logics there are, which are maximal, and which properties hold on whole intervals.
One theorem about an interval, such as Bull's theorem on the extensions of $\mathsf{S4.3}$, replaces infinitely many separate completeness proofs.

The lattice is dually isomorphic to the lattice of varieties of [[modal algebras|3H85NSFWHK]], so lattice theory and universal algebra apply.
The same picture returns in the [[Blok-Esakia theorem|BB9TA5Q9PN]], which matches one interval of this lattice with the lattice of superintuitionistic logics.

## Notation

$L \oplus \Gamma$ is the smallest normal logic that contains $L$ and the set $\Gamma$.
$\mathrm{Log}(\mathsf{C})$ is the set of formulas valid on every frame of a class $\mathsf{C}$, and $\mathrm{Log}(\mathfrak{F})$ is the logic of one frame.
We write $\circ$ for the reflexive one-point frame and $\bullet$ for the irreflexive one-point frame.
Some texts write $\mathcal{E}L$ or $\Lambda(L)$ for $\mathrm{NExt}(L)$.

## Remarks

### Two logics at the top

Compare the two one-point frames.
On $\circ$ the box means "true here", so $\square p \leftrightarrow p$ is valid, and $\square \bot$ fails.
On $\bullet$ there are no successors, so every boxed formula is true, $\square \bot$ is valid, and $\square p \to p$ fails with $p$ false.
So $\square \bot \in \mathrm{Log}(\bullet) \setminus \mathrm{Log}(\circ)$ and $\square p \to p \in \mathrm{Log}(\circ) \setminus \mathrm{Log}(\bullet)$, and neither logic contains the other.
[[Makinson's theorem|8AF7AN5HE1]] says that every consistent normal logic lies below one of them, so these two are the only coatoms of the lattice.

### A first splitting

The second picture of the lattice is a cut.
Every normal logic either lies below $\mathrm{Log}(\bullet)$ or contains $\mathsf{KD} = \mathsf{K} \oplus \lozenge \top$, and never both; see [[the irreflexive point splits the lattice|Q6P4T6YH9Z]].
For example, $\mathsf{S4}$ proves $\square \bot \to \bot$, an instance of T, which is $\lozenge \top$, so $\mathsf{S4}$ is on the upper side.
$\mathsf{GL}$ is valid on $\bullet$, so it is on the lower side.
A pair $\langle L_1, L_2 \rangle$ with this property *splits* $\mathrm{NExt}(L)$.
Blok proved that the logic of a finite rooted frame splits $\mathrm{NExt}(\mathsf{K})$ exactly when the frame has no cycles.
In $\mathrm{NExt}(\mathsf{K4})$ every finite rooted transitive frame gives a splitting, whose upper logic is axiomatized by the [[Jankov-Fine formula|W0CYVZ48CK]] of the frame.

### Chains inside the lattice

Familiar logics line up as $\mathsf{K} \subset \mathsf{K4} \subset \mathsf{S4} \subset \mathsf{S4.2} \subset \mathsf{S4.3} \subset \mathsf{S5}$.
The interval above $\mathsf{S5}$ is a chain.
Its consistent members are $\mathsf{S5}$, which is the logic of all finite clusters, and the logics of the clusters with $n$ points, one for each $n \geq 1$.

### What is not in the lattice

The formulas true in one Kripke model do not form a normal logic, since they are not closed under substitution; see [[global truth in a model is not a logic|WYJ1D6HPJ5]].
The Lewis systems $\mathsf{S2}$ and $\mathsf{S3}$ are not normal, because they are not closed under necessitation, so they lie outside $\mathrm{NExt}(\mathsf{K})$.

### The rules you can use

$\mathrm{NExt}(\mathsf{K})$ is distributive, because it is dually isomorphic to the lattice of subvarieties of a congruence distributive variety.
It has $2^{\aleph_0}$ elements: there are at most that many sets of formulas, and already $\mathrm{NExt}(\mathsf{S4})$ has that many.
Bull proved that every normal extension of $\mathsf{S4.3}$ has the finite model property, and Fine proved that each is finitely axiomatizable, so each is decidable.
Fine also proved that every normal extension of $\mathsf{K4}$ of finite width is Kripke complete.
Many logics in the lattice are [[Kripke incomplete|W67YJQTT50]], so different logics can have the same Kripke frames.

### Watch out

The join $L_1 \oplus L_2$ is not the union.
The union of $\mathsf{KT} = \mathsf{K} \oplus (\square p \to p)$ and $\mathsf{K4}$ contains both axioms, but not the theorem $\square p \to (p \wedge \square \square p)$ of $\mathsf{S4}$.
That formula fails on the irreflexive point, a $\mathsf{K4}$ frame, and on a reflexive two-step chain, a $\mathsf{KT}$ frame, so it lies in neither part of the union.
A second slip is to think the lattice countable: there are only countably many finitely axiomatizable logics, but $2^{\aleph_0}$ logics in all.

### History

McKinsey, Tarski and others studied single modal systems in the 1940s, and Kripke semantics made frame classes available around 1960.
Bull proved the finite model property of the extensions of $\mathsf{S4.3}$ in 1966.
David Makinson described the two coatoms in 1971.
Kit Fine proved the finite axiomatizability of the extensions of $\mathsf{S4.3}$ in 1971, and studied the extensions of $\mathsf{K4}$ in 1974.
Blok developed the theory of splittings and of the degree of incompleteness, and Marcus Kracht extended the theory of splittings.

### Try it

First, is $\mathsf{K} \oplus \square \bot$ below $\mathrm{Log}(\circ)$?
No: $\square \bot$ fails on $\circ$, so the logic lies below $\mathrm{Log}(\bullet)$, and in fact it equals $\mathrm{Log}(\bullet)$.

Second, on which side of the splitting by $\bullet$ is $\mathsf{K4}$?
On the lower side: $\bullet$ is transitive, so $\mathsf{K4} \subseteq \mathrm{Log}(\bullet)$, and $\mathsf{K4}$ does not prove $\lozenge \top$.

## Explanations

### L1 human

A modal logic is a list of accepted laws about necessity and possibility.
One logic is stronger than another when it accepts more laws.
All the logics, ordered by strength, form a map with the weakest logic $\mathsf{K}$ at the bottom and the logic that accepts everything at the top.
Just below the top there are only two logics: the logic of one point that sees itself, and the logic of one point that sees nothing.

### L2 human

We place $\mathsf{S4}$ in the lattice.
By definition $\mathsf{K4} = \mathsf{K} \oplus (\square p \to \square \square p)$ and $\mathsf{S4} = \mathsf{K4} \oplus (\square p \to p)$, which gives a chain:
$$\mathsf{K} \subseteq \mathsf{K4} \subseteq \mathsf{S4}$$
The reflexive point validates $\square p \to p$ and $\square p \to \square \square p$, so $\mathsf{S4} \subseteq \mathrm{Log}(\circ)$.
The irreflexive point refutes $\square p \to p$ with $p$ false, so $\mathsf{S4} \not\subseteq \mathrm{Log}(\bullet)$.
By the splitting, $\mathsf{S4}$ must then contain $\lozenge \top$.
Check: the instance $\square \bot \to \bot$ of T is equivalent to $\lozenge \top$.
This is the typical use of the lattice: one test on a finite frame decides a whole family of questions.

### L3 human

By Jónsson-Tarski duality and [[Birkhoff's theorem|5083DHSK82]], $\mathrm{NExt}(\mathsf{K})$ is dually isomorphic to the lattice of subvarieties of the variety of modal algebras.
Splittings correspond to splitting algebras: finite subdirectly irreducible algebras $\mathfrak{A}$ such that the varieties omitting $\mathfrak{A}$ have a largest element.
The structure of the lattice is far from understood; for finitely axiomatized logics, Kripke completeness and the finite model property are undecidable, by results of Chagrov.
Through the [[Blok-Esakia theorem|BB9TA5Q9PN]], the interval $\mathrm{NExt}(\mathsf{Grz})$ is isomorphic to the lattice of superintuitionistic logics.
