---
tag: 4BRXSBXXWG
kind: concept
name: Axiological logic
aliases: [logic-of-value, logic-of-better, preference-logic]
msc: ["03B45", "03A05"]
topics: [CQM9SRN8PM]
audience: grad
uses: [5W4SQ86GPS, 0VABYWJWH9, 09K9MWD2QQ]
sources:
  - wikipedia: en:76765067@r1368301704
    locator: Glossary of logic, section A
    note: adopted
    mention: wikipedia://en/76765067#6SL5
    sections: [Summary]
  - url: https://en.wikipedia.org/wiki/Value_theory
    locator: Absolute and relative
  - url: https://en.wikipedia.org/wiki/Value_theory
    locator: Evaluative terms
inventory: [JQ2VFSANTG]
---

## Summary

Axiological logic, or the logic of value, is the branch of logic that deals with value concepts such as good, bad, indifferent and better, including ethical and aesthetic values, often in the context of modal logic.
Its basic notion is a betterness relation $p \succ q$, "$p$ is better than $q$", between propositions, and $p \succeq q$, "$p$ is at least as good as $q$".
The monadic value notions are defined from it:

1. $p$ is good, $\mathrm{G}p$, iff $p \succ \neg p$;
2. $p$ is bad, $\mathrm{B}p$, iff $\neg p \succ p$;
3. $p$ is indifferent iff neither $\mathrm{G}p$ nor $\mathrm{B}p$.

In a possible-worlds semantics, a [[preference relation|5W4SQ86GPS]] $\le$ on worlds, a total [[preorder|0VABYWJWH9]], is lifted to propositions.
On the all-all lifting, $p \succ q$ holds iff $|p \wedge \neg q|$ and $|\neg p \wedge q|$ are nonempty and every world in the first set is strictly better than every world in the second.
The logic matters because it makes precise the inferences that ethics, decision theory and the semantics of "ought" draw from comparisons of value.

## Motivation

Reasoning about values uses comparisons: one outcome is better than another, an action is good because it is better than not doing it.
These comparisons obey laws, such as asymmetry, and they also invite fallacies, such as inferring that a conjunction of goods is good in every reading.
Deontic logic studies what ought to be, and many accounts explain "ought" by "best", so a logic of "better" is a foundation for deontic logic.
A formal logic of value separates the laws that hold for every betterness relation from those that depend on substantive views.

## Notation

1. $p \succ q$: $p$ is better than $q$; $p \succeq q$: $p$ is at least as good as $q$; $p \approx q$: $p$ and $q$ are equally good.
2. $\mathrm{G}p$, $\mathrm{B}p$: $p$ is good, $p$ is bad.
3. $w \le v$: world $v$ is at least as good as world $w$, on a set $W$ of worlds; $|p|$ is the set of worlds where $p$ holds.

## Remarks

### Examples

1. On four worlds over atoms $p, q$ ranked $11 > 10 > 01 > 00$, the formula $p$ is good and $q$ is indifferent on the all-all lifting, although $q$ is good ceteris paribus, see [[a value ranking on four worlds|~179ca374]].
2. Von Wright's principle of conjunctive expansion, $p \succ q$ iff $(p \wedge \neg q) \succ (\neg p \wedge q)$, holds by definition on the all-all lifting and gives contraposition, see [[von Wright's preference principles|~6048cd3b]].
3. Under the all-all lifting, $\mathrm{G}p$ and $\mathrm{G}q$ imply $\mathrm{G}(p \wedge q)$.

### Non-examples

1. A cyclic betterness $p \succ q$, $q \succ r$, $r \succ p$ among three pairwise incompatible outcomes is not the all-all lifting of any preorder of worlds, see [[cyclic betterness|~89be0e6d]].
2. Probability is not a value: $p$ can be more probable than $q$ while $q$ is better than $p$, and the two orders obey different laws.

### Basic properties

1. Asymmetry: $p \succ q$ implies not $q \succ p$. The nonemptiness condition is needed here; without it, $p \succ q$ and $q \succ p$ would both hold vacuously when $p$ implies $q$.
2. $\mathrm{G}p$ iff $\mathrm{B}\neg p$, since both say $p \succ \neg p$.
3. No proposition is both good and bad, by asymmetry.
4. On the all-all lifting, transitivity of $\succ$ between propositions can fail, although the order of worlds is transitive, because the comparisons $p \wedge \neg q$ versus $\neg p \wedge q$ change with the pair.
5. The ceteris paribus reading compares $p$-worlds and $\neg p$-worlds that agree on all other atoms; it gives a different notion of good from the all-all reading.

### History

Sören Halldén's "On the logic of 'better'" (1957) and Georg Henrik von Wright's The Logic of Preference (1963) began the formal study of betterness and value.
Von Wright stated the principle of conjunctive expansion and used ceteris paribus comparisons of states of affairs.
Later work gave possible-worlds semantics for preference and studied the different liftings from worlds to propositions, and dynamic logics of preference change.
The link with [[deontic logic|~19b899d4]] goes through the reading of "it ought to be that $p$" as "the best worlds are $p$-worlds".

### Common errors

1. Reading "good" as "better than average" or "better than the status quo". In the logic of value, $\mathrm{G}p$ compares $p$ with its negation.
2. Assuming that the betterness order on propositions inherits every property of the order on worlds. Totality and transitivity can fail after lifting.
3. Assuming that one lifting is the correct one. All-all, ceteris paribus and other liftings formalize different value judgements.

## Explanations

### L1 human

Axiological logic studies the word "better" and the words built from it.
"Good" means better than the opposite: it is good that it rains if rain is better than no rain.
"Bad" means worse than the opposite.
The logic finds which conclusions follow, for example that nothing can be both good and bad.

### L2 human

We check $\mathrm{G}p$ on worlds $11 > 10 > 01 > 00$ for the atoms $p, q$ with the all-all lifting.

1. The $p$-worlds are $11$ and $10$, and the $\neg p$-worlds are $01$ and $00$.
2. The worst $p$-world, $10$, is better than the best $\neg p$-world, $01$.
3. So every $p$-world beats every $\neg p$-world, and $p$ is good.

The typical use is to compare ethical principles by the inferences they license.
A trap: the conclusion depends on the lifting from worlds to propositions, so state the lifting before drawing an inference.

### L3 human

A betterness order on worlds is the same structure as a plausibility order in belief revision or a sphere system in conditional logic, read as value instead of likelihood.
Dyadic deontic logic uses it to define conditional obligation: $p$ ought to be the case given $q$ iff the best $q$-worlds are $p$-worlds.
Modal preference logics add a modality for "at some better world" and express several liftings as modal formulas.
