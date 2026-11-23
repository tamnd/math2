---
tag: 1DMFNR7FZT
kind: statement
role: theorem
name: Kripke completeness of GL
msc: ["03B45", "03F45"]
topics: [3E7M66WW6Q]
audience: research
uses: [61THBNS8WE, QQ6PZFGGB3, NGHWZ9Y7ZV, 0GJZW9JFZQ, 0DQPNJNPYK, SC0BSJ3GT6, JWC9CE07Q2]
about: [WJK0YA4GP2, NGHWZ9Y7ZV]
proofs: [HQYKDFW4VS]
history:
  first_stated: "Segerberg, 1971, An essay in classical modal logic"
  notes: "Completeness of GL for finite transitive irreflexive frames."
sources:
  - url: https://en.wikipedia.org/wiki/Kripke_semantics
    locator: Correspondence and completeness
  - url: https://en.wikipedia.org/wiki/Provability_logic
    locator: lead section
  - url: https://builds.openlogicproject.org/
    locator: Modal Logic
---

## Statement

Every formula that $\mathsf{GL}$ does not prove is refuted on a small finite frame whose arrows compose and never loop, so $\mathsf{GL}$ is decidable.

Let $\mathsf{GL}$ be the modal logic of the [[definition of provability logic|61THBNS8WE]].
A frame $(W, R)$ is finite transitive irreflexive when $W$ is finite, $R$ is [[transitive|0GJZW9JFZQ]], and no $w$ has $w R w$.
For every modal formula $\varphi$, the following are equivalent.

1. $\mathsf{GL} \vdash \varphi$.
2. $\varphi$ is valid on every frame $(W, R)$ with $R$ transitive and conversely [[well-founded|0DQPNJNPYK]].
3. $\varphi$ is valid on every finite transitive irreflexive frame.
4. $\varphi$ is valid on every transitive irreflexive frame with at most $2^n$ worlds, where $n$ is the number of subformulas of $\varphi$.

Validity on a frame is defined in [[Kripke semantics|NGHWZ9Y7ZV]], and converse well-foundedness in [[Löb's axiom in provability logic|QQ6PZFGGB3]].
The proof is in [[the proof of the Kripke completeness of GL|HQYKDFW4VS]].

## Remarks

### A countermodel in practice

We show that $\mathsf{GL} \nvdash \square(p \vee q) \to (\square p \vee \square q)$.
Take the frame with worlds $1$, $2$, $3$ and the arrows $1 R 2$ and $1 R 3$ only, which is finite, transitive and irreflexive.
Put $p$ true only at $2$, and $q$ true only at $3$.
The successors of $1$ are $2$ and $3$, and $p \vee q$ is true at both, so $1 \models \square(p \vee q)$.
But $1 \not\models \square p$, since $p$ is false at $3$, and $1 \not\models \square q$, since $q$ is false at $2$.
So the formula fails at $1$, and by the soundness direction $\mathsf{GL}$ does not prove it.
This is the typical use of the theorem: to show $\mathsf{GL} \nvdash \varphi$, give one finite transitive irreflexive countermodel.

### Why each hypothesis is needed

Transitivity cannot be dropped from item 3.
The frame $a R b$, $b R c$ is finite and irreflexive, and it refutes Löb's axiom, as [[Löb's axiom in provability logic|QQ6PZFGGB3]] shows.
Irreflexivity cannot be dropped either, since the one-world frame with $a R a$ is finite and transitive, and it refutes Löb's axiom.
Finiteness matters too.
The frame $(\mathbb{N}, <)$ is transitive and irreflexive, and it refutes Löb's axiom because it is not conversely well-founded.

### Weak, not strong, completeness

The theorem is about single formulas, and it fails for infinite sets.
Consider the following set of formulas:
$$\Gamma = \{ \lozenge p_0 \} \cup \{ \square(p_i \to \lozenge p_{i+1}) : i \in \mathbb{N} \}.$$
Each finite part of $\Gamma$ is true at the root of a finite chain, with $p_i$ true at the $i$-th world after the root, so $\Gamma$ is consistent with $\mathsf{GL}$.
But a world that makes all of $\Gamma$ true sees a $p_0$-world, which sees a $p_1$-world, and so on, by transitivity.
That is an infinite chain, which no conversely well-founded frame has, so $\mathsf{GL}$ is not compact.
For the same reason the canonical model of $\mathsf{GL}$ is not a frame of $\mathsf{GL}$, since otherwise $\Gamma$ would be true at one of its worlds.

### What it gives you

The theorem gives the finite model property: if $\mathsf{GL} \nvdash \varphi$, then $\varphi$ fails at a world of a finite model of $\mathsf{GL}$.
It gives decidability, because by item 4 we only need to check the finitely many frames with at most $2^n$ worlds and all valuations of the variables of $\varphi$.
The problem "$\mathsf{GL} \vdash \varphi$" is even in PSPACE.
The countermodel of the proof has chains of length at most the number of boxed subformulas of $\varphi$, so a depth-first search for it needs only polynomial space.
The problem is also [[PSPACE-complete|JWC9CE07Q2]], and we cite the hardness without proof.
Together with [[Solovay's theorem|1ZRWVDYPX0]], the theorem decides which schemes $\mathsf{PA}$ proves about its own provability.

### Watch out

The canonical model method of basic modal logic does not work for $\mathsf{GL}$, as the set $\Gamma$ shows.
A proof that builds one model for all consistent sets at once must fail, so the proof has to build a separate finite model for each formula.

### The converse

The direction from item 1 to item 2 is soundness, and it holds by part 3 of [[Löb's axiom in provability logic|QQ6PZFGGB3]].
The direction from item 3 to item 1 is the completeness.
So the theorem is an equivalence, and its converse is part of it.

### Generalizations

$\mathsf{GL}$ is also complete for finite transitive irreflexive trees, by unraveling a finite countermodel into a tree.
[[Grzegorczyk logic|2Q8E4GQF3B]] is complete for finite partial orders, by a similar finite construction.
Polymodal analogues fail, since [[Japaridze's polymodal logic GLP|3EDRQJJHMT]] is not complete for any class of Kripke frames.

## History

Krister Segerberg proved the completeness of $\mathsf{GL}$ for finite transitive irreflexive frames in his 1971 work "An essay in classical modal logic".
The finite construction of the proof is the standard one in Boolos's book "The Logic of Provability".

## Explanations

### L1 human

A modal formula is a theorem of $\mathsf{GL}$ exactly when it holds in every finite diagram of points and arrows where the arrows never loop and always compose.
For example, $\square p \to p$ fails on the diagram with one point and no arrow, so it is not a theorem.
Since we can list all small diagrams, a computer can decide whether a formula is a theorem.

### L2 human

Is $\square(\square p \to q) \vee \square(\square q \to p)$ a theorem of $\mathsf{GL}$?
This is the linearity axiom, and a frame that branches should refute it.
Take worlds $1$, $2$, $3$ with $1 R 2$ and $1 R 3$, and put $p$ true only at $3$ and $q$ true only at $2$.
At $2$, there are no successors, so $\square p$ is true and $q$ is true, and $\square p \to q$ holds.
At $3$, the formula $\square p$ is true and $q$ is false, so $\square p \to q$ fails, and $1 \not\models \square(\square p \to q)$.
In the same way $\square q \to p$ fails at $2$, so $1 \not\models \square(\square q \to p)$.
So the disjunction fails at $1$, and $\mathsf{GL}$ does not prove it.
The search for a countermodel is the whole decision procedure, and the theorem guarantees that a small one exists whenever the formula is not a theorem.

### L3 human

The proof is a filtration-style construction: maximal consistent sets are taken only inside the finite set of subformulas of $\varphi$, and the relation is chosen so that it is transitive and irreflexive by design.
The failure of compactness separates $\mathsf{GL}$ from the canonical logics of the [[modal logic|C3RZY20ETK]] foundations.
It is the same phenomenon as the failure of compactness for well-foundedness in first-order logic.
Arithmetically, the finite frames of this theorem are the input of Solovay's construction, which turns each finite countermodel into sentences of arithmetic.
