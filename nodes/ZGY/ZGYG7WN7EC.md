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

Conditional logic is the logic of "if it were the case that $\varphi$, it would be the case that $\psi$", written $\varphi > \psi$.
Its idea is to test the consequent only in the closest worlds where the antecedent holds, so that the set of worlds tested changes with the antecedent.
In Stalnaker's semantics a selection function $f$ picks, for each formula $\varphi$ and world $w$, one closest $\varphi$-world $f(\varphi, w)$, and $\varphi > \psi$ is true at $w$ when $\psi$ is true at $f(\varphi, w)$.
In Lewis's semantics each world $w$ has a system of spheres $\$_w$, a set of sets of worlds that is linearly ordered by inclusion, and the system is centered when $\{w\} \in \$_w$.
Then $\varphi > \psi$ is true at $w$ when no sphere of $\$_w$ contains a $\varphi$-world, or when some sphere contains a $\varphi$-world and $\varphi \to \psi$ holds at all its worlds.
The logic of all centered sphere models is Lewis's $\mathsf{VC}$, and the logic of Stalnaker's models is $\mathsf{C2}$.

## Motivation

"If the match had been struck, it would have lit" is true.
"If the match had been struck and had been wet, it would have lit" is false.
So counterfactuals are not monotone: adding a conjunct to the antecedent can turn a true conditional into a false one.

The two familiar conditionals cannot model this.
The [[material conditional|0NMG7W7Q11]] is true whenever the antecedent is false, so it makes "if this match had been struck, it would have turned into a bird" true.
The [[strict conditional|5JW54NP52K]] $\square(\varphi \to \psi)$ avoids that, but it is monotone, because it checks every antecedent on the same set of worlds.
The fix is to let the antecedent choose the worlds: the closest worlds where the match is struck are dry, and the closest where it is struck and wet are farther away.

Ramsey's test gives the same picture for belief.
To judge "if $\varphi$ then $\psi$", add $\varphi$ to your beliefs, adjust them as little as possible, and check $\psi$.
Counterfactuals also sit under Lewis's analysis of causation and under causal models in statistics.

## Notation

Stalnaker writes $\varphi > \psi$ and Lewis writes $\varphi \mathrel{\square\!\!\rightarrow} \psi$ for the "would" conditional.
Lewis's "might" conditional is $\varphi \mathrel{\lozenge\!\!\rightarrow} \psi := \neg(\varphi > \neg\psi)$.
Some authors let the selection function $f(\varphi, w)$ return a set of worlds instead of one world.
Lewis's logics $\mathsf{V}$, $\mathsf{VW}$ and $\mathsf{VC}$ have no centering, weak centering and centering.
Watch the symbol $>$: it is a connective here, not an order, so $p > q$ is a formula and not a comparison.

## Remarks

### The match in a sphere model

Take worlds $w, u, v$ with spheres $\$_w = \{\{w\}, \{w, u\}, \{w, u, v\}\}$.
Let $p$ ("struck") be true at $u$ and $v$, $q$ ("lights") at $w$ and $u$, and $r$ ("wet") at $v$ only.
The smallest sphere that meets $p$ is $\{w, u\}$.
There $p \to q$ holds at $w$, where $p$ is false, and at $u$, where $q$ is true, so $p > q$ is true at $w$.
The only $(p \wedge r)$-world is $v$, so the antecedent $p \wedge r$ pushes us out to the whole set.
At $v$ the consequent $q$ fails, so $(p \wedge r) > q$ is false at $w$.

The same model refutes transitivity and contraposition, as [[the three-world model|PTQNQF2K3T]] shows step by step.
Watch out for the smallest sphere $\{w\}$: it contains no $p$-world, so it has no say about $p > q$.

### Stalnaker or Lewis

The two semantics differ on ties.
A Stalnaker selection function picks one closest world, so for each $\psi$ either $\psi$ or $\neg\psi$ holds there.
That makes conditional excluded middle $(\varphi > \psi) \vee (\varphi > \neg\psi)$ valid.
A Lewis sphere can hold two equally close $\varphi$-worlds that disagree on $\psi$, and then both disjuncts fail.
[[Conditional excluded middle|1JJ4GR402Y]] works both cases.

A classic test, which Lewis discusses, is a pair of counterfactuals: "if Bizet and Verdi had been compatriots, Bizet would have been Italian", and its twin with "Verdi would have been French".
Neither seems true, and that is evidence against the schema.
Stalnaker's logic $\mathsf{C2}$ is $\mathsf{VC}$ plus conditional excluded middle.

### The laws that remain

Some laws hold in every centered sphere model: $\varphi > \varphi$, the step $(\varphi > \psi) \to (\varphi \to \psi)$, and the step $(\varphi \wedge \psi) \to (\varphi > \psi)$.
The last two come from centering, since $\{w\}$ is the first sphere that meets a true antecedent.
Disjunction of antecedents is valid as well: $((\varphi > \chi) \wedge (\psi > \chi)) \to ((\varphi \vee \psi) > \chi)$.

For a fixed antecedent the operator $\varphi > \cdot$ is a normal box.
If $\vdash \psi \to \chi$ then $\vdash (\varphi > \psi) \to (\varphi > \chi)$, and $\varphi > \psi$ with $\varphi > \chi$ gives $\varphi > (\psi \wedge \chi)$.
Two weak forms of monotonicity survive.
Rational monotonicity infers $(\varphi \wedge \chi) > \psi$ from $\varphi > \psi$ and $\neg(\varphi > \neg\chi)$.
Cumulative transitivity infers $\varphi > \chi$ from $\varphi > \psi$ and $(\varphi \wedge \psi) > \chi$.
Lewis axiomatized $\mathsf{VC}$ and proved it complete for centered sphere models.

### What it is not

The strict conditional is not a variably strict conditional, because it obeys strengthening of the antecedent, as [[the strict conditional|5F6H9XXMVN]] proves.
The material conditional is not a counterfactual, since $\neg\varphi$ alone makes $\varphi \to \psi$ true.
A function with $f(\varphi, w) = w$ for every $\varphi$ is not a Stalnaker selection function either, because the selected world must satisfy $\varphi$.

### Watch out

The first trap is to treat $>$ as a strict conditional, so that strengthening holds and the wet match becomes a contradiction.
The second is to read "closest world" as "the actual world with one atom changed".
Closeness is part of the model, not a fixed metric.
The third is to infer $\varphi > \neg\psi$ from $\neg(\varphi > \psi)$.
That step is conditional excluded middle, and it fails in $\mathsf{VC}$ whenever two closest worlds disagree.

### History

The study of the strict conditional goes back to C. I. Lewis.
Ramsey stated his test for conditionals in a footnote of a 1929 paper.
Stalnaker gave the selection function semantics in 1968.
David Lewis gave the sphere semantics and the logics $\mathsf{V}$ to $\mathsf{VC}$ in Counterfactuals (1973).
Gärdenfors connected the Ramsey test with belief revision and proved his [[triviality theorem|WMZ1QP7KQY]] in 1986.

### Try it

First, in the match model, is $q > p$ true at $w$?
The first sphere that meets $q$ is $\{w\}$, and $p$ is false at $w$, so $q > p$ is false.

Second, in the same model, is $r > \neg q$ true at $w$?
The only $r$-world is $v$, it lies in the outer sphere, and $q$ is false at $v$, so $r > \neg q$ is true.

## Explanations

### L1 human

"If I had left earlier, I would have caught the train" is a counterfactual.
To judge it, imagine the situations most like the real one in which you left earlier.
If you catch the train in all of them, the sentence is true.
Adding a detail can change the answer: "if I had left earlier and the train had been canceled" sends you to other situations.
So the logic of this "if" does not let you add details freely.

### L2 human

We evaluate $p > q$ at $w$ when the worlds are ranked $w$ first, then $u$ and $v$ together.
The spheres are $\{w\}$ and $\{w, u, v\}$, and we let $p$ hold at $u$ and $v$, and $q$ at $u$ only.
The first sphere that meets $p$ is the outer one.
At $v$ the antecedent $p$ holds and $q$ fails, so $p > q$ is false at $w$.
Now split the tie by adding the sphere $\{w, u\}$.
The first sphere that meets $p$ becomes $\{w, u\}$, where $p \to q$ holds, so $p > q$ becomes true.
The typical use of such models is to test whether an inference with "would" is safe: you look for a ranking of worlds that makes the premises true and the conclusion false.

### L3 human

A system of spheres is a total preorder of worlds around each world, and $\varphi > \psi$ says that the minimal $\varphi$-worlds are $\psi$-worlds.
The same minimal-model semantics appears in Hansson's dyadic [[deontic logic|7B74J6J5JV]], in the preferential models of nonmonotonic logic, and in Grove's spheres for [[AGM belief revision|Y05YQN7HGQ]].
The laws $\varphi > \varphi$ and the disjunction of antecedents are also rules of the preferential consequence relations of Kraus, Lehmann and Magidor.

Through the Ramsey test, a sphere model for one belief state is a revision operator, and the [[Gärdenfors triviality theorem|WMZ1QP7KQY]] shows that the test cannot hold for all belief states that contain conditionals.
Selection-function semantics is the conditional analogue of neighborhood semantics, and Chellas's minimal conditional logic $\mathsf{CK}$ plays the role of $\mathsf{K}$.
