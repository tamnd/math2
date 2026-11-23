---
tag: Q5MT8WY7JM
kind: concept
name: Weak theories of arithmetic
aliases: [weak-arithmetic, essentially-undecidable-weak-theories]
msc: ["03F30", "03B25"]
topics: [QHCRN4JVG0]
audience: research
uses: [3K1AKGXF8A, HWC687ES0Q, 92SWXST1ZM, X9WYNYE29C]
sources:
  - url: https://en.wikipedia.org/wiki/Decidability_(logic)
    locator: Decidability of a theory
  - url: https://en.wikipedia.org/wiki/Robinson_arithmetic
  - book: isbn:9780521857840
---

## Summary

A weak theory of arithmetic knows almost nothing, yet it already makes every consistent extension of itself undecidable.
Picture a theory that only knows the addition and multiplication tables, such as $\overline{2} + \overline{3} = \overline{5}$ and $\overline{2} \cdot \overline{3} = \overline{6}$, that distinct numerals are distinct, and how each element compares with each numeral.
It proves no general law, not even $\forall x\,(x + 0 = x)$.
This theory is $\mathsf{R}$, and no algorithm decides its theorems or the theorems of any consistent theory that contains it.

Exactly, a [[theory|92SWXST1ZM]] $T$ is essentially undecidable when $T$ is consistent and every consistent theory $T' \supseteq T$ in the language of $T$ is [[undecidable|HWC687ES0Q]].
The weak theories of arithmetic are the essentially undecidable theories that sit far below [[Peano arithmetic|HACXBCM7SS]].
The standard ones are [[Robinson arithmetic|3K1AKGXF8A]] $\mathsf{Q}$, the theory $\mathsf{R}$ of Tarski, Mostowski and Robinson, and Grzegorczyk's theory of concatenation $\mathsf{TC}$.

## Motivation

The [[incompleteness theorems|X9WYNYE29C]] seem to depend on arithmetic: numbers code formulas, and the theory must prove facts about the codes.
So one asks what is really needed: induction, multiplication, infinitely many axioms, or numbers at all.
Each weak theory answers one part of the question.
$\mathsf{Q}$ shows that induction is not needed.
$\mathsf{R}$ shows that no general law such as commutativity is needed.
$\mathsf{TC}$ shows that numbers are not needed, since strings with concatenation suffice.

Weak theories also give a cheap tool for proving undecidability.
If a consistent theory interprets an essentially undecidable theory, then it is undecidable.
To show that the theory of some structure is undecidable, you interpret $\mathsf{Q}$ or $\mathsf{R}$ in it.

## Notation

We write $\mathsf{Q}$, $\mathsf{R}$ and $\mathsf{TC}$ for the three standard theories.
For theories in the same language, $T \subseteq T'$ means that every theorem of $T$ is a theorem of $T'$.
Some books call an essentially undecidable theory "essentially incomplete" when the extensions are taken to be recursively axiomatized.

## Remarks

### Three theories at the bottom

[[The theory R|W0ST3STV51]] has five axiom schemas about numerals, such as $\overline{n} + \overline{m} = \overline{n + m}$ and $\forall x\,(x \le \overline{n} \lor \overline{n} \le x)$.
Every finite part of it has a finite model, so $\mathsf{R}$ is not finitely axiomatizable.

$\mathsf{Q}$ has eight axioms and no induction.
It proves every axiom of $\mathsf{R}$, when $x \le y$ is read as $x < y \lor x = y$, so $\mathsf{R} \subseteq \mathsf{Q} \subseteq \mathsf{PA}$.

[[The theory TC|KAA92JQ7TH]] speaks about strings over a two-letter alphabet, with concatenation as its only operation and five axioms.
For example, its standard model glues $\mathtt{ab}$ and $\mathtt{ba}$ into $\mathtt{abba}$.

For $\mathsf{Q}$ and $\mathsf{R}$, essential undecidability follows from the [[representability of recursive functions|BJF29XET83]].
For $\mathsf{TC}$ it needs a separate argument, because the coding of sequences and computations has to be done with strings.

### What is not essentially undecidable

[[Presburger arithmetic|4W0E9G7PPV]] is weak in that it has no multiplication, but it is complete and decidable.
So it is its own decidable consistent extension, and [[it is not essentially undecidable|GBA8FSMWKN]].

The theory of groups is undecidable, but the theory of abelian groups extends it and is decidable.
So the theory of groups is not essentially undecidable either.
Undecidable and essentially undecidable are different properties.

### The first properties

A consistent theory that contains an essentially undecidable theory in the same language is again essentially undecidable, because its consistent extensions are extensions of the smaller theory.
An essentially undecidable theory is incomplete, and so is each of its consistent recursively axiomatized extensions.
The reason is that a complete recursively axiomatized theory is decidable.
If a finitely axiomatized essentially undecidable theory $T$ is consistent with a theory $T'$ in a common language, then $T'$ is undecidable.
This is why $\mathsf{Q}$, being finite, is more useful as a tool than $\mathsf{R}$.

### Watch out

Do not think that a weak theory must be decidable.
$\mathsf{R}$ cannot prove $\forall x\,(x + 0 = x)$, and it is still essentially undecidable.

Do not think either that interpreting $\mathsf{Q}$ makes a theory strong.
It makes the theory undecidable, and incomplete when it is recursively axiomatized, but it may still prove very few general laws.

### History

Tarski, Mostowski and Robinson developed essentially undecidable theories and the method of interpretations in their book Undecidable Theories of 1953, with $\mathsf{Q}$ and $\mathsf{R}$ as their main tools.
Robinson had introduced $\mathsf{Q}$ in 1950.
Grzegorczyk introduced $\mathsf{TC}$ in 2005, under the slogan of undecidability without arithmetization, and proved it undecidable.
Grzegorczyk and Zdanowski then proved that $\mathsf{TC}$ is essentially undecidable.

### Try it

First, is the complete theory of $(\mathbb{N}, 0, S, +, \cdot, <)$ essentially undecidable?
Yes: it is consistent, it contains $\mathsf{Q}$, and its only consistent extension in the same language is itself, which is undecidable.

Second, why does every finite part of $\mathsf{R}$ have a finite model, while $\mathsf{Q}$ has none?
A finite part mentions finitely many numerals, so numbers up to a large $k$, with sums and products capped at $k$, satisfy it.
$\mathsf{Q}$ makes $S$ injective with $0$ outside its range, which no finite set allows.

## Explanations

### L1 human

Gödel showed that strong theories of arithmetic always leave some questions open.
Logicians then asked how weak such a theory can be and still have this problem.
The answer is: very weak.
A theory that only knows facts such as $2 + 3 = 5$, $2 \cdot 3 = 6$ and "every number at most $3$ is $0$, $1$, $2$ or $3$" already has the problem.
Even a theory about strings of letters, with no numbers at all, has it.

### L2 human

We show that the theory of groups is undecidable but not essentially undecidable.
Tarski proved that the theory of groups is undecidable.
The theory of abelian groups adds the axiom $\forall x\, \forall y\,(x y = y x)$, and it has models, so it is a consistent extension in the same language.
Szmielew proved that the theory of abelian groups is decidable.
So the theory of groups has a consistent decidable extension, and it is not essentially undecidable.
The typical use of weak theories runs the other way: to show a theory undecidable, interpret $\mathsf{Q}$ or $\mathsf{R}$ in it.
The trap is the language, since essential undecidability is about extensions in the same language.

### L3 human

Current research compares weak theories by interpretability, which preorders theories by strength.
$\mathsf{Q}$ and $\mathsf{TC}$ are mutually interpretable, so they have the same strength in this sense.
$\mathsf{R}$ is strictly weaker than $\mathsf{Q}$ in this order.
An interpretation of $\mathsf{Q}$ in $\mathsf{R}$ would use finitely many axioms of $\mathsf{R}$, and these have a finite model, which would then give a finite model of $\mathsf{Q}$.
Weak theories also measure the cost of coding.
In $\mathsf{Q}$ the coding of sequences needs the [[β-function|BM6P0C2AC2]], while in $\mathsf{TC}$ strings are themselves sequences.
Weak set theories, such as adjunctive set theory, also interpret $\mathsf{Q}$, and the [[Σ1-completeness of Q|69234Z1V00]] is the property that the incompleteness theorems use.
