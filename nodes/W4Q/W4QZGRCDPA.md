---
tag: W4QZGRCDPA
kind: example
name: The closed-world assumption is not monotonic
msc: ["68T27", "03B22"]
topics: [H8QZY0RZXZ]
audience: ug3
not_instance_of:
  - target: FCXHSC6Z4R
    note: closed-world inference fails monotonicity, since the empty set of premises yields not p while the larger set containing p does not
uses: [J78Y1M4GND, 1HK0VYWTV7]
sources:
  - url: https://en.wikipedia.org/wiki/Closed-world_assumption
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Non-monotonic_logic
    locator: lead section
---

## Example

Let $L$ be the formulas of propositional logic over the two variables $p$ and $q$, and let $\models$ be classical [[logical consequence|1HK0VYWTV7]].
The closed-world assumption treats every atomic fact that does not follow from the premises as false.
For $\Gamma \subseteq L$ put $\overline{\Gamma} = \Gamma \cup \set{\neg a : a \in \set{p, q} \text{ and } \Gamma \not\models a}$, and define
$$\Gamma \mathrel{|\!\sim} \varphi \iff \overline{\Gamma} \models \varphi.$$
This is how a database answers queries: a fact not stored is taken to be false.
We show that $\mathrel{|\!\sim}$ is not a [[consequence relation|J78Y1M4GND]], because monotonicity fails.

1. Take $\Gamma = \emptyset$. Neither $p$ nor $q$ is a tautology, so $\overline{\emptyset} = \set{\neg p, \neg q}$.
2. Hence $\emptyset \mathrel{|\!\sim} \neg p$.
3. Take $\Delta = \set{p}$, so $\emptyset \subseteq \Delta$. Here $\Delta \models p$ and $\Delta \not\models q$, so $\overline{\Delta} = \set{p, \neg q}$.
4. The valuation with $p = 1$ and $q = 0$ makes $\overline{\Delta}$ true and $\neg p$ false, so $\overline{\Delta} \not\models \neg p$.
5. Hence $\Delta \not\mathrel{|\!\sim} \neg p$, although $\emptyset \mathrel{|\!\sim} \neg p$ and $\emptyset \subseteq \Delta$. Monotonicity fails.

Reflexivity still holds.

6. If $\varphi \in \Gamma$, then $\varphi \in \overline{\Gamma}$, so $\overline{\Gamma} \models \varphi$ and $\Gamma \mathrel{|\!\sim} \varphi$.

## Remarks

The failure is the point of the closed-world assumption: new information should be able to cancel a default conclusion.
Inference relations of this kind are studied in non-monotonic logic, which keeps reflexivity and replaces monotonicity by weaker conditions.

The assumption has a second defect with disjunctive information.
For $\Gamma = \set{p \vee q}$, neither $p$ nor $q$ follows, so $\overline{\Gamma} = \set{p \vee q, \neg p, \neg q}$, which has no model.
Then $\Gamma \mathrel{|\!\sim} \varphi$ for every $\varphi$, although $\Gamma$ itself is satisfiable.
For this reason the closed-world assumption is used mainly for sets of atomic facts and Horn clauses, where it gives a consistent result.
Raymond Reiter studied it for databases in 1978.

A second non-example is "most likely" inference for a fair die.
Let $\Gamma \mathrel{|\!\sim} \varphi$ mean that $\varphi$ has probability greater than $\tfrac12$ given $\Gamma$.
With no information, "the result is at least $3$" has probability $\tfrac46 = \tfrac23$, so it is inferred.
Given "the result is at most $4$", the outcomes are $1, 2, 3, 4$, and "at least $3$" has probability $\tfrac24 = \tfrac12$, so it is no longer inferred.

## Explanations

### L1 human

A train timetable lists the trains that run.
If a train from Paris at 3 o'clock is not listed, we conclude that there is no such train.
If the company adds that train to the list, the conclusion disappears.
Adding information destroyed a conclusion, so this kind of reasoning is not monotone.
Logical consequence never behaves like this, and this is the difference.

### L2 human

We repeat the check with a database of flights.

1. The variables are $a$ for "there is a flight from A to B" and $b$ for "there is a flight from B to C".
2. The empty database gives $\overline{\emptyset} = \set{\neg a, \neg b}$, so the query "no flight from A to B" is answered yes.
3. After storing $a$, the closure is $\set{a, \neg b}$, and the same query is answered no.
4. The premises grew from $\emptyset$ to $\set{a}$, and an answer was lost.

The typical use of the closed-world assumption is in databases and in logic programming, where negation as failure plays the same role.
A trap is to apply the rules of a consequence relation, such as monotonicity, to conclusions obtained by default.
