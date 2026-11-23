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
If $\Lambda$ has the [[finite model property|3NT8RCA6HE]], then $\Lambda$ is [[decidable|HWC687ES0Q]]: there is an algorithm that, given $\varphi$, decides whether $\Lambda \vdash \varphi$.

A more general form also holds.
If $\Lambda$ is recursively axiomatized and there is a [[computably enumerable|MWSD85BB4X]] list of finite $\Lambda$-frames that refutes every non-theorem, then $\Lambda$ is decidable.

The proof is in [[the proof of Harrop's theorem|88X6NP6478]].

## Remarks

### Why each hypothesis is needed

The FMP is needed.
Some finitely axiomatized normal modal logics are undecidable, so a finite axiomatization alone is not enough.

The finite axiomatization is needed.
There are $2^{\aleph_0}$ normal logics with the FMP, for example the logics of different sets of frames drawn from a suitable infinite family of finite frames.
There are only countably many algorithms, so some logics with the FMP are undecidable.

The FMP must be in the frame form of [[the definition|K12PSCFX3Y]], or be known to be equivalent to it.
With a finite model of the axioms only, we cannot check that the model makes all theorems true, because the set of formulas true in a model is not closed under substitution.
Validity on the frame is closed under substitution, and that is what the proof checks.

### What it gives you

$\mathsf{K}$, $\mathsf{T} = \mathsf{KT}$, $\mathsf{D} = \mathsf{KD}$, $\mathsf{K4}$, $\mathsf{S4} = \mathsf{KT4}$, $\mathsf{B} = \mathsf{KTB}$ and $\mathsf{S5} = \mathsf{KT5}$ are decidable, by [[the finite model property theorem|XNPJK6B921]].
$\mathsf{GL}$ is decidable, since it is finitely axiomatized and complete for finite strict orders, by [[Kripke completeness of GL|1DMFNR7FZT]].
The search through finite frames finds concrete countermodels, as in [[the Harrop search|XQ8W9DEBD2]].

### The converse

The converse fails.
A decidable logic need not have the FMP, and a decidable logic need not be finitely axiomatized.
The theorem gives one sufficient condition for decidability, not a characterization.

### Generalizations

The theorem holds for any logic whose theorems and whose finite countermodels can be listed by an algorithm, for example intermediate propositional logics, and Harrop's paper treats propositional calculi in general.
When the FMP has a computable bound $f$, the algorithm needs no search for proofs: it tests the finite $\Lambda$-frames with at most $f(\lvert \varphi \rvert)$ worlds.

## History

Harrop proved the theorem in 1958, in a paper on finite models and decision procedures for propositional calculi.
Segerberg's An Essay in Classical Modal Logic of 1971 combined it with filtration to decide many modal logics.

## Explanations

### L1 human

Two searches run side by side.
One search lists all proofs, and it stops when it finds a proof of the statement.
The other lists all small finite pictures that obey the laws, and it stops when one of them refutes the statement.
The finite model property guarantees that one of the two searches stops.

### L2 human

We watch the two searches for $\mathsf{K4}$ and the formula $\square p \to p$.
$\mathsf{K4}$ is $\mathsf{K}$ plus the single axiom $\square p \to \square\square p$, a finite axiomatization.
The search through finite frames tests each finite frame for axiom $\mathrm{4}$, which means that it checks every valuation of $p$.
The frame with one world and no arrows passes the test, since every box is true there.
On it, with $p$ false, $\square p$ is true and $p$ is false, so $\square p \to p$ fails.
The search stops, and the answer is $\mathsf{K4} \nvdash \square p \to p$.
The typical use is a proof of decidability without any analysis of the complexity.
Watch out: the frame test must check the axioms under all valuations, not under one.

### L3 human

The theorem shows that the non-theorems of a logic with the FMP form a computably enumerable set as soon as its finite frames can be recognized effectively.
A finite axiomatization gives both halves: the theorems are listed by proofs, and the frames are recognized by checking finitely many axioms.
The proof gives no bound on the running time, and a bound needs a computable bound on the size of countermodels, as in [[the finite model property theorem|XNPJK6B921]].
