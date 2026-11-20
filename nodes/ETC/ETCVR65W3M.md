---
tag: ETCVR65W3M
kind: definition
name: Paraconsistent logic
msc: [03B53]
topics: [NJB94B39QK]
audience: ug2
defines: C7YWCR87QJ
uses: [1HK0VYWTV7, 09K9MWD2QQ, 029JBBF693, TTKZGJEEK7]
sources:
  - url: https://en.wikipedia.org/wiki/Paraconsistent_logic
    locator: Definition
  - url: https://plato.stanford.edu/entries/logic-paraconsistent/
    locator: Paraconsistent Logic (SEP entry), section 1
---

## Definition

Let $\vdash$ be a [[consequence relation|1HK0VYWTV7]] between sets of formulas and formulas of a language with a [[negation|029JBBF693]] $\neg$.
The relation $\vdash$ is [[explosive|TTKZGJEEK7]] when $\set{\varphi, \neg\varphi} \vdash \psi$ for all formulas $\varphi$ and $\psi$.
A logic is *paraconsistent* when its consequence relation is not explosive.
That is, there are formulas $\varphi$ and $\psi$ with $\set{\varphi, \neg\varphi} \nvdash \psi$.

## Notation

We write $\nvdash$ for "does not follow".
For a semantic consequence relation we write $\vDash$; then $\Gamma \vDash \psi$ means that every valuation that designates all of $\Gamma$ designates $\psi$.
Some authors define paraconsistency for theories: a theory $T$ is paraconsistent when it is inconsistent but not trivial.

## Remarks

Example: Priest's logic of paradox $\mathrm{LP}$ has the truth values $t$, $b$ ("both") and $f$, ordered $f < b < t$.
Negation swaps $t$ and $f$ and fixes $b$; conjunction is the minimum and disjunction the maximum.
The designated values are $t$ and $b$, and $\Gamma \vdash \psi$ means that every valuation giving all of $\Gamma$ designated values gives $\psi$ one too.
The valuation $p \mapsto b$, $q \mapsto f$ makes $p$ and $\neg p$ designated and $q$ not, so $\set{p, \neg p} \nvdash q$.

Non-example: classical [[propositional logic|09K9MWD2QQ]] is explosive.
No valuation makes both $\varphi$ and $\neg\varphi$ true, so every $\psi$ follows from them.
Intuitionistic logic is explosive too, through the rule that derives every $\psi$ from $\bot$.

The definition is negative: it names a property that a logic lacks.
So it covers systems with very different motives, from the [[logic of paradox|~26a0362d]] to [[da Costa's systems|~3c6ff4aa]].
A variant requires that $\set{\varphi, \neg\varphi} \nvdash \psi$ for some $\psi$ in the language, even when $\psi$ is restricted to atoms; for logics closed under substitution the two forms agree.
The definition depends on the choice of $\neg$; a logic can be paraconsistent for one negation and explosive for another.

## Explanations

### L1 human

A paraconsistent logic is any logic in which some contradiction fails to prove some statement.
Such logics weaken negation, or the notion of consequence, so that a contradiction can hold in a model without making everything hold.

### L2 human

To show that a logic is paraconsistent, you need one counterexample: a valuation, or a model, where $\varphi$ and $\neg\varphi$ are accepted and $\psi$ is not.
To show that a logic is not paraconsistent, you need a proof that works for all $\varphi$ and $\psi$, such as the Lewis argument.
A trap is to test only the formula $(\varphi \land \neg\varphi) \to \psi$; in a logic without a deduction theorem, this formula and the inference can differ.

### L3 human

In abstract terms, a Tarskian consequence operator $C$ is paraconsistent when $C(\set{\varphi, \neg\varphi})$ is a proper subset of the set of formulas for some $\varphi$.
Logics of formal inconsistency refine this: they are paraconsistent, but every contradiction about a consistent formula explodes, $\circ\varphi, \varphi, \neg\varphi \vdash \psi$.
In algebraic semantics, paraconsistency means that $a \land \neg a$ need not be the bottom element.
