---
tag: VQPY7BHMV0
kind: example
name: The least model of a set of definite clauses
msc: ["03B05", "03B70"]
topics: [JDK63589SA]
audience: ug2
instance_of: [QR92EZDTKF]
uses: [T3SXVH3ZZC, QN7M1JCGT9, H31CS3HK5P]
sources:
  - url: https://en.wikipedia.org/wiki/Horn_clause
    locator: Logic programming
---

## Example

Let $D$ be the set of the four definite clauses $\set{p}$, $\set{\neg p, q}$, $\set{\neg q, \neg r, s}$, $\set{\neg t, r}$, that is, the fact $p$ and the rules $p \to q$, $q \land r \to s$, $t \to r$, over the variables $p$, $q$, $r$, $s$, $t$.
We find all models of $D$, and we check that their intersection is the least model.
We write a model as the set of variables it makes true.

1. Each clause has exactly one positive literal, so $D$ is a set of definite clauses.
2. Every model contains $p$, by the fact $\set{p}$, and then $q$, by $p \to q$.
3. Given $p$ and $q$, the remaining clauses say $r \to s$ and $t \to r$.
4. The triples of values of $(r, s, t)$ that satisfy $r \to s$ and $t \to r$ are $(0, 0, 0)$, $(0, 1, 0)$, $(1, 1, 0)$ and $(1, 1, 1)$. The other four triples have $r = 1, s = 0$ or $t = 1, r = 0$.
5. So the models of $D$ are $\set{p, q}$, $\set{p, q, s}$, $\set{p, q, r, s}$ and $\set{p, q, r, s, t}$.
6. Their intersection is $\set{p, q}$, and it is one of the models, as the intersection property of Horn clauses predicts.
7. The marking algorithm marks $p$ by the fact, then $q$ by $p \to q$. The rule $q \land r \to s$ needs $r$, and $t \to r$ needs $t$, which no rule gives, so the marks stop at $\set{p, q}$, the same set.

## Remarks

The least model $\set{p, q}$ is the set of variables that follow from $D$: $D \models p$ and $D \models q$, while $D \not\models r$, $D \not\models s$, $D \not\models t$ because of the model $\set{p, q}$.
In a logic program with these clauses, the queries $p$ and $q$ succeed and the queries $r$, $s$, $t$ fail.
If we add the fact $\set{t}$, the marks give $\set{p, q, t, r, s}$, and this is then the only model.
The models are not closed under union in general: here they happen to form a chain, but for the clauses $\set{\neg p, \neg q, r}$ alone, $\set{p}$ and $\set{q}$ are models while $\set{p, q}$ is not.

## Explanations

### L1 human

The rules say: "Pam comes." "If Pam comes, Quin comes." "If Quin and Rob come, Sue comes." "If Tom comes, Rob comes."
Pam must come, and so Quin must come.
Nobody forces Tom to come, so nobody forces Rob or Sue either.
The smallest party that obeys all rules is Pam and Quin, and every party that obeys the rules contains these two.

### L2 human

We compute the least model by the immediate consequence step.

1. Start with $M_0 = \emptyset$.
2. $M_1$ is the set of heads of clauses whose bodies lie in $M_0$: only the fact gives $p$, so $M_1 = \set{p}$.
3. $M_2$ adds the heads of clauses whose bodies lie in $M_1$: the rule $p \to q$ gives $q$, so $M_2 = \set{p, q}$.
4. $M_3$ adds nothing new, since $q \land r \to s$ needs $r$ and $t \to r$ needs $t$. So $M_3 = M_2$, and the least model is $\set{p, q}$.

The typical use: in Datalog and logic programming, the answer to a program is its least model, computed in this bottom-up way.
A trap: the least model is least among models, not among all assignments; the empty set is smaller but makes the fact $p$ false.
