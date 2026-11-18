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

A filtration shrinks a [[Kripke model|NGHWZ9Y7ZV]] $\mathfrak{M}$ to a model with at most $2^{|\Sigma|}$ worlds.
Here $\Sigma$ is a finite set of formulas closed under subformulas.
We identify worlds that agree on every formula of $\Sigma$.
Then we choose a relation on the classes between a smallest and a largest admissible relation.
The [[filtration theorem|T99DK51S0W]] says that each formula of $\Sigma$ keeps its truth value.
Filtration is the main method to prove the [[finite model property|3NT8RCA6HE]] and hence the decidability of modal logics.

## Motivation

The canonical model of a logic refutes every non-theorem, but it is uncountable.
A decision procedure needs a bound: if $\varphi$ fails somewhere, it should fail in a model whose size depends on $\varphi$ only.
A formula $\varphi$ can only see the formulas in $\operatorname{Sub}(\varphi)$, and there are finitely many truth patterns on that set.
So worlds with the same pattern can be merged, provided the relation between the merged worlds is chosen with care.

## Notation

Let $\mathfrak{M} = (W, R, V)$ be a model and $\Sigma$ a set of [[modal formulas|G8VGTW9P4F]] closed under subformulas.

1. $w \sim_\Sigma v$ when $\mathfrak{M}, w \models \varphi \iff \mathfrak{M}, v \models \varphi$ for every $\varphi \in \Sigma$; this is an [[equivalence relation|0G8VEZ3WTK]], and $[w]$ is the class of $w$.
2. $W_\Sigma = \set{[w] : w \in W}$, and $V^f(p) = \set{[w] : w \in V(p)}$ for $p \in \Sigma$; other variables get $V^f(p) = \emptyset$.
3. A relation $R^f$ on $W_\Sigma$ is a filtration of $R$ through $\Sigma$ when it satisfies two conditions. Condition (min) says that $w R v$ implies $[w] R^f [v]$. Condition (max) says that $[w] R^f [v]$ implies that $\mathfrak{M}, w \models \square\varphi$ gives $\mathfrak{M}, v \models \varphi$ for each $\square\varphi \in \Sigma$.
4. Then $\mathfrak{M}^f = (W_\Sigma, R^f, V^f)$ is a filtration of $\mathfrak{M}$ through $\Sigma$.
5. The smallest filtration $R^s$: $[w] R^s [v]$ iff $w' R v'$ for some $w' \sim_\Sigma w$ and $v' \sim_\Sigma v$.
6. The largest filtration $R^l$: $[w] R^l [v]$ iff $\mathfrak{M}, w \models \square\varphi$ implies $\mathfrak{M}, v \models \varphi$ for each $\square\varphi \in \Sigma$.
7. The transitive filtration $R^t$: $[w] R^t [v]$ iff $\mathfrak{M}, w \models \square\varphi$ implies $\mathfrak{M}, v \models \square\varphi \wedge \varphi$ for each $\square\varphi \in \Sigma$.

The conditions are named (min) and (max) in Blackburn, de Rijke and Venema; Chellas and Segerberg use other letters.

## Remarks

### Examples

1. The successor model on $\N$ with $p$ true at the even numbers filters through $\set{p, \square p}$ to two worlds, see [[the successor model|42QZ2YBM2R]].
2. The failure of axiom $\mathrm{4}$ at $0$ in a successor model becomes a failure in a 3-world model, see [[the countermodel for axiom 4|VK1RP97KKY]].
3. If all worlds of $\mathfrak{M}$ agree on $\Sigma$, then $W_\Sigma$ has one world, $R^s$ is a loop when $R \neq \emptyset$, and $R^s$ is empty when $R = \emptyset$.

### Non-examples

1. Merging worlds that agree on the variables only, and not on all of $\Sigma$, does not give a filtration, see [[the collapsing example|CYP4SYP20S]].
2. For a transitive $R$, the smallest filtration need not be transitive, so it is not a filtration that stays inside $\mathsf{K4}$-frames, see [[the transitive example|V0J3A9Q4SY]].

### Basic properties

1. $|W_\Sigma| \le 2^{|\Sigma|}$, since a class is determined by the set of formulas of $\Sigma$ true at its members.
2. $R^s$ and $R^l$ are filtrations, $R^s \subseteq R^f \subseteq R^l$ for every filtration $R^f$, and every relation between $R^s$ and $R^l$ is a filtration, see [[the filtration theorem|T99DK51S0W]].
3. If $R$ is reflexive, every filtration is reflexive, by (min). If $R$ is serial, every filtration is serial.
4. If $R$ is symmetric, then $R^s$ is symmetric.
5. If $R$ is transitive, then $R^t$ is a filtration and it is transitive.
6. If $R$ is an equivalence relation, then the relation "$w$ and $v$ agree on all $\square\varphi \in \Sigma$" is a filtration and an equivalence relation.

### History

McKinsey's proof of 1941 that $\mathsf{S2}$ and $\mathsf{S4}$ are decidable used finite algebras, the algebraic form of filtration.
Lemmon in 1966 and Segerberg in 1968 developed the relational form.
Segerberg's An essay in classical modal logic of 1971 made it a standard tool.

### Common errors

1. Using a set $\Sigma$ that is not closed under subformulas; then the induction of the filtration theorem breaks.
2. Expecting a filtration to preserve every frame property; the smallest filtration of a transitive frame can fail to be transitive.
3. Forgetting that formulas outside $\Sigma$ can change their truth value in $\mathfrak{M}^f$.

## Explanations

### L1 human

Imagine a huge map of possible situations.
For a fixed question, many situations look the same, because they give the same answers to the few things the question mentions.
A filtration glues such situations together.
The glued map is small, and it still gives the same answers to the question.

### L2 human

We filter a model of $\mathsf{T}$ and keep it reflexive.

1. Take $W = \N$, $R = \le$, $V(p) = \set{0}$, and $\Sigma = \set{p, \square p}$.
2. $p$ is true only at $0$, and $\square p$ is true nowhere, since every $n$ sees $n + 1 \ge 1$.
3. So the classes are $A = \set{0}$ and $B = \set{n : n \ge 1}$.
4. $R^s$ has $(A, A)$, $(A, B)$ and $(B, B)$, the images of the pairs $(0, 0)$, $(0, 1)$ and $(1, 1)$.
5. $R^s$ is reflexive, and $\square p$ is false at $A$ and $B$, as in $\mathfrak{M}$.

The typical use is to keep the frame property of the logic while making the model finite.
A trap: the choice of the relation matters; the right choice depends on the property to keep.

### L3 human

Algebraically, a filtration through $\Sigma$ is a finite subalgebra of the complex algebra generated by the sets $[\![\varphi]\!]$, $\varphi \in \Sigma$.
This subalgebra has an operator that agrees with $\lozenge$ where $\Sigma$ needs it.
Selective filtrations, which choose a subset of worlds instead of a quotient, give the finite model property of logics such as $\mathsf{S4.3}$ and $\mathsf{GL}$.
With [[Harrop's theorem|VSYQ1AZ9G7]], a filtration argument for a finitely axiomatized logic gives a decision procedure.
The size bound $2^{|\Sigma|}$ gives an upper bound on its complexity.
