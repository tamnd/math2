---
tag: ~cb6fe1cd
kind: example
name: A disjunction of two variables is not a Horn clause
msc: ["03B05"]
topics: [JDK63589SA]
audience: ug2
not_instance_of:
  - target: QR92EZDTKF
    note: the clause p ∨ q has two positive literals, and no set of Horn clauses is equivalent to it, because its models {p} and {q} have the intersection ∅, which is not a model
uses: [T3SXVH3ZZC, ~41f42e3d]
sources:
  - url: https://en.wikipedia.org/wiki/Horn_clause
    locator: Definition
---

## Example

Let $p$ and $q$ be distinct propositional variables, and let $C = \set{p, q}$, the clause $p \lor q$.
We show that $C$ is not a Horn clause, and that no set of Horn clauses is equivalent to it.

1. The literals $p$ and $q$ are both positive, so $C$ has two positive literals, and it is not a Horn clause.
2. Suppose that a set $S$ of Horn clauses, in any variables, is equivalent to $C$: it has the same models.
3. Let $v_1$ make $p$ true and every other variable false, and let $v_2$ make $q$ true and every other variable false.
4. Both make $p \lor q$ true, so both are models of $S$ by step 2.
5. By the intersection property of Horn clauses, the assignment $u$ with $u(x) = \min(v_1(x), v_2(x))$ for each variable $x$ is a model of $S$.
6. But $u(p) = \min(1, 0) = 0$ and $u(q) = \min(0, 1) = 0$, so $u$ makes $p \lor q$ false, against step 2.
7. So no set of Horn clauses is equivalent to $p \lor q$.

## Remarks

The example shows that the Horn formulas are not closed under disjunction, although $p$ and $q$ are Horn formulas.
The clause $\neg p \lor q$ differs from $p \lor q$ in one sign, and it is a Horn clause; flipping the sign of a variable everywhere, $p$ to $\neg p$, can turn some non-Horn sets into Horn sets, and such sets are called renamable Horn.
A set of definite clauses has a least model, but $p \lor q$ has two minimal models, $\set{p}$ and $\set{q}$, and no least one.
This is why logic programs with disjunctive heads need a different semantics.

## Explanations

### L1 human

"Pia comes or Quin comes" leaves a choice.
A Horn rule never leaves a choice: from what is known, it either forces one more thing or forbids a combination.
So no list of Horn rules can say exactly "Pia or Quin", because the rules would have to allow "only Pia" and "only Quin" and forbid "nobody", which needs a choice.

### L2 human

We check the minimal models of $p \lor q$ over the variables $p$ and $q$.

1. The models are $\set{p}$, $\set{q}$ and $\set{p, q}$.
2. The model $\set{p, q}$ is not minimal, since $\set{p}$ is a smaller model.
3. The models $\set{p}$ and $\set{q}$ are minimal, since their only proper subset, $\emptyset$, is not a model.
4. There are two minimal models, so there is no least model.

The typical use: to show that a property cannot be written with Horn clauses, find two models whose intersection is not a model.
A trap: the formula $p \lor q$ can still be satisfiable and simple to solve; the point is only that the marking algorithm and the least-model semantics do not apply to it.
