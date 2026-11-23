---
tag: C028FF4TWM
kind: statement
role: theorem
name: Kirby-Paris hydra
msc: ["03F30", "03F15", "05C05"]
topics: [T6FK1E7GJ1]
audience: grad
uses: [0C9J6W2A8A, 0YSCSX5YZC, 6GD30FGYDZ, KT50SMH3EC, MPSCREYC3M, Z742YPHPNS]
about: [MPSCREYC3M, KT50SMH3EC]
history:
  first_stated: "1982"
  notes: "Kirby and Paris introduced the hydra game in 'Accessible independence results for Peano arithmetic', Bull. London Math. Soc. 14 (1982)."
sources:
  - url: https://en.wikipedia.org/wiki/Hydra_game
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Hydra_game
    locator: Kirby–Paris and Buchholz hydras
---

## Statement

A path of three edges, cut by the standard rule below, grows to nine nodes and still dies after $37$ cuts.
The theorem says that every hydra dies in this way, and that Peano arithmetic cannot prove it.

A *hydra* is a finite [[rooted tree|0C9J6W2A8A]].
Its *heads* are the leaves other than the root, and the hydra is *dead* when it is the root alone.
A *battle* has steps $n = 1, 2, 3, \dots$.
At step $n$ Hercules chooses a head $h$ and a number $N_n \ge 0$, and $p$ denotes the parent of $h$.

1. If $p$ is the root, the head $h$ is removed.
2. Otherwise let $g$ be the parent of $p$. The head $h$ is removed, and then $N_n$ copies of the subtree rooted at $p$ are attached to $g$ as new children.

A *strategy* is a rule that chooses $h$ and $N_n$ from the battle so far.
The *standard battle* uses $N_n = n$ and always cuts the rightmost head, where new copies are drawn to the right.
Let $\mathrm{Hydra}(k)$ be the number of steps of the standard battle that starts with a path of $k$ edges.

**Theorem** (Kirby and Paris).

1. Every battle ends: for every hydra and every strategy, the hydra is dead after finitely many steps.
2. The function $\mathrm{Hydra}$ eventually dominates every function that [[Peano arithmetic|MPSCREYC3M]] $\mathsf{PA}$ proves total.
3. So $\mathsf{PA}$ does not prove that the standard battle kills every hydra, and hence it does not prove that every recursive strategy kills every hydra.
4. $\mathsf{PA}$ plus transfinite induction up to [[epsilon nought|KT50SMH3EC]] $\varepsilon_0$ proves that the standard battle kills every hydra.

The [[proof|EDZN6B9AWQ]] proves parts 1 and 4 in full and derives part 3 from part 2, which it cites.

## Remarks

### A first battle

Take the path $r - a - b - c$ with root $r$ and one head $c$.
Each node gets an ordinal: a leaf gets $0$, and a node gets the natural sum of $\omega^{\beta}$ over the values $\beta$ of its children.
So $b$ is worth $1$, $a$ is worth $\omega$, and the hydra is worth $\omega^\omega$.

At step $1$ we cut $c$.
Its parent $b$ becomes a leaf, and $N_1 = 1$ copy of $b$ grows on $a$, so $a$ has two leaves:
$$o = \omega^{1 \# 1} = \omega^2.$$
At step $2$ we cut a leaf of $a$.
Now $a$ keeps one leaf, and $2$ copies of $a$ grow on $r$, so $r$ has three children with one leaf each:
$$o = \omega \cdot 3.$$
At step $3$ we cut the head of the rightmost child.
That child becomes a leaf, and $3$ copies of it grow on $r$:
$$o = \omega \cdot 2 + 4.$$
Steps $4$ to $7$ remove the four leaves on $r$, and $o = \omega \cdot 2$.
Step $8$ turns one more child into a leaf and adds $8$ copies, so $o = \omega + 9$, and steps $9$ to $17$ remove these leaves.
Step $18$ gives $19$ leaves on $r$, and steps $19$ to $37$ remove them.
So $\mathrm{Hydra}(3) = 37$.

### Why it ends, and why that is hard to prove

The ordinal went down at every step, even when the tree grew from $4$ nodes to $9$.
This is the whole proof of part 1: a cut turns one term $\omega^{\beta + 1}$ at the grandparent into finitely many terms $\omega^\beta$, and any finite number of these is smaller.
A strictly decreasing sequence of ordinals is finite, so the battle ends.

The proof uses ordinals up to $\varepsilon_0$.
For $k \ge 2$ the path of $k$ edges has the ordinal $\omega^{\omega^{\cdot^{\cdot^{\omega}}}}$ with $k - 1$ letters $\omega$, and these ordinals tend to $\varepsilon_0$.
$\mathsf{PA}$ proves transfinite induction up to each ordinal below $\varepsilon_0$, but not up to $\varepsilon_0$ itself.
Part 2 turns this limit into growth: the battles last longer than any function that $\mathsf{PA}$ proves total can predict.

### Why each hypothesis is needed

The theory in part 3 is $\mathsf{PA}$.
The stronger theory of part 4, and also $\mathsf{ZFC}$, proves that every battle ends.

The copies grow on the grandparent $g$, one level nearer to the root.
If they grew on $p$ itself with $N_n \ge 1$, then $p$ would gain at least as many leaves as it loses, and on a path of two edges the battle would never end.

The strategy in part 3 is recursive.
The phrase "every strategy" quantifies over arbitrary functions, and it is not a sentence of first-order arithmetic.
The hydra is finite, since on an infinite tree Hercules can cut heads for ever.

### What it gives you

The standard battle gives $\mathrm{Hydra}(0) = 0$, $\mathrm{Hydra}(1) = 1$, $\mathrm{Hydra}(2) = 3$ and $\mathrm{Hydra}(3) = 37$.
The value $\mathrm{Hydra}(4)$ is far too large to write out in decimal digits.
Part 1 holds for every choice of the numbers $N_n$, however large, so only the shape of the tree decides that the battle ends.
Parts 2 and 3 give one more true statement that $\mathsf{PA}$ does not prove, next to [[Goodstein's theorem|XQMNJF241J]].

### The converse and the generalizations

The converse question asks whether the hydra can win.
By part 1 it cannot: no strategy of Hercules, however bad, keeps a hydra alive for ever.

The [[Buchholz hydra|9APRFM0G7F]] puts labels on the nodes, and its proof needs ordinals up to the [[Takeuti-Feferman-Buchholz ordinal|S5FTQGHVKC]].
[[Beklemishev's worm principle|MHDZGDNEPS]] is a game on words with the same ordinal $\varepsilon_0$, and $\mathsf{PA}$ does not prove it either.

### Watch out

The number of nodes is not a measure that goes down.
In the first battle it goes from $4$ to $4$, then to $7$, then to $9$.
Only the ordinal goes down.

The ordinal must use the natural sum $\#$, not the ordinary sum.
With the ordinary sum, a root with children of values $0$ and $1$ would be worth $1 + \omega = \omega$ in one order and $\omega + 1$ in the other.
The natural sum gives $\omega + 1$ in both orders, so the value does not depend on how we draw the tree.

### Try it

First, check $\mathrm{Hydra}(2) = 3$.
Step $1$ cuts the head of the path $r - p - h$ and grows one copy of $p$ on $r$, giving two leaves; steps $2$ and $3$ remove them.

Second, find the ordinal of a root with two children, one a leaf and one with two leaves, and the ordinal after step $1$ cuts a head of the second child.
Before the cut it is $\omega^2 + 1$, after it the root has two children with one leaf each and one leaf, so it is $\omega \cdot 2 + 1$, which is smaller.

## History

Laurence Kirby and Jeff Paris introduced the hydra game in 1982, in the paper "Accessible independence results for Peano arithmetic" in the Bulletin of the London Mathematical Society.
In the same paper they proved that $\mathsf{PA}$ does not prove [[Goodstein's theorem|XQMNJF241J]].

## Explanations

### L1 human

A hydra is a tree drawn upside down, and its heads are the ends of the branches.
Hercules cuts one head at each step.
The hydra then grows new copies of a part of itself, and more copies at each later step.
Even so, Hercules always wins, and after enough steps only the root is left.
For a path with three edges the standard battle takes $37$ steps.
For a path with four edges it takes so many steps that no computer could ever count them.

### L2 human

We check $\mathrm{Hydra}(2) = 3$ with the ordinals of the [[proof|EDZN6B9AWQ]].
The hydra is the path $r - p - h$, and its ordinal is $\omega^{\omega^0} = \omega$.
At step $1$ we cut $h$.
Its parent $p$ is not the root, so $p$ becomes a leaf and $1$ copy of $p$ grows on $r$:
$$o = \omega^0 \# \omega^0 = 2.$$
Steps $2$ and $3$ cut the two leaves of $r$, and the ordinal goes $2, 1, 0$.

The ordinal fell from $\omega$ to $2$ in one step, although the number of heads went from $1$ to $2$.
This is the typical use of the idea: to show that a process ends, attach to each state an ordinal that strictly decreases.

### L3 human

The hydras code the ordinals below $\varepsilon_0$: a root with subtrees $T_1, \dots, T_j$ has the ordinal $\omega^{o(T_1)} \# \cdots \# \omega^{o(T_j)}$.
Every ordinal below $\varepsilon_0$ is the ordinal of some hydra, and the standard battle follows the fundamental sequences of the [[Hardy hierarchy|X8RKXQASR9]].
This is why the length of the battle grows like $H_{\varepsilon_0}$, a function of the order of $f_{\varepsilon_0}$ in the [[fast-growing hierarchy|R6ZC4BJGXV]], and outgrows the [[provably total functions|Z742YPHPNS]] of $\mathsf{PA}$.
The same idea with labeled trees and collapsing functions gives the [[Buchholz hydra|9APRFM0G7F]], which measures much stronger subsystems of [[second-order arithmetic|DC60FYCSPM]].
