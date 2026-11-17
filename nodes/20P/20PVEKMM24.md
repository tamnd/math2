---
tag: 20PVEKMM24
kind: example
name: A run of the Davis-Putnam procedure
msc: ["03B05", "03B35"]
topics: [JDK63589SA]
audience: ug2
instance_of: [ZDW6N1PGJ7]
uses: [ZDW6N1PGJ7, T3SXVH3ZZC, QN7M1JCGT9]
sources:
  - url: https://en.wikipedia.org/wiki/Resolution_(logic)
    locator: Resolution in propositional logic
  - url: https://en.wikipedia.org/wiki/Davis%E2%80%93Putnam_algorithm
    locator: lead section
---

## Example

The Davis-Putnam procedure tests a finite set of [[clauses|T3SXVH3ZZC]] for [[satisfiability|QN7M1JCGT9]].
Each round picks a variable $p$ and keeps the clauses that contain neither $p$ nor $\neg p$.
It adds all [[resolvents|ZDW6N1PGJ7]] on $p$ and drops the clauses that contain $p$ or $\neg p$.
We run it on
$$S = \set{\set{p, q}, \set{\neg p, r}, \set{\neg q, r}, \set{\neg r}}.$$

1. Eliminate $r$. The clauses with $r$ are $\set{\neg p, r}$ and $\set{\neg q, r}$, and the only clause with $\neg r$ is $\set{\neg r}$.
2. The resolvents on $r$ are $\set{\neg p}$ and $\set{\neg q}$. The clause $\set{p, q}$ has no $r$, so it stays.
3. The new set is $S_1 = \set{\set{p, q}, \set{\neg p}, \set{\neg q}}$, with the two variables $p$ and $q$.
4. Eliminate $p$. The only clause with $p$ is $\set{p, q}$, and the only clause with $\neg p$ is $\set{\neg p}$. The resolvent on $p$ is $\set{q}$.
5. The clause $\set{\neg q}$ has no $p$, so it stays. The new set is $S_2 = \set{\set{q}, \set{\neg q}}$.
6. Eliminate $q$. The resolvent of $\set{q}$ and $\set{\neg q}$ on $q$ is $\square$.
7. The set $S_3 = \set{\square}$ contains the empty clause, so it is unsatisfiable. Each elimination keeps satisfiability, so $S$ is unsatisfiable.
8. Check by hand: $\set{\neg r}$ forces $r = 0$, then $\set{\neg p, r}$ and $\set{\neg q, r}$ force $p = q = 0$, and then $\set{p, q}$ is false.

## Remarks

Each elimination step is the inductive step of the [[completeness proof for resolution|EQH5KN1VPZ]]: the new set is satisfiable exactly when the old one is.
If the procedure ends with the empty set of clauses instead, the input is satisfiable.
For example, without $\set{\neg r}$ the first step has no clause with $\neg r$, so it adds no resolvent and leaves only $\set{\set{p, q}}$.
The procedure then ends with the empty set, and indeed $p = q = r = 1$ satisfies the smaller input.
The number of resolvents can grow fast: $a$ clauses with $p$ and $b$ clauses with $\neg p$ give up to $a b$ resolvents.

## Explanations

### L1 human

The procedure removes the letters one by one.
To remove a letter, it combines every rule that says "this letter" with every rule that says "not this letter".
The new rules no longer mention the letter.
At the end either an empty rule appears, and the rules contradict each other, or no rules are left, and they can all hold.
Here three letters give a contradiction after three rounds.

### L2 human

The procedure is a decision procedure: it always stops, because each round removes one variable.
Its correctness rests on one fact about each round.
The new set is satisfiable exactly when the old set is.
The order of the variables does not change the answer, but it changes the size of the sets in between.
A trap is to keep the clauses with $p$ after the round.
They are dropped, since the resolvents carry all that they say about the other variables.
