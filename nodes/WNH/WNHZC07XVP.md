---
tag: WNHZC07XVP
kind: conjecture
name: Feder–Vardi dichotomy conjecture
msc: ["68Q25", "08A70"]
uses: [MJF9M19E3E, KBXSZC6BV1]
sources:
  - url: https://en.wikipedia.org/wiki/Constraint_satisfaction_problem
history:
  posed_by: Tomás Feder and Moshe Y. Vardi
  first_stated: "1993"
---

## Statement

Let $\mathbb{B}$ be a finite [[relational structure|MJF9M19E3E]] with finitely many relations.
The problem $\mathrm{CSP}(\mathbb{B})$ takes as input a finite structure $\mathbb{A}$ of the same signature.
It asks whether there is a [[homomorphism|KBXSZC6BV1]] from $\mathbb{A}$ to $\mathbb{B}$.
The conjecture states that every such constraint satisfaction problem $\mathrm{CSP}(\mathbb{B})$ is either solvable in polynomial time or NP-complete.

## Remarks

The conjecture is now a theorem: it follows from the [[CSP dichotomy theorem|ZA4YXJ9T1P]], proved independently by Andrei Bulatov and by Dmitriy Zhuk.
It is not a consequence of general complexity theory.
By Ladner's theorem, if $\mathrm{P} \ne \mathrm{NP}$ then NP contains problems that are neither in P nor NP-complete.
Feder and Vardi studied a logically defined fragment of NP called monotone monadic SNP, defined by three syntactic restrictions.
They showed that its problems are equivalent to fixed-template CSPs.
They also showed that dropping any one of the three restrictions gives a class that contains, up to polynomial-time equivalence, every problem in NP.
So, assuming $\mathrm{P} \ne \mathrm{NP}$, a dichotomy can only hold for the restricted class, and CSPs are its natural representatives.
Before the proof, the conjecture was known for structures with a two-element domain (Schaefer), for undirected graphs (Hell and Nešetřil), and for three-element domains (Bulatov).

## Explanations

### L1 human

Fix a finite set of labels and a finite list of rules saying which combinations of labels are allowed.
The task is then: given a finite input, can its points be labelled so that every rule is obeyed?
Feder and Vardi guessed that each such task is either easy, with a fast algorithm, or as hard as the hardest problems in NP.
There would be no task of intermediate difficulty in this family, even though such tasks exist elsewhere in NP if P differs from NP.
