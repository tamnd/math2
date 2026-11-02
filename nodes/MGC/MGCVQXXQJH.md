---
tag: MGCVQXXQJH
kind: definition
name: Lindenbaum–Tarski algebra
msc: ["03G05", "03B05"]
defines: QC9M3Q8B8Q
uses: [09K9MWD2QQ, 0G8VEZ3WTK, 0011MTQMR6, 0XADJKM699]
sources:
  - url: https://en.wikipedia.org/wiki/Lindenbaum–Tarski_algebra
---

## Definition

Let $P$ be a set of propositional variables.
Let $F$ be the set of formulas of classical [[propositional logic|09K9MWD2QQ]] over $P$ built with $\wedge$, $\vee$, $\neg$, $\top$ and $\bot$.
Let $T \subseteq F$ be a theory.
For $\varphi, \psi \in F$, put $\varphi \sim_T \psi$ if $T \vdash \varphi \leftrightarrow \psi$.
This is an [[equivalence relation|0G8VEZ3WTK]] on $F$; write $[\varphi]$ for the class of $\varphi$.
The *Lindenbaum–Tarski algebra* of $T$ is the [[quotient set|0011MTQMR6]] $F / {\sim_T}$ with the operations
$$[\varphi] \wedge [\psi] = [\varphi \wedge \psi], \quad [\varphi] \vee [\psi] = [\varphi \vee \psi], \quad \neg [\varphi] = [\neg \varphi],$$
and the constants $0 = [\bot]$ and $1 = [\top]$.

## Remarks

The operations are well defined because provable equivalence is compatible with the connectives, and the result is a [[Boolean algebra|0XADJKM699]].
Its order is given by $[\varphi] \le [\psi]$ if and only if $T \vdash \varphi \to \psi$.

Example: for $P = \set{p}$ and $T = \emptyset$, every formula is equivalent to one of $\bot$, $p$, $\neg p$, $\top$, and no two of these are equivalent, as their truth tables differ.
So the algebra is the four-element Boolean algebra with atoms $[p]$ and $[\neg p]$.

Non-example: identify formulas only when they are equal as strings.
Then the classes $[p \wedge q]$ and $[q \wedge p]$ differ, so $\wedge$ is not commutative and the result is not a Boolean algebra.

The same construction for intuitionistic logic gives a Heyting algebra.
A theory $T$ is consistent if and only if $0 \ne 1$ in its algebra.
