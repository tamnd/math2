---
tag: VSYQ1AZ9G7
kind: statement
role: theorem
name: Harrop's theorem
msc: ["03B45", "03B25"]
topics: [SKY7AQFG1V]
audience: grad
uses: [3NT8RCA6HE, K12PSCFX3Y, JS8W7PA6JK, E87G6ZTMTN, MWSD85BB4X, HWC687ES0Q]
about: [3NT8RCA6HE]
proofs: [88X6NP6478]
sources:
  - url: https://en.wikipedia.org/wiki/Kripke_semantics
    locator: Finite model property
  - url: https://builds.openlogicproject.org/
    locator: Boxes and Diamonds, chapter on filtrations and decidability
---

## Statement

Let $\Lambda = \mathsf{K}\Gamma$ be a [[normal modal logic|JS8W7PA6JK]] axiomatized by a finite set $\Gamma$ of formulas.
If $\Lambda$ has the [[finite model property|3NT8RCA6HE]], then $\Lambda$ is decidable: there is an algorithm that, given $\varphi$, decides whether $\Lambda \vdash \varphi$.

A more general form also holds.
If $\Lambda$ is recursively axiomatized and the finite $\Lambda$-frames form a [[computably enumerable|MWSD85BB4X]] set of frames that refute every non-theorem, then $\Lambda$ is decidable.

The proof is in [[the proof of Harrop's theorem|88X6NP6478]].

## Remarks

### Why each hypothesis is needed

1. The FMP is needed. Isard proved in 1977 that some finitely axiomatized normal modal logic is undecidable, so a finite axiomatization alone is not enough.
2. The finite axiomatization is needed. There are $2^{\aleph_0}$ normal logics with the FMP. Examples are the logics of the sets of frames from an infinite antichain of finite frames. There are only countably many algorithms. So some logics with the FMP are undecidable.
3. The FMP must be in the frame form of [[the definition|K12PSCFX3Y]], or be known to be equivalent to it. With a finite model of the axioms only, we cannot check that the model validates all theorems. The reason is that the set of formulas true in a model is not closed under substitution.

### Consequences

1. $\mathsf{K}$, $\mathsf{T}$, $\mathsf{D}$, $\mathsf{K4}$, $\mathsf{S4}$, $\mathsf{B}$ and $\mathsf{S5}$ are decidable, by [[the finite model property theorem|XNPJK6B921]].
2. $\mathsf{GL}$ is decidable, since it is finitely axiomatized and complete for finite strict orders, see [[Kripke completeness of GL|1DMFNR7FZT]].
3. A search through finite frames finds countermodels, see [[the Harrop search|XQ8W9DEBD2]].

### Generalizations

1. The theorem holds for any logic whose theorems and whose finite models can be listed by an algorithm, for example intermediate propositional logics. Harrop's paper treats propositional calculi in general.
2. When the FMP has a computable bound $f$, the algorithm needs no search for proofs: it tests the finite $\Lambda$-frames with at most $f(|\varphi|)$ worlds.

## History

Harrop proved the theorem in 1958, in a paper on finite models and decision procedures for propositional calculi.
In modal logic it became the standard route to decidability after Segerberg's work on filtration around 1970.

## Explanations

### L1 human

Two searches run side by side.
One search lists all proofs, and it stops when it finds a proof of the statement.
The other lists all small finite pictures that obey the laws, and it stops when one of them refutes the statement.
The finite model property guarantees that one of the two searches stops.

### L2 human

We see the two searches for $\mathsf{K4}$ and the formula $\square p \to p$.

1. $\mathsf{K4} = \mathsf{K}\set{\square p \to \square\square p}$, a finite axiomatization.
2. The search through finite frames tests each finite frame for axiom $\mathrm{4}$, which means that it checks every valuation of $p$.
3. The frame with one world and no arrows passes the test, since every box is true there.
4. On it, with $p$ false, $\square p$ is true and $p$ is false, so $\square p \to p$ fails.
5. The search stops, and the answer is $\mathsf{K4} \nvdash \square p \to p$.

The typical use is a proof of decidability without any analysis of the complexity.
A trap: the frame test must check the axioms under all valuations, not under one.

### L3 human

The theorem shows that a logic with the FMP is co-computably enumerable as soon as its finite frames are effectively recognizable.
Finite axiomatization gives both halves.
The proof gives no bound on the running time.
A bound needs a computable bound on the size of countermodels, as in [[the finite model property theorem|XNPJK6B921]].
