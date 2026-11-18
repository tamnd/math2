---
tag: P2ZVNZDNHV
kind: example
name: Impossible worlds block logical omniscience
msc: ["03B45", "03B42"]
topics: [SPQVNPZDTB]
audience: research
instance_of: [8PAJMAN8DM]
uses: [8PAJMAN8DM, NGHWZ9Y7ZV]
sources:
  - url: https://en.wikipedia.org/wiki/Impossible_world
    locator: Applications
  - url: https://builds.openlogicproject.org/
    locator: Modal Logic
---

## Example

Read $\square \varphi$ as "the agent knows $\varphi$".
Let $W = \set{w, i}$ with $w$ possible and $i$ an [[impossible world|8PAJMAN8DM]], and let $R = \set{(w, w), (w, i)}$.
At $w$, variables get values as usual: $p$ and $q$ are true.
At $i$, as in a Rantala model, every formula gets a value directly.
At $i$, let $p$ and $p \to q$ be true, let $q$ be false, and let $q \vee \neg q$ be false.

1. At $w$, the formulas $p$, $p \to q$, $q$ and $q \vee \neg q$ are true, by the classical clauses.
2. $p$ is true at both successors $w$ and $i$ of $w$, so $w \models \square p$.
3. $p \to q$ is true at $w$ and at $i$, so $w \models \square(p \to q)$.
4. $q$ is false at $i$, so $w \not\models \square q$.
5. So at $w$ the agent knows $p$ and $p \to q$ but not $q$: knowledge is not closed under known implication.
6. $q \vee \neg q$ is false at $i$, so $w \not\models \square(q \vee \neg q)$: the agent does not know this tautology.

## Remarks

Steps 4 and 6 show the two forms of logical omniscience that fail: closure of knowledge under consequence, and knowledge of all tautologies.
In an ordinary [[Kripke model|NGHWZ9Y7ZV]], both forms hold, since every accessible world is classical.
The price is that the semantics validates almost no epistemic principle; constraints on the impossible worlds restore the principles that are wanted.

## Explanations

### L1 human

The agent cannot rule out a "world" in which $p$ holds and "$p$ implies $q$" holds, but $q$ fails.
Such a world breaks logic, but the agent has not done the reasoning that rules it out.
So the agent knows the premises without knowing the conclusion.

### L2 human

1. List the formulas true at $i$: $p$ and $p \to q$; list the formulas false at $i$: $q$ and $q \vee \neg q$.
2. The agent at $w$ knows a formula iff it is true at $w$ and at $i$.
3. $p$ and $p \to q$ pass this test; $q$ and $q \vee \neg q$ do not.

The typical use is to model agents with limited reasoning power.
A trap: at $i$ the value of $p \to q$ is not computed from the values of $p$ and $q$; it is given directly.
