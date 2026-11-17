---
tag: C7ZTS8N0VB
kind: example
name: Resolving two variables at once
msc: ["03B05"]
topics: [JDK63589SA]
audience: ug2
not_instance_of:
  - target: ZDW6N1PGJ7
    note: The step cuts two complementary pairs at once, and the rule of resolution cuts exactly one.
uses: [ZDW6N1PGJ7, T3SXVH3ZZC]
sources:
  - url: https://en.wikipedia.org/wiki/Resolution_(logic)
    locator: Resolution rule
---

## Example

Consider the [[clauses|T3SXVH3ZZC]] $C_1 = \set{p, q}$ and $C_2 = \set{\neg p, \neg q}$.
A false rule would remove both $p, \neg p$ and $q, \neg q$, and derive $\square$ from $C_1$ and $C_2$.
This step is not an instance of [[resolution|ZDW6N1PGJ7]].

1. The rule of resolution cuts one variable. So a resolvent of $C_1$ and $C_2$ is on $p$ or on $q$.
2. The resolvent on $p$ is $\set{q, \neg q}$. The resolvent on $q$ is $\set{p, \neg p}$.
3. Neither resolvent is $\square$. Both are tautological clauses, true under every assignment.
4. The false step is not sound. The assignment $p = 1$, $q = 0$ makes $p$ true, so it satisfies $C_1$.
5. It makes $\neg q$ true, so it satisfies $C_2$. So $\set{C_1, C_2}$ is satisfiable, and no sound rule derives $\square$ from it.

## Remarks

The example shows why the rule cuts exactly one variable.
The two clauses say "$p$ or $q$" and "not both $p$ and $q$", and these hold together when exactly one of $p$, $q$ is true.
If we add the clauses $\set{\neg p, q}$ and $\set{p, \neg q}$, which say that $p$ and $q$ are equal, the set becomes unsatisfiable.
Then a correct refutation exists.
Resolve $\set{p, q}$ and $\set{\neg p, q}$ on $p$ to get $\set{q}$, and $\set{p, \neg q}$ and $\set{\neg p, \neg q}$ on $p$ to get $\set{\neg q}$.
Then resolve $\set{q}$ and $\set{\neg q}$ on $q$ to get $\square$.

## Explanations

### L1 human

One rule says "Ann or Bob comes", and the other says "Ann does not come or Bob does not come".
It is tempting to cancel Ann and Bob together and claim a contradiction.
But the two rules hold when Ann comes and Bob stays home.
So the shortcut gives a wrong answer.

### L2 human

To check a step of a resolution proof, find the one variable that is cut.
It must occur positively in one premise and negatively in the other.
Everything else in both premises goes into the resolvent, including other complementary pairs.
A resolvent with a complementary pair is true under every assignment, so it never helps a refutation.
The trap is to treat the clauses like an equation and cancel all opposite pairs at once.
