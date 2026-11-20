---
tag: TTKZGJEEK7
kind: concept
name: Explosion
aliases: [explosive-consequence-relation]
msc: ["03B53", "03B05"]
topics: [NJB94B39QK]
audience: ug2
uses: [J78Y1M4GND, 029JBBF693, VM8TQ70CVJ, WK2P0E82B4]
sources:
  - wikipedia: en:76765067@r1368301704
    locator: Glossary of logic, section E
    note: adopted
    mention: wikipedia://en/76765067#50UG
    sections: [Summary]
  - url: https://en.wikipedia.org/wiki/Principle_of_explosion
    locator: lead section
  - url: https://plato.stanford.edu/entries/logic-paraconsistent/
    locator: Paraconsistent Logic (SEP entry), section 1
inventory: [MX47FRXAEM]
---

## Summary

Let $\vdash$ be a [[consequence relation|J78Y1M4GND]] on a language with a [[negation|029JBBF693]] $\neg$.
The relation $\vdash$ is *explosive* when $\set{\varphi, \neg\varphi} \vdash \psi$ for all formulas $\varphi$ and $\psi$.
In words: from a contradiction, every formula follows.
This property is called *explosion*, or *ex contradictione quodlibet*.
For classical logic it is the [[principle of explosion|~53891d1b]].
Explosion matters because it makes every inconsistent theory trivial, so in an explosive logic "consistent" and "not every formula is provable" mean the same.

## Motivation

A theory $T$ is *trivial* when $T \vdash \psi$ for every formula $\psi$.
In an explosive logic, one contradiction makes a theory trivial.
This is useful in mathematics, where a contradiction shows that an assumption is false.
It is a problem when we must reason with data that we know to be inconsistent, such as two witnesses who disagree.
The concept of explosion lets us state exactly which logics have this problem.
The logics without it are the [[paraconsistent logics|C7YWCR87QJ]].

## Notation

The rule is often written $\varphi, \neg\varphi \vdash \psi$, or with the constant $\bot$ as $\bot \vdash \psi$ (*ex falso quodlibet*).
The two forms are equivalent in classical and intuitionistic logic, where $\varphi, \neg\varphi \vdash \bot$.
They are different in [[minimal logic|3MBG95617E]], where $\bot$ is an ordinary atom.
Some authors write ECQ for ex contradictione quodlibet and EFQ for ex falso quodlibet.

## Remarks

### Examples

- Classical propositional logic is explosive. This is the [[principle of explosion|~53891d1b]], with a syntactic and a semantic proof.
- [[Intuitionistic logic is explosive|~e32fccda]], by $\to$-elimination and ex falso.
- [[Strong Kleene logic K3 is explosive|~8e0cd38f]], although it has a third truth value: no valuation designates both $p$ and $\neg p$.

### Non-examples

- The [[logic of paradox|~05cece33]] is not explosive: the valuation $v(p) = \mathsf{B}$, $v(q) = \mathsf{F}$ designates $p$ and $\neg p$ but not $q$.
- [[Minimal logic|T2SXPH67RQ]] does not prove $\bot \to p$, and $p, \neg p \nvdash q$ in it, although $p, \neg p \vdash \neg q$.
- [[Jaśkowski's discussive logic|~5e13c759]] is not explosive, because $p$ and $\neg p$ can be possible at different worlds.

### Basic properties

- In an explosive logic, a set $\Gamma$ is [[consistent|VM8TQ70CVJ]] (no $\varphi$ with $\Gamma \vdash \varphi$ and $\Gamma \vdash \neg\varphi$) if and only if it is [[Post consistent|WK2P0E82B4]] (some formula is not derivable).
- Every consequence relation that has disjunction introduction, disjunctive syllogism and transitivity is explosive, by the Lewis argument in the [[proof of the principle|~9dabb726]].
- Explosion is a property of $\vdash$, not of a theory. A paraconsistent logic can still have theories that are trivial.

### History

A version of the Lewis argument was found in the twelfth century by William of Soissons.
The argument is now named after Lewis, who published it.
Paraconsistent logics, which reject explosion, were developed in the twentieth century by Jaśkowski, da Costa, Priest and others.

### Common errors

- To think that explosion says that contradictions are true. It says only what follows from a contradiction.
- To identify the rejection of explosion with [[dialetheism|3P0FM0AQF3]]. A logician can reject explosion and still hold that no contradiction is true.
- To think that $\set{\varphi, \neg\varphi} \vdash \psi$ and $\vdash (\varphi \land \neg\varphi) \to \psi$ are the same property in every logic. They are linked by the deduction theorem and adjunction, and both can fail.

## Explanations

### L1 human

Imagine a list of facts that says both "the shop is open" and "the shop is not open".
In ordinary logic, from these two facts you can prove any statement at all, for example "two plus two is five".
This rule is called explosion: one contradiction makes the whole list useless.
Some logics are built so that a contradiction does not explode.
In such a logic the list can still give sensible answers about other things.

### L2 human

We check that explosion fails in a three-valued logic and holds in classical logic.

1. In classical logic, a valuation makes $p$ true and $\neg p$ true only if $v(p) = 1$ and $v(p) = 0$. This is impossible.
2. So no valuation makes both premises true, and every $q$ follows from $\set{p, \neg p}$ by the definition of consequence.
3. In the logic of paradox, values are $\mathsf{T}, \mathsf{B}, \mathsf{F}$, with $\mathsf{T}$ and $\mathsf{B}$ designated, and $\neg\mathsf{B} = \mathsf{B}$.
4. The valuation $v(p) = \mathsf{B}$, $v(q) = \mathsf{F}$ designates $p$ and $\neg p$, and does not designate $q$.
5. So $\set{p, \neg p} \nvDash_{\mathrm{LP}} q$, and LP is not explosive.

The typical use of explosion is the step "a contradiction proves the goal" at the end of a proof by cases.
A trap is to think that every three-valued logic avoids explosion: [[K3|~8e0cd38f]] has three values and is explosive.

### L3 human

Explosion is the statement that the trivial theory is the only inconsistent theory.
In algebraic terms, for a logic with an algebraic semantics, explosion says that an element and its negation have meet $0$, as in Boolean and Heyting algebras.
Paraconsistent semantics drop this law: De Morgan algebras, used for [[first-degree entailment|KXTP4P3GHT]], have elements with $a \land \neg a \ne 0$.
Logics of formal inconsistency keep explosion for consistent formulas only, through the gentle explosion rule $\circ\varphi, \varphi, \neg\varphi \vdash \psi$; see [[da Costa's systems|~3c6ff4aa]].
Weaker and stronger forms are the [[weak paraconsistency|V5AWSJJJ4G]] and [[strong paraconsistency|GYCRTA2TN9]] of a logic.
