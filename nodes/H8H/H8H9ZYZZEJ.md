---
tag: H8H9ZYZZEJ
kind: example
name: Modus ponens as a logical consequence
msc: ["03B05"]
topics: [JDK63589SA]
audience: ug1
instance_of: [1HK0VYWTV7]
uses: [H31CS3HK5P, 0NMG7W7Q11, 05RSK4Q657]
sources:
  - url: https://en.wikipedia.org/wiki/Logical_consequence
    locator: Semantic consequence
  - url: https://en.wikipedia.org/wiki/Modus_ponens
    locator: lead section
---

## Example

The most used step in mathematics, "we have $p$, and $p$ implies $q$, so $q$", is a [[logical consequence|1HK0VYWTV7]].
Let $p$ and $q$ be propositional variables.
We show $p, \; p \to q \models q$ by the [[truth table|05RSK4Q657]] of [[implication|0NMG7W7Q11]]:
$$\begin{array}{cc|c} p & q & p \to q \\ \hline 1 & 1 & 1 \\ 1 & 0 & 0 \\ 0 & 1 & 1 \\ 0 & 0 & 1 \end{array}$$

1. The formulas contain only $p$ and $q$, so the four rows are all the cases.
2. The premise $p$ is true in rows 1 and 2.
3. Of these two rows, the premise $p \to q$ is true only in row 1.
4. In row 1 the conclusion $q$ has the value $1$.
5. So every row that makes both premises true makes $q$ true, and $p, \; p \to q \models q$.

Check: rows 3 and 4 make $p \to q$ true with $p$ false, and $q$ is $1$ in one and $0$ in the other, so these rows say nothing about $q$; the premise $p$ removes them.

## Remarks

This is the semantic form of the rule [[modus ponens|0Y0MQYST0M]].
It is the reason the rule is sound: if a derivation step uses modus ponens on true lines, the new line is true.
By the semantic deduction theorem the same fact says that $p \to ((p \to q) \to q)$ is a tautology, and so is $(p \land (p \to q)) \to q$.

The consequence stays true when we put any formulas $\varphi$ and $\psi$ in place of $p$ and $q$, so $\varphi, \; \varphi \to \psi \models \psi$.
Each premise is needed.
Without $p$ the consequence fails, since $p \to q \not\models q$ with the countermodel $v(p) = v(q) = 0$.
Without $p \to q$ it also fails, since $p \not\models q$ with the countermodel $v(p) = 1$, $v(q) = 0$.

Watch out.
The reverse argument "$q$ and $p \to q$, so $p$" looks similar but is not valid; see [[affirming the consequent|ZW5A420AA9]].

Try it.
Does $\neg q, \; p \to q \models \neg p$ hold?
Yes: the premise $\neg q$ forces $q = 0$, then $p \to q$ forces $p = 0$, and so $\neg p = 1$.
This valid form is called modus tollens.

## Explanations

### L1 human

Suppose we know two things: "it is raining" and "if it is raining, the street is wet".
Then we may conclude "the street is wet".
To check this, we list the four cases of rain or no rain and wet or dry street.
Only one case makes both facts true, rain and a wet street, and in that case the street is wet.

### L2 human

The same check works for any formulas in place of $p$ and $q$.

1. Let $\varphi$ and $\psi$ be formulas, and let $v$ be a truth assignment with $\bar v(\varphi) = 1$ and $\bar v(\varphi \to \psi) = 1$.
2. If $\bar v(\psi) = 0$, then $\bar v(\varphi \to \psi) = 0$ by the table, since $\bar v(\varphi) = 1$.
3. This contradicts step 1, so $\bar v(\psi) = 1$.
4. Hence $\varphi, \; \varphi \to \psi \models \psi$.

In the proof of the [[soundness theorem|XD629S54CS]], this check is the step that shows that modus ponens takes true lines to true lines.
