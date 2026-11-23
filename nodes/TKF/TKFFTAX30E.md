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

Bisimilar worlds satisfy exactly the same modal formulas, so no modal formula can tell them apart.

The basic modal formulas are built from propositional variables and $\bot$ with $\neg$, $\wedge$ and $\lozenge$, and $\square \varphi$ abbreviates $\neg \lozenge \neg \varphi$.
Let $\mathfrak{M} = (W, R, V)$ and $\mathfrak{M}' = (W', R', V')$ be Kripke models, with truth $\mathfrak{M}, w \models \varphi$ as in [[Kripke semantics|NGHWZ9Y7ZV]].
Let $Z$ be a [[bisimulation|7T740SFHHV]] between $\mathfrak{M}$ and $\mathfrak{M}'$, and let $w Z w'$.
Then, for every basic modal formula $\varphi$,
$$\mathfrak{M}, w \models \varphi \iff \mathfrak{M}', w' \models \varphi.$$
In particular, the following hold for every formula $\varphi$.

1. If $\mathfrak{N}$ is a generated submodel of $\mathfrak{M}$ and $u$ is a world of $\mathfrak{N}$, then $\mathfrak{N}, u \models \varphi$ if and only if $\mathfrak{M}, u \models \varphi$.
2. If $f \colon \mathfrak{M} \to \mathfrak{M}'$ is a bounded morphism, then $\mathfrak{M}, w \models \varphi$ if and only if $\mathfrak{M}', f(w) \models \varphi$.
3. If $w$ is a world of $\mathfrak{M}_i$, then $\mathfrak{M}_i, w \models \varphi$ if and only if $\biguplus_j \mathfrak{M}_j, w \models \varphi$.

## Remarks

### Why each clause of a bisimulation is needed

Drop zig, and the theorem fails.
Let $\mathfrak{M}$ have $w R v$ only, and let $\mathfrak{N}$ be the single world $w$ with no successor.
The relation $\{(w, w)\}$ from $\mathfrak{N}$ to $\mathfrak{M}$ has the atom and zag clauses, but $\lozenge \top$ is false at $w$ in $\mathfrak{N}$ and true in $\mathfrak{M}$.
Read in the other direction, the same pair shows that zag is needed.

Drop the atom clause, and the theorem fails for the plainest reason.
Two one-world models without arrows, with $p$ true in one and false in the other, are related by a relation with zig and zag, and they differ on $p$.

The language matters too.
The universal modality, the counting modality "at least two successors" and the nominals of [[hybrid logic|NVPQ9W9DED]] are not invariant.
For example, the bisimilar worlds $a$ and $x$ of the L2 explanation below differ on the number of successors.

### What it gives you

The theorem is used mostly in the negative direction: a property that differs on two bisimilar worlds is not modally definable.
For frames it gives three closure rules.
A formula valid on a frame stays valid on its generated subframes and its bounded morphic images, and a formula valid on every $\mathfrak{F}_i$ is valid on $\biguplus_i \mathfrak{F}_i$.
These are three of the four conditions of the [[Goldblatt-Thomason theorem|GX5E3GNRCS]].

Here is a worked use.
The chain $(\mathbb{N}, S)$ with $S(n) = n+1$ is irreflexive, and it maps onto a single reflexive point by a bounded morphism; see [[the successor chain example|T3YJ84YDV4]].
So every formula valid on all irreflexive frames is valid on the reflexive point, and no formula defines the class of irreflexive frames.
A second use is the tree model property: every world is bisimilar to the root of its tree unraveling, so every satisfiable formula is satisfiable at the root of a tree.

### The converse

The converse is false in general: some pairs of worlds satisfy the same modal formulas and are still not bisimilar.
The [[Hennessy-Milner theorem|DBDNYXA7ME]] gives such a pair, built from paths of every finite length and one infinite path.
The same theorem shows that the converse does hold on image-finite models and on modally saturated models.

### Generalizations

The same proof works with any set of modalities, one relation for each, and so for labeled transition systems.
Formulas of the [[modal mu-calculus|MZ0M2KR9S0]] and of [[propositional dynamic logic|VJ78A0Q22R]] are invariant too.
Infinitary modal formulas, with conjunctions over arbitrary sets, are invariant, and for them the converse holds on all models.
Inside first-order logic, invariance characterizes the modal formulas exactly, by the [[van Benthem characterization theorem|Y89MGMWE4H]].

### Watch out

The theorem is about truth in models, with a fixed valuation.
Statements about frames quantify over all valuations, so they need the frame versions above, not the model version.
For example, a reflexive point and the two-cycle are bisimilar as models with no atoms true, yet the frame formula $p \to \lozenge p$ is valid on the first and not on the second.

## History

Johan van Benthem proved the invariance theorem for his p-relations in his 1976 dissertation.
Generated submodels and bounded morphisms, then called p-morphisms, were already in use in the completeness theory of modal logic.

## Explanations

### L1 human

A modal formula only talks about the facts at a world and about the worlds you can step to.
A bisimulation pairs worlds that have the same facts and matching steps.
So a modal formula cannot tell paired worlds apart.
For example, "after every step, another step is possible" is true both in a room with a door into itself and in a pair of rooms with doors into each other.

### L2 human

Let us show that "$w$ has at least two successors" is not definable by a modal formula.
Let $\mathfrak{M}$ have $a R b$ and $a R c$, and let $\mathfrak{M}'$ have $x R' y$, with every variable false everywhere.
The relation $\{(a, x), (b, y), (c, y)\}$ is a bisimulation: atoms agree, each move from $a$ goes to a world paired with $y$, and the move from $x$ is answered by $a R b$.
Suppose some formula $\varphi$ were true exactly at the worlds with two or more successors, in every model.
Then $\varphi$ would be true at $a$ and false at $x$.
The theorem says that $a$ and $x$ agree on $\varphi$, so no such formula exists.
This is the typical shape of an undefinability proof: find two bisimilar worlds, one with the property and one without.

### L3 human

Bisimulation invariance says that modal formulas describe behavior in the coalgebraic sense, not the shape of a graph.
It is the modal counterpart of the invariance of first-order formulas under isomorphism, and of $k$-variable formulas under pebble games.
The converse inside first-order logic is the [[van Benthem characterization theorem|Y89MGMWE4H]], and the Janin-Walukiewicz theorem gives the converse for the modal mu-calculus inside [[monadic second-order logic|3WHQFSHR58]].
Together these results explain the tree model property of modal logics, and why extended modal languages are classified by the bisimulations they respect.
