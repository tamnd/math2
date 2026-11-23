---
tag: 3NT8RCA6HE
kind: concept
name: Finite model property
msc: ["03B45", "03B25"]
topics: [SKY7AQFG1V]
audience: grad
uses: [K12PSCFX3Y, JS8W7PA6JK, 6ZZSHAKG5F, T99DK51S0W, NGHWZ9Y7ZV]
sources:
  - url: https://en.wikipedia.org/wiki/Kripke_semantics
    locator: Finite model property
  - url: https://builds.openlogicproject.org/
    locator: Boxes and Diamonds, chapter on filtrations and decidability
---

## Summary

A [[normal modal logic|JS8W7PA6JK]] has the finite model property when every formula it does not prove fails on some finite frame of the logic.

Here is a first case.
$\mathsf{K}$ does not prove axiom $\mathrm{4}$, $\square p \to \square\square p$.
The frame with arrows $0 \to 1 \to 2 \to 2$ and $p$ true only at $1$ refutes it at $0$: $\square p$ holds there, because $1$ has $p$, while $\square\square p$ fails, because $\square p$ fails at $1$.
Three worlds are enough, and every frame is a $\mathsf{K}$-frame.
The finite model property says that a finite witness like this exists for every non-theorem.

[[The definition|K12PSCFX3Y]] makes this exact, and an equivalent form says that the logic is the set of formulas valid on some class of finite frames.
For the basic logics the property is proved by [[filtration|6ZZSHAKG5F]], and together with a finite axiomatization it gives decidability, by [[Harrop's theorem|VSYQ1AZ9G7]].

## Motivation

Completeness for a class of frames tells us where to look for countermodels, but the countermodels built from the canonical model are huge.
A computer cannot search through infinite models.
If every non-theorem has a finite countermodel on a frame of the logic, then the non-theorems can be listed by a search through finite frames.
The theorems can be listed by a search through proofs, and the two searches together decide the logic.

## Notation

FMP abbreviates the finite model property.
We write $\operatorname{Log}(\mathsf{C})$ for the set of formulas valid on every frame of a class $\mathsf{C}$, and $\mathsf{C}_{\mathrm{fin}}$ for the class of finite frames in $\mathsf{C}$.
A logic has the $f$-bounded FMP when its countermodels can be chosen with at most $f(\lvert \varphi \rvert)$ worlds, and for $f(n) = 2^n$ some books speak of the exponential FMP.

## Remarks

### Where the property holds

$\mathsf{K}$, $\mathsf{T} = \mathsf{KT}$, $\mathsf{D} = \mathsf{KD}$, $\mathsf{K4}$, $\mathsf{S4} = \mathsf{KT4}$, $\mathsf{B} = \mathsf{KTB}$ and $\mathsf{S5} = \mathsf{KT5}$ have the FMP, with countermodels of at most $2^n$ worlds for a formula with $n$ subformulas, by [[the finite model property theorem|XNPJK6B921]].
The countermodel in the summary comes from filtering an infinite model, as in [[the countermodel for axiom 4|VK1RP97KKY]].
The McKinsey formula $\square\lozenge p \to \lozenge\square p$ fails on a 2-world $\mathsf{S4}$-frame, which a finite search finds, as in [[the Harrop search|XQ8W9DEBD2]].
$\mathsf{GL}$ has the FMP, since it is complete for finite transitive irreflexive frames, by [[Kripke completeness of GL|1DMFNR7FZT]].
Every tabular logic, such as $\mathsf{K} + \square\bot$, has the FMP.

### Where it fails

First-order logic has no analogue of the property, since a sentence can have only infinite models, as [[the serial strict order|VF0M5JS8EK]] shows.
Makinson found in 1969 a normal modal logic between $\mathsf{T}$ and $\mathsf{S4}$ without the FMP.
A [[Kripke incomplete|W67YJQTT50]] logic has no FMP, since a logic with the FMP is the logic of a class of frames.

### The rules you can use

The FMP implies Kripke completeness, since the logic is the logic of its finite frames.
A finitely axiomatized normal logic with the FMP is decidable, by [[Harrop's theorem|VSYQ1AZ9G7]].
There are $2^{\aleph_0}$ normal logics with the FMP and only countably many decidable logics, so the FMP alone does not give decidability.
Bull proved in 1966 that every normal extension of $\mathsf{S4.3}$ has the FMP.
The FMP of $\Lambda$ also says that every formula consistent with $\Lambda$ is satisfiable on a finite $\Lambda$-frame, which is the form used in satisfiability algorithms.

### Watch out

A finite model is not the same as a finite frame.
A finite model can make every theorem of $\Lambda$ true while its frame does not validate $\Lambda$, so the definition asks for the frame.

The FMP does not by itself give an efficient algorithm.
The size bound can be exponential, while the true complexity can be lower, as in [[the complexity theorem|1P2B0C7CQ4]].

Harrop's theorem needs a finite axiomatization, or at least a way to recognize the finite frames of the logic.

### History

McKinsey proved in 1941 that $\mathsf{S2}$ and $\mathsf{S4}$ have finite algebraic countermodels for their non-theorems, which gave the first decidability results by finite models in modal logic.
Harrop's paper of 1958 isolated the link between finite models and decision procedures.
Segerberg's An Essay in Classical Modal Logic of 1971 proved the FMP for many logics by filtration.
Makinson's example of 1969 showed that the property can fail.

### Try it

First, does $\mathsf{T}$ prove $\lozenge\square p \to \square p$?
No: take the reflexive frame with worlds $a$ and $b$, arrows $a \to a$, $b \to b$ and $a \to b$, and $p$ true only at $b$.
At $a$, $\lozenge\square p$ holds via $b$, and $\square p$ fails because $a$ sees itself.

Second, why does the FMP imply Kripke completeness?
If $\Lambda \nvdash \varphi$, some finite $\Lambda$-frame refutes $\varphi$, so $\Lambda$ is exactly the logic of its finite frames.

## Explanations

### L1 human

Some rule books for "necessarily" have a useful feature.
Whenever a statement does not follow from the rules, a small finite picture shows it.
Then a computer can settle every question: it searches for a proof and for a small picture at the same time, and one of the two searches succeeds.

### L2 human

We see why $\mathsf{S5}$ has the FMP with a very small bound.
Let $\mathsf{S5} \nvdash \varphi$.
By completeness, $\varphi$ fails at a world $w$ of a universal model.
For each subformula $\square\psi$ of $\varphi$ that is false in this model, pick a world where $\psi$ fails.
Keep $w$ and the picked worlds, with the universal relation on them.
A true box stays true on fewer worlds, and a false box keeps its witness, so every subformula keeps its value, by induction on subformulas.
So $\varphi$ fails in a universal model with at most $1 + m$ worlds, where $m$ is the number of boxed subformulas.
Watch out: the induction needs witnesses for all false boxes, not only the outer ones.

### L3 human

For a normal logic, the FMP says that the variety of its modal algebras is generated by its finite members.
The FMP gives decidability only together with an effective description of the finite $\Lambda$-frames, which a finite axiomatization provides.
Large families of logics have the FMP at once: Fine proved in 1985 that every subframe logic above $\mathsf{K4}$ has it.
