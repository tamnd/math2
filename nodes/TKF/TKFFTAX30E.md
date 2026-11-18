---
tag: TKFFTAX30E
kind: statement
role: theorem
name: Bisimulation invariance of modal formulas
msc: ["03B45"]
topics: [SPQVNPZDTB]
audience: grad
uses: [7T740SFHHV, NGHWZ9Y7ZV]
about: [X27BR4YP2Y, C3RZY20ETK]
proofs: [2TQ99Y9TEJ]
sources:
  - url: https://en.wikipedia.org/wiki/Bisimulation
    locator: Bisimulation and modal logic
  - url: https://en.wikipedia.org/wiki/Kripke_semantics
    locator: Model constructions
  - url: https://builds.openlogicproject.org/
    locator: Modal Logic
---

## Statement

The basic modal formulas are built from propositional variables and $\bot$ with $\neg$, $\wedge$ and $\lozenge$, and $\square \varphi$ abbreviates $\neg \lozenge \neg \varphi$.
Let $\mathfrak{M} = (W, R, V)$ and $\mathfrak{M}' = (W', R', V')$ be Kripke models, with truth $\mathfrak{M}, w \models \varphi$ as in [[Kripke semantics|NGHWZ9Y7ZV]].
Let $Z$ be a [[bisimulation|7T740SFHHV]] between $\mathfrak{M}$ and $\mathfrak{M}'$, and let $w Z w'$.
Then for every basic modal formula $\varphi$,
$$\mathfrak{M}, w \models \varphi \iff \mathfrak{M}', w' \models \varphi.$$
In particular, the following hold for every formula $\varphi$.

1. If $\mathfrak{N}$ is a generated submodel of $\mathfrak{M}$ and $u$ is a world of $\mathfrak{N}$, then $\mathfrak{N}, u \models \varphi$ if and only if $\mathfrak{M}, u \models \varphi$.
2. If $f \colon \mathfrak{M} \to \mathfrak{M}'$ is a bounded morphism, then $\mathfrak{M}, w \models \varphi$ if and only if $\mathfrak{M}', f(w) \models \varphi$.
3. If $w$ is a world of $\mathfrak{M}_i$, then $\mathfrak{M}_i, w \models \varphi$ if and only if $\biguplus_j \mathfrak{M}_j, w \models \varphi$.

The proof is in [[the proof of bisimulation invariance|2TQ99Y9TEJ]].

## Remarks

### Why each hypothesis is needed

1. The zig clause is needed. Let $\mathfrak{M}$ have $w R v$ only, and let $\mathfrak{N}$ be one world $w$ with no successor. The relation $\set{(w, w)}$ has the atom and zag clauses, but $\lozenge \top$ is true at $w$ in $\mathfrak{M}$ and false in $\mathfrak{N}$.
2. The zag clause is needed, by the same pair of models in the other order.
3. The atom clause is needed. Two one-world models without successors, with $p$ true in one and false in the other, are related by a relation with zig and zag, and they differ on $p$.
4. The language matters. The universal modality, the counting modality "at least two successors", and nominals are not invariant. For example, the bisimilar worlds $a$ and $x$ of the L2 explanation below differ on the number of successors.

### Consequences

1. Irreflexivity is not modally definable on frames. The chain $(\N, S)$ of [[the successor chain example|T3YJ84YDV4]] is irreflexive, and it has a bounded morphism onto a reflexive point. By Consequence 2, a formula valid on all irreflexive frames is valid on the reflexive point, so it does not define irreflexivity.
2. Validity on frames is preserved by the three constructions: a formula valid on $\mathfrak{F}$ is valid on its generated subframes and on its bounded morphic images, and a formula valid on every $\mathfrak{F}_i$ is valid on $\biguplus \mathfrak{F}_i$. These closure conditions appear in the [[Goldblatt-Thomason theorem|GX5E3GNRCS]].
3. Every satisfiable formula is satisfiable at the root of a tree, by passing to the tree unravelling.
4. Trace-equivalent processes can be told apart by modal formulas; see [[two trace-equivalent models that are not bisimilar|KAMG2T6622]].

### Converse

The converse is false in general: there are worlds that satisfy the same modal formulas and are not bisimilar.
It is true on image-finite models, by the [[Hennessy-Milner theorem|DBDNYXA7ME]], and on modally saturated models.

### Generalizations

1. The same proof works for every finite or infinite set of modalities, with one relation for each modality, and so for labelled transition systems.
2. The formulas of the modal mu-calculus and of propositional dynamic logic are also invariant under bisimulation.
3. Infinitary modal formulas with arbitrary conjunctions are invariant, and for them the converse holds on all models.
4. By the [[van Benthem characterization theorem|Y89MGMWE4H]], invariance under bisimulation characterizes the modal formulas among the first-order formulas.

## History

Johan van Benthem proved the invariance theorem for his p-relations in his 1976 dissertation.
The special cases of generated submodels and bounded morphisms were in use earlier in the completeness theory of modal logic, under the names generated submodels and p-morphisms.

## Explanations

### L1 human

A modal formula only talks about the facts at a world and about the worlds one can step to.
A bisimulation pairs worlds that have the same facts and matching steps.
So a modal formula cannot tell paired worlds apart.
For example, "after every step, a step is possible" is true at a room with a door into itself and at a pair of rooms with doors into each other.

### L2 human

We use the theorem to show that "$w$ has at least two successors" is not definable by a modal formula.

1. Let $\mathfrak{M}$ have $a R b$, $a R c$, and let $\mathfrak{M}'$ have $x R' y$. All variables are false everywhere.
2. The relation $\set{(a, x), (b, y), (c, y)}$ is a bisimulation: the atoms agree, and each move from $a$ or $x$ is answered by a move to a paired world.
3. Assume that a formula $\varphi$ is true exactly at the worlds with at least two successors, in every model.
4. Then $\varphi$ is true at $a$ and false at $x$.
5. By the theorem, $\varphi$ has the same truth value at $a$ and $x$. This is a contradiction.

The typical use is in this negative form: a property that differs on bisimilar worlds is not modally definable.
A trap: the theorem concerns truth in models; definability of frame classes uses all valuations, and needs the frame versions of Consequence 2.

### L3 human

Bisimulation invariance says that modal formulas are the logic of a coalgebraic notion of behaviour.
It is the modal analogue of the invariance of first-order formulas under isomorphism, and of the invariance of formulas with $n$ variables under the corresponding pebble games.
The [[van Benthem characterization theorem|Y89MGMWE4H]] gives the converse inside first-order logic, and the Janin-Walukiewicz theorem gives the converse for the modal mu-calculus inside monadic second-order logic.
These invariance results explain why modal logics have the tree model property and good decidability, and why extended modal languages are classified by the bisimulations they respect.
