---
tag: 1H650VRZVT
kind: definition
name: Algebraic approach to constraint satisfaction
msc: [08A70, 68Q25]
defines: 3EH4F5H7FT
uses: [A0K9EZRM7E, PTKR703G6A, 052JJ9YVNM, BQ0AC9QX7E]
sources:
  - url: https://en.wikipedia.org/wiki/Constraint_satisfaction_problem
---

## Definition

Let $\mathbb{A} = (A; R_1, \dots, R_k)$ be a relational structure with a finite nonempty universe $A$ and finitely many relations.
The *constraint satisfaction problem* $\operatorname{CSP}(\mathbb{A})$ is the following decision problem.
The input is a finite relational structure $\mathbb{X}$ with relations of the same arities.
The question is whether there is a homomorphism from $\mathbb{X}$ to $\mathbb{A}$, a map preserving each relation.
The *polymorphism clone* of $\mathbb{A}$ is the [[clone|PTKR703G6A]] $\operatorname{Pol}(\mathbb{A})$ of all operations on $A$ that are [[polymorphisms|A0K9EZRM7E]] of every $R_i$.
The *algebraic approach* is the study of the computational complexity of $\operatorname{CSP}(\mathbb{A})$ through the algebra $(A; \operatorname{Pol}(\mathbb{A}))$.

## Remarks

The approach rests on a reduction principle.
If $\mathbb{A}$ and $\mathbb{B}$ share the universe $A$ and $\operatorname{Pol}(\mathbb{A}) \subseteq \operatorname{Pol}(\mathbb{B})$, then $\operatorname{CSP}(\mathbb{B})$ reduces to $\operatorname{CSP}(\mathbb{A})$ in polynomial time.
The reason is that each relation of $\mathbb{B}$ is then primitive positive definable from $\mathbb{A}$, by the [[Pol–Inv Galois connection|BQ0AC9QX7E]].
Example: for the complete graph $K_2$, $\operatorname{CSP}(K_2)$ asks whether a graph is $2$-colourable, as a [[graph homomorphism|052JJ9YVNM]] to $K_2$.
The majority operation on $\set{0, 1}$ is a polymorphism of the edge relation $\set{(0, 1), (1, 0)}$, and the problem is in polynomial time.
Non-example of tractability: every polymorphism of $K_3$ has the form $\sigma(x_i)$ for a permutation $\sigma$ of $\set{0, 1, 2}$.
So $K_3$ has no Taylor polymorphism, and $3$-colouring is NP-complete.
