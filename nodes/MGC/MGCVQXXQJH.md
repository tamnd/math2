---
tag: MGCVQXXQJH
kind: definition
name: Lindenbaum–Tarski algebra
msc: ["03G05", "03B05"]
topics: [QYA4H5Y7VR]
audience: grad
defines: QC9M3Q8B8Q
uses: [09K9MWD2QQ, 1MGMQX43B8, 0G8VEZ3WTK, 0011MTQMR6, 0XADJKM699]
sources:
  - url: https://en.wikipedia.org/wiki/Lindenbaum–Tarski_algebra
    locator: lead section
  - url: https://plato.stanford.edu/entries/logic-algebraic-propositional/
    locator: "5. The algebraic counterparts of classical and intuitionistic logic"
---

## Definition

Let $P$ be a nonempty set of propositional variables.
Let $F$ be the set of formulas of classical [[propositional logic|09K9MWD2QQ]] over $P$ built with $\neg$ and $\to$.
Write $\vdash$ for derivability in the [[Hilbert system L|1MGMQX43B8]], and use the abbreviations
$$\varphi \lor \psi := \neg \varphi \to \psi, \quad \varphi \land \psi := \neg(\varphi \to \neg \psi), \quad \top := p_0 \to p_0, \quad \bot := \neg \top,$$
for a fixed variable $p_0 \in P$.
Let $T \subseteq F$ be a theory.
For $\varphi, \psi \in F$, put $\varphi \sim_T \psi$ if $T \vdash \varphi \to \psi$ and $T \vdash \psi \to \varphi$.
This is an [[equivalence relation|0G8VEZ3WTK]] on $F$; write $[\varphi]$ for the class of $\varphi$.
The *Lindenbaum-Tarski algebra* of $T$ is the [[quotient set|0011MTQMR6]] $F / {\sim_T}$ with the operations
$$\neg [\varphi] = [\neg \varphi], \quad [\varphi] \to [\psi] = [\varphi \to \psi], \quad [\varphi] \wedge [\psi] = [\varphi \wedge \psi], \quad [\varphi] \vee [\psi] = [\varphi \vee \psi],$$
and the constants $0 = [\bot]$ and $1 = [\top]$.

## Notation

Write $\mathbf{L}_T$ or $F/{\sim_T}$ for the algebra, and $[\varphi]_T$ when the theory must be shown.
The order is $[\varphi] \le [\psi]$ iff $T \vdash \varphi \to \psi$.

## Remarks

The operations are well defined, and the result is a [[Boolean algebra|0XADJKM699]]; both facts are proved in [[the Lindenbaum-Tarski theorem|~b1e6292b]].
The same construction works for any language with the connectives taken as primitive; the algebras that result are isomorphic.

Example: for $P = \set{p}$ and $T = \emptyset$, every formula is equivalent to one of $\bot$, $p$, $\neg p$, $\top$, and no two of these are equivalent, as their truth tables differ.
So the algebra is the four-element Boolean algebra with atoms $[p]$ and $[\neg p]$.

## Explanations

### L1 human

Take all formulas, and put two formulas in the same box when the theory proves each from the other.
The boxes are the elements of the algebra.
The connectives act on boxes, because equivalent inputs give equivalent outputs.
With one variable there are four boxes.

### L2 human

1. Take $T = \set{p}$ over $P = \set{p}$.
2. Then $T \vdash \top \to p$, because $p \in T$ and $p \to (\top \to p)$ is an instance of axiom A1.
3. Also $T \vdash p \to \top$, by axiom A1 and $\vdash \top$.
4. So $[p] = 1$, and $[\neg p] = 0$.
5. The algebra has two elements.

The trap: the relation needs both implications; one implication gives only the order $\le$.

### L3 human

The definition is the special case for classical logic of the quotient of the formula algebra by the Leibniz congruence of a theory.
For logics with a good implication, this congruence is "provably equivalent", as here.
For other logics the Leibniz congruence is the right replacement; see [[the Leibniz hierarchy|~5cf31243]].
