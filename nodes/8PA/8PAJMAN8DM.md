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

An *impossible world*, also called a *non-normal world*, is a point of a world-based model at which the usual laws of logic may fail.
At such a world a contradiction $p \wedge \neg p$ may be true, a tautology may be false, or every formula $\square \varphi$ may be false.
*Impossible worlds semantics* adds such worlds to [[Kripke models|NGHWZ9Y7ZV]] and evaluates validity only at the possible, or normal, worlds.
The impossible worlds are still accessible, so they change the truth of modal formulas at the normal worlds.
Two main versions are Kripke's non-normal worlds for the Lewis systems $\mathsf{S2}$ and $\mathsf{S3}$, and Rantala's models, where formulas get arbitrary values at impossible worlds.

## Motivation

In a Kripke model, every world obeys classical logic, and so the [[modal logic|C3RZY20ETK]] is normal: it contains $\mathsf{K}$ and is closed under [[necessitation|G989VP2NGP]].
Some modal notions are not normal.
An agent who knows the axioms of arithmetic does not know all their consequences, but in a normal epistemic logic knowledge is closed under consequence: this is the *problem of logical omniscience*.
Two formulas that are true at the same possible worlds, such as two tautologies, can still differ in content; contexts that distinguish them are *hyperintensional*.
Impossible worlds separate such formulas, since a world can make one of them true and the other false.

## Notation

A *Kripke model with non-normal worlds* is $(W, N, R, V)$ with $N \subseteq W$ the set of normal worlds.
At $w \in N$, $\square \varphi$ is true iff $\varphi$ is true at every $R$-successor; at $w \in W \setminus N$, $\square \varphi$ is false for every $\varphi$.
The Boolean connectives are evaluated as usual at every world.
A formula is *valid* if it is true at every normal world of every model.
A *Rantala model* is $(W, P, R, V)$ with $P \subseteq W$ the possible worlds; at $w \notin P$, the valuation assigns a truth value to every formula, not only to variables.

## Remarks

### Examples

1. In a model with one normal and one non-normal world, $\square(p \vee \neg p)$ is valid but $\square \square(p \vee \neg p)$ is not, so necessitation fails; see [[a non-normal world refutes necessitation|S7CGCSAVMN]].
2. In a Rantala model, an agent can know $p$ and $p \to q$ without knowing $q$; see [[impossible worlds block logical omniscience|P2ZVNZDNHV]].

### Non-examples

1. A Kripke model in which every world is normal has no impossible worlds, and its knowledge operator is closed under known implication; see [[a Kripke model forces logical omniscience|ETA9WHZP38]].
2. A world at which a contingent fact differs from the actual world, such as a world where it rains, is merely another possible world, not an impossible one.

### Basic properties

1. With non-normal worlds, every formula $\square \varphi$ is false at a non-normal world, and every formula $\lozenge \varphi$ is true there.
2. Kripke proved that the valid formulas form $\mathsf{S2}$ when $R$ is reflexive, and $\mathsf{S3}$ when $R$ is reflexive and transitive. With $R$ arbitrary, they form a weaker non-normal logic, often called $\mathsf{N}$.
3. These logics contain $\square \varphi$ for every tautology $\varphi$, but they do not contain $\square \square (p \vee \neg p)$, so they are not closed under necessitation.
4. In a Rantala model, let a possible world $w$ see only one impossible world $i$. Then $\square \varphi$ holds at $w$ exactly for the formulas true at $i$, and this set can be any set of formulas.
5. [[Neighborhood semantics|CN7HK9K1B6]] is another way to avoid normality, but it still identifies formulas that are logically equivalent; impossible worlds do not.

### History

Saul Kripke introduced non-normal worlds in 1965, in the second part of his "Semantical analysis of modal logic", to give semantics for the Lewis systems $\mathsf{S2}$ and $\mathsf{S3}$.
Jaakko Hintikka and Veikko Rantala proposed impossible worlds as a solution to the problem of logical omniscience in epistemic logic.
Graham Priest, Francesco Berto and Mark Jago developed impossible worlds for relevant logics, counterpossible conditionals and hyperintensional contents.

### Common errors

1. Confusing a non-normal world in Kripke's sense with a world where a contradiction is true. At Kripke's non-normal worlds the Boolean connectives behave classically; only $\square$ is changed.
2. Evaluating validity at all worlds. Then no formula $\square \varphi$ would be valid, since it fails at a non-normal world.
3. Expecting $\square \varphi \to \varphi$ to fail because of non-normal worlds. In the semantics for $\mathsf{S2}$, every normal world sees itself, so $\square \varphi \to \varphi$ is valid.

## Explanations

### L1 human

A possible world is a complete way things could be, and it always respects the rules of logic.
An impossible world is a "way things could not be": in it a rule of logic may break.
Such worlds help to describe agents who make mistakes in reasoning, since the agent cannot rule them out.

### L2 human

1. Take a normal world $w$ that sees itself and a non-normal world $n$.
2. The formula $p \vee \neg p$ is true at both worlds, so $\square(p \vee \neg p)$ is true at $w$.
3. At $n$ every boxed formula is false, so $\square(p \vee \neg p)$ is false at $n$.
4. Since $w$ sees $n$, $\square \square(p \vee \neg p)$ is false at $w$.

The typical use is to give semantics to modal and epistemic logics that are not normal.
A trap: the impossible worlds take part in the truth conditions of $\square$, but not in the definition of validity.

### L3 human

Kripke's non-normal worlds keep classical logic inside each world and break only the modal clause, which gives the subnormal Lewis systems.
Rantala's worlds break everything, which gives a semantics in which any set of formulas can be the set known by an agent; then logical structure must be added back by constraints on the impossible worlds.
In hyperintensional semantics, impossible worlds play the role of fine-grained propositions, and the resulting logics are often relevant or [[paraconsistent|C7YWCR87QJ]].
