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

Let $p$ and $q$ be propositional variables.
We show $p, \; p \to q \models q$.

1. The formulas contain only $p$ and $q$, so it suffices to look at the four truth assignments to $p$ and $q$.
2. The [[truth table|05RSK4Q657]] of [[implication|0NMG7W7Q11]] gives these values.

| $v(p)$ | $v(q)$ | $p \to q$ |
|---|---|---|
| 1 | 1 | 1 |
| 1 | 0 | 0 |
| 0 | 1 | 1 |
| 0 | 0 | 1 |

3. The premise $p$ is true in rows 1 and 2.
4. Of these, the premise $p \to q$ is true only in row 1.
5. In row 1 the conclusion $q$ has value 1.
6. So every assignment that makes both premises true makes $q$ true, and $p, \; p \to q \models q$.

## Remarks

This is the semantic form of the rule [[modus ponens|0Y0MQYST0M]].
The rule is sound because of this consequence: if a derivation step uses modus ponens on true lines, the new line is true.
By the semantic deduction theorem the same fact says that $p \land (p \to q) \to q$ is a tautology, and also that $p \to ((p \to q) \to q)$ is one.
The consequence stays true when we put any formulas $\varphi$ and $\psi$ in place of $p$ and $q$: $\varphi, \; \varphi \to \psi \models \psi$.
If we drop the premise $p$, the consequence fails: $p \to q \not\models q$, with the countermodel $v(p) = v(q) = 0$.

## Explanations

### L1 human

Suppose we know two things: "it is raining" and "if it is raining, the street is wet".
Then we may conclude "the street is wet".
To check this, we list the four cases of rain or no rain and wet or dry street.
Only one case makes both facts true, rain and a wet street, and in that case the street is wet.

### L2 human

The same check works for any formulas in place of $p$ and $q$.

1. Let $\varphi$ and $\psi$ be formulas and let $v$ be a truth assignment with $\bar v(\varphi) = 1$ and $\bar v(\varphi \to \psi) = 1$.
2. If $\bar v(\psi) = 0$, then $\bar v(\varphi \to \psi) = 0$ by the truth table, since $\bar v(\varphi) = 1$.
3. This contradicts step 1, so $\bar v(\psi) = 1$.
4. Hence $\varphi, \; \varphi \to \psi \models \psi$.

The typical use: in a proof of the soundness theorem, this check shows that modus ponens takes true lines to true lines.
A trap: the reverse argument "$q$ and $p \to q$, so $p$" is not valid; see [[affirming the consequent|ZW5A420AA9]].
