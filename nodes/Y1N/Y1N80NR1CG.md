---
tag: Y1N80NR1CG
kind: definition
name: Priority method
msc: [03D25, 03D28]
defines: 3BZFSC5QZ2
uses: [TN9G24VABN, KZSB5E471K]
sources:
  - url: https://en.wikipedia.org/wiki/Turing_degree
---

## Definition

A *finite-injury priority construction* builds sets $A \subseteq \N$ by a computable process in stages $s = 0, 1, 2, \ldots$, as follows.

1. The goal is a list of *requirements* $R_0, R_1, R_2, \ldots$, and $R_i$ has *higher priority* than $R_j$ when $i < j$.
2. At each stage $s$, finitely many numbers are added to the finite approximation $A_s$, so $A_0 \subseteq A_1 \subseteq \cdots$ and $A = \bigcup_s A_s$ is [[computably enumerable|TN9G24VABN]].
3. At a stage, an action taken for $R_i$ may undo the work done for some $R_j$ with $j > i$; then $R_j$ is *injured* and starts again.
4. An action for $R_j$ never injures any $R_i$ with $i < j$.

The construction is *finite-injury* if each requirement is injured only finitely often and acts only finitely often.
The *priority method* is the use of such constructions to prove the existence of computably enumerable sets with given properties.
It also covers extensions in which requirements may be injured infinitely often.

## Remarks

Example: the proof of the [[Friedberg–Muchnik theorem|RA358M9QCN]] is a finite-injury construction with requirements $A \ne \Phi_e^B$ and $B \ne \Phi_e^A$.
By induction on $i$, after some stage no requirement before $R_i$ acts, so $R_i$ is injured only finitely often and is met.

Non-example: a construction of $A$ that at each stage asks whether a given program halts is not a priority construction in this sense.
It is not a computable process, so it does not make $A$ computably enumerable.

The proof that a finite-injury construction succeeds is usually an induction on the priority order.
Infinite-injury methods, such as those used for the Sacks density theorem, allow some requirements to be injured infinitely often.
