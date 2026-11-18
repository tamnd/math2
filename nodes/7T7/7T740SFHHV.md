---
tag: 7T740SFHHV
kind: definition
name: Bisimulation
msc: ["03B45", "68Q85", "68Q55"]
topics: [SPQVNPZDTB]
audience: grad
defines: X27BR4YP2Y
uses: [05AVARPXA2, NGHWZ9Y7ZV]
sources:
  - url: https://en.wikipedia.org/wiki/Bisimulation
  - url: https://en.wikipedia.org/wiki/Bisimulation
    locator: Bisimulation and modal logic
  - url: https://en.wikipedia.org/wiki/Kripke_semantics
    locator: Model constructions
  - url: https://builds.openlogicproject.org/
    locator: Modal Logic
---

## Definition

A Kripke model is a triple $\mathfrak{M} = (W, R, V)$, where $W$ is a nonempty set of worlds, $R \subseteq W \times W$, and $V$ sends each propositional variable $p$ to a set $V(p) \subseteq W$; see [[Kripke semantics|NGHWZ9Y7ZV]].
Let $\mathfrak{M} = (W, R, V)$ and $\mathfrak{M}' = (W', R', V')$ be Kripke models.
A *bisimulation* between $\mathfrak{M}$ and $\mathfrak{M}'$ is a nonempty [[binary relation|05AVARPXA2]] $Z \subseteq W \times W'$ such that, for every pair with $w Z w'$:

1. (atom) for every variable $p$, $w \in V(p)$ if and only if $w' \in V'(p)$;
2. (zig) if $w R v$, then there is $v' \in W'$ with $w' R' v'$ and $v Z v'$;
3. (zag) if $w' R' v'$, then there is $v \in W$ with $w R v$ and $v Z v'$.

Worlds $w$ and $w'$ are *bisimilar*, written $w \mathrel{\underline{\leftrightarrow}} w'$, if $w Z w'$ for some bisimulation $Z$.

Three special cases have their own names.

- $\mathfrak{N} = (U, R \cap U^2, V(\cdot) \cap U)$ is a *generated submodel* of $\mathfrak{M}$ when $\emptyset \neq U \subseteq W$ and $u \in U$, $u R v$ imply $v \in U$.
- A map $f \colon W \to W'$ is a *bounded morphism* when $w$ and $f(w)$ satisfy the same variables, $w R v$ implies $f(w) R' f(v)$, and $f(w) R' v'$ implies $v' = f(v)$ for some $v$ with $w R v$.
- The *disjoint union* of models $\mathfrak{M}_i = (W_i, R_i, V_i)$ with pairwise disjoint $W_i$ is $(\bigcup W_i, \bigcup R_i, p \mapsto \bigcup V_i(p))$.

For a *labelled transition system* $(S, A, \to)$, with $\to \subseteq S \times A \times S$, a bisimulation is a relation $Z \subseteq S \times S$ such that, for every $(s, t) \in Z$ and every action $a \in A$:

1. if $s \xrightarrow{a} s'$, then $t \xrightarrow{a} t'$ and $(s', t') \in Z$ for some $t'$;
2. if $t \xrightarrow{a} t'$, then $s \xrightarrow{a} s'$ and $(s', t') \in Z$ for some $s'$.

A Kripke model with one relation $R_a$ for each action $a$ is a labelled transition system with a valuation, and the two definitions then agree.

## Notation

In modal logic the usual symbol is $\mathrel{\underline{\leftrightarrow}}$, and in process theory it is $\sim$.
We write $Z \colon \mathfrak{M}, w \mathrel{\underline{\leftrightarrow}} \mathfrak{M}', w'$ when $Z$ is a bisimulation with $w Z w'$.
The zig and zag clauses are also called the forth and back clauses.
We write $\mathfrak{M} \uplus \mathfrak{M}'$ or $\biguplus_i \mathfrak{M}_i$ for disjoint unions.

## Remarks

### Examples

1. A loop and a two-cycle are bisimilar; see [[a loop and a two-cycle are bisimilar|2D9T8ERY94]].
2. The graph of a bounded morphism is a bisimulation; see [[the successor chain maps onto a reflexive point|T3YJ84YDV4]].
3. If $\mathfrak{N}$ is a generated submodel of $\mathfrak{M}$, then $\set{(u, u) : u \in U}$ is a bisimulation. The zag clause holds because every successor of $u$ in $\mathfrak{M}$ lies in $U$.
4. For each $i$, the identity on $W_i$ is a bisimulation between $\mathfrak{M}_i$ and $\biguplus_j \mathfrak{M}_j$, since $\mathfrak{M}_i$ is a generated submodel of the union.

### Non-examples

1. Two models with the same paths of atoms need not be bisimilar; see [[two trace-equivalent models that are not bisimilar|KAMG2T6622]].
2. Let $\mathfrak{M}$ have worlds $w$, $v$ with $w R v$, and let $\mathfrak{N}$ be the restriction to $\set{w}$. The relation $\set{(w, w)}$ between $\mathfrak{N}$ and $\mathfrak{M}$ fails the zag clause, because the move $w R v$ in $\mathfrak{M}$ has no answer in $\mathfrak{N}$.

### Bisimulation games

The bisimulation game on $\mathfrak{M}$ and $\mathfrak{M}'$ has two players, Spoiler and Duplicator.
A position is a pair $(w, w')$.
In each round Spoiler picks one of the two models and a successor of the current world there.
Duplicator must answer with a successor of the current world in the other model.
Duplicator loses if the two current worlds differ on some variable, or if she cannot answer.
Spoiler loses if he cannot move.
Duplicator has a winning strategy in the game of infinitely many rounds from $(w, w')$ if and only if $w \mathrel{\underline{\leftrightarrow}} w'$.
The pairs of positions from which she wins form the largest bisimulation, and a bisimulation is a strategy for her.
If Duplicator wins the game of $n$ rounds, we say that $w$ and $w'$ are $n$-bisimilar.
For finitely many variables, $n$-bisimilarity is the same as agreement on all formulas of modal depth at most $n$.

### Basic properties

1. Bisimilarity is the union of all bisimulations, so it is the largest bisimulation when it is nonempty.
2. On one model, bisimilarity is an equivalence relation, since converses and nonempty composites of bisimulations are bisimulations.
3. Bisimilar worlds satisfy the same modal formulas; see [[bisimulation invariance of modal formulas|TKFFTAX30E]].
4. Bisimilarity on a labelled transition system is the greatest fixed point of the monotone map $Z \mapsto \set{(s, t) : \text{clauses 1 and 2 hold for } (s, t) \text{ with respect to } Z}$ on the [[complete lattice|D7A0ZGZT5S]] of relations.

## Explanations

### L1 human

A bisimulation is a list of pairs of states that behave alike.
Paired states must show the same facts.
Each step from one state of a pair must be copied by a step from the other state.
The two new states must again be paired.
For example, a light that blinks forever looks the same as two lights that take turns forever, if one only watches whether something is on.

### L2 human

We show that the bisimulation game detects a difference.

1. Let $\mathfrak{M}$ have $w R v$ and nothing else, and let $\mathfrak{M}'$ have $w' R' v'$ and $v' R' u'$. All variables are false everywhere.
2. Spoiler starts at $(w, w')$ and moves in $\mathfrak{M}'$ from $w'$ to $v'$.
3. Duplicator must answer in $\mathfrak{M}$ from $w$, and her only move is to $v$.
4. At $(v, v')$ Spoiler moves in $\mathfrak{M}'$ from $v'$ to $u'$.
5. Duplicator must move from $v$, but $v$ has no successor, so she loses.
6. So $w$ and $w'$ are not bisimilar, and the formula $\lozenge \lozenge \top$ separates them.

The typical use is to show that two worlds are not bisimilar, by a short winning strategy for Spoiler.
Each winning strategy for Spoiler with $n$ rounds gives a formula of modal depth at most $n$ that separates the worlds.
A trap: Spoiler may change the model in each round, and a strategy that always plays in one model can miss the difference.

### L3 human

A bisimulation is a relation $Z$ that is a post-fixed point of a monotone operator, $Z \subseteq \Phi(Z)$.
So the largest bisimulation exists by the [[Knaster-Tarski theorem|RHXP3HA64M]], and proofs that two worlds are bisimilar are proofs by coinduction.
Bounded morphisms are the morphisms of Kripke models seen as coalgebras of the powerset functor, and generated submodels and disjoint unions are the subcoalgebras and coproducts.
The same three constructions on frames appear in the Goldblatt-Thomason theorem, which characterizes the modally definable classes of frames.
