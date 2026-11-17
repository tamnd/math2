---
tag: ~f5ae30ed
kind: example
name: A formula and its negation as equisatisfiable formulas
msc: ["03B05"]
topics: [JDK63589SA]
audience: ug2
instance_of: [B37TYWXS74]
uses: [QN7M1JCGT9, 0JMR2HM2N2, 029JBBF693]
sources:
  - url: https://en.wikipedia.org/wiki/Equisatisfiability
    locator: lead section
---

## Example

Let $p$ be a propositional variable.
We show that $p$ and $\neg p$ are equisatisfiable, although no assignment makes both true.

1. The assignment $v(p) = 1$ satisfies $p$, so $p$ is satisfiable.
2. The assignment $w(p) = 0$ gives $\bar w(\neg p) = 1$ by the truth table of [[negation|029JBBF693]], so $\neg p$ is satisfiable.
3. Both formulas are satisfiable, so each is satisfiable if and only if the other is; they are equisatisfiable.
4. Every assignment $u$ gives $\bar u(p) \neq \bar u(\neg p)$, so no assignment makes both true. In particular they are not [[logically equivalent|0JMR2HM2N2]].

## Remarks

The example shows that equisatisfiable formulas can have disjoint sets of models.
It also shows that equisatisfiability does not respect the connectives: $p$ and $\neg p$ are equisatisfiable, and $p$ and $p$ are equisatisfiable, but $p \land p$ is satisfiable while $p \land \neg p$ is not.
The same holds for every formula $\varphi$ that is neither a tautology nor unsatisfiable: then $\varphi$ and $\neg \varphi$ are both satisfiable, so they are equisatisfiable.
If $\varphi$ is a tautology, then $\neg \varphi$ is unsatisfiable, and $\varphi$ and $\neg \varphi$ are not equisatisfiable.

## Explanations

### L1 human

"The coin shows heads" and "the coin does not show heads" are both possible.
So they are equisatisfiable, since each can be made true.
But they can never be true at the same time.
Equisatisfiable means only "possible together with possible", not "true together".

### L2 human

We find all formulas in the variable $p$ that are equisatisfiable with $p$.

1. Up to equivalence, the formulas in $p$ alone are $p$, $\neg p$, $p \lor \neg p$ and $p \land \neg p$, one for each function from $\set{0, 1}$ to $\set{0, 1}$.
2. The first three are satisfiable, and the last is not.
3. So $p$ is equisatisfiable with formulas equivalent to $p$, $\neg p$ and $p \lor \neg p$, and not with $p \land \neg p$.

The typical use: this shows how coarse the relation is, with only two classes.
A trap: an equisatisfiable replacement inside a larger formula can change the answer, as the remark with $p \land \neg p$ shows.
