---
tag: 28FPR0F5WK
kind: example
name: Medvedev frames validate the Kreisel-Putnam axiom
msc: ["03B55"]
topics: [38EQ20GR7M]
audience: research
instance_of: [669Y0EGM3N]
uses: [X0C1NC7FXX, 5GTQ69W47T, R2FD01J3PC]
sources:
  - arxiv: 2404.04349v1
    locator: page 1
---

## Example

For a finite nonempty set $X$, the Medvedev frame $M(X)$ is the set of nonempty subsets of $X$, with $I \leq J$ iff $J \subseteq I$.
Its root is $X$, and its maximal worlds are the singletons.
We show that every instance of the [[Kreisel-Putnam axiom|X0C1NC7FXX]] is valid on $M(X)$.

1. Fix a model on $M(X)$ and a formula $\varphi$. Let $A = \set{i \in X : \set{i} \nVdash \varphi}$.
2. Claim: $J \Vdash \neg \varphi$ iff $J \subseteq A$. If $i \in J \setminus A$, then $\set{i} \geq J$ forces $\varphi$, so $J \nVdash \neg \varphi$.
3. Conversely, let $J \subseteq A$ and $K \geq J$, so $K \subseteq J$. Pick $i \in K$. Then $\set{i} \geq K$ and $\set{i} \nVdash \varphi$, so $K \nVdash \varphi$ by persistence. Hence $J \Vdash \neg \varphi$.
4. Let $I \Vdash \neg \varphi \to \psi \vee \chi$. The worlds above $I$ that force $\neg \varphi$ are the nonempty $J \subseteq I \cap A$, by step 2.
5. If $I \cap A = \emptyset$, no world above $I$ forces $\neg \varphi$. Then $I \Vdash \neg \varphi \to \psi$.
6. Otherwise $K = I \cap A$ is a world above $I$ that forces $\neg \varphi$, so $K \Vdash \psi$ or $K \Vdash \chi$. Say $K \Vdash \psi$.
7. Every world above $I$ that forces $\neg \varphi$ is some $J \subseteq K$, so $J \geq K$ and $J \Vdash \psi$ by persistence. Hence $I \Vdash \neg \varphi \to \psi$.
8. In all cases $I \Vdash (\neg \varphi \to \psi) \vee (\neg \varphi \to \chi)$. So every theorem of $\mathsf{KP}$ is valid on $M(X)$, and $\mathsf{KP} \subseteq \mathsf{ML}$.

## Remarks

The key fact is step 4: above any world, the worlds that force a negation form either the empty set or a principal up-set.
The weak Kreisel-Putnam axiom, with $\neg \psi$ and $\neg \chi$ in place of $\psi$ and $\chi$, follows as a special case.
The inclusion $\mathsf{KP} \subseteq$ [[Medvedev's logic|R2FD01J3PC]] is strict, since Medvedev's logic is not finitely axiomatizable.

## Explanations

### L1 human

In a Medvedev frame, a world is a set of possible solutions, and going up means narrowing the set.
"Not $\varphi$" holds exactly on the sets that avoid every solution where $\varphi$ holds.
So above a world there is a largest such set, and whatever it decides is decided for all the smaller ones.

### L2 human

1. Compute the set $A$ of maximal worlds that refute $\varphi$.
2. Then the truth set of $\neg \varphi$ consists of the nonempty subsets of $A$.
3. Intersect with the current world to get the least world forcing $\neg \varphi$, and read off the disjunct there.

The typical use is to show that a formula is in Medvedev's logic, or to find frames of $\mathsf{KP}$.
A trap: the frame with a root below three leaves is not a Medvedev frame, and it refutes the axiom.
