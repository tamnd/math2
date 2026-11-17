---
tag: 9APRFM0G7F
kind: statement
role: theorem
name: Buchholz hydra theorem
msc: ["03F15", "03F35", "05C05"]
topics: [T6FK1E7GJ1]
audience: research
uses: [9APRFM0G7F, C028FF4TWM, 0C9J6W2A8A, S5FTQGHVKC, DC60FYCSPM, C72RBH0CDR]
about: [9APRFM0G7F, S5FTQGHVKC, DC60FYCSPM]
history:
  first_stated: "1987"
  notes: "Buchholz introduced the labelled hydras in 'An independence result for (Π¹₁-CA)+BI' (1987)."
sources:
  - url: https://en.wikipedia.org/wiki/Buchholz_hydra
    locator: Rules
  - url: https://en.wikipedia.org/wiki/Buchholz_hydra
    locator: lead section
same_as:
  wikidata: Q108582264
  wikipedia: Buchholz hydra
---

## Statement

A *[[Buchholz hydra|9APRFM0G7F]]* is a finite [[rooted tree|0C9J6W2A8A]] whose root has the label $+$, and whose other nodes have labels in $\N \cup \set{\omega}$.
Every child of the root has the label $0$.
The *heads* are the leaves other than the root, and the hydra is *dead* when it is the root alone.
At step $n$ of a battle Hercules cuts a head $\sigma$ with parent $\tau$, and the hydra changes as follows.

1. Label $0$, and $\tau$ is the root: remove $\sigma$.
2. Label $0$, and $\tau$ is not the root: remove $\sigma$, then attach $n$ copies of the subtree at $\tau$ to the parent of $\tau$.
3. Label $u \in \N$ with $u > 0$: let $\varepsilon$ be the first node below $\sigma$, on the path to the root, with a label $v < u$. Take a copy of the subtree at $\varepsilon$, give its root the label $u - 1$ and give the copy of $\sigma$ the label $0$. Put this copy in the place of $\sigma$.
4. Label $\omega$: give $\sigma$ the label $n + 1$.

In rule 3 the node $\varepsilon$ exists, because the child of the root on the path has the label $0 < u$.
Let $R_x$ be the path of $x$ nodes with labels $+, 0, \omega, \dots, \omega$.
Let $\mathrm{BH}(x)$ be the number of steps of the battle on $R_x$ that always cuts the rightmost head at step $n = 1, 2, 3, \dots$.

**Theorem** (Buchholz).

1. Every battle ends: for every Buchholz hydra and every choice of the heads, the hydra is dead after finitely many steps.
2. Statement 1, written in the language of [[second-order arithmetic|DC60FYCSPM]], is not provable in $(\Pi^1_1\text{-}\mathsf{CA}) + \mathsf{BI}$, the system with $\Pi^1_1$ comprehension and bar induction.
3. Statement 1 is provable in $\mathsf{ZFC}$, through the well-foundedness of an ordinal notation system up to the [[Takeuti-Feferman-Buchholz ordinal|S5FTQGHVKC]] $\psi_0(\varepsilon_{\Omega_\omega + 1})$.

The [[proof outline|YYQ76F4812]] gives the ordinal assignment and marks the cited lemmas.

## Remarks

### Why each hypothesis is needed

- The theory in part 2 is $(\Pi^1_1\text{-}\mathsf{CA}) + \mathsf{BI}$. It is much stronger than [[Peano arithmetic|MPSCREYC3M]], and still it does not prove statement 1; $\mathsf{ZFC}$ proves it.
- The children of the root have the label $0$. This makes the node $\varepsilon$ of rule 3 exist for every head.
- The labels are at most $\omega$. With labels up to $\omega$ only, all the ordinals of the proof stay below $\psi_0(\varepsilon_{\Omega_\omega + 1})$.
- Rule 4 replaces $\omega$ by a finite label. If it kept the label $\omega$, a head with label $\omega$ would never change and could be cut for ever.

### Consequences

- $\mathrm{BH}(1) = 0$, because $R_1$ is the root alone. $\mathrm{BH}(2) = 1$, because $R_2$ has one head with label $0$ on the root, and rule 1 removes it.
- On $R_3$ the first three steps give $+(0(\omega))$, then $+(0(2))$, then $+(0(1(0)))$, by rules 4 and 3. Step $3$ then uses rule 2 with $3$ copies.
- The function $\mathrm{BH}$ is total by part 1, but $(\Pi^1_1\text{-}\mathsf{CA}) + \mathsf{BI}$ does not prove that it is total, as the Wikipedia article states.
- The [[Kirby-Paris hydra|C028FF4TWM]] is the special case of hydras with labels $0$ only, where only rules 1 and 2 apply.

### Converse

Part 1 says that Hercules always wins, so no strategy of the hydra survives.
The converse question, whether some battle lasts for ever, has the answer no for every battle.

## History

Wilfried Buchholz introduced the labelled hydras in 1987, in the paper "An independence result for $(\Pi^1_1\text{-}\mathsf{CA}) + \mathsf{BI}$".
He used them to give a combinatorial statement that is true and independent of this subsystem of second-order arithmetic.
The Wikipedia article also cites a later direct independence proof by Hamano and Okada.

## Explanations

### L1 human

A Buchholz hydra is a tree with numbers written on its nodes, and Hercules cuts its heads one by one.
Cutting a head can make the tree much larger, as for the ordinary hydra.
A head with a number $u$ larger than $0$ is replaced by a copy of a large part of the tree, with the number lowered to $u - 1$.
In spite of this, every battle ends with the root alone.
The proof needs very large infinite numbers, and strong systems of axioms cannot carry it out.

### L2 human

The first steps of the standard battle on $R_3 = +(0(\omega))$, written with parentheses for children.

1. Step $1$ cuts the head with label $\omega$. Rule 4 gives it the label $2$: $+(0(2))$.
2. Step $2$ cuts the head with label $2$. The first node below it with a smaller label is the node $0$.
3. Rule 3 copies the subtree $0(2)$, gives the copy of the node $0$ the label $1$, and gives the copy of the head the label $0$. This gives $1(0)$.
4. The copy replaces the head, so the hydra is $+(0(1(0)))$.
5. Step $3$ cuts the head with label $0$. Its parent has label $1$ and is not the root, so rule 2 attaches $3$ copies of the node $1$ to the node $0$.
6. The hydra is now $+(0(1)(1)(1)(1))$, and the battle goes on for a very long time.

The ordinals of the hydras in this battle are $\psi_0(\Omega_\omega)$ at the start, then the Bachmann-Howard ordinal $\psi_0(\Omega_2)$, and then smaller ordinals.
The trap: the hydra changes shape in a way that does not decrease any simple size, so only an ordinal measure shows termination.

### L3 human

Buchholz hydras are the trees of the terms of his notation system for the collapsing functions $\psi_\nu$, $\nu \le \omega$.
A node with label $\nu$ and children of values $\alpha_1, \dots, \alpha_j$ has the value $\psi_\nu(\alpha_1 + \cdots + \alpha_j)$, and the root takes the sum.
The rules of the game follow the fundamental sequences of these terms, so a battle is a descending sequence below the [[Takeuti-Feferman-Buchholz ordinal|S5FTQGHVKC]].
This ordinal is the [[proof-theoretic ordinal|C72RBH0CDR]] of $(\Pi^1_1\text{-}\mathsf{CA}) + \mathsf{BI}$, which is why the termination escapes this system.
The [[theories of iterated inductive definitions|5VNT564Y2W]] have ordinals of the same kind, and the game is a standard example in [[ordinal analysis|C5E5TG8PGP]].
