---
tag: B2BQWC4FMP
kind: example
name: A clause with three literals
msc: ["03B05"]
topics: [JDK63589SA]
audience: ug1
instance_of: [T3SXVH3ZZC]
uses: [H31CS3HK5P, 0F72FK8EKB, 029JBBF693]
sources:
  - url: https://en.wikipedia.org/wiki/Clause_(logic)
    locator: lead section
---

## Example

Let $C = \{ p, \neg q, r \}$, where $p$, $q$ and $r$ are distinct propositional variables.
We check that $C$ is a [[clause|T3SXVH3ZZC]], and we find the assignments that satisfy it.

1. Each member of $C$ is a literal: $p$ and $r$ are positive literals, and $\neg q$ is a negative literal.
2. $C$ is a finite set of literals, so it is a clause, and it stands for the [[disjunction|0F72FK8EKB]] $p \lor \neg q \lor r$.
3. An assignment $v$ falsifies $C$ exactly when it makes every literal false.
   That means $v(p) = 0$, $\bar v(\neg q) = 0$ and $v(r) = 0$, that is,
$$v(p) = 0, \qquad v(q) = 1, \qquad v(r) = 0.$$
4. So exactly one of the eight assignments to $p, q, r$ falsifies $C$, and the other seven satisfy it.
5. $C$ has no complementary pair, so it is not a tautology, and it is not empty, so it is satisfiable.

Check one satisfying row: at $p = 0$, $q = 0$, $r = 0$ the literal $\neg q$ is true, so $C$ is true.

## Remarks

The clause has one negative literal, $\neg q$, so its implicative form is $q \to p \lor r$.
It has two positive literals, so it is not a [[Horn clause|QR92EZDTKF]]; the clause $\{ \neg p, \neg q, r \}$ is one.

The count in step 4 is general.
A clause on $k$ distinct variables without a complementary pair is falsified by exactly one of the $2^k$ assignments to its variables.
So a clause can be read as "exclude one row of the truth table", and a set of such clauses can exclude any set of rows, which is one proof that every formula has a conjunctive normal form.
If we add the literal $q$, the clause $\{ p, q, \neg q, r \}$ becomes a tautology, and it excludes no row at all.

## Explanations

### L1 human

The rule "Pia comes, or Quin stays home, or Rosa comes" is a clause.
It is broken only when Pia stays home, Quin comes, and Rosa stays home.
Of the eight ways the three people can come or stay, seven obey the rule.

### L2 human

We write the formula $\neg(\neg p \land q \land \neg r)$ as a clause.
By [[De Morgan's laws|09PKJKA6J0]] it is equivalent to
$$\neg\neg p \lor \neg q \lor \neg\neg r,$$
and by the double negation law this is $p \lor \neg q \lor r$, the clause $C$.
The formula inside the negation describes exactly the bad row $p = 0$, $q = 1$, $r = 0$.
So to forbid one row of a truth table, negate the term of that row, and the result is a clause.
Watch out: order and repetition do not matter in a clause, so $\{ r, \neg q, p, p \}$ is the same clause as $C$.
