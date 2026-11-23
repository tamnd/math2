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

One added conjunct can change whether a formula has a model, and then the two formulas are not [[equisatisfiable|B37TYWXS74]].
Let $p$ be a propositional variable.
We show that $p$ and $p \land \neg p$ are not equisatisfiable.

1. The assignment $v(p) = 1$ satisfies $p$, so $p$ is satisfiable.
2. Let $w$ be any assignment.
   If $w(p) = 1$, then $\bar w(\neg p) = 0$, and if $w(p) = 0$, then $\bar w(p) = 0$.
3. In both cases one conjunct of $p \land \neg p$ is false, so $\bar w(p \land \neg p) = 0$ by the table of [[conjunction|025YZN3VJW]].
4. So $p \land \neg p$ is unsatisfiable.
5. One formula is satisfiable and the other is not, so they are not equisatisfiable.

Check: the two rows for $p$ give $p \land \neg p$ the values $\min(1, 0) = 0$ and $\min(0, 1) = 0$.

## Remarks

The formula $p \land \neg p$ is $p$ with the conjunct $\neg p$ added.
So adding a conjunct does not keep equisatisfiability in general.
It does keep it when the new conjunct defines a fresh variable, as in $\chi \land (x \leftrightarrow \psi)$ with $x$ new, and the concept page proves this.
The conjunct $\neg p$ is not of that kind, because it speaks about the old variable $p$.

Compare it with a conjunct that is allowed.
The formula $p \land (x \leftrightarrow \neg p)$, with $x$ new, is satisfiable by $v(p) = 1$, $v(x) = 0$, so it is equisatisfiable with $p$.

Watch out.
The formulas $p$ and $p \land \neg p$ look alike, but one conjunct is enough to change satisfiability.

Try it.
Are $p \lor q$ and $(p \lor q) \land \neg p \land \neg q$ equisatisfiable?
No: the first is satisfiable, and in the second the conjuncts $\neg p$ and $\neg q$ make $p \lor q$ false.

## Explanations

### L1 human

"The door is open" can be true.
"The door is open and the door is not open" can never be true.
So one statement has a way to be true and the other has none, and they are not equisatisfiable.

### L2 human

A satisfiability-preserving conversion, such as the Tseitin transformation, may add only conjuncts that constrain new symbols.
Each such conjunct has the form $x \leftrightarrow \psi$ with $x$ fresh, and any value of the old variables can be kept by choosing $x$ to match $\psi$.
A conjunct about the old variables alone, such as $\neg p$, removes old models, and it can remove all of them.
