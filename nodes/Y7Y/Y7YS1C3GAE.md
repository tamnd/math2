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

Let $L$ be a signature of relation symbols, possibly with equality.
The guarded fragment $\mathrm{GF}$ is the smallest set of first-order $L$-[[formulas|HYJ10AF6RT]] that contains all atomic formulas, is closed under $\neg$, $\wedge$, $\vee$ and $\to$, and is closed under guarded quantification.
Guarded quantification forms $\exists \vec{y} \, (\alpha \wedge \varphi)$ and $\forall \vec{y} \, (\alpha \to \varphi)$, where $\varphi$ is in $\mathrm{GF}$ and the guard $\alpha$ is an atomic formula that contains every free variable of $\varphi$ and every variable of $\vec{y}$.
The guarded fragment contains the translations of [[modal logic|C3RZY20ETK]], and its [[satisfiability|QN7M1JCGT9]] problem is decidable, so it explains in first-order terms why modal logic is decidable.

## Motivation

Basic modal logic is decidable, and its formulas translate into first-order logic with two variables.
For a time, the [[two-variable fragment|S7C3C7DJRF]] was taken as the reason for the decidability of modal logic.
But many decidable extensions of modal logic, such as modal logics with operators of higher arity, need more than two variables, and natural extensions of two-variable logic are undecidable.
Andréka, van Benthem and Németi observed that in a modal translation each quantifier is relativized to an atom: $\Diamond p$ becomes $\exists y \, (R(x, y) \wedge P(y))$.
The guarded fragment keeps exactly this pattern and drops the bound on the number of variables.

## Notation

A guard is an atomic formula $\alpha(\vec{x}, \vec{y})$; an equality $x = x$ can serve as a guard for a single variable.
Some authors write $(\exists \vec{y} . \alpha) \varphi$ and $(\forall \vec{y} . \alpha) \varphi$ for the guarded quantifiers.
The loosely guarded fragment allows a conjunction of atoms as guard, provided that every two quantified or free variables occur together in one of the atoms.

## Remarks

### Examples

1. The modal formula $\Diamond p$ translates into $\exists y \, (R(x, y) \wedge P(y))$, which is guarded by $R(x, y)$; see [[the standard translation of a modal formula is guarded|N5YVK89ZQ9]].
2. Symmetry $\forall x \, \forall y \, (R(x, y) \to R(y, x))$ is guarded by $R(x, y)$; see [[symmetry is expressible in the guarded fragment|SJ5EESEWFR]].
3. The sentence $\forall x \, (x = x \to P(x))$ is guarded by the equality $x = x$, so every universal property of single elements is guarded.
4. The formula $\exists y \, \exists z \, (S(x, y, z) \wedge P(z))$ is guarded by the ternary atom $S(x, y, z)$, and it uses three variables, so it is not in two-variable logic.
5. The description-logic statement "every child of $x$ is a doctor" is $\forall y \, (\mathit{Child}(x, y) \to D(y))$, guarded by $\mathit{Child}(x, y)$.

### Non-examples

1. Transitivity $\forall x \, \forall y \, \forall z \, (R(x, y) \wedge R(y, z) \to R(x, z))$ is not guarded, because no atom contains $x$, $y$ and $z$; see [[transitivity is not guarded|F7EJ2VVKBE]].
2. The sentence $\forall x \, \forall y \, (P(x) \wedge P(y) \to R(x, y))$ is not guarded as written, because the antecedent is not an atom and no single atom of it contains both $x$ and $y$.
3. A formula with a function symbol, such as $\forall x \, P(f(x))$, is outside the guarded fragment, which is defined for relational signatures.

### Basic properties

1. The standard translation maps each formula of basic modal logic to a guarded formula with one free variable, which holds at a world exactly when the modal formula holds there in the [[Kripke model|NGHWZ9Y7ZV]].
2. Grädel proved in 1999 that satisfiability of guarded sentences is decidable. It is complete for doubly exponential time in general, and complete for exponential time when the arity of the relation symbols is bounded.
3. Grädel also proved that the guarded fragment has the finite model property: every satisfiable guarded sentence has a finite model.
4. Guarded sentences have a tree-like model property: each satisfiable guarded sentence has a model of bounded tree width, with a bound that depends only on the arities of the relation symbols.
5. Guarded formulas are invariant under guarded bisimulation, the analogue of the modal [[bisimulation|X27BR4YP2Y]] in which partial isomorphisms between guarded sets of elements play the role of related worlds.

### History

Andréka, van Benthem and Németi introduced the guarded fragment in a paper published in 1998, as a first-order explanation of the good behavior of modal logic.
Grädel proved in 1999 the decidability, the exact complexity and the finite model property of the guarded fragment.
Ganzinger, Meyer and Veanes showed in 1999 that the two-variable guarded fragment becomes undecidable when some binary relations are required to be transitive.

### Common errors

- Using a non-atomic guard. The guard must be a single atom, or in the loosely guarded fragment a conjunction with the covering condition; an arbitrary formula as guard gives all of first-order logic.
- Forgetting that the guard must contain the free variables of the body. The formula $\exists y \, (R(x, y) \wedge S(y, z))$ is not guarded, because $z$ is free in the body and does not occur in $R(x, y)$.
- Assuming that every modal axiom stays guarded. The modal axiom for transitive frames corresponds to transitivity, which is not guarded.

## Explanations

### L1 human

In everyday language, "for all" is often limited by a relation: "for every friend of Anna, the friend is happy".
The guarded fragment is the part of logic where every "for all" and every "there is" is limited in this way by one basic relation.
This restriction keeps the statements local: they only talk about objects that are directly related.
Because of this, a computer can always decide whether such a statement can be true.

### L2 human

We check that the formula $\theta(x) = \forall y \, (R(x, y) \to \exists z \, (R(y, z) \wedge P(z)))$ is guarded.
It is the translation of the modal formula $\Box \Diamond p$.

1. The atom $P(z)$ is guarded, since every atomic formula is in $\mathrm{GF}$.
2. The formula $\exists z \, (R(y, z) \wedge P(z))$ has guard $R(y, z)$. The body $P(z)$ has free variable $z$, which occurs in the guard, and the quantified variable $z$ occurs in the guard.
3. The formula $\forall y \, (R(x, y) \to \exists z \, (R(y, z) \wedge P(z)))$ has guard $R(x, y)$. The body has free variable $y$, and the quantified variable is $y$; both occur in the guard.
4. So $\theta(x)$ is in $\mathrm{GF}$, and its satisfiability is decidable by Grädel's theorem.

The typical use of the guarded fragment is to show that a modal or description logic is decidable, by translating it into $\mathrm{GF}$.
A trap is to check only the quantified variables: in step 3 the guard must also contain the free variables of the body.

### L3 human

The guarded fragment is one answer to the question why modal logic is robustly decidable.
Its decidability rests on the tree-like model property, which allows automata-theoretic decision procedures on tree decompositions, as for the modal mu-calculus.
The guarded fixed-point logic, which adds least and greatest fixed points to $\mathrm{GF}$, is still decidable, and it contains the modal mu-calculus.
Guarded logics are a link between the classical decision problem, model theory with guarded bisimulation, and database theory, where guarded rules describe tractable classes of queries.
