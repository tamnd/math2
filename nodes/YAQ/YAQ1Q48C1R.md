---
tag: YAQ1Q48C1R
kind: problem
name: Decidability of Medvedev's logic
msc: ["03B55", "03B25"]
topics: [38EQ20GR7M]
audience: research
uses: [R2FD01J3PC]
about: [R2FD01J3PC]
sources:
  - url: https://en.wikipedia.org/wiki/Intermediate_logic
    locator: Syntactics
  - arxiv: 2404.04349v1
    locator: page 1
---

## Problem

Let $\mathsf{ML}$ be [[Medvedev's logic|R2FD01J3PC]], the set of propositional formulas valid on every Medvedev frame $M_n$, $n \geq 1$.

1. Is $\mathsf{ML}$ decidable: is there an algorithm that decides, for a formula $\varphi$, whether $\varphi \in \mathsf{ML}$?
2. Equivalently, is $\mathsf{ML}$ recursively axiomatizable?

The problem is open.

## Remarks

The two questions are equivalent for the following reason.

1. The complement of $\mathsf{ML}$ is recursively enumerable. Enumerate all pairs of $n$ and a valuation of the atoms of $\varphi$ on the finite frame $M_n$, and check forcing at each world.
2. If $\mathsf{ML}$ is decidable, then $\mathsf{ML}$ itself is a recursive set of axioms for $\mathsf{ML}$.
3. If $\mathsf{ML}$ has a recursive set of axioms, then its theorems are recursively enumerable. With step 1, $\mathsf{ML}$ is then decidable.

The difficulty is that no bound is known on the size $n$ of a Medvedev frame needed to refute a formula that is not in $\mathsf{ML}$.
For [[intermediate logics|H5NSKEP3P2]] with the finite model property and a finite axiomatization, decidability follows from a theorem of Harrop; $\mathsf{ML}$ is not finitely axiomatizable, by a theorem of Maksimova, Skvortsov and Shehtman.
The logic is [[structurally complete|TWCP5X6PGQ]] and has the [[disjunction property|TH1ZZFWEH1]], so it has a rich theory despite the open question.

## Explanations

### L1 human

Medvedev's logic is defined by a family of finite pictures, one for each number of candidates.
To show that a formula is not a law, it is enough to find one picture where it fails, and a computer can search for it.
To show that a formula is a law, one must check all the pictures, and there are infinitely many.
Nobody knows a method that always stops with the right answer.

### L2 human

1. To refute $\neg p \vee \neg \neg p$, the search tries $M_1$ and then $M_2$, where it finds a countermodel.
2. To confirm the Kreisel-Putnam axiom, a search over frames never stops; a proof such as [[the Medvedev frame argument|28FPR0F5WK]] is needed.
3. A decision method would need a bound on $n$ in terms of $\varphi$, or a recursive axiom system.

The typical use of this problem is as a test of general methods for deciding intermediate logics.
A trap: finiteness of each frame $M_n$ does not give decidability, because the class of frames is infinite and has no known axiomatization.
