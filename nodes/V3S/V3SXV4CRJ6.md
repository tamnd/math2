---
tag: V3SXV4CRJ6
kind: example
name: A conjunction of literals is not a clause
msc: ["03B05"]
topics: [JDK63589SA]
audience: ug1
not_instance_of:
  - target: T3SXVH3ZZC
    note: p ∧ q is a conjunction of two literals, while a clause is a disjunction of literals, and no clause is even equivalent to p ∧ q
uses: [H31CS3HK5P, 025YZN3VJW, 0F72FK8EKB]
sources:
  - url: https://en.wikipedia.org/wiki/Clause_(logic)
    locator: lead section
---

## Example

Let $p$ and $q$ be distinct propositional variables.
We show that $p \land q$ is not a clause, and that it is not even equivalent to a clause.

1. A clause is a disjunction of literals. The formula $p \land q$ has the main connective $\land$, so it is not of this form.
2. Suppose that some clause $C$ is equivalent to $p \land q$.
3. If $C$ contains a complementary pair, it is a tautology. But $p \land q$ is false under $v(p) = v(q) = 0$, so this case is impossible.
4. So $C$ has no complementary pair. The formula $p \land q$ is false under any assignment $v$ with $v(p) = 0$, $v(q) = 1$, so $C$ is false under $v$, and every literal of $C$ is false under $v$. Hence $C$ contains neither $p$ nor $\neg q$.
5. In the same way, an assignment $w$ with $w(p) = 1$, $w(q) = 0$ falsifies $C$, so $C$ contains neither $\neg p$ nor $q$.
6. Let $u$ make every literal of $C$ false, which is possible since $C$ has no complementary pair, and let $u(p) = u(q) = 1$, which is possible since by steps 4 and 5 no literal of $C$ is in $p$ or $q$.
7. Then $\bar u(C) = 0$ and $\bar u(p \land q) = 1$, against step 2.
8. So no clause is equivalent to $p \land q$.

## Remarks

The formula $p \land q$ is equivalent to the set of two clauses $\set{p}$, $\set{q}$, that is, to a conjunction of two unit clauses.
It is a conjunction of literals, which is the building block of a disjunctive normal form; some books call it a conjunctive clause, while the plain word "clause" means a disjunction.
The argument shows a general fact: a clause without complementary pairs is false in exactly one row of the truth table of its variables, while $p \land q$ is false in three rows of four.

## Explanations

### L1 human

"Pia comes and Quin comes" asks for two things at once.
A clause asks for at least one thing from a list.
These are different kinds of demands, and one clause cannot do the job of an "and".
We need two clauses, "Pia comes" and "Quin comes", to say the same thing.

### L2 human

We count rows to see the difference.

1. The formula $p \land q$ is false in three of the four rows of the truth table on $p$ and $q$.
2. A clause in $p$ and $q$ without a complementary pair, such as $\set{p, q}$ or $\set{\neg p}$, is false in exactly one row when it uses both variables, and in two rows when it uses one.
3. So no such clause has the same truth table as $p \land q$.

The typical use: when we turn a formula into clauses, a conjunction splits into several clauses.
A trap: the set notation $\set{p, q}$ for a clause means $p \lor q$, not $p \land q$; the clause set $\set{\set{p}, \set{q}}$ means $p \land q$.
