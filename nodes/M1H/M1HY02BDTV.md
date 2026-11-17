---
tag: M1HY02BDTV
kind: example
name: A satisfiable formula and a contradiction are not equisatisfiable
msc: ["03B05"]
topics: [JDK63589SA]
audience: ug2
not_instance_of:
  - target: B37TYWXS74
    note: p is satisfiable by v(p) = 1, while p ∧ ¬p is false under every assignment, so the two formulas differ in satisfiability
uses: [QN7M1JCGT9, 025YZN3VJW, 029JBBF693]
sources:
  - url: https://en.wikipedia.org/wiki/Equisatisfiability
    locator: lead section
---

## Example

Let $p$ be a propositional variable.
We show that $p$ and $p \land \neg p$ are not equisatisfiable.

1. The assignment $v(p) = 1$ satisfies $p$, so $p$ is satisfiable.
2. Let $w$ be any assignment. If $w(p) = 1$, then $\bar w(\neg p) = 0$; if $w(p) = 0$, then $\bar w(p) = 0$.
3. In both cases one conjunct of $p \land \neg p$ is false, so $\bar w(p \land \neg p) = 0$ by the truth table of [[conjunction|025YZN3VJW]].
4. So $p \land \neg p$ is unsatisfiable.
5. One formula is satisfiable and the other is not, so they are not equisatisfiable.

## Remarks

The formula $p \land \neg p$ is $p$ with the conjunct $\neg p$ added.
Adding a conjunct can turn a satisfiable formula into an unsatisfiable one, so the step "add a conjunct" does not keep equisatisfiability in general.
It does keep it when the new conjunct defines a fresh variable, as in $\chi \land (x \leftrightarrow \psi)$ with $x$ new; the concept page proves this.
The conjunct $\neg p$ is not of that kind, because it speaks about the old variable $p$.

## Explanations

### L1 human

"The door is open" can be true.
"The door is open and the door is not open" can never be true.
So one statement has a way to be true and the other has none, and they are not equisatisfiable.

### L2 human

We compare with a conjunct that is allowed.

1. The formula $p \land (x \leftrightarrow \neg p)$, with $x$ new, is satisfiable by $v(p) = 1$, $v(x) = 0$.
2. So $p$ and $p \land (x \leftrightarrow \neg p)$ are equisatisfiable.
3. The formula $p \land \neg p$ is not, by the example.

The typical use: a satisfiability-preserving transformation may add only conjuncts that constrain new symbols.
A trap: the formulas $p$ and $p \land \neg p$ look similar, but satisfiability can change with a single conjunct.
