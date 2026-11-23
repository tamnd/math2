---
tag: Y7YS1C3GAE
kind: concept
name: Guarded fragment
aliases: [guarded-fragment-of-first-order-logic, guarded-quantification]
msc: ["03B25", "03B45", "03B10"]
topics: [E4AVTNWE9E]
audience: research
uses: [086QKPF0A6, HYJ10AF6RT, C3RZY20ETK, NGHWZ9Y7ZV, QN7M1JCGT9, S7C3C7DJRF]
sources:
  - url: https://en.wikipedia.org/wiki/Guarded_logic
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Two-variable_logic
    locator: lead section
---

## Summary

The guarded fragment is the part of first-order logic in which every quantifier only looks at elements that are already linked to each other by one atomic fact.
"Every child of $x$ is a doctor" is a typical guarded statement, $\forall y \, (\mathit{Child}(x, y) \to D(y))$, where the atom $\mathit{Child}(x, y)$ is the guard.
This one restriction makes [[satisfiability|QN7M1JCGT9]] decidable, and it explains in first-order terms why [[modal logic|C3RZY20ETK]] is decidable.

Exactly, let $L$ be a signature of relation symbols, possibly with equality.
The guarded fragment $\mathrm{GF}$ is the smallest set of first-order $L$-[[formulas|HYJ10AF6RT]] that contains all atomic formulas, is closed under $\neg$, $\wedge$, $\vee$ and $\to$, and is closed under guarded quantification.
Guarded quantification forms the following two formulas:
$$\exists \vec{y} \, (\alpha \wedge \varphi), \qquad \forall \vec{y} \, (\alpha \to \varphi).$$
Here $\varphi$ is in $\mathrm{GF}$, and the guard $\alpha$ is an atomic formula that contains every free variable of $\varphi$ and every variable of $\vec{y}$.

## Motivation

Basic modal logic is decidable, and its formulas translate into first-order logic with two variables.
So the [[two-variable fragment|S7C3C7DJRF]] looked like a good explanation of why modal logic is decidable.
But many decidable extensions of modal logic, such as modal operators of higher arity, need more than two variables, while natural extensions of two-variable logic become undecidable.

Andréka, van Benthem and Németi looked at the translation more closely.
In it, each quantifier is tied to an atom: $\Diamond p$ becomes $\exists y \, (R(x, y) \wedge P(y))$, and the atom $R(x, y)$ says that $y$ is a neighbor of $x$.
The guarded fragment keeps exactly this pattern and drops the bound on the number of variables.
The same pattern appears in description logics for knowledge bases and in database queries, so the decidability of $\mathrm{GF}$ is used in practice.

## Notation

A guard is an atomic formula $\alpha(\vec{x}, \vec{y})$.
An equality $x = x$ can serve as the guard when the body has at most the one free variable $x$.
Some authors write $(\exists \vec{y} . \alpha) \varphi$ and $(\forall \vec{y} . \alpha) \varphi$ for the guarded quantifiers.
The loosely guarded fragment allows a conjunction of atoms as the guard, provided that each quantified variable occurs together with each other variable of the guard in one of the atoms.

## Remarks

### A first check

Take $\theta(x) = \forall y \, (R(x, y) \to \exists z \, (R(y, z) \wedge P(z)))$, the translation of the modal formula $\Box \Diamond p$.
We check it from the inside out.
The atom $P(z)$ is in $\mathrm{GF}$, as every atom is.
The formula $\exists z \, (R(y, z) \wedge P(z))$ has the guard $R(y, z)$, which contains the quantified $z$ and the free variable $z$ of the body.
The outer formula has the guard $R(x, y)$, and the body has the single free variable $y$, which the guard contains.
Check: every quantifier has an atom that covers its variables, so $\theta$ is guarded.

### Inside the fragment

The [[standard translation of every modal formula|N5YVK89ZQ9]] is guarded, with the accessibility atom $R(x, y)$ as the guard at each $\Diamond$ and $\Box$.
[[Symmetry, reflexivity and seriality|SJ5EESEWFR]] are guarded; for example, symmetry $\forall x \, \forall y \, (R(x, y) \to R(y, x))$ has the guard $R(x, y)$.
The sentence $\forall x \, (x = x \to P(x))$ is guarded by an equality, so every universal property of single elements is guarded.
The formula $\exists y \, \exists z \, (S(x, y, z) \wedge P(z))$ is guarded by the ternary atom $S(x, y, z)$, and it uses three variables, so $\mathrm{GF}$ goes beyond two-variable logic.

### Outside the fragment

[[Transitivity is not guarded|F7EJ2VVKBE]]: $\forall x \, \forall y \, \forall z \, (R(x, y) \wedge R(y, z) \to R(x, z))$ quantifies three variables, and no atom of it contains all three.
The sentence $\forall x \, \forall y \, (P(x) \wedge P(y) \to R(x, y))$ is not guarded as written, because its antecedent is not an atom and neither $P(x)$ nor $P(y)$ contains both variables.
A formula with a function symbol, such as $\forall x \, P(f(x))$, is outside, since $\mathrm{GF}$ is defined for relational signatures.

### What the fragment gives

Grädel proved in 1999 that satisfiability of guarded sentences is decidable.
The problem is complete for doubly exponential time in general, and complete for exponential time when the arity of the relation symbols is bounded.
He also proved the finite model property: every satisfiable guarded sentence has a finite model.

Guarded sentences have a tree-like model property as well.
A satisfiable guarded sentence has a model of bounded tree width, with a bound that depends only on the arities of the relation symbols.
Guarded formulas are invariant under guarded bisimulation, the analogue of modal [[bisimulation|X27BR4YP2Y]] in which partial isomorphisms between guarded sets of elements play the role of related worlds.
Through the standard translation, a modal formula holds at a world of a [[Kripke model|NGHWZ9Y7ZV]] exactly when its guarded translation holds there.

### Watch out

The guard must be one atom.
An arbitrary formula as the guard gives back all of first-order logic, since $\forall \vec{y} \, \varphi$ is the same as $\forall \vec{y} \, (\top \to \varphi)$.

The guard must contain the free variables of the body, not only the quantified ones.
The formula $\exists y \, (R(x, y) \wedge S(y, z))$ is not guarded, because $z$ is free in the body and does not occur in $R(x, y)$.

Not every modal frame condition stays guarded.
The axiom $\Box p \to \Box \Box p$ corresponds to transitive frames, and transitivity is outside $\mathrm{GF}$.

### History

Andréka, van Benthem and Németi introduced the guarded fragment in a paper published in 1998, as a first-order explanation of the good behavior of modal logic.
Grädel proved the decidability, the exact complexity and the finite model property in 1999.
Ganzinger, Meyer and Veanes showed in 1999 that the two-variable guarded fragment becomes undecidable when some binary relations are required to be transitive.

### Try it

Is $\exists y \, (R(x, y) \wedge \forall x \, (R(y, x) \to P(x)))$ guarded?
Yes: the inner guard $R(y, x)$ covers $x$, and the outer guard $R(x, y)$ covers $y$, the only free variable of its body.

Is $\forall x \, \forall y \, (R(x, y) \to S(y, z))$ guarded?
No: the body has the free variable $z$, and the guard $R(x, y)$ does not contain it.

## Explanations

### L1 human

In everyday language, "for all" is often limited by a relation, as in "every friend of Anna is happy".
The guarded fragment is the part of logic where every "for all" and every "there is" is limited in this way by one basic relation.
The restriction keeps statements local: they only talk about objects that are directly linked.
Because of this, a computer can always decide whether such a statement can be true.

### L2 human

We use the guarded fragment to decide a small modal question: can a world satisfy $\Diamond p$ while every world it reaches satisfies $\neg p$?
The translation of $\Diamond p \wedge \Box \neg p$ at $x$ is the following guarded formula:
$$\exists y \, (R(x, y) \wedge P(y)) \wedge \forall y \, (R(x, y) \to \neg P(y)).$$
Both quantifiers have the guard $R(x, y)$, so the formula is in $\mathrm{GF}$, and Grädel's theorem says its satisfiability is decidable.
Here the answer is quick: a witness $y$ would satisfy both $P(y)$ and $\neg P(y)$, so the formula is unsatisfiable.
Check: the modal reading agrees, since $\Diamond p$ and $\Box \neg p$ are contradictory in every Kripke model.

The typical use of $\mathrm{GF}$ is to prove that a modal or description logic is decidable by translating it into the fragment.
Watch out: the guard must cover the free variables of the body as well as the quantified ones.

### L3 human

The guarded fragment is one answer to the question of why modal logic stays decidable under so many extensions.
Its decidability rests on the tree-like model property, which allows decision procedures by automata that run on tree decompositions, as for the modal mu-calculus.
Guarded fixed-point logic, which adds least and greatest fixed points to $\mathrm{GF}$, is still decidable, and it contains the modal mu-calculus.
Guarded logics link the classical decision problem, model theory with guarded bisimulation, and database theory, where guarded rules describe well-behaved classes of queries.
The [[decidable prefix classes|ZF79MZRQ8V]] and [[two-variable logic|S7C3C7DJRF]] are the other main families of decidable fragments.
