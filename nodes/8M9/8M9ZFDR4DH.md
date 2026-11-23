---
tag: 8M9ZFDR4DH
kind: statement
role: theorem
name: Deduction theorem for predicate logic
aliases: [the-deduction-theorem-in-predicate-logic]
msc: ["03B10", "03F03"]
topics: [TTCRX3NFNY]
audience: ug2
about: [N95HV0VWSM]
uses: [2B00FE6K5W, 9X08XK5RV2, 0ZNX6DQ3EJ]
sources:
  - wikipedia: en:480010@r1320842012
    locator: Deduction theorem, section The deduction theorem in predicate logic
    note: adopted
    mention: wikipedia://en/480010#Y3DL
    sections: [Statement]
  - url: https://en.wikipedia.org/wiki/Deduction_theorem
    locator: The deduction theorem in predicate logic
  - book: isbn:9781482237726
    locator: Chapter 2
  - book: isbn:9780122384523
    locator: Section 2.4
inventory: [TGSPJ68GEB]
---

## Statement

The deduction theorem says that to deduce $\varphi \to \psi$ it is enough to add $\varphi$ as a hypothesis and deduce $\psi$, with one restriction in systems that have a rule of generalization.

Let $\Gamma$ be a set of formulas of a first-order language, and let $\varphi$ and $\psi$ be formulas.
We use the two forms $\mathsf{H}$ and $\mathsf{H}_G$ of the [[Hilbert-style predicate calculus|2B00FE6K5W]].
In $\mathsf{H}$ the axioms are closed under generalization and modus ponens is the only rule, and in $\mathsf{H}_G$ generalization is a rule.

1. In both systems, if $\Gamma \vdash \varphi \to \psi$, then $\Gamma \cup \{ \varphi \} \vdash \psi$.
2. In $\mathsf{H}$, if $\Gamma \cup \{ \varphi \} \vdash_{\mathsf{H}} \psi$, then $\Gamma \vdash_{\mathsf{H}} \varphi \to \psi$.
3. In $\mathsf{H}_G$, suppose that $\psi$ has a derivation from $\Gamma \cup \{ \varphi \}$ in which the rule of generalization is never applied to a variable that is free in $\varphi$.
   Then $\Gamma \vdash_{\mathsf{H}_G} \varphi \to \psi$.

In particular, if $\varphi$ is a sentence, then in both systems $\Gamma \cup \{ \varphi \} \vdash \psi$ holds exactly when $\Gamma \vdash \varphi \to \psi$.
The [[proof|GTRGQ7XZP7]] is an induction on derivations, as for the [[propositional deduction theorem|9X08XK5RV2]].

## Remarks

### A first use

We deduce $\forall x\, P(x) \to \forall x\, Q(x)$ from $\Gamma = \{ \forall x\,(P(x) \to Q(x)) \}$ in $\mathsf{H}_G$.
The [[derivation with the rule of generalization|C8ANFQQ843]] derives $\forall x\, Q(x)$ from $\Gamma \cup \{ \forall x\, P(x) \}$.
Its only use of generalization is on $x$, and $x$ is not free in the added hypothesis $\forall x\, P(x)$.
So part 3 applies, and it gives
$$\Gamma \vdash_{\mathsf{H}_G} \forall x\, P(x) \to \forall x\, Q(x).$$
This is how mathematicians prove "if $\varphi$ then $\psi$": they assume $\varphi$ and derive $\psi$, as in a [[direct proof|0NTF6DMVAP]].

### Why the restriction is needed

The condition on generalization in part 3 cannot be dropped.
In $\mathsf{H}_G$ the two lines $P(x)$ and $\forall x\, P(x)$ derive $\forall x\, P(x)$ from $\{ P(x) \}$.
But $P(x) \to \forall x\, P(x)$ is not a theorem.
In a structure with domain $\{ 0, 1 \}$, with $P$ true of $0$ only and $x$ assigned to $0$, it is false.
The [[counterexample|D3SW6V4R1B]] checks every step.

Part 2 needs no condition, because $\mathsf{H}$ does not derive $\forall x\, P(x)$ from $P(x)$ in the first place.
The condition has moved into the [[generalization theorem|VKSK35Y52Z]], which asks that $x$ is not free in the hypotheses.

### What it gives you

The theorem turns derivations from finitely many sentences into theorems.
If $\varphi_1, \dots, \varphi_n$ are sentences, then $n$ uses of it give
$$\Gamma \cup \{ \varphi_1, \dots, \varphi_n \} \vdash \psi \quad \text{exactly when} \quad \Gamma \vdash \varphi_1 \to (\varphi_2 \to \cdots (\varphi_n \to \psi) \cdots).$$

It also gives [[proof by contradiction|0J0XBKG64S]] inside the calculus.
Let $\varphi$ be a sentence, and suppose that $\Gamma \cup \{ \varphi \}$ derives both $\chi$ and $\neg \chi$.
The theorem gives $\Gamma \vdash \varphi \to \chi$ and $\Gamma \vdash \varphi \to \neg \chi$.
The tautology $(\varphi \to \chi) \to ((\varphi \to \neg \chi) \to \neg \varphi)$ and modus ponens twice give $\Gamma \vdash \neg \varphi$.

### The converse

Part 1 is the converse of parts 2 and 3, and it holds with no condition.
A derivation of $\varphi \to \psi$ from $\Gamma$, followed by the line $\varphi$ and one step of [[modus ponens|0Y0MQYST0M]], is a derivation of $\psi$ from $\Gamma \cup \{ \varphi \}$.

### Generalizations

Mendelson states part 3 with a weaker condition.
Generalization may use a free variable of $\varphi$, as long as the formula it is applied to has a derivation that does not depend on $\varphi$.

In [[natural deduction|6KT3BJZ7D1]] the theorem becomes a rule, $\to$-introduction, and in the [[sequent calculus|W72CA3R9MP]] it is the right rule for $\to$.
Modal logic shows the same failure as $\mathsf{H}_G$.
With the rule of necessitation, which infers $\Box \varphi$ from $\varphi$, we get $\{ p \} \vdash \Box p$, but $p \to \Box p$ is not a theorem of the modal logic K.

## History

Herbrand proved a deduction theorem in his thesis of 1930.
Mendelson's textbook states the restricted form for a system with a rule of generalization.

## Explanations

### L1 human

To prove "if it rains, then the street is wet", we assume that it rains and then show that the street is wet.
The deduction theorem says that the formal calculus allows this way of proving an "if ... then" statement.
In predicate logic there is one catch, about letters such as $x$ that stand for an unknown object.
If we assume "$x$ is even" and then use the assumption as if $x$ were every number, we get "every number is even".
The statement "if $x$ is even, then every number is even" is false for $x = 2$, so this use must be forbidden.

### L2 human

We decide whether the theorem applies to a derivation in $\mathsf{H}_G$ of $\forall y\, R(x, y)$ from $\{ \forall y\, R(x, y) \}$ that goes through $R(x, y)$ and then generalizes on $y$.
The free variables of the hypothesis $\forall y\, R(x, y)$ are just $x$.
The derivation generalizes only on $y$, which is not in that list.
So part 3 gives $\vdash \forall y\, R(x, y) \to \forall y\, R(x, y)$, which is valid, as it should be.
If the derivation had instead generalized on $x$, the theorem could not be used.
The typical use is to find a derivation of $\varphi \to \psi$: assume $\varphi$, derive $\psi$, and discharge $\varphi$.
Watch out: check every generalization step that depends on $\varphi$, not only the last one.

### L3 human

The theorem says that implication internalizes the consequence relation: $\varphi \to \psi$ is derivable exactly when $\psi$ is derivable from $\varphi$.
In a category of proofs this is the adjunction between the product with $\varphi$ and the exponential, the same law that gives currying in the lambda calculus and the [[Curry-Howard correspondence|A77FER1Q5H]].
The failure in $\mathsf{H}_G$ comes from a mismatch of two readings: a free variable in a hypothesis is read universally, while in $\varphi \to \psi$ it is read for one fixed value.
The systems $\mathsf{H}$, [[natural deduction|6KT3BJZ7D1]] and the sequent calculus avoid the mismatch.
They put the condition on generalization into the generalization theorem or into an eigenvariable condition.
