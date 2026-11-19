---
tag: AN8J46ZCD2
kind: statement
role: theorem
name: Rieger-Nishimura theorem on one-variable formulas
aliases: [classification-of-one-variable-intuitionistic-formulas]
msc: ["03B55", "06D20"]
topics: [38EQ20GR7M]
audience: research
uses: [5GTQ69W47T, 480TCT5CJ9, MGCVQXXQJH, GTS4DRRMZR]
about: [KAB6KM98ZZ]
proofs: [1ECGA3GKRC]
sources:
  - url: https://plato.stanford.edu/entries/logic-intuitionistic/
    locator: 6.1 Subintuitionistic and Intermediate Logics
  - url: https://eprints.illc.uva.nl/id/document/492
    locator: Section 3.6, Definition 37 and Theorem 38
---

## Statement

Let $p$ be a propositional variable.
Define Nishimura's formulas by $F_0 = p \wedge \neg p$, $F_1 = p$, $F_2 = \neg p$, $F_\infty = p \to p$, and for $n \geq 0$
$$F_{2n+3} = F_{2n+1} \vee F_{2n+2}, \qquad F_{2n+4} = F_{2n+3} \to F_{2n+1}.$$
For $k \geq 0$ put $I_k = \set{0, \dots, k - 1}$ and $J_k = I_k \cup \set{k + 1}$, subsets of $\mathbb{N}$.
Let $t(F_0) = I_0$, $t(F_{2n+1}) = I_{n+1}$, $t(F_{2n+2}) = J_n$ and $t(F_\infty) = \mathbb{N}$.

**Theorem.**

1. Every formula $\varphi$ whose only variable is $p$ is $\mathsf{IPC}$-equivalent to some $F_m$, with $m \in \mathbb{N} \cup \set{\infty}$.
2. For all $m, m' \in \mathbb{N} \cup \set{\infty}$, $\mathsf{IPC} \vdash F_m \to F_{m'}$ iff $t(F_m) \subseteq t(F_{m'})$.
3. In particular the formulas $F_m$ are pairwise not equivalent, and the [[Lindenbaum algebra|MGCVQXXQJH]] of $\mathsf{IPC}$ in one variable is infinite.

## Remarks

### Why each hypothesis is needed

The theorem is about one variable.
With two variables the free Heyting algebra is far more complex, and its dual is the 2-universal model rather than a ladder.
The equivalence is that of $\mathsf{IPC}$.
In $\mathsf{CPC}$ every one-variable formula is equivalent to $\bot$, $p$, $\neg p$ or $\top$, so the list collapses to four classes.

### Consequences

1. The [[free Heyting algebra|GTS4DRRMZR]] on one generator is the [[Rieger-Nishimura lattice|KAB6KM98ZZ]], with the order of part 2.
2. Whether $\mathsf{IPC} \vdash \varphi$ for a one-variable $\varphi$ can be decided. Compute its truth set from those of its subformulas, using the operations on the sets $I_k$, $J_k$ and $\mathbb{N}$, and test whether it is $\mathbb{N}$.
3. $F_{2n+1}$ and $F_{2n+2}$ are incomparable for every $n$; for example $p$ and $\neg p$, or $p \vee \neg p$ and $\neg \neg p$.

### Converse

Part 2 is an equivalence.
Its "only if" direction is soundness on the ladder, and its "if" direction is the universality of the ladder.

### Generalizations

For $n$ variables, the formulas up to equivalence correspond to definable up-sets of the $n$-universal model.
Bezhanishvili and de Jongh describe these models; only for one variable is the result a simple ladder.

## History

The lattice is named after Rieger and Nishimura.
Nishimura's description of the formulas appeared in 1960.

## Explanations

### L1 human

Take all statements you can build from one letter $p$, using "and", "or", "if then" and "not".
Classically you only get four different meanings.
Intuitionistically you get infinitely many, but they are very orderly.
Each one is equivalent to a rung of a ladder, and the rungs are listed by a simple rule.

### L2 human

1. Take $\varphi = \neg p \vee \neg \neg p$.
2. In the ladder, $\neg p$ holds only at $1$, and $\neg \neg p$ holds at $0$ and $2$.
3. So the truth set of $\varphi$ is $\set{0, 1, 2} = I_3$.
4. $I_3 = t(F_5)$, so $\varphi$ is equivalent to $F_5 = (p \vee \neg p) \vee ((p \vee \neg p) \to p)$.
5. $F_6$ has truth set $J_2 = \set{0, 1, 3}$, and $I_3 \not\subseteq J_2$, so $\mathsf{IPC} \nvdash \varphi \to F_6$.

The typical use is a quick decision procedure for one-variable formulas.
A trap: the formulas $F_m$ are not the shortest ones.
$F_4$ is $(p \vee \neg p) \to p$, which is equivalent to $\neg \neg p$.

### L3 human

The theorem computes the free Heyting algebra on one generator, which is the first nontrivial case of the free algebras of the variety.
Its dual is the ladder, the 1-universal model, and the proof is a universality argument: every finite one-variable model maps onto a generated submodel of the ladder by a p-morphism.
The same pattern, a universal model with p-morphisms into it, underlies the Jankov-de Jongh formulas and the $n$-universal models.
For an intermediate logic $L$, the one-variable Lindenbaum algebra of $L$ is a quotient of this lattice.
It is finite as soon as $L$ proves a one-variable formula that $\mathsf{IPC}$ does not prove.
