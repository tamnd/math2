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
We show that $p \land q$ is not a [[clause|T3SXVH3ZZC]], and that no clause is even equivalent to it.

1. A clause is a [[disjunction|0F72FK8EKB]] of literals.
   The main connective of $p \land q$ is $\land$, so the formula does not have this shape.
2. Now suppose that some clause $C$ is equivalent to $p \land q$.
3. If $C$ contains a complementary pair, it is a tautology.
   But $p \land q$ is false when $p = q = 0$, so $C$ has no complementary pair.
4. The formula $p \land q$ is false under each assignment $v$ with $v(p) = 0$ and $v(q) = 1$.
   So $C$ is false under $v$, every literal of $C$ is false under $v$, and $C$ contains neither $p$ nor $\neg q$.
5. In the same way, an assignment $w$ with $w(p) = 1$ and $w(q) = 0$ falsifies $C$, so $C$ contains neither $\neg p$ nor $q$.
6. So no literal of $C$ mentions $p$ or $q$.
   Let $u$ make every literal of $C$ false, which is possible because $C$ has no complementary pair, and let $u(p) = u(q) = 1$.
7. Then $C$ is false under $u$ while $p \land q$ is true under $u$, which contradicts step 2.

So no clause is equivalent to $p \land q$.

## Remarks

The formula $p \land q$ is equivalent to the set of two unit clauses $\{ p \}$ and $\{ q \}$.
It is a [[conjunction|025YZN3VJW]] of literals, which is the building block of a disjunctive normal form.
Some books call it a conjunctive clause, but the plain word "clause" always means a disjunction.

The proof hides a counting fact.
A clause on $k$ variables without a complementary pair is false in exactly one row of its $2^k$ rows, and a clause on fewer variables is false in more rows.
On the variables $p$ and $q$ a clause is false in one or two of the four rows, while $p \land q$ is false in three.
If we replace $p \land q$ by $p \lor q$, the formula is false in one row only, and it is the clause $\{ p, q \}$.

## Explanations

### L1 human

"Pia comes and Quin comes" asks for two things at once.
A clause asks for at least one thing from a list.
These are different kinds of demand, and one clause cannot do the job of an "and".
We need two clauses, "Pia comes" and "Quin comes", to say the same thing.

### L2 human

We count rows to see the difference.
The formula $p \land q$ is false in three of the four rows on $p$ and $q$.
A clause such as $\{ p, q \}$, which uses both variables, is false in one row, and a clause such as $\{ \neg p \}$, which uses one, is false in two rows.
The empty clause is false in all four rows, and a tautological clause in none.
So no clause has the same truth table as $p \land q$.
In practice this means that a conjunction splits into several clauses when you put a formula into clause form.
Watch out: the clause $\{ p, q \}$ means $p \lor q$, and the clause set $\{ \{ p \}, \{ q \} \}$ means $p \land q$.
