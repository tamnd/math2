---
tag: ETCVR65W3M
kind: definition
name: Paraconsistent logic
msc: [03B53]
defines: C7YWCR87QJ
uses: [1HK0VYWTV7, 09K9MWD2QQ, 029JBBF693]
sources:
  - url: https://en.wikipedia.org/wiki/Paraconsistent_logic
---

## Definition

Let $\vdash$ be a [[consequence relation|1HK0VYWTV7]] between sets of formulas and formulas of a language with a [[negation|029JBBF693]] $\neg$.
The relation $\vdash$ is explosive when $\set{\varphi, \neg\varphi} \vdash \psi$ for all formulas $\varphi$ and $\psi$.
A logic is paraconsistent when its consequence relation is not explosive.
That is, there are formulas $\varphi$ and $\psi$ with $\set{\varphi, \neg\varphi} \nvdash \psi$.

## Remarks

Example: Priest's logic of paradox $\mathrm{LP}$ has the truth values $t$, $b$ ("both") and $f$, ordered $f < b < t$.
Negation swaps $t$ and $f$ and fixes $b$; conjunction is the minimum and disjunction the maximum.
The designated values are $t$ and $b$, and $\Gamma \vdash \psi$ means that every valuation giving all of $\Gamma$ designated values gives $\psi$ one too.
The valuation $p \mapsto b$, $q \mapsto f$ makes $p$ and $\neg p$ designated and $q$ not, so $\set{p, \neg p} \nvdash q$.

Non-example: classical [[propositional logic|09K9MWD2QQ]] is explosive.
No valuation makes both $\varphi$ and $\neg\varphi$ true, so every $\psi$ follows from them.
Intuitionistic logic is explosive too, through the axiom $\bot \to \psi$.

## Explanations

### L1 human

A paraconsistent logic is any logic in which some contradiction fails to prove some statement.
Such logics weaken negation, or the notion of consequence, so that a contradiction can be true in a model without making everything true.
