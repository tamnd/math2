---
tag: 9APRFM0G7F
kind: statement
role: theorem
name: Buchholz hydra theorem
msc: ["03F15", "03F35", "05C05"]
topics: [T6FK1E7GJ1]
audience: research
uses: [C028FF4TWM, 0C9J6W2A8A, S5FTQGHVKC, DC60FYCSPM, C72RBH0CDR]
about: [S5FTQGHVKC, DC60FYCSPM]
history:
  first_stated: "1987"
  notes: "Buchholz introduced the labeled hydras in 'An independence result for (Π¹₁-CA)+BI' (1987)."
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

With labels on its nodes, a hydra can copy large parts of itself at each cut.
Every battle still ends, but a strong subsystem of second-order arithmetic cannot prove it.

A *Buchholz hydra* is a finite [[rooted tree|0C9J6W2A8A]] whose root has the label $+$, and whose other nodes have labels in $\mathbb{N} \cup \{ \omega \}$.
Every child of the root has the label $0$.
The *heads* are the leaves other than the root, and the hydra is *dead* when it is the root alone.
At step $n$ of a battle Hercules cuts a head $\sigma$ with parent $\tau$, and the hydra changes as follows.

1. Label $0$, and $\tau$ is the root: remove $\sigma$.
2. Label $0$, and $\tau$ is not the root: remove $\sigma$, then attach $n$ copies of the subtree at $\tau$ to the parent of $\tau$.
3. Label $u \in \mathbb{N}$ with $u > 0$: let $\varepsilon$ be the first node below $\sigma$, on the path to the root, with a label $v < u$.
   Take a copy of the subtree at $\varepsilon$, give its root the label $u - 1$ and give the copy of $\sigma$ the label $0$, and put this copy in the place of $\sigma$.
4. Label $\omega$: give $\sigma$ the label $n + 1$.

Let $R_x$ be the path of $x$ nodes with labels $+, 0, \omega, \dots, \omega$.
Let $\mathrm{BH}(x)$ be the number of steps of the battle on $R_x$ that always cuts the rightmost head.

**Theorem** (Buchholz).

1. Every battle ends: for every Buchholz hydra and every choice of the heads, the hydra is dead after finitely many steps.
2. Statement 1, written in the language of [[second-order arithmetic|DC60FYCSPM]], is not provable in $(\Pi^1_1\text{-}\mathsf{CA}) + \mathsf{BI}$, the system with $\Pi^1_1$ comprehension and bar induction.
3. Statement 1 is provable in $\mathsf{ZFC}$, through the well-foundedness of an ordinal notation system up to the [[Takeuti-Feferman-Buchholz ordinal|S5FTQGHVKC]] $\psi_0(\varepsilon_{\Omega_\omega + 1})$.

The [[proof outline|YYQ76F4812]] gives the ordinal assignment and marks the cited lemmas.

## Remarks

### The first steps on a small hydra

Write a node with its children in parentheses, so $R_3$ is $+(0(\omega))$.
Step $1$ cuts the head $\omega$, and rule 4 relabels it with $n + 1 = 2$:
$$+(0(\omega)) \;\to\; +(0(2)).$$
Step $2$ cuts the head $2$.
The first node below it with a label less than $2$ is the node $0$, so rule 3 copies the subtree $0(2)$, relabels its root as $1$ and the copy of the head as $0$:
$$+(0(2)) \;\to\; +(0(1(0))).$$
Step $3$ cuts the head $0$, whose parent $1$ is not the root.
Rule 2 removes the head and attaches $3$ copies of the node $1$ to the node $0$:
$$+(0(1(0))) \;\to\; +(0(1)(1)(1)(1)).$$
Each of the four heads with label $1$ will be replaced by a copy of a larger tree, and the battle goes on for a very long time.

### Why each hypothesis is needed

The theory in part 2 is $(\Pi^1_1\text{-}\mathsf{CA}) + \mathsf{BI}$.
It is much stronger than [[Peano arithmetic|MPSCREYC3M]] and than $\mathsf{ATR}_0$, and still it does not prove statement 1, while $\mathsf{ZFC}$ does.

The children of the root have the label $0$, and this makes the node $\varepsilon$ of rule 3 exist for every head, because the child of the root on the path has the label $0 < u$.
Without it, a head with label $1$ just above the root would have no node to copy.

Rule 4 replaces $\omega$ by a finite label.
If it kept the label $\omega$, a head with label $\omega$ would never change and could be cut for ever.

### What it gives you

The [[Kirby-Paris hydra|C028FF4TWM]] is the special case of hydras with labels $0$ only.
Then only rules 1 and 2 apply, and they are the Kirby-Paris rules with $n$ copies at step $n$.

The first values of $\mathrm{BH}$ are small.
$\mathrm{BH}(1) = 0$, because $R_1$ is the root alone, and $\mathrm{BH}(2) = 1$, because $R_2 = +(0)$ has one head on the root and rule 1 removes it.
From $R_3$ on the values are huge.
The function $\mathrm{BH}$ is total by part 1, but by part 2 the system $(\Pi^1_1\text{-}\mathsf{CA}) + \mathsf{BI}$ does not prove that it is total.

### The converse

The converse question asks whether some battle lasts for ever.
Part 1 says no, for every hydra and every choice of heads, so Hercules cannot lose even with a bad choice.

### Watch out

The size of the hydra is no guide.
In the small battle above, the number of nodes goes $3, 3, 4, 6$, and it keeps growing for a long time.
Only an ordinal measure shows that the battle ends, and here the ordinals are far beyond $\varepsilon_0$.

The node $\varepsilon$ of rule 3 is searched strictly below $\sigma$, toward the root, and the test is $v < u$, not $v \le u$.
In $+(0(1(1)))$ the head has label $1$, its parent also has label $1$, and $\varepsilon$ is the node $0$, not the parent.

### Try it

First, cut the head of $+(0(0))$ at step $1$.
The head has label $0$ and its parent is not the root, so rule 2 removes it and attaches $1$ copy of the node $0$ to the root, giving $+(0)(0)$.

Second, cut the head of $+(0(1))$ at step $1$.
The node $\varepsilon$ is the node $0$, and the copy of $0(1)$ gets the labels $u - 1 = 0$ and $0$, so the hydra becomes $+(0(0(0)))$.
Its value $\psi_0(\omega) = \omega^\omega$ is far below the value $\psi_0(\Omega_1) = \varepsilon_0$ of $+(0(1))$.

## History

Wilfried Buchholz introduced the labeled hydras in 1987, in the paper "An independence result for $(\Pi^1_1\text{-}\mathsf{CA}) + \mathsf{BI}$".
He used them to give a combinatorial statement that is true and independent of this subsystem of second-order arithmetic.
Masahiro Hamano and Mitsuhiro Okada later gave a direct independence proof for the game on finite labeled trees.

## Explanations

### L1 human

A Buchholz hydra is a tree with numbers written on its nodes, and Hercules cuts its heads one by one.
Cutting a head can make the tree much larger, as for the ordinary hydra.
A head with a number $u$ larger than $0$ is replaced by a copy of a large part of the tree, with the number lowered to $u - 1$.
In spite of this, every battle ends with the root alone.
The proof needs very large infinite numbers, and strong systems of axioms cannot carry it out.

### L2 human

We follow the values of the hydras in the small battle above, with Buchholz's functions $\psi_\nu$ from the [[proof outline|YYQ76F4812]].
A node with label $\nu$ and children of values $\alpha_1, \dots, \alpha_j$ is worth $\psi_\nu(\alpha_1 + \cdots + \alpha_j)$, and the root takes the sum.
So $R_3 = +(0(\omega))$ is worth
$$\psi_0(\psi_\omega(0)) = \psi_0(\Omega_\omega).$$
After step $1$ the hydra $+(0(2))$ is worth $\psi_0(\Omega_2)$, the Bachmann-Howard ordinal, which is smaller.
After step $2$ the hydra $+(0(1(0)))$ is worth $\psi_0(\psi_1(1))$, smaller again.

A label is not the size of a node: lowering a label from $\omega$ to $2$ is a large drop in value, even though the tree did not change shape.
This is the typical use of the game: it is a concrete descending sequence through a large ordinal notation system.

### L3 human

Buchholz hydras are the trees of the terms of his notation system for the collapsing functions $\psi_\nu$ with $\nu \le \omega$.
The rules of the game follow the fundamental sequences of these terms, so a battle is a descending sequence below the [[Takeuti-Feferman-Buchholz ordinal|S5FTQGHVKC]].
This ordinal is the [[proof-theoretic ordinal|C72RBH0CDR]] of $(\Pi^1_1\text{-}\mathsf{CA}) + \mathsf{BI}$, which is why the termination escapes this system.
The [[theories of iterated inductive definitions|5VNT564Y2W]] have ordinals of the same kind, and the game is a standard example in [[ordinal analysis|C5E5TG8PGP]].
