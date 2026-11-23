---
tag: 6CCK0TT69P
kind: concept
name: Friedman's A-translation
msc: ["03F25", "03F30", "03F55"]
topics: [8XY7JYZKFW]
audience: grad
uses: [Q11N8X99FK, PAQ4ZX2TX1, RXHJPVMPJH, 0QFT7Z76N5, HGJVM49PA4, NCDZ969V7X]
sources:
  - url: https://en.wikipedia.org/wiki/Friedman_translation
    locator: Definition
  - url: https://en.wikipedia.org/wiki/Friedman_translation
    locator: Application
  - url: https://en.wikipedia.org/wiki/Heyting_arithmetic
    locator: Conservativity
---

## Summary

Friedman's A-translation takes an intuitionistic proof that "a counterexample is impossible" and turns it into a proof that names an actual witness.
It does this by replacing falsity $\bot$, everywhere in the proof, by the very statement we want to prove.

Let $A$ be a formula of a first-order language with $\bot$.
For a formula $B$ whose bound variables are not free in $A$, the *A-translation* $B^A$ is obtained from $B$ by replacing each atomic subformula $P$, including $\bot$, by $P \vee A$.
Its main property is that if [[Heyting arithmetic|RXHJPVMPJH]] proves $B$, then HA proves $B^A$, for every formula $A$.
After the [[double-negation translation|HGJVM49PA4]], this turns a classical proof of a $\Pi^0_2$ sentence into an intuitionistic one.

## Motivation

Take the $\Pi^0_2$ sentence $\forall x\, \exists y\, (x < y)$ and suppose we only know that [[Peano arithmetic|0QFT7Z76N5]] proves it.
The negative translation gives HA a proof of
$$\neg \forall y\, \neg (x < y), \quad \text{that is,} \quad \forall y\, (x < y \to \bot) \to \bot.$$
This names no $y$, and [[intuitionistic logic|Q11N8X99FK]] has no general rule that removes the double negation.

Friedman's idea is to choose $A = \exists y\, (x < y)$, the goal itself, and replace $\bot$ by it.
With the atoms also weakened to $P \vee A$, HA proves the translated formula
$$\forall y\, (x < y \vee A \to \bot \vee A) \to \bot \vee A.$$
The premise is provable, since either disjunct of $x < y \vee A$ gives $A$, so HA proves $\bot \vee A$, and that gives $A$.
The double negation is gone.

The method is the shortest route to the [[Pi-0-2 conservativity of PA over HA|PY679V9MVR]], and it is a basic tool of program extraction from classical proofs.

## Notation

We write $B^A$, where the letter $A$ refers to the formula added to the atoms.
Books also say *Friedman translation*, *Friedman-Dragalin translation* or *$A$-translation*, and some write $B_A$.
We write $\vdash_i$ for intuitionistic [[natural deduction|PAQ4ZX2TX1]] NJ.
Watch the bound variables: $B^A$ is defined only after renaming the bound variables of $B$ away from the free variables of $A$.

## Remarks

### How the clauses read

For an equation, $(s = t)^A$ is $s = t \vee A$, and $\bot^A$ is $\bot \vee A$, which is equivalent to $A$.
The connectives and quantifiers are kept, so a negation $\neg B = B \to \bot$ becomes $B^A \to \bot \vee A$, that is, "$B$ implies $A$".
So the translated proof reads every refutation of $B$ as a reduction of $A$ to $B$.
For a quantifier-free $\varphi$, HA proves $\varphi^A \leftrightarrow \varphi \vee A$, because $\varphi$ is decidable.

### Two worked uses

[[Markov's rule|Z22K35X95F]] is the simplest use.
If HA proves $\neg \neg \exists y\, \varphi(x, y)$ with $\varphi$ quantifier-free, take $A = \exists y\, \varphi(x, y)$.
The argument of the Motivation then gives an HA proof of $\exists y\, \varphi(x, y)$.

A more instructive use is [[infinite descent|KE1C94RNF3]].
Classically, no function $f : \mathbb{N} \to \mathbb{N}$ decreases forever, so some $y$ has $f(y) \le f(y + 1)$.
The A-translation of the proof by contradiction is a search through $0, 1, \dots, f(0)$, and it gives the bound $y \le f(0)$ for free.

### The rules you can use

The main property, $\mathsf{HA} \vdash B$ implies $\mathsf{HA} \vdash B^A$, is proved in two parts in the [[proof of conservativity|ANXVZG97MG]].
The logical rules are preserved because the translation commutes with the connectives, quantifiers and [[substitution|NCDZ969V7X]].
Ex falso is preserved because $A \vdash_i B^A$ for every $B$: each atom of $B^A$ has the disjunct $A$.
The axioms of HA are preserved because an induction axiom translates into an induction axiom.
The same property holds for HA in all finite types and for intuitionistic second-order arithmetic.

### What it is not

[[Replacing only falsity by A|K9KMSBSAKK]] is not enough in intuitionistic logic.
HA proves $\bot \to 0 = 1$, but with $A = (0 = 0)$ the map gives $0 = 0 \to 0 = 1$, which HA does not prove.
Replacing each atom $P$ by $P \wedge A$ fails too.
HA proves $0 = 0$, but not $0 = 0 \wedge A$ for $A = (0 = 1)$.

### Watch out

The A-translation acts on intuitionistic proofs, so the negative translation must come first.
A classical theorem need not have a provable A-translation.
With $A = \bot$, the translation of $P \vee \neg P$ is equivalent to $P \vee \neg P$ itself, and HA does not prove this for $P = \exists y\, T(x, x, y)$.

The method also stops at $\Pi^0_2$.
The goal $A$ must be an existential formula whose matrix is decidable, so that the premise of the translated formula is provable.
For $\Pi^0_3$ sentences the conclusion is false, as the [[Pi-0-3 non-example|HVHEKG9FA5]] shows.

### History

Harvey Friedman published the translation in 1978, and used it to show that PA and HA have the same provably recursive functions.
Albert Dragalin found the same method independently.
A refined form for minimal logic, in which only $\bot$ is replaced, was later developed by Ulrich Berger, Wilfried Buchholz and Helmut Schwichtenberg for program extraction.

### Try it

First, compute $(\neg (x = 0))^A$.
It is $(x = 0 \vee A) \to (\bot \vee A)$, which HA proves equivalent to $x = 0 \to A$.

Second, why must the bound variables of $B$ avoid the free variables of $A$?
Take $A$ to be $y = 0$ and $B$ to be $\bot \to \forall y\, \bot$, which HA proves.
Without renaming, $B^A$ is $(\bot \vee y = 0) \to \forall y\, (\bot \vee y = 0)$, which is equivalent to $y = 0 \to \forall y\, (y = 0)$ and is false for $y = 0$.

## Explanations

### L1 human

A classical proof of "there is a number $y$ with property $P$" may only show that "no such number" leads to a contradiction.
Friedman's trick is to replace every "contradiction" in the proof by the goal itself, "there is such a number".
The rewritten proof is still correct, and its last line now states the goal.
For example, a classical proof that a list of natural numbers cannot decrease forever becomes a search that finds the place where it stops decreasing.

### L2 human

We remove a double negation by hand.
Suppose HA proves $\neg \neg \exists y\, (y \cdot y = 4)$, that is, $(\exists y\, (y \cdot y = 4) \to \bot) \to \bot$.
Let $A = \exists y\, (y \cdot y = 4)$.
The main property gives HA a proof of the translation:
$$(\exists y\, (y \cdot y = 4 \vee A) \to \bot \vee A) \to \bot \vee A.$$
The premise holds, since from $y \cdot y = 4 \vee A$ we get $A$ in both cases, and then $\bot \vee A$.
So HA proves $\bot \vee A$, and ex falso in the first case gives $A$.
This is the typical use: the negative translation produces a double negation, and the A-translation removes it for a decidable existential.

### L3 human

The A-translation is a continuation-passing transform with answer type $A$: the negative translation uses the answer type $\bot$, and Friedman's step changes it.
In algebraic terms, $p \mapsto p \vee a$ is a nucleus on a Heyting algebra, the closed nucleus of $a$, and the translation applies it to the atoms.
Together with the [[Dialectica interpretation|HZ17ES9PDY]] it shows that PA and HA have the same provably recursive functions, the functions of type $\mathbb{N} \to \mathbb{N}$ definable in [[system T|A4WR995XZP]].
The general pattern, a stronger theory that proves no new sentences of a given form, is the subject of [[conservation theorems|TNZ995J8AP]].
