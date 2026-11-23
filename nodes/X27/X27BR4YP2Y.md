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

A bisimulation is a way of matching the worlds of two Kripke models so that each matched pair looks the same from inside, now and after every move.
It is the notion of sameness that [[modal logic|C3RZY20ETK]] can see: modal formulas never tell bisimilar worlds apart.

Here is the smallest interesting case.
Let $\mathfrak{M}$ have worlds $a, b, c$ with $a R b$ and $a R c$, and let $\mathfrak{M}'$ have worlds $x, y$ with $x R' y$.
Make $p$ true at $b$, $c$ and $y$ only.
The two models are not isomorphic, since one has three worlds and the other two, but the relation $Z = \{(a, x), (b, y), (c, y)\}$ matches them perfectly.

In general, let $\mathfrak{M} = (W, R, V)$ and $\mathfrak{M}' = (W', R', V')$ be [[Kripke models|NGHWZ9Y7ZV]].
A bisimulation is a nonempty [[relation|05AVARPXA2]] $Z \subseteq W \times W'$ such that, whenever $w Z w'$:

1. (atom) $w \in V(p)$ if and only if $w' \in V'(p)$, for every variable $p$;
2. (zig) if $w R v$, then $w' R' v'$ and $v Z v'$ for some $v' \in W'$;
3. (zag) if $w' R' v'$, then $w R v$ and $v Z v'$ for some $v \in W$.

Worlds $w$ and $w'$ are bisimilar when some bisimulation contains the pair $(w, w')$.
The [[formal definition|7T740SFHHV]] adds the version for transition systems with labeled actions.

## Motivation

A modal formula is evaluated by an observer who stands at one world.
The observer sees which atoms are true there, and can step to a successor and look again, finitely often.
So two worlds that offer the same atoms and the same possible moves, forever, should satisfy the same formulas, even when the models are different graphs.
Bisimulation turns this intuition into a definition, and the [[invariance theorem|TKFFTAX30E]] proves that the intuition is right.

The same idea arose in computer science, where a process is known only through the actions it can perform.
Two programs are interchangeable when every step of one can be matched by a step of the other, and the match persists.
In modal model theory, bisimulation is the tool for proving that a property is not modally definable, and it returns in the [[Hennessy-Milner theorem|DBDNYXA7ME]], the [[van Benthem characterization theorem|Y89MGMWE4H]] and the [[Goldblatt-Thomason theorem|GX5E3GNRCS]].

## Notation

Modal logic books write $w \mathrel{\underline{\leftrightarrow}} w'$, or $\mathfrak{M}, w \mathrel{\underline{\leftrightarrow}} \mathfrak{M}', w'$ when the models must be named.
Process theory writes $p \sim q$.
The zig clause is also called the forth clause, and the zag clause the back clause.
Older modal texts say p-relation or zigzag relation.
For frames without valuations the atom clause is dropped.

## Remarks

### Checking the first example

Take the models $\mathfrak{M}$ and $\mathfrak{M}'$ of the Summary and the relation $Z = \{(a, x), (b, y), (c, y)\}$.
We check the three clauses at each of the three pairs.

1. Atoms: $p$ is false at $a$ and at $x$, and true at $b$, $c$ and $y$.
   So every pair agrees on $p$.
2. At $(a, x)$, zig: the move $a R b$ is answered by $x R' y$ with $b Z y$, and the move $a R c$ by the same $x R' y$ with $c Z y$.
3. At $(a, x)$, zag: the move $x R' y$ is answered by $a R b$, and $b Z y$.
4. At $(b, y)$ and $(c, y)$, no world has a successor, so zig and zag hold with nothing to check.

So $a$ and $x$ are bisimilar.
Notice what this shows: "has at least two successors" is true at $a$ and false at $x$, so no modal formula expresses it.

### Three constructions that are bisimulations

Three ways of building models give bisimulations for free, and they are the standard tools of the subject.
A *generated submodel* keeps a set $U$ of worlds that is closed under $R$; the identity on $U$ is a bisimulation, and zag holds because no successor has been thrown away.
A *bounded morphism* is a map $f$ whose graph is a bisimulation; [[the successor chain onto a reflexive point|T3YJ84YDV4]] is the standard case.
A *disjoint union* places models side by side, and each summand is a generated submodel of the union.

A fourth construction is the tree unraveling.
Its worlds are the finite paths $w = w_0 R w_1 R \cdots R w_n$, and the map that sends a path to its last world $w_n$ is a bounded morphism.
So every world is bisimilar to the root of a tree, which is why modal logic has the tree model property.

### A bisimulation that is not a bijection

A world $a$ with a loop $a R a$ and a cycle $b_0 R' b_1 R' b_0$, with the same atoms everywhere, are bisimilar by $\{(a, b_0), (a, b_1)\}$.
The [[loop and two-cycle example|2D9T8ERY94]] checks it.
One world is matched with two, and the reflexive loop at $a$ has no counterpart at $b_0$.

### What fails to be a bisimulation

Two models can produce the same sequences of atoms along their paths and still not be bisimilar.
In [[the trace-equivalent pair|KAMG2T6622]], one model postpones a choice and the other makes it at once, and zag fails after one step.
Leaving worlds out also breaks the definition.
If $w R v$ and a submodel keeps $w$ but drops $v$, then zig fails at $w$, and $\lozenge \top$ is true at $w$ only in the larger model.
Finally, a world where $p$ is true and a world where $p$ is false are never bisimilar, since the atom clause fails at the first pair.

### The rules you can use

The union of any family of bisimulations between two models is again a bisimulation, since each clause asks only for some witness.
So bisimilarity itself is the largest bisimulation.
The converse of a bisimulation is a bisimulation, and so is the composite of two, when it is nonempty.
On one model, then, bisimilarity is an equivalence relation.
Bisimilar worlds satisfy the same modal formulas, by [[bisimulation invariance|TKFFTAX30E]], and on image-finite models the converse holds, by the [[Hennessy-Milner theorem|DBDNYXA7ME]].

### Watch out

The most common slip is to check zig and forget zag.
Let $\mathfrak{M}$ have $a R b$ with $p$ true at $b$, and let $\mathfrak{M}'$ have $x R' y$ and $x R' z$ with $p$ true at $y$ only.
The relation $\{(a, x), (b, y)\}$ satisfies the atom and zig clauses.
Zag fails at $(a, x)$, because the move $x R' z$ would need a successor of $a$ where $p$ is false.
And the formula $\square p$ is true at $a$ and false at $x$.
A relation with only atom and zig is a *simulation*, and it preserves formulas built with $\wedge$, $\vee$ and $\lozenge$, but not $\square$ or $\neg$.

### History

Johan van Benthem used these relations, under the name p-relations, in his 1976 dissertation on modal correspondence theory.
David Park introduced bisimulation for concurrent processes in 1981.
Robin Milner made bisimilarity the central equivalence of his calculus of communicating systems.

### Try it

First, is $\{(a, b_0)\}$ alone a bisimulation between the loop at $a$ and the cycle $b_0 R' b_1 R' b_0$?
No: zig at $(a, b_0)$ answers $a R a$ by $b_0 R' b_1$, and then the pair $(a, b_1)$ must also be in the relation.

Second, find a bisimulation between $\mathbb{N}$ with the successor relation and the two-cycle, with no atoms true.
The relation $\{(n, b_{n \bmod 2}) : n \in \mathbb{N}\}$ works, because the move $n \to n+1$ matches the move $b_{n \bmod 2} \to b_{(n+1) \bmod 2}$.

## Explanations

### L1 human

Imagine two buildings of rooms joined by one-way doors, with some lights on in each room.
Two starting rooms are bisimilar when a guide in one building can always copy a walker in the other.
After each step, the guide must stand in a room with the same lights, and the copying must be possible forever.
One room with a door into itself copies two rooms with doors into each other: in both, one can always walk on, and nothing ever changes.

### L2 human

How do you find the largest bisimulation of a finite model?
Take worlds $1, 2, 3, 4, 5$ with $1 R 2$, $1 R 3$, $2 R 4$ and $3 R 5$, and make $p$ true at $4$ and $5$ only.
Start by grouping worlds by their atoms:
$$A = \{1, 2, 3\}, \qquad B = \{4, 5\}.$$
Now ask, for each world, which groups its successors fall into.
World $1$ has successors only in $A$, worlds $2$ and $3$ have successors only in $B$, and $4$ and $5$ have none.
So $A$ splits, and the new partition is
$$\{1\}, \qquad \{2, 3\}, \qquad \{4, 5\}.$$
Ask again: $1$ reaches $\{2, 3\}$, both $2$ and $3$ reach $\{4, 5\}$, and nothing changes.
Check: the relation that pairs worlds in the same block satisfies atom, zig and zag.
So the five-world model is bisimilar to the chain $[1] \to [23] \to [45]$ with $p$ at the end, and this splitting procedure, partition refinement, is how bisimilarity is computed in practice.

### L3 human

Bisimilarity is a greatest fixed point on the [[complete lattice|D7A0ZGZT5S]] of relations, so proofs that two worlds are bisimilar are proofs by coinduction.
A Kripke model is a coalgebra for the functor $X \mapsto \mathcal{P}(\mathrm{Prop}) \times \mathcal{P}(X)$, bounded morphisms are its coalgebra morphisms, and bisimilarity is the kernel of the map to a final coalgebra when one exists.
Bisimulation is the modal analogue of the back-and-forth systems of first-order model theory and of the [[Ehrenfeucht-Fraïssé game|2RE7YAZK8R]].
Richer languages need finer notions: graded modalities need counting bisimulations, and the nominals of [[hybrid logic|NVPQ9W9DED]] need bisimulations that respect named worlds.
The [[modal mu-calculus|MZ0M2KR9S0]] and [[propositional dynamic logic|VJ78A0Q22R]] stay invariant under plain bisimulation.
