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

Let $D$ be the set of four definite clauses over the variables $p, q, r, s, t$:
$$\{ p \}, \qquad \{ \neg p, q \}, \qquad \{ \neg q, \neg r, s \}, \qquad \{ \neg t, r \}.$$
In implicative form these are the fact $p$ and the rules $p \to q$, $q \land r \to s$ and $t \to r$.
We find all models of $D$, written as the sets of variables that they make true, and we check that their intersection is the least model.

1. Each clause has exactly one positive literal, so $D$ is a set of definite [[Horn clauses|QR92EZDTKF]].
2. Every model contains $p$, by the fact, and then $q$, by $p \to q$.
3. With $p$ and $q$ true, the remaining clauses say $r \to s$ and $t \to r$.
4. Of the eight triples of values of $(r, s, t)$, these four satisfy both rules: $(0, 0, 0)$, $(0, 1, 0)$, $(1, 1, 0)$ and $(1, 1, 1)$.
   Each of the other four has $r = 1$ with $s = 0$, or $t = 1$ with $r = 0$.
5. So the models of $D$ are
$$\{ p, q \}, \quad \{ p, q, s \}, \quad \{ p, q, r, s \}, \quad \{ p, q, r, s, t \}.$$
6. Their intersection is $\{ p, q \}$, and it is one of the models, as the intersection property of Horn clauses predicts.
7. The marking algorithm agrees.
   It marks $p$ by the fact and then $q$ by $p \to q$; the rule $q \land r \to s$ needs $r$, and $t \to r$ needs $t$, which nothing gives, so the marks stop at $\{ p, q \}$.

## Remarks

The least model $\{ p, q \}$ is exactly the set of variables that follow from $D$.
We have $D \models p$ and $D \models q$, while the model $\{ p, q \}$ itself shows that $D \not\models r$, $D \not\models s$ and $D \not\models t$.
In a logic program with these clauses, the queries $p$ and $q$ succeed and the queries $r$, $s$ and $t$ fail.

If we add the fact $\{ t \}$, marking gives $t$, then $r$, then $s$, and $\{ p, q, r, s, t \}$ becomes the only model.
Here the models happen to form a chain, but the models of a Horn formula are not closed under union in general.
For the single clause $\{ \neg p, \neg q, r \}$, the sets $\{ p \}$ and $\{ q \}$ are models, while their union $\{ p, q \}$ is not.

## Explanations

### L1 human

The rules say: "Pam comes." "If Pam comes, Quin comes." "If Quin and Rob come, Sue comes." "If Tom comes, Rob comes."
Pam must come, and so Quin must come.
Nobody forces Tom to come, so nobody forces Rob or Sue either.
The smallest party that obeys all rules is Pam and Quin, and every party that obeys the rules contains these two.

### L2 human

We compute the least model by the immediate consequence step, which adds the heads of all rules whose bodies are already true.
Start with $M_0 = \emptyset$.
Only the fact has an empty body, so $M_1 = \{ p \}$.
Now the rule $p \to q$ fires, so $M_2 = \{ p, q \}$.
No new rule fires, because $q \land r \to s$ needs $r$ and $t \to r$ needs $t$, so $M_3 = M_2$ and the least model is $\{ p, q \}$.
This bottom-up computation is how Datalog and logic programming find the answers of a program.
Watch out: the least model is least among models, not among all assignments; the empty set is smaller, but it makes the fact $p$ false.
