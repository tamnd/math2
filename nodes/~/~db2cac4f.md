---
tag: ~db2cac4f
kind: example
name: An argument checked in the propositional calculus
msc: ["03B05"]
topics: [JDK63589SA]
audience: ug1
instance_of: [09K9MWD2QQ]
uses: [0NMG7W7Q11, 029JBBF693, 1HK0VYWTV7, 05RSK4Q657]
sources:
  - url: https://en.wikipedia.org/wiki/Propositional_logic
    locator: Semantics
  - url: https://en.wikipedia.org/wiki/Modus_tollens
    locator: lead section
---

## Example

Consider the argument with three premises and one conclusion.
Premise 1: if it rains, then the match is cancelled.
Premise 2: if the match is cancelled, then the tickets are refunded.
Premise 3: the tickets are not refunded.
Conclusion: it does not rain.
Let $p$ stand for "it rains", $q$ for "the match is cancelled" and $r$ for "the tickets are refunded".
The argument has the form
$$\set{p \to q,\ q \to r,\ \neg r} \models \neg p .$$
We check this [[logical consequence|1HK0VYWTV7]] in the propositional calculus.

1. By the definition of consequence, we must show: each valuation that gives the value $1$ to the three premises gives the value $1$ to $\neg p$.
2. Let $v$ be a valuation with $v(p \to q) = v(q \to r) = v(\neg r) = 1$.
3. From $v(\neg r) = 1$ and the table of [[negation|029JBBF693]], $v(r) = 0$.
4. From $v(q \to r) = 1$ and $v(r) = 0$, the table of [[implication|0NMG7W7Q11]] gives $v(q) = 0$, because $1 \to 0$ has the value $0$.
5. From $v(p \to q) = 1$ and $v(q) = 0$, the same table gives $v(p) = 0$.
6. So $v(\neg p) = 1$.
7. Steps 3 to 5 show that only one of the $2^3 = 8$ rows of the [[truth table|05RSK4Q657]] makes all premises true, the row $p = q = r = 0$.
8. In that row $\neg p$ is true, so the argument is valid by its form alone.

## Remarks

The argument combines a hypothetical syllogism with modus tollens.
Its correctness does not depend on rain, matches or tickets: any three statements in the places of $p$, $q$ and $r$ give a correct argument.
The premise $\neg r$ is necessary.
The valuation $v(p) = v(q) = v(r) = 1$ makes $p \to q$ and $q \to r$ true and makes $\neg p$ false, so $\set{p \to q,\ q \to r} \not\models \neg p$.
If we replace the conclusion $\neg p$ by $\neg q$, the argument stays valid, because step 4 already gives $v(q) = 0$.
If we replace the premise $\neg r$ by $r$, the valuation with all values $1$ shows that the argument becomes invalid.

## Explanations

### L1 human

The argument says: rain cancels the match, a cancelled match gives a refund, and there was no refund.
So there was no rain.
To check it, we only look at which of the three statements are true or false.
If there was no refund, the match was not cancelled, since a cancellation always gives a refund.
And if the match was not cancelled, it did not rain.
This reasoning works for any three statements with the same pattern.

### L2 human

We check the same form with the full table instead of the shortcut.

1. List the $8$ rows of values for $p$, $q$ and $r$.
2. In each row, compute $p \to q$, $q \to r$ and $\neg r$.
3. The premise $\neg r$ is true only in the $4$ rows with $r = 0$.
4. Among these rows, $q \to r$ is true only in the $2$ rows with $q = 0$.
5. Among these rows, $p \to q$ is true only in the row with $p = 0$.
6. In that row $\neg p = 1$, so the conclusion is true in every row where all premises are true.

The typical use is to test an everyday argument: write its form, then search for a row with true premises and a false conclusion.
A trap is to look only at the row where everything is true.
The definition of consequence asks about every row where the premises are true.
