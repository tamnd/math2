---
tag: X27BR4YP2Y
kind: concept
name: Bisimulation
msc: ["03B45", "68Q85", "68Q55"]
topics: [SPQVNPZDTB]
audience: grad
uses: [05AVARPXA2, NGHWZ9Y7ZV, C3RZY20ETK]
sources:
  - url: https://en.wikipedia.org/wiki/Bisimulation
    locator: Bisimulation and modal logic
  - url: https://en.wikipedia.org/wiki/Bisimulation
    locator: Ehrenfeucht–Fraïssé game definition
  - url: https://builds.openlogicproject.org/
    locator: Modal Logic
same_as:
  wikidata: Q866364
  wikipedia: Bisimulation
---

## Summary

A Kripke model is a triple $\mathfrak{M} = (W, R, V)$ of a nonempty set $W$ of worlds, a relation $R \subseteq W \times W$ and a valuation $V$ that sends each propositional variable to a subset of $W$; see [[Kripke semantics|NGHWZ9Y7ZV]].
A bisimulation between Kripke models $\mathfrak{M} = (W, R, V)$ and $\mathfrak{M}' = (W', R', V')$ is a nonempty [[binary relation|05AVARPXA2]] $Z \subseteq W \times W'$ with three properties for every pair $w Z w'$.
The atom clause: $w \in V(p)$ if and only if $w' \in V'(p)$, for every variable $p$.
The zig clause: if $w R v$, then $w' R' v'$ and $v Z v'$ for some $v' \in W'$.
The zag clause: if $w' R' v'$, then $w R v$ and $v Z v'$ for some $v \in W$.
Two worlds $w$ and $w'$ are bisimilar, written $w \mathrel{\underline{\leftrightarrow}} w'$, when some bisimulation relates them.
The formal definition, with the version for labelled transition systems, is in [[the definition of bisimulation|7T740SFHHV]].
Bisimulation is the notion of sameness for which [[modal logic|C3RZY20ETK]] is designed: modal formulas cannot distinguish bisimilar worlds.

## Motivation

Two Kripke models can be different as graphs and still look the same from inside.
An observer at a world sees only the atoms that are true there and the worlds one step away.
A modal formula describes what such an observer can find in finitely many steps.
So the right notion of sameness compares the local views and the possible moves, not the sets of worlds.
The same problem arose in the theory of concurrent processes, where a process is known only through the actions it can perform.
Bisimulation answers both problems with one definition: every move on one side has a matching move on the other side, and the match persists.

## Notation

We write $\mathfrak{M}, w \mathrel{\underline{\leftrightarrow}} \mathfrak{M}', w'$, or $w \mathrel{\underline{\leftrightarrow}} w'$ when the models are fixed.
In process theory the usual symbol is $p \sim q$.
The zig clause is also called the forth clause, and the zag clause the back clause.
Older modal texts call bisimulations zigzag relations or p-relations.
On frames without valuations, the atom clause is dropped.

## Remarks

### Examples

1. A world with a loop and a cycle of two worlds, with the same atoms everywhere, are bisimilar; see [[a loop and a two-cycle are bisimilar|~6615a7e8]].
2. The graph of a bounded morphism is a bisimulation; see [[the successor chain maps onto a reflexive point|~0052c5a7]].
3. If $\mathfrak{N}$ is a generated submodel of $\mathfrak{M}$, then the identity relation on the worlds of $\mathfrak{N}$ is a bisimulation between $\mathfrak{N}$ and $\mathfrak{M}$. The zag clause holds because $\mathfrak{N}$ is closed under $R$.
4. Each summand of a disjoint union is bisimilar to its copy in the union, by the identity map on the summand.
5. A world $w$ is bisimilar to the root of the tree unravelling of the model at $w$. The worlds of the unravelling are the finite paths from $w$, and the map that sends a path to its last world is a bounded morphism.

### Non-examples

1. Two models can have the same paths of atoms and still fail to be bisimilar; see [[two trace-equivalent models that are not bisimilar|~03467eec]]. The zag clause fails after one step.
2. The inclusion of a submodel that is not generated is not a bisimulation in general. If $w R v$ and $v$ is left out, the zig clause fails at $w$, and $\lozenge \top$ is true at $w$ only in the larger model.
3. A world where $p$ is true and a world where $p$ is false are never bisimilar, since the atom clause fails.

### Basic properties

1. The union of any family of bisimulations between $\mathfrak{M}$ and $\mathfrak{M}'$ is a bisimulation. So bisimilarity is the largest bisimulation, when it is nonempty.
2. The converse of a bisimulation is a bisimulation, and the composition of two bisimulations is a bisimulation, when it is nonempty. So bisimilarity is an equivalence relation on the worlds of one model.
3. Bisimilar worlds satisfy the same modal formulas; see [[bisimulation invariance of modal formulas|~88334673]].
4. On image-finite models the converse holds; see [[the Hennessy-Milner theorem|~613466ad]].
5. A first-order formula in one free variable is equivalent to the standard translation of a modal formula exactly when it is invariant under bisimulation; see [[the van Benthem characterization theorem|~bf053ff5]].

### History

Johan van Benthem used bisimulations, under the name p-relations, in his 1976 dissertation on modal correspondence theory.
David Park introduced bisimulation for automata and concurrent processes in 1981.
Robin Milner made bisimilarity the central equivalence of his calculus of communicating systems.

### Common errors

1. Checking only the zig clause. A relation with zig and the atom clause is a simulation. Simulations preserve the formulas built from atoms with $\wedge$, $\vee$ and $\lozenge$, but not formulas with $\square$ or negation.
2. Requiring a bisimulation to be a function or a bijection. Bisimilar models can have very different sizes, as the loop and the two-cycle show.
3. Confusing bisimilarity with equality of traces. Trace equivalence is coarser, as Non-example 1 shows.

## Explanations

### L1 human

Imagine two maps of rooms joined by one-way doors.
Each room has some lights on.
The maps are bisimilar from two starting rooms when a guide on one map can always copy a walker on the other map.
The copied room must have the same lights, and the copying must go on forever.
A single room with a door to itself copies a pair of rooms with doors in a circle: in both maps one can always walk on, and nothing ever changes.

### L2 human

We check that a relation is a bisimulation.

1. Let $\mathfrak{M}$ have worlds $a$, $b$, $c$ with $a R b$ and $a R c$, and with $p$ true at $b$ and $c$ only.
2. Let $\mathfrak{M}'$ have worlds $x$, $y$ with $x R' y$ only, and with $p$ true at $y$ only.
3. Let $Z = \set{(a, x), (b, y), (c, y)}$.
4. Atom clause: $p$ is false at $a$ and $x$, and true at $b$, $c$ and $y$.
5. Zig at $(a, x)$: the moves $a R b$ and $a R c$ are answered by $x R' y$, and $b Z y$, $c Z y$.
6. Zag at $(a, x)$: the move $x R' y$ is answered by $a R b$, and $b Z y$.
7. At $(b, y)$ and $(c, y)$, no world has a successor, so zig and zag hold vacuously.

So $a$ and $x$ are bisimilar, although $\mathfrak{M}$ has three worlds and $\mathfrak{M}'$ has two.
The typical use is negative: to show that a property is not modally definable, find bisimilar worlds that differ on the property.
Here $a$ has two successors and $x$ has one, so "$w$ has at least two successors" is not modally definable.
A trap: the relation must contain the starting pair and be closed under the moves, so one must check all pairs that the moves reach.

### L3 human

A Kripke model is a coalgebra for the functor $X \mapsto \mathcal{P}(\mathrm{Prop}) \times \mathcal{P}(X)$, and bisimulations are the relations that carry a coalgebra structure making both projections coalgebra morphisms.
In this view bounded morphisms are the coalgebra morphisms, and bisimilarity is the kernel of the map to a final coalgebra, when one exists.
Bisimilarity is a greatest fixed point on the [[complete lattice|D7A0ZGZT5S]] of relations, which is why proofs about it use coinduction.
It is the modal analogue of the back-and-forth systems of first-order model theory and of the [[Ehrenfeucht-Fraïssé game|2RE7YAZK8R]].
The van Benthem and Rosen theorems make this precise: the modal fragment of first-order logic is the fragment invariant under bisimulation.
Extended modal languages change the notion: graded modalities need counting bisimulations, and nominals of [[hybrid logic|~be12fd35]] need bisimulations that respect named worlds.
