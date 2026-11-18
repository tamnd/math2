---
tag: ZGYG7WN7EC
kind: concept
name: Conditional logic
msc: ["03B45", "03B60"]
topics: [CQM9SRN8PM]
audience: research
uses: [C3RZY20ETK, 6BQ71KQ6QT, 0NMG7W7Q11, 5JW54NP52K]
aliases: [counterfactual-logic]
sources:
  - wikipedia: en:76765067@r1368301704
    locator: Glossary of logic, section C
    note: adopted
    mention: wikipedia://en/76765067#8C5G
    sections: [Summary]
  - url: https://en.wikipedia.org/wiki/Conditional_logic
    locator: Possible worlds semantics
  - url: https://en.wikipedia.org/wiki/Counterfactual_conditional
    locator: Variably strict conditional
  - book: isbn:9780631224259
    locator: Lewis, Counterfactuals
inventory: [VNQ9G94612]
---

## Summary

Conditional logic studies a binary connective $\varphi > \psi$, read "if $\varphi$ were the case, $\psi$ would be the case", with a semantics of possible worlds.
In Stalnaker's semantics, a selection function $f$ picks for each formula $\varphi$ and world $w$ the closest $\varphi$-world $f(\varphi, w)$, and $\varphi > \psi$ is true at $w$ when $\psi$ is true at $f(\varphi, w)$.
In Lewis's semantics, each world $w$ has a system of spheres $\$_w$, a set of sets of worlds that is linearly ordered by inclusion.
The system is centered when $\set{w}$ belongs to $\$_w$.
Then $\varphi > \psi$ is true at $w$ when no sphere of $\$_w$ contains a $\varphi$-world, or some sphere contains a $\varphi$-world and $\varphi \to \psi$ holds at all its worlds.
The logic of all centered sphere models is Lewis's $\mathsf{VC}$; the logic of Stalnaker's models is $\mathsf{C2}$.
Conditional logic matters because counterfactual and hypothetical reasoning is not monotone, and these logics give exact rules for it.

## Motivation

The [[material conditional|0NMG7W7Q11]] makes "if $\varphi$ then $\psi$" true whenever $\varphi$ is false.
So it makes every counterfactual with a false antecedent true, including "if this match had been struck, it would have turned into a bird".
The [[strict conditional|5JW54NP52K]] $\square(\varphi \to \psi)$ avoids this, but it is monotone: it gives $\square((\varphi \wedge \chi) \to \psi)$ for every $\chi$.
Counterfactuals are not monotone.
"If the match had been struck, it would have lit" is true, while "if the match had been struck and had been wet, it would have lit" is false.
The fix is to look only at the closest worlds where the antecedent holds, and closeness depends on the antecedent.
Ramsey's test gives the same picture for belief: to judge "if $\varphi$ then $\psi$", add $\varphi$ to your beliefs, adjust them minimally, and check $\psi$.

## Notation

1. $\varphi > \psi$ (Stalnaker) or $\varphi \mathrel{\square\!\!\rightarrow} \psi$ (Lewis) is the "would" conditional.
2. Lewis's "might" conditional is $\varphi \mathrel{\lozenge\!\!\rightarrow} \psi := \neg(\varphi > \neg\psi)$.
3. $f(\varphi, w)$ is a selection function; some authors let it return a set of worlds instead of one world.
4. $\$_w$ is the system of spheres around $w$; $\mathsf{V}$, $\mathsf{VW}$, $\mathsf{VC}$ are Lewis's logics with no centering, weak centering and centering.

## Remarks

### Examples

1. In a three-world sphere model, $p > q$ is true while $(p \wedge r) > q$ is false. The same model refutes transitivity and contraposition, see [[the failure of strengthening|~cec455a6]].
2. Conditional excluded middle $(p > q) \vee (p > \neg q)$ is valid for Stalnaker's selection functions and fails in $\mathsf{VC}$, see [[conditional excluded middle|~48e4297a]].
3. "If Bizet and Verdi had been compatriots, Bizet would have been Italian" is a classical example, used by Lewis. Neither it nor its "French" twin seems true, which argues against conditional excluded middle.
4. The Ramsey test for belief sets says that $(\varphi > \psi) \in K$ exactly when $\psi \in K * \varphi$, where $*$ is a revision operator. It links conditional logic with [[AGM belief revision|~30b6c328]].

### Non-examples

1. The strict conditional $\square(\varphi \to \psi)$ is not a variably strict conditional: it obeys strengthening of the antecedent, see [[the strict conditional|~9312723e]].
2. The material conditional $\varphi \to \psi$ is not a counterfactual conditional: $\neg\varphi$ alone makes it true.
3. A selection function with $f(\varphi, w) = w$ for every $\varphi$ is not a Stalnaker model. It breaks the condition that the selected world satisfies $\varphi$.

### Basic properties

1. The following principles are valid in all centered sphere models: $\varphi > \varphi$; $(\varphi > \psi) \to (\varphi \to \psi)$; $(\varphi \wedge \psi) \to (\varphi > \psi)$; $((\varphi > \chi) \wedge (\psi > \chi)) \to ((\varphi \vee \psi) > \chi)$.
2. Rational monotonicity is valid in sphere models: $((\varphi > \psi) \wedge \neg(\varphi > \neg\chi)) \to ((\varphi \wedge \chi) > \psi)$.
3. If $\vdash \psi \to \chi$ then $\vdash (\varphi > \psi) \to (\varphi > \chi)$, and $(\varphi > \psi) \wedge (\varphi > \chi)$ gives $\varphi > (\psi \wedge \chi)$. So for a fixed antecedent, $\varphi > \cdot$ is a normal box.
4. Strengthening of the antecedent, transitivity and contraposition all fail, see [[the three-world model|~cec455a6]].
5. Lewis axiomatized $\mathsf{VC}$ and proved completeness for centered sphere models; Stalnaker's $\mathsf{C2}$ is $\mathsf{VC}$ plus conditional excluded middle.
6. The law $\varphi > \varphi$ and the disjunction law of item 1 are also rules of the preferential consequence relations of Kraus, Lehmann and Magidor in nonmonotonic reasoning.

### History

The study of the strict conditional goes back to Clarence Irving Lewis.
Ramsey stated the test for conditionals in a footnote of a 1929 paper.
Stalnaker gave the selection function semantics in 1968, and David Lewis gave the sphere semantics and the logics $\mathsf{V}$ to $\mathsf{VC}$ in Counterfactuals (1973).
Gärdenfors connected the Ramsey test with belief revision and proved his [[triviality theorem|WMZ1QP7KQY]] in 1986.

### Common errors

1. Treating $>$ as a strict conditional. Then strengthening holds, and the wet match example becomes a contradiction.
2. Reading "closest world" as "the actual world with one atom changed". Closeness is a parameter of the model, not a fixed metric.
3. Assuming that $\neg(\varphi > \psi)$ gives $\varphi > \neg\psi$. This step is conditional excluded middle, which fails in $\mathsf{VC}$.

## Explanations

### L1 human

"If I had left earlier, I would have caught the train" is a counterfactual.
To judge it, imagine the situations most like the real one in which you left earlier.
If you catch the train in all of them, the sentence is true.
Adding a detail can change the answer: "if I had left earlier and the train had been cancelled" gives a different result.
So the logic of "if" here does not let you add details freely.

### L2 human

We evaluate $p > q$ in a sphere model.

1. Take worlds $w, u, v$ and spheres $\$_w = \set{\set{w}, \set{w, u}, \set{w, u, v}}$.
2. Let $p$ be false at $w$, true at $u$ and $v$; let $q$ be true at $u$ only.
3. The smallest sphere that contains a $p$-world is $\set{w, u}$.
4. In it, $p \to q$ holds at $w$, since $p$ is false there, and at $u$, since $q$ is true there.
5. So $p > q$ is true at $w$, although $v$ is a $p$-world where $q$ fails.

The typical use is to model "would" statements in philosophy, linguistics and AI, and to test which inferences with them are safe.
A trap: a sphere must contain a $p$-world before it decides $p > q$; the smaller sphere $\set{w}$ says nothing about $p$.

### L3 human

Sphere systems are total preorders of worlds, one for each world, and $\varphi > \psi$ says that the minimal $\varphi$-worlds are $\psi$-worlds.
The same minimal-model semantics appears in Hansson's dyadic [[deontic logic|~19b899d4]], in the preferential models of nonmonotonic logic, and in Grove's spheres for [[AGM belief revision|~30b6c328]].
Through the Ramsey test, sphere models for one belief state are revision operators, and the [[Gärdenfors triviality theorem|WMZ1QP7KQY]] shows that the test cannot hold for all belief states with conditionals inside them.
Selection-function semantics is the conditional analogue of neighbourhood semantics, and the minimal conditional logic $\mathsf{CK}$ plays the role of $\mathsf{K}$.
Counterfactuals are also the base of Lewis's analysis of causation and of causal models in statistics.
