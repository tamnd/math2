---
tag: WXSPR8HPJA
kind: problem
name: Logic optimization
msc: [94C11, "06E30", 68Q17]
uses: [0X05GS525E, 0GVDFAY4KW, MHA48AWBXN]
about: [0X05GS525E]
sources:
  - url: https://en.wikipedia.org/wiki/Logic_optimization
same_as:
  wikidata: Q6667469
  wikipedia: Logic optimization
history:
  posed_by: "Willard Van Orman Quine"
  first_stated: "1952"
---

## Problem

Let $f \colon \set{0,1}^n \to \set{0,1}$ be a [[Boolean function|0X05GS525E]], given by its truth table or by a formula.
Find a formula in [[disjunctive normal form|0GVDFAY4KW]] that computes $f$ and has the smallest number of terms.
Among those, it should have the smallest total number of literals.
This is the two-level case of logic optimization.
The general problem asks for a smallest circuit of gates of a given kind that computes $f$.

## Remarks

Quine posed the two-level problem as the problem of simplifying truth functions, and showed that a shortest form can be built from prime implicants.
The [[Quine–McCluskey algorithm|W0HDZBF5FC]] solves it exactly, and the [[Karnaugh map|TS1B16HX5K]] solves small cases by hand.
The problem is [[NP-hard|MHA48AWBXN]] when $f$ is given by its truth table.
When $f$ is given by a formula in disjunctive normal form, the problem is complete for the second level of the polynomial hierarchy, a result of Umans.
In practice, heuristic programs such as Espresso find short but not always shortest forms.
For example, $f = (x \wedge y) \vee (x \wedge \neg y)$ has two terms, and the shortest form is the single term $x$.

## Explanations

### L1 human

A logic circuit can often be built in many ways, some with far fewer gates than others.
Logic optimization asks for the cheapest one.
Even for the simple form of an OR of ANDs, finding the shortest formula is hard in general.
So practical tools combine exact methods for small parts with clever heuristics.
