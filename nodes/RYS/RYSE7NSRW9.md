---
tag: RYSE7NSRW9
kind: example
name: Resolution refutation of a chain of implications
msc: ["03B05", "03B35"]
topics: [JDK63589SA]
audience: ug2
instance_of: [ZDW6N1PGJ7]
uses: [ZDW6N1PGJ7, T3SXVH3ZZC, 1HK0VYWTV7]
sources:
  - url: https://en.wikipedia.org/wiki/Resolution_(logic)
    locator: A simple example
---

## Example

We show $p, \; p \to q, \; q \to r \models r$ with a [[resolution|ZDW6N1PGJ7]] refutation.

1. The premise $p$ is the clause $\set{p}$. The premise $p \to q$ is equivalent to $\neg p \lor q$, the clause $\set{\neg p, q}$.
2. The premise $q \to r$ is equivalent to $\neg q \lor r$, the clause $\set{\neg q, r}$.
3. The negated goal $\neg r$ is the clause $\set{\neg r}$. Let $S$ be the set of these four [[clauses|T3SXVH3ZZC]].
4. Resolve $\set{p}$ and $\set{\neg p, q}$ on $p$. We remove $p$ from the first clause and $\neg p$ from the second, and get $\set{q}$.
5. Resolve $\set{q}$ and $\set{\neg q, r}$ on $q$. The resolvent is $\set{r}$.
6. Resolve $\set{r}$ and $\set{\neg r}$ on $r$. The resolvent is the empty clause $\square$.
7. The list $\set{p}, \set{\neg p, q}, \set{\neg q, r}, \set{\neg r}, \set{q}, \set{r}, \square$ is a resolution refutation of $S$. Each line is in $S$ or is a resolvent of two earlier lines.
8. By the [[soundness of resolution|DH1P95R390]], $S$ is unsatisfiable. So every assignment that makes the three premises true makes $r$ true, which is the [[logical consequence|1HK0VYWTV7]] $p, p \to q, q \to r \models r$.

## Remarks

The refutation follows the chain of modus ponens steps: each resolution with a unit clause is one application of modus ponens.
All clauses here are [[Horn clauses|QR92EZDTKF]], and every step uses a unit clause, so this is a unit resolution refutation.
If we drop the premise $p$, the set $\set{\set{\neg p, q}, \set{\neg q, r}, \set{\neg r}}$ is satisfiable, for example by $p = q = r = 0$.
Then no refutation exists: the only resolvents are $\set{\neg p, r}$, $\set{\neg q}$ and $\set{\neg p}$, and none of them is empty.

## Explanations

### L1 human

Suppose we know three facts: it rains, rain makes the street wet, and a wet street is slippery.
We want to show that the street is slippery.
We assume the opposite, that the street is not slippery.
Then we combine the facts two at a time and reach a plain contradiction.
So the assumption was wrong, and the street is slippery.

### L2 human

The method turns a proof of a consequence into a search for the empty clause.
We negate only the goal, and we keep the premises as they are.
Each resolution step here has a one-literal premise, so each step makes a clause shorter by one literal.
A trap is to add the goal $\set{r}$ instead of its negation $\set{\neg r}$: the set with $\set{r}$ is satisfiable, and no refutation exists.
