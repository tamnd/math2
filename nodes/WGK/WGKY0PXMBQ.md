---
tag: WGKY0PXMBQ
kind: concept
name: Beth semantics
msc: ["03B20"]
topics: [38EQ20GR7M]
audience: research
uses: [Q11N8X99FK, 35VKJY77TY, 062D9KXJB1]
sources:
  - url: https://plato.stanford.edu/entries/logic-intuitionistic/
    locator: Kripke and Beth semantics for intuitionistic logic
---

## Summary

*Beth semantics* interprets [[intuitionistic logic|Q11N8X99FK]] on [[trees|062D9KXJB1]] of nodes, read as stages of knowledge, with paths as possible histories; see [[the definition|GPC8Y4ZCSA]].
Variables are true on up-sets that are closed under bars: a node is in the set when every path through it eventually enters the set.
A node forces $\varphi \vee \psi$ when some bar above it consists of nodes that force $\varphi$ or force $\psi$, and the other clauses are those of [[Kripke semantics|35VKJY77TY]].
Beth semantics is sound and complete for intuitionistic logic, and it is the natural semantics for choice sequences and for intuitionistic analysis.

## Motivation

In Brouwer's mathematics, a real number is given by a sequence of approximations that is never finished.
A statement about it is known when every continuation of the sequence eventually decides it.
Beth modelled this with trees: the nodes are finite stages, the paths are the infinite sequences, and "known" means "barred".
The clause for disjunction matches the reading: a disjunction may be decided at different stages on different paths.

## Notation

$w \Vdash \varphi$ is forcing, and $N_w$ is the set of paths through $w$.
A *bar* for $w$ is a set of nodes above $w$ that meets every path through $w$.

## Remarks

### Examples

1. On the tree with root $r$ and two leaves, the root can force $p \vee q$ without forcing $p$ or $q$; see [[a Beth model of a disjunction|7YFCQSP53A]].
2. On the full binary tree, with $p$ true at the nodes that contain a $1$, the root does not force $p \vee \neg p$; see [[the Beth countermodel to excluded middle|4H4MQG78DW]].
3. On a finite tree, a barred up-set is determined by the leaves that it contains. So finite Beth models are classical, and countermodels need infinite trees.

### Non-examples

1. A valuation that is an up-set but not barred breaks soundness; see [[a valuation that is not barred|DSSNTBS3XM]].
2. A Kripke model on a poset that is not a tree is not a Beth model, although it can be unravelled into a tree.

### Basic properties

1. Persistence and bar closure: every truth set is an up-set, and it is barred.
2. Soundness and completeness for $\mathsf{IPC}$; see [[the Beth completeness theorem|BTG0J9V3H4]].
3. Every Kripke model can be turned into a Beth model that forces the same formulas, by the construction with repeated worlds in the proof.
4. The barred up-sets of a tree correspond to the open sets of its space of paths. So Beth models on the full binary tree are topological models on the Cantor space.

### History

Beth introduced his semantics in the 1950s, before Kripke semantics.
Kripke's semantics of 1965 simplified the clause for disjunction, and it replaced trees by arbitrary partial orders.

### Common errors

1. Using the Kripke clause for $\vee$ on a Beth tree. Then the model of example 1 does not force $p \vee q$ at the root.
2. Forgetting that valuations must be barred. Then $p \vee p \to p$ can fail.

## Explanations

### L1 human

Imagine a coin that is tossed again and again, forever.
Each node of the tree is a finite record of tosses, and each path is a full infinite history.
"Some toss shows heads" is not known at the start.
"Heads or tails at toss one" is known at the start, because every history decides it after one toss.

### L2 human

1. Take the tree with root $r$ and leaves $a$, $b$, with $p$ true at $a$ and $q$ true at $b$.
2. The set $\set{a, b}$ is a bar for $r$, and each of its nodes forces $p$ or $q$.
3. So $r \Vdash p \vee q$ in Beth semantics.
4. In Kripke semantics on the same frame, $r \nVdash p \vee q$, since $r$ forces neither $p$ nor $q$.

The typical use of Beth semantics is in completeness proofs for intuitionistic analysis, where Kripke models are not available.
A trap: Beth and Kripke semantics validate the same propositional formulas, but they differ on single models.

### L3 human

Beth semantics is topological semantics in disguise: the paths of the tree form a space, the sets $N_w$ are its basic open sets, and barred up-sets are open sets.
For intuitionistic predicate logic, the Beth clause for $\exists$ also uses bars: a node forces $\exists x \varphi$ when a bar above it consists of nodes with witnesses.
In terms of Grothendieck topologies, Beth semantics is the sheaf semantics for the bar covering, while Kripke semantics is the presheaf semantics; see [[topological semantics|RKFTMQNWRC]].
