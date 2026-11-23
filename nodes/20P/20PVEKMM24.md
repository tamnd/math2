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

We test the set of four [[clauses|T3SXVH3ZZC]]
$$S = \{ \{ p, q \}, \{ \neg p, r \}, \{ \neg q, r \}, \{ \neg r \} \}$$
for [[satisfiability|QN7M1JCGT9]] by removing its variables one at a time.
This is the Davis-Putnam procedure, in its simplest form.
Each round picks a variable $p$ and keeps the clauses that contain neither $p$ nor $\neg p$.
It adds all [[resolvents|ZDW6N1PGJ7]] on $p$ and drops the clauses that contain $p$ or $\neg p$.

1. Remove $r$.
   The clauses with $r$ are $\{ \neg p, r \}$ and $\{ \neg q, r \}$, and the only clause with $\neg r$ is $\{ \neg r \}$.
2. The resolvents on $r$ are $\{ \neg p \}$ and $\{ \neg q \}$.
   The clause $\{ p, q \}$ has no $r$, so it stays.
3. The new set is $S_1 = \{ \{ p, q \}, \{ \neg p \}, \{ \neg q \} \}$, with the two variables $p$ and $q$.
4. Remove $p$.
   The only clause with $p$ is $\{ p, q \}$, and the only clause with $\neg p$ is $\{ \neg p \}$, so the resolvent on $p$ is $\{ q \}$.
5. The clause $\{ \neg q \}$ has no $p$, so it stays.
   The new set is $S_2 = \{ \{ q \}, \{ \neg q \} \}$.
6. Remove $q$.
   The resolvent of $\{ q \}$ and $\{ \neg q \}$ on $q$ is $\square$.
7. The set $S_3 = \{ \square \}$ contains the empty clause, so it is unsatisfiable.
   Each round keeps satisfiability, so $S$ is unsatisfiable.

Check by hand: $\{ \neg r \}$ forces $r = 0$, then $\{ \neg p, r \}$ and $\{ \neg q, r \}$ force $p = q = 0$, and then $\{ p, q \}$ is false.

## Remarks

Each round is the inductive step of the [[completeness proof for resolution|EQH5KN1VPZ]]: the new set is satisfiable exactly when the old one is.
If the procedure ends with the empty set of clauses instead, the input is satisfiable.
For example, without $\{ \neg r \}$ the first round has no clause with $\neg r$, so it adds no resolvent and leaves only $\{ \{ p, q \} \}$.
The procedure then ends with the empty set, and indeed $p = q = r = 1$ satisfies the smaller input.

The number of resolvents can grow fast.
If $a$ clauses contain $p$ and $b$ clauses contain $\neg p$, one round can add up to $ab$ resolvents.

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
Watch out: the clauses with $p$ are not kept after the round.
They are dropped, since the resolvents carry all that they say about the other variables.
