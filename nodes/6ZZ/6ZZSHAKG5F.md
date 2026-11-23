---
tag: 6ZZSHAKG5F
kind: concept
name: Filtration
msc: ["03B45"]
topics: [SKY7AQFG1V]
audience: grad
uses: [NGHWZ9Y7ZV, G8VGTW9P4F, 0G8VEZ3WTK]
sources:
  - url: https://en.wikipedia.org/wiki/Kripke_semantics
    locator: Finite model property
  - url: https://builds.openlogicproject.org/
    locator: Boxes and Diamonds, chapter on filtrations and decidability
---

## Summary

A filtration cuts an infinite [[Kripke model|NGHWZ9Y7ZV]] down to a finite one that agrees with it on a chosen finite set of formulas.

Here is the first case to keep in mind.
Take the successor model on $\mathbb{N}$: the worlds are $0, 1, 2, \dots$, each $n$ sees only $n + 1$, and $p$ is true at the even numbers.
Let $\Sigma = \{ p, \square p \}$, a set of $n = 2$ formulas closed under subformulas.
At an even world $p$ is true and $\square p$ is false, because the next world is odd.
At an odd world $p$ is false and $\square p$ is true.
So every world has one of only two truth patterns on $\Sigma$, and we merge the worlds into two classes, $E$ for the evens and $O$ for the odds.
We let $E$ see $O$ and $O$ see $E$, because $0$ sees $1$ and $1$ sees $2$.
In this two-world model, $p$ and $\square p$ have the same truth values as in the infinite one.
In general there are at most $2^n$ truth patterns on $n$ formulas, so the quotient never has more than $2^n$ worlds.

The [[filtration theorem|T99DK51S0W]] says that this works for every model and every finite $\Sigma$ closed under subformulas, provided the relation on the classes is chosen between a smallest and a largest admissible relation.
Filtration is the main method for proving the [[finite model property|3NT8RCA6HE]] and hence the decidability of modal logics.

## Motivation

The [[canonical model|TVE4F04KME]] of a logic refutes every non-theorem, but it has uncountably many worlds.
A decision procedure needs a bound: if $\varphi$ fails somewhere, it should fail in a model whose size depends only on $\varphi$.
A formula $\varphi$ can only see its own subformulas, and there are finitely many truth patterns on that set.
So worlds with the same pattern can be merged, provided the relation between the merged worlds is chosen with care.

## Notation

Let $\mathfrak{M} = (W, R, V)$ be a model and let $\Sigma$ be a set of [[modal formulas|G8VGTW9P4F]] closed under subformulas.
We write $w \sim_\Sigma v$ when $w$ and $v$ make the same formulas of $\Sigma$ true.
This is an [[equivalence relation|0G8VEZ3WTK]], and $[w]$ is the class of $w$.
The set of classes is $W_\Sigma = \{ [w] : w \in W \}$, and the valuation is $V^f(p) = \{ [w] : w \in V(p) \}$ for $p \in \Sigma$ and $V^f(p) = \emptyset$ for other variables.

A relation $R^f$ on $W_\Sigma$ is a filtration of $R$ through $\Sigma$ when it satisfies two conditions.
Condition (min) says that $w R v$ implies $[w] R^f [v]$.
Condition (max) says that if $[w] R^f [v]$ and $\square\varphi \in \Sigma$ is true at $w$, then $\varphi$ is true at $v$.
The model $\mathfrak{M}^f = (W_\Sigma, R^f, V^f)$ is then a filtration of $\mathfrak{M}$ through $\Sigma$.

Three filtrations have names.
The smallest filtration $R^s$ puts $[w] R^s [v]$ when $w' R v'$ for some $w' \sim_\Sigma w$ and $v' \sim_\Sigma v$.
The largest filtration $R^l$ puts $[w] R^l [v]$ when every $\square\varphi \in \Sigma$ true at $w$ has $\varphi$ true at $v$.
The transitive filtration $R^t$, due to Lemmon, puts $[w] R^t [v]$ when every $\square\varphi \in \Sigma$ true at $w$ has both $\square\varphi$ and $\varphi$ true at $v$.
The names (min) and (max) follow Blackburn, de Rijke and Venema, and Chellas and Segerberg use other letters.

## Remarks

### Worked cases

The successor model of the summary is worked out in full in [[the successor model example|42QZ2YBM2R]], which also shows that the smallest and largest filtrations differ there.
The failure of axiom $\mathrm{4}$ at $0$ in a successor model becomes a failure in a 3-world model in [[the countermodel for axiom 4|VK1RP97KKY]].
If all worlds of $\mathfrak{M}$ agree on $\Sigma$, then $W_\Sigma$ has one world, and $R^s$ is a loop when $R$ is nonempty and empty when $R$ is empty.

### What is not a filtration

Merging worlds that agree on the variables only, and not on all of $\Sigma$, does not give a filtration, as [[the collapsing example|CYP4SYP20S]] shows.
For a transitive $R$, the smallest filtration need not be transitive, so it can leave the class of $\mathsf{K4}$ frames, as [[the transitive example|V0J3A9Q4SY]] shows.

### The rules you can use

A class is determined by the set of formulas of $\Sigma$ that are true at its members, so $W_\Sigma$ has at most $2^{\lvert \Sigma \rvert}$ elements.
$R^s$ and $R^l$ are filtrations, every filtration lies between them, and every relation between them is a filtration.
If $R$ is reflexive or serial, then so is every filtration, by (min).
If $R$ is symmetric, then $R^s$ is symmetric.
If $R$ is transitive, then $R^t$ is a filtration and it is transitive.
If $R$ is an equivalence relation, then the relation "$w$ and $v$ agree on all $\square\varphi \in \Sigma$" is a filtration and an equivalence relation.

### Watch out

The set $\Sigma$ must be closed under subformulas, or the induction in the filtration theorem breaks.
A filtration need not keep every frame property: the smallest filtration of a transitive frame can fail to be transitive.
And formulas outside $\Sigma$ can change their truth value in $\mathfrak{M}^f$, so the theorem promises nothing about them.

### History

McKinsey's proof of 1941 that $\mathsf{S2}$ and $\mathsf{S4}$ are decidable used finite algebras, the algebraic form of filtration.
Segerberg's An Essay in Classical Modal Logic of 1971 developed the relational form for many logics and made it a standard tool.

### Try it

First, filter the model $W = \mathbb{N}$, $R = {\le}$, $V(p) = \{ 0 \}$ through $\Sigma = \{ p, \square p \}$, and check that the smallest filtration is reflexive.
Here $p$ is true only at $0$, and $\square p$ is true nowhere, since every $n$ sees $n + 1 \geq 1$.
So the classes are $A = \{ 0 \}$ and $B = \{ n : n \geq 1 \}$, and $R^s = \{ (A, A), (A, B), (B, B) \}$, the images of the pairs $(0, 0)$, $(0, 1)$ and $(1, 1)$.
It is reflexive, and $\square p$ is false at $A$ and at $B$, as in $\mathfrak{M}$.

Second, what is the largest possible number of worlds in a filtration through the subformulas of $\square(p \to q)$?
The subformulas are $p$, $q$, $p \to q$ and $\square(p \to q)$, so the bound is $2^4 = 16$.

## Explanations

### L1 human

Imagine a huge map of possible situations.
For a fixed question, many situations look the same, because they give the same answers to the few things the question mentions.
A filtration glues such situations together.
The glued map is small, and it still gives the same answers to the question.

### L2 human

The typical use is to keep the frame property of a logic while making the model finite.
For $\mathsf{T} = \mathsf{KT}$ and $\mathsf{D} = \mathsf{KD}$ any filtration works, since reflexivity and seriality pass through (min).
For $\mathsf{K4}$ and $\mathsf{S4} = \mathsf{KT4}$ we use the transitive filtration $R^t$.
For $\mathsf{S5} = \mathsf{KT5}$ we use the relation that compares the boxed formulas of $\Sigma$.
Watch out: the choice of the relation matters, and the right choice depends on the property to keep.

### L3 human

Algebraically, a filtration through $\Sigma$ gives a finite subalgebra of the complex algebra, generated by the sets $[\![\varphi]\!]$ for $\varphi \in \Sigma$, with an operator that agrees with $\lozenge$ where $\Sigma$ needs it.
Selective filtrations choose a subset of worlds instead of a quotient, and they give the finite model property of logics such as $\mathsf{S4.3}$ and $\mathsf{GL}$.
With [[Harrop's theorem|VSYQ1AZ9G7]], a filtration argument for a finitely axiomatized logic gives a decision procedure.
The size bound $2^{\lvert \Sigma \rvert}$ also bounds the cost of that procedure, though the best bounds come from other methods, as in [[the complexity theorem|1P2B0C7CQ4]].
