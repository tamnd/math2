---
tag: K33VPAPJQG
kind: statement
role: theorem
name: Principle of explosion
aliases: [ex-falso-quodlibet, ex-contradictione-quodlibet, principle-of-pseudo-scotus]
msc: ["03B05", "03B53"]
topics: [NJB94B39QK]
audience: ug1
about: [TTKZGJEEK7, 029JBBF693, 1HK0VYWTV7]
uses: [TTKZGJEEK7, 1HK0VYWTV7, 029JBBF693, 0F72FK8EKB, 6EFJF9NAYX, H31CS3HK5P]
history:
  first_stated: "A version of the Lewis argument was found by William of Soissons in the twelfth century"
  notes: "The syntactic proof by disjunction introduction and disjunctive syllogism is called the Lewis argument, after C. I. Lewis."
sources:
  - url: https://en.wikipedia.org/wiki/Principle_of_explosion
    locator: lead section; Symbolic representation
  - url: https://plato.stanford.edu/entries/logic-paraconsistent/
    locator: Paraconsistent Logic (SEP entry), section 1.2
  - book: isbn:9780521670265
---

## Statement

Let $\varphi$ and $\psi$ be formulas of classical propositional logic.
Then
$$\set{\varphi, \neg\varphi} \vDash \psi.$$
Here $\vDash$ is classical [[logical consequence|1HK0VYWTV7]]: every [[valuation|H31CS3HK5P]] that makes all premises true makes the conclusion true.
In words: from a formula and its [[negation|029JBBF693]], every formula follows.
So classical consequence is [[explosive|TTKZGJEEK7]].

There are two proofs.
The [[Lewis argument|ZPCMHD9HJ7]] derives $\psi$ by [[disjunction|0F72FK8EKB]] introduction and [[disjunctive syllogism|6EFJF9NAYX]].
The [[semantic proof|RRWN8BHANP]] shows that no valuation makes both premises true.

## Remarks

### Why each hypothesis is needed

The statement has one hypothesis: the logic is classical.
It uses two features of classical logic: a valuation gives each formula exactly one of two values, and $\neg$ swaps them.

- If a valuation can give a formula both values, explosion fails. In the [[logic of paradox|AX6G3E9CQJ]], $v(p) = \mathsf{B}$ makes $p$ and $\neg p$ designated, and $q$ can be false.
- If the rule of disjunctive syllogism is dropped, the Lewis argument stops at the line $\varphi \lor \psi$, and this is what the logic of paradox does.
- If both premises are not given together, nothing follows: $\set{\varphi} \nvDash \psi$ when $\psi$ is a variable that does not occur in $\varphi$ and $\varphi$ is satisfiable.

### Consequences

- The formula $(\varphi \land \neg\varphi) \to \psi$ is a tautology, by the deduction theorem.
- A set of formulas is consistent if and only if some formula does not follow from it. So inconsistent theories are trivial.
- Proof by contradiction can end with any goal: once a branch contains $\varphi$ and $\neg\varphi$, the goal follows.

### Converse

The converse question is whether every formula that follows from all sets also follows from $\set{\varphi, \neg\varphi}$; this holds by monotonicity.
The more useful converse is false: $\set{\varphi, \neg\varphi} \vDash \psi$ does not mean that $\psi$ follows from $\varphi$ alone.
For example $\set{p} \nvDash q$, by the valuation $v(p) = 1$, $v(q) = 0$.

### Generalizations

- The Lewis argument shows: every [[consequence relation|J78Y1M4GND]] with disjunction introduction, disjunctive syllogism and transitivity is explosive.
- [[Intuitionistic logic is explosive|EQ9DND41TR]], and so is [[strong Kleene logic K3|2ZDYGB4J5N]].
- Logics of formal inconsistency keep a restricted form, gentle explosion: $\circ\varphi, \varphi, \neg\varphi \vdash \psi$.

## History

A version of the Lewis argument was found in the twelfth century by William of Soissons.
The argument is named after Lewis.
The rejection of the principle led to the paraconsistent logics of the twentieth century.

## Explanations

### L1 human

Suppose someone tells you "all lemons are yellow" and also "not all lemons are yellow".
From the first claim, the statement "all lemons are yellow, or unicorns exist" is true, since one part is true.
The second claim says the first part is false.
So the second part must be true: unicorns exist.
The same steps prove any statement in place of "unicorns exist".
This is the principle of explosion.

### L2 human

We check the principle with a truth table for $\varphi = p$ and $\psi = q$.

1. The four rows give $(p, q)$ the values $(1,1)$, $(1,0)$, $(0,1)$, $(0,0)$.
2. In the rows with $p = 1$, the premise $\neg p$ is $0$.
3. In the rows with $p = 0$, the premise $p$ is $0$.
4. So no row makes both premises true, and there is no row where the premises are true and $q$ is false.
5. By the definition of consequence, $\set{p, \neg p} \vDash q$.

The typical use is the last step of a proof by cases, when one case is impossible.
A trap is to think that the principle needs a "connection" between the premises and $q$; classical consequence needs none, which is one motive for relevance logic.

### L3 human

Explosion is equivalent, in the presence of the deduction theorem, to the validity of $\bot \to \psi$ and to the law that $a \land \neg a = 0$ in the algebraic semantics.
Paraconsistent logics block it in different places: the logic of paradox drops disjunctive syllogism, relevance logics change the conditional, discussive logic drops adjunction, and logics of formal inconsistency restrict explosion to consistent formulas.
The substructural view reads explosion as a combination of weakening with $\bot$-elimination; see the topic on [[substructural and relevance logics|98QF5J4W16]].
