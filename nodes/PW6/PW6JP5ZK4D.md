---
tag: PW6JP5ZK4D
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

"The coin shows heads" and "the coin does not show heads" can each be true, but never together.
Two such formulas are still [[equisatisfiable|B37TYWXS74]].
Let $p$ be a propositional variable.
We show that $p$ and $\neg p$ are equisatisfiable, although no assignment makes both true.

1. The assignment $v(p) = 1$ satisfies $p$, so $p$ is satisfiable.
2. The assignment $w(p) = 0$ gives $\bar w(\neg p) = 1$ by the table of [[negation|029JBBF693]], so $\neg p$ is satisfiable.
3. Both formulas are satisfiable, so they are equisatisfiable.
4. Every assignment $u$ gives $\bar u(p) \neq \bar u(\neg p)$, so no assignment makes both true.
   In particular they are not [[logically equivalent|0JMR2HM2N2]].

Check: the models of $p$ are the assignments with $p = 1$, the models of $\neg p$ are those with $p = 0$, and the two sets do not meet.

## Remarks

Equisatisfiable formulas can have disjoint sets of models.
The same holds for every formula $\varphi$ that is neither a tautology nor unsatisfiable, since then $\varphi$ and $\neg \varphi$ are both satisfiable.
If $\varphi$ is a tautology, then $\neg \varphi$ is unsatisfiable, and $\varphi$ and $\neg \varphi$ are not equisatisfiable.

The example also shows that equisatisfiability does not respect the connectives.
The formula $p$ is equisatisfiable with $p$ and with $\neg p$.
But $p \land p$ is satisfiable, while $p \land \neg p$ is not.

Watch out.
An equisatisfiable replacement inside a larger formula can change the answer, as $p \land p$ and $p \land \neg p$ show.

Try it.
Are $p \lor q$ and $\neg p \land \neg q$ equisatisfiable?
Yes: $p = 1$ satisfies the first, and $p = q = 0$ satisfies the second, although each is the negation of the other up to equivalence.

## Explanations

### L1 human

"The coin shows heads" and "the coin does not show heads" are both possible.
So they are equisatisfiable, since each can be made true.
But they can never be true at the same time.
Equisatisfiable means only "possible and possible", not "true together".

### L2 human

We find all formulas in the variable $p$ alone that are equisatisfiable with $p$.

1. Up to equivalence, the formulas in $p$ alone are $p$, $\neg p$, $p \lor \neg p$ and $p \land \neg p$, one for each function from $\{ 0, 1 \}$ to $\{ 0, 1 \}$.
2. The first three are satisfiable, and the last is not.
3. So $p$ is equisatisfiable with every formula equivalent to $p$, $\neg p$ or $p \lor \neg p$, and with none equivalent to $p \land \neg p$.

The relation has only two classes, so it is very coarse.
