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

A recovery is better than no recovery, whatever the treatment costs, so recovery is good in the sense that it is better than its own negation.
Axiological logic, or the logic of value, deals with value concepts such as good, bad, indifferent and better, including ethical and aesthetic values, often in the setting of modal logic.
Its basic notion is a betterness relation between propositions, $p \succ q$ for "$p$ is better than $q$" and $p \succeq q$ for "$p$ is at least as good as $q$".
The proposition $p$ is good, $\mathrm{G}p$, when $p \succ \neg p$, and it is bad, $\mathrm{B}p$, when $\neg p \succ p$.
It is indifferent when it is neither good nor bad.
In a possible-worlds semantics, a [[preference relation|5W4SQ86GPS]] $\le$ on worlds, a total [[preorder|0VABYWJWH9]], is lifted to propositions.
On the all-all lifting, $p \succ q$ holds when $|p \wedge \neg q|$ and $|\neg p \wedge q|$ are nonempty and every world in the first set is strictly better than every world in the second.

## Motivation

Reasoning about values uses comparisons: one outcome is better than another, and an action is good because it is better than not doing it.
These comparisons obey laws, such as asymmetry, and they also invite fallacies, such as the step from $p \succ q$ and $q \succ r$ to $p \succ r$ for arbitrary propositions.
Deontic logic studies what ought to be, and many accounts explain "ought" by "best", so a logic of "better" is a foundation for deontic logic.
A formal logic of value separates the laws that hold for every betterness relation from those that depend on substantive views, and it makes precise the inferences that ethics and decision theory draw from comparisons of value.

## Notation

We write $p \succ q$ for "$p$ is better than $q$", $p \succeq q$ for "$p$ is at least as good as $q$", and $p \approx q$ for "$p$ and $q$ are equally good".
$\mathrm{G}p$ and $\mathrm{B}p$ say that $p$ is good and that $p$ is bad.
On a set $W$ of worlds, $w \le v$ says that world $v$ is at least as good as world $w$, and $|p|$ is the set of worlds where $p$ holds.

## Remarks

### A first ranking

Take atoms $p$ ("the patient recovers") and $q$ ("the treatment is cheap"), write a world as $ab$ with $a$ the value of $p$ and $b$ the value of $q$, and rank $11 > 10 > 01 > 00$.
The worst $p$-world, $10$, is better than the best $\neg p$-world, $01$, so $p$ is good on the all-all lifting.
The formula $q$ is indifferent there, because $01 < 10$ and $00 < 11$.
Yet $q$ is good ceteris paribus, since $11 > 10$ and $01 > 00$, as [[a value ranking on four worlds|Q30PEWXTJ6]] shows.

### The laws you can use

Asymmetry holds: $p \succ q$ excludes $q \succ p$.
It needs the nonemptiness condition, since without it $p \succ q$ and $q \succ p$ would both hold vacuously when $p$ implies $q$.
So no proposition is both good and bad.
Von Wright's conjunctive expansion, $p \succ q$ exactly when $(p \wedge \neg q) \succ (\neg p \wedge q)$, holds by definition on the all-all lifting, and it gives contraposition, as [[von Wright's preference principles|SX1BBMRE98]] shows.
Contraposition makes $\mathrm{G}p$ equivalent to $\mathrm{B}\neg p$.
On the all-all lifting, $\mathrm{G}p$ and $\mathrm{G}q$ imply $\mathrm{G}(p \wedge q)$.

### Which lifting

The all-all lifting compares every world where only $p$ holds with every world where only $q$ holds.
The ceteris paribus lifting compares only $p$-worlds and $\neg p$-worlds that agree on all other atoms, and it gives a different notion of good.
Other liftings compare the best worlds, or the worst worlds, of the two propositions.
Each lifting formalizes a different value judgment, so a value principle is valid or invalid only relative to a lifting.

### What it is not

A cyclic betterness $a \succ b$, $b \succ c$, $c \succ a$ among three pairwise incompatible outcomes is not the all-all lifting of any preorder of worlds, as [[cyclic betterness|92RQC86NTE]] shows.
Probability is not a value, since $p$ can be more probable than $q$ while $q$ is better than $p$, and the two orders obey different laws.

### Watch out

The first trap is to read "good" as "better than average" or "better than the status quo".
In the logic of value, $\mathrm{G}p$ compares $p$ with its negation.
The second trap is to expect the order on propositions to inherit every property of the order on worlds.
On the ranking $11 > 10 > 01 > 00$, we have $q \succ (p \leftrightarrow q)$ by $01 > 00$ and $(p \leftrightarrow q) \succ \neg q$ by $11 > 10$.
But $q \succ \neg q$ fails, since $01 < 10$, so transitivity fails after lifting.

### History

Sören Halldén's "On the logic of 'better'" (1957) and Georg Henrik von Wright's The Logic of Preference (1963) began the formal study of betterness and value.
Von Wright stated the principle of conjunctive expansion and used ceteris paribus comparisons of states of affairs.
Later work gave possible-worlds semantics for preference, studied the different liftings from worlds to propositions, and built dynamic logics of preference change.
The link with [[deontic logic|7B74J6J5JV]] goes through the reading of "it ought to be that $p$" as "the best worlds are $p$-worlds".

### Try it

First, on the ranking $11 > 10 > 01 > 00$, is $p \vee q$ good?
Its worlds are $11$, $10$ and $01$, and the only other world is $00$, the worst, so $p \vee q$ is good.

Second, on the same ranking, is $q \succ \neg p$?
The worlds where only $q$ holds are those of $q \wedge p$, that is $11$, and the worlds where only $\neg p$ holds are those of $\neg p \wedge \neg q$, that is $00$.
Since $11 > 00$, the answer is yes.

## Explanations

### L1 human

Axiological logic studies the word "better" and the words built from it.
"Good" means better than the opposite: it is good that it rains if rain is better than no rain.
"Bad" means worse than the opposite.
The logic finds which conclusions follow, for example that nothing can be both good and bad.

### L2 human

We check $\mathrm{G}p$ on the worlds $11 > 10 > 01 > 00$ for the atoms $p, q$ with the all-all lifting.

1. The $p$-worlds are $11$ and $10$, and the $\neg p$-worlds are $01$ and $00$.
2. The worst $p$-world, $10$, is better than the best $\neg p$-world, $01$.
3. So every $p$-world beats every $\neg p$-world, and $p$ is good.

The typical use is to compare ethical principles by the inferences they license.
Watch out: the conclusion depends on the lifting from worlds to propositions, so state the lifting before drawing an inference.

### L3 human

A betterness order on worlds is the same structure as a plausibility order in belief revision or a sphere system in conditional logic, read as value instead of likelihood.
Dyadic deontic logic uses it to define conditional obligation: $p$ ought to be the case given $q$ when the best $q$-worlds are $p$-worlds.
Modal preference logics add a modality for "at some better world" and express several liftings as modal formulas.
