---
tag: 8PAJMAN8DM
kind: concept
name: Impossible world
aliases: [impossible-worlds, non-normal-world]
msc: ["03B45", "03B42"]
topics: [SPQVNPZDTB]
audience: research
uses: [NGHWZ9Y7ZV, C3RZY20ETK, G989VP2NGP, CN7HK9K1B6, C7YWCR87QJ]
sources:
  - wikipedia: en:3792679@r1281582499
    locator: Impossible world
    note: adopted
    mention: wikipedia://en/3792679
    sections: [Summary]
  - url: https://en.wikipedia.org/wiki/Impossible_world
    locator: Non-normal modal logics
  - url: https://en.wikipedia.org/wiki/Impossible_world
    locator: Applications
  - url: https://builds.openlogicproject.org/
    locator: Modal Logic
same_as:
  wikidata: Q6007516
  wikipedia: Impossible world
inventory: [26EVVFWFFK]
---

## Summary

Take a world $w$ that sees itself and a second world $n$, and declare $n$ non-normal: there, every formula $\square \varphi$ is false.
The tautology $p \vee \neg p$ is true at both worlds, so $\square(p \vee \neg p)$ is true at $w$.
But $\square(p \vee \neg p)$ is false at $n$, and $w$ sees $n$, so $\square \square(p \vee \neg p)$ is false at $w$.
One extra world has broken the rule of necessitation.

An *impossible world*, also called a *non-normal world*, is a point of a model at which the usual laws of logic or of $\square$ may fail.
Impossible worlds semantics adds such worlds to [[Kripke models|NGHWZ9Y7ZV]] and evaluates validity only at the possible, or normal, worlds.
It works because the impossible worlds are still accessible, so they change the truth of modal formulas at the normal worlds, without counting in the definition of validity.
Students slip on that last point: validity is checked at normal worlds only.

## Motivation

In a Kripke model every world obeys classical logic, so the [[modal logic|C3RZY20ETK]] is normal: it contains $\mathsf{K}$ and is closed under [[necessitation|G989VP2NGP]].
Some modal notions are not normal.
An agent who knows the axioms of arithmetic does not know all their consequences.
But in a normal epistemic logic, knowledge is closed under consequence, and this is the *problem of logical omniscience*.
Two formulas true at the same possible worlds, such as two tautologies, can still differ in content, and contexts that distinguish them are *hyperintensional*.
Impossible worlds separate such formulas, since a world can make one of them true and the other false.

## Notation

A *Kripke model with non-normal worlds* is $(W, N, R, V)$ with $N \subseteq W$ the set of normal worlds.
At $w \in N$, $\square \varphi$ is true when $\varphi$ is true at every $R$-successor, and at $w \in W \setminus N$, $\square \varphi$ is false for every $\varphi$.
The Boolean connectives are evaluated as usual at every world.
A formula is *valid* if it is true at every normal world of every model.
A *Rantala model* is $(W, P, R, V)$ with $P \subseteq W$ the possible worlds.
At $w \notin P$, the valuation assigns a truth value to every formula, not only to variables.

## Remarks

### Worked examples

The model of the Summary is checked in detail in [[a non-normal world refutes necessitation|S7CGCSAVMN]].
In a Rantala model, an agent can know $p$ and $p \to q$ without knowing $q$; see [[impossible worlds block logical omniscience|P2ZVNZDNHV]].
In a Rantala model, let a possible world $w$ see only one impossible world $i$.
Then $\square \varphi$ holds at $w$ exactly for the formulas true at $i$, and this set can be any set of formulas, even one containing $p \wedge \neg p$.

### Worked example: the axiom T survives

Let every normal world see itself, as in Kripke's semantics for $\mathsf{S2}$.
If $\square \varphi$ is true at a normal world $w$, then $\varphi$ is true at $w$, because $w R w$.
So $\square \varphi \to \varphi$ is valid, although at a non-normal world $\square \varphi$ is false and the implication holds there for another reason.

### Non-examples

A Kripke model in which every world is normal has no impossible worlds, and its knowledge operator is closed under known implication; see [[a Kripke model forces logical omniscience|ETA9WHZP38]].
A world where a contingent fact differs from the actual world, such as a world where it rains, is merely another possible world.

### The rules you can use

1. With non-normal worlds, every formula $\square \varphi$ is false at a non-normal world, and every formula $\lozenge \varphi$ is true there.
2. Kripke proved that the valid formulas form $\mathsf{S2}$ when $R$ is reflexive, and $\mathsf{S3}$ when $R$ is reflexive and transitive.
   With $R$ arbitrary they form a weaker non-normal logic, called $\mathsf{N}$ in some textbooks.
3. These logics contain $\square \varphi$ for every tautology $\varphi$, but not $\square \square (p \vee \neg p)$, so they are not closed under necessitation.
4. [[Neighborhood semantics|CN7HK9K1B6]] also avoids normality, but it still identifies logically equivalent formulas, and impossible worlds do not.

### History

Saul Kripke introduced non-normal worlds in 1965, in the second part of his "Semantical analysis of modal logic", to give semantics for the Lewis systems $\mathsf{S2}$ and $\mathsf{S3}$.
Jaakko Hintikka and Veikko Rantala proposed impossible worlds as a solution to the problem of logical omniscience in epistemic logic.
Graham Priest, Francesco Berto and Mark Jago developed impossible worlds for relevant logics, counterpossible conditionals and hyperintensional contents.

### Watch out

At Kripke's non-normal worlds the Boolean connectives behave classically, and only $\square$ is changed.
So a non-normal world in Kripke's sense is not a world where a contradiction is true; that happens only in Rantala's models.
Evaluating validity at all worlds is also a mistake, since then no formula $\square \varphi$ would be valid.

### Try it

In the model of the Summary, at which worlds is $\lozenge \bot$ true?
Answer: at $n$ only.
At $n$, $\lozenge \bot$ is $\neg \square \neg \bot$, and every boxed formula is false there, so $\lozenge \bot$ is true.
At $w$, $\lozenge \bot$ would need a successor where $\bot$ is true, so it is false.
Does this make $\lozenge \bot$ consistent with Kripke's logics?
Answer: no.
Validity is checked only at normal worlds, and $\neg \lozenge \bot$ holds at every normal world, so $\neg \lozenge \bot$ is valid.

## Explanations

### L1 human

A possible world is a complete way things could be, and it always respects the rules of logic.
An impossible world is a "way things could not be": in it a rule of logic may break.
Such worlds help to describe agents who make mistakes in reasoning, since the agent cannot rule them out.

### L2 human

Compare $\square(p \to p)$ and $\square(q \to q)$ in a Rantala model.
Let the possible world $w$ see the possible world $w$ itself and an impossible world $i$.
At $i$, let $p \to p$ be true and $q \to q$ false, which the valuation of impossible worlds allows.
Then $w \models \square(p \to p)$ and $w \not\models \square(q \to q)$, although the two formulas are true at every possible world.
The typical use is to give semantics to epistemic logics in which knowledge is not closed under logical equivalence.
Watch out: the impossible worlds take part in the truth conditions of $\square$, but not in the definition of validity.

### L3 human

Kripke's non-normal worlds keep classical logic inside each world and break only the modal clause, which gives the subnormal Lewis systems.
Rantala's worlds break everything, so any set of formulas can be the set known by an agent.
Then logical structure must be added back by constraints on the impossible worlds.
In hyperintensional semantics, impossible worlds play the role of fine-grained propositions, and the resulting logics are often relevant or [[paraconsistent|C7YWCR87QJ]].
