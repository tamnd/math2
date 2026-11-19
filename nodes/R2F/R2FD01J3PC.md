---
tag: R2FD01J3PC
kind: concept
name: Medvedev's logic of finite problems
aliases: [medvedevs-logic, ml]
msc: ["03B55"]
topics: [38EQ20GR7M]
audience: research
uses: [H5NSKEP3P2, 5GTQ69W47T]
sources:
  - url: https://en.wikipedia.org/wiki/Intermediate_logic
    locator: Syntactics
  - arxiv: 2404.04349v1
    locator: pages 1 to 3
---

## Summary

For a finite nonempty set $X$, the *Medvedev frame* $M(X)$ is the set of nonempty subsets of $X$, ordered by $I \leq J$ iff $J \subseteq I$.
Write $M_n = M(\set{1, \dots, n})$; it has $2^n - 1$ worlds, the root $\set{1, \dots, n}$ and the $n$ maximal worlds $\set{i}$.
*Medvedev's logic* $\mathsf{ML}$ is the set of propositional formulas valid on every $M_n$, in the sense of [[Kripke semantics|5GTQ69W47T]].
It is an [[intermediate logic|H5NSKEP3P2]] with the disjunction property, it is structurally complete, and it is not finitely axiomatizable.
Whether it is decidable is an [[open problem|YAQ1Q48C1R]].
It matters because it is a natural logic of problems that is strictly stronger than intuitionistic logic and still constructive.

## Motivation

Kolmogorov read a formula as a problem, and a proof as a solution of that problem; this is one source of the [[BHK interpretation|7B53ZGXXEQ]].
Medvedev made this reading precise for problems with finitely many possible solutions.
Such a problem is given by a finite set of candidates and the subset of candidates that solve it.
In the frame form, a world $I$ is a state of knowledge in which the true candidate is known to lie in $I$.
Going up in the frame means learning more, so the set shrinks, and the maximal worlds are the states of full knowledge.
The resulting logic is strictly stronger than intuitionistic logic.

## Notation

The names $\mathsf{ML}$ and $\mathsf{LM}$ are both in use.
Some authors order $M(X)$ by inclusion on the proper subsets of $X$; complementation $I \mapsto X \setminus I$ is an isomorphism with the frame above.
In algebraic terms, $M_n$ is a Boolean algebra with $n$ atoms minus its bottom element, with the order reversed.

## Remarks

### Examples

1. $M_1$ is a single point, so its logic is classical logic; every theorem of $\mathsf{ML}$ is a classical tautology.
2. $M_2$ is the fork: a root below two maximal worlds.
3. $M_3$ has seven worlds: the root, three worlds $\set{i, j}$, and three maximal worlds, with each $\set{i, j}$ below $\set{i}$ and $\set{j}$.
4. [[The Kreisel-Putnam axiom is valid on every Medvedev frame|28FPR0F5WK]], so the [[Kreisel-Putnam logic|669Y0EGM3N]] is contained in $\mathsf{ML}$.
5. [[Every finite chain is a p-morphic image of a Medvedev frame|P0GMP7KQ44]], so $\mathsf{ML}$ is contained in [[Gödel-Dummett logic|474SGS2N0X]].

### Non-examples

1. [[Intuitionistic logic is strictly smaller than ML|MG4574RE7V]]: the Kreisel-Putnam axiom separates them.
2. [[ML does not prove weak excluded middle|GNTDZ4S97V]], so $\mathsf{ML}$ is not $\mathsf{KC}$, $\mathsf{LC}$ or classical logic.
3. The frame with a root below three maximal worlds is not a Medvedev frame, and it refutes the Kreisel-Putnam axiom.

### Basic properties

1. $\mathsf{ML}$ contains $\mathsf{IPC}$, by soundness in [[the completeness theorem|480TCT5CJ9]]. It is closed under modus ponens and substitution, because validity on a frame is.
2. $\mathsf{ML}$ is consistent, since $\bot$ fails on $M_1$. So it is an intermediate logic, between $\mathsf{IPC}$ and classical logic.
3. [[ML has the disjunction property|TH1ZZFWEH1]].
4. [[ML is structurally complete|TWCP5X6PGQ]]: every admissible rule is derivable; see [[admissible rules|C5K35H0R4Y]].
5. By a theorem of Maksimova, a variant of a theorem of Levin, $\mathsf{ML}$ is the largest extension of the weak Kreisel-Putnam logic with the disjunction property. We cite this without proof.
6. Maksimova, Skvortsov and Shehtman proved that $\mathsf{ML}$ is not finitely axiomatizable. We cite this without proof.
7. The complement of $\mathsf{ML}$ is recursively enumerable, since a refutation is a valuation on some finite frame $M_n$. So $\mathsf{ML}$ is decidable iff it is recursively axiomatizable.

### History

Medvedev introduced the logic of finite problems in papers from 1962 on.
Prucnal proved its structural completeness in 1976, and Skvortsov later gave a second proof.
Levin and Maksimova proved that it is maximal among logics with a form of the disjunction property.
Maksimova, Skvortsov and Shehtman proved in 1979 that it has no finite axiomatization.

### Common errors

1. Including the empty set as a world. It would lie above every world, and a frame with a greatest world validates weak excluded middle.
2. Expecting $\mathsf{ML}$ to be recursively axiomatizable because each frame $M_n$ is finite. Finiteness of the frames gives only the recursive enumerability of the complement.
3. Confusing $\mathsf{ML}$ with Kreisel-Putnam logic. Both have the disjunction property, but $\mathsf{KP}$ is finitely axiomatized and $\mathsf{ML}$ is not.

## Explanations

### L1 human

Think of a puzzle whose answer is one of a few candidates, say 1, 2 or 3.
At any moment you know a set of candidates that may still be right, such as $\set{1, 3}$.
As you learn, the set shrinks, until a single candidate remains.
A statement is accepted at a moment if it stays true however the remaining doubt is resolved.
The logic of all such puzzles is Medvedev's logic.
It accepts a few principles that intuitionistic logic rejects, but it still rejects the law of excluded middle.

### L2 human

1. In $M_2$, the root is $\set{1, 2}$ and the maximal worlds are $\set{1}$ and $\set{2}$.
2. Let $p$ hold only at $\set{1}$.
3. At the root, $p$ fails, and $\neg p$ fails because $\set{1}$ forces $p$.
4. So $p \vee \neg p$ fails at the root, and excluded middle is not in $\mathsf{ML}$.
5. Also $\neg \neg p$ fails at the root, since $\set{2}$ forces $\neg p$. So weak excluded middle fails too.

The typical use of $\mathsf{ML}$ is as a test case: it shows that a constructive logic with the disjunction property need not be $\mathsf{IPC}$.
A trap: $M_n$ has no greatest world.
Adding the empty set as a top would give a frame that validates weak excluded middle.

### L3 human

Medvedev frames are the posets of nonempty subsets, so $\mathsf{ML}$ is the logic of the finite Boolean cubes without their top.
The disjunction property comes from gluing: $M_m$ and $M_n$ sit as disjoint generated subframes in $M_{m+n}$.
Structural completeness comes from a universal valuation on $M_n$, built from pairwise inconsistent formulas, which turns every valuation into a substitution instance.
Both arguments use only the combinatorics of subsets and are given in full in the linked proofs.

The open questions about $\mathsf{ML}$ are of a computational kind.
It is co-recursively enumerable, but no recursive axiomatization is known, and the [[decidability problem|YAQ1Q48C1R]] is open.
In the lattice of [[intermediate logics|H5NSKEP3P2]] it is a maximal logic with the disjunction property, and the same question for other base logics leads to the study of [[admissible rules|C5K35H0R4Y]].
The formulas all of whose substitution instances are valid in [[inquisitive logic|EX0ND8DCTN]] are exactly the theorems of $\mathsf{ML}$.
