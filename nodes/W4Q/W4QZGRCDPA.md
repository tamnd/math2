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

A database answers queries as if every fact it does not store were false.
This is the closed-world assumption, and it is not a [[consequence relation|J78Y1M4GND]], because new facts can cancel old answers.

Let $L$ be the formulas of propositional logic over the two variables $p$ and $q$, and let $\models$ be classical [[logical consequence|1HK0VYWTV7]].
For $\Gamma \subseteq L$, add the negation of every variable that does not follow from $\Gamma$:
$$\overline{\Gamma} = \Gamma \cup \{ \neg a : a \in \{ p, q \} \text{ and } \Gamma \not\models a \}.$$
Then define closed-world inference by
$$\Gamma \mathrel{|\!\sim} \varphi \iff \overline{\Gamma} \models \varphi.$$

We show that monotonicity fails.

1. Take $\Gamma = \emptyset$.
   Neither $p$ nor $q$ is a tautology, so $\overline{\emptyset} = \{ \neg p, \neg q \}$, and $\emptyset \mathrel{|\!\sim} \neg p$.
2. Take $\Delta = \{ p \}$, so $\emptyset \subseteq \Delta$.
   Here $\Delta \models p$ and $\Delta \not\models q$, so $\overline{\Delta} = \{ p, \neg q \}$.
3. The valuation with $p = 1$ and $q = 0$ makes $\overline{\Delta}$ true and $\neg p$ false, so $\Delta \not\mathrel{|\!\sim} \neg p$.
4. The premises grew from $\emptyset$ to $\{ p \}$, and the conclusion $\neg p$ was lost, so monotonicity fails.

Reflexivity still holds: if $\varphi \in \Gamma$, then $\varphi \in \overline{\Gamma}$, so $\overline{\Gamma} \models \varphi$ and $\Gamma \mathrel{|\!\sim} \varphi$.

## Remarks

The failure is the purpose of the closed-world assumption: new information should be able to cancel a default conclusion.
Inference relations of this kind are studied in non-monotonic logic, which keeps reflexivity and replaces monotonicity by weaker conditions.

The assumption has a second defect with disjunctions.
For $\Gamma = \{ p \vee q \}$, neither $p$ nor $q$ follows, so $\overline{\Gamma} = \{ p \vee q, \neg p, \neg q \}$, which has no model.
Then $\Gamma \mathrel{|\!\sim} \varphi$ for every $\varphi$, although $\Gamma$ itself is satisfiable.
This is why the assumption is used mainly for sets of atomic facts and Horn clauses, where its result is consistent.
Raymond Reiter studied it for databases in 1978.

## Explanations

### L1 human

A train timetable lists the trains that run.
If a train from Paris at 3 o'clock is not listed, we conclude that there is no such train.
If the company adds that train to the list, the conclusion disappears.
New information destroyed an old conclusion, so this kind of reasoning is not monotone, and logical consequence never behaves like this.

### L2 human

We repeat the check with a small database of flights.
Let $a$ say "there is a flight from A to B" and $b$ say "there is a flight from B to C".
The empty database gives $\overline{\emptyset} = \{ \neg a, \neg b \}$, so the query "is there no flight from A to B?" gets the answer yes.
After we store $a$, the closure is $\{ a, \neg b \}$, and the same query gets the answer no.

The typical use of the closed-world assumption is in databases and in logic programming, where negation as failure plays the same role.
Watch out: rules of a consequence relation, such as monotonicity, do not apply to conclusions drawn by default.
