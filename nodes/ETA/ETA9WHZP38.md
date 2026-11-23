---
tag: ETA9WHZP38
kind: example
name: A Kripke model forces logical omniscience
msc: ["03B45", "03B42"]
topics: [SPQVNPZDTB]
audience: research
not_instance_of:
  - target: 8PAJMAN8DM
    note: every world of a Kripke model is possible and obeys classical logic, so the model has no impossible worlds
uses: [8PAJMAN8DM, NGHWZ9Y7ZV]
sources:
  - url: https://en.wikipedia.org/wiki/Impossible_world
    locator: Applications
  - url: https://builds.openlogicproject.org/
    locator: Modal Logic
---

## Example

Take worlds $w$, $u$, $v$ with $w R u$ and $w R v$, let $p$ be true at $u$ and $v$, and let $q$ be true at $u$ and $v$ as well.
Read $\square \varphi$ as "the agent at $w$ knows $\varphi$".
The agent knows $p$ and knows $p \to q$, and the only way to make $q$ fail would be a successor where $p$ and $p \to q$ hold and $q$ does not.
No such world exists, because each world computes $p \to q$ by the truth table.

Let $(W, R, V)$ be any [[Kripke model|NGHWZ9Y7ZV]].
Every world evaluates all connectives classically, so no world is an [[impossible world|8PAJMAN8DM]].
We show that knowledge in this model is closed under known implication and contains all tautologies.

1. Let $w \models \square p$ and $w \models \square(p \to q)$.
2. Let $v$ be a world with $w R v$.
   Then $v \models p$ and $v \models p \to q$.
3. The clause for $\to$ is classical at $v$, so $v \models q$.
4. As $v$ was arbitrary, $w \models \square q$.
5. Let $\varphi$ be a tautology.
   Every world $v$ evaluates $\varphi$ classically, so $v \models \varphi$, and hence $w \models \square \varphi$.

## Remarks

The model is a non-example: without impossible worlds, the agent is logically omniscient.
Step 3 is the place to compare with [[impossible worlds block logical omniscience|P2ZVNZDNHV]], where the world $i$ does not compute $p \to q$ from $p$ and $q$.
The argument is the soundness of the axiom $\square(p \to q) \to (\square p \to \square q)$ and of necessitation for Kripke models.

## Explanations

### L1 human

In an ordinary model, every world the agent considers obeys logic.
So whatever follows logically from what the agent knows is true in all these worlds, and the agent knows it.
No real person reasons this well, which is why impossible worlds were introduced.

### L2 human

Change the opening model so that $q$ fails at $v$.
Then $p \to q$ is false at $v$ by the truth table, so the agent no longer knows $p \to q$.
The agent also no longer knows $q$, and closure is not violated.
A Kripke model can make the agent ignorant of $q$ only by making the agent ignorant of a premise too.
The typical use of this argument is to explain why epistemic logic based on Kripke models assumes idealized agents.
Watch out: the closure does not depend on properties of $R$, and it holds for every Kripke model.
