---
tag: TQT5N8ZMGK
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

An everyday argument becomes a question about truth tables once we replace its sentences by letters.
Take this argument.
If it rains, then the match is cancelled.
If the match is cancelled, then the tickets are refunded.
The tickets are not refunded.
So it does not rain.

Let $p$ stand for "it rains", $q$ for "the match is cancelled" and $r$ for "the tickets are refunded".
The argument has the form
$$\{ p \to q,\ q \to r,\ \neg r \} \models \neg p .$$
We check this [[logical consequence|1HK0VYWTV7]]: every valuation that makes the three premises true must make $\neg p$ true.
Instead of writing all $2^3 = 8$ rows of the [[truth table|05RSK4Q657]], we work backward from the premises.

1. Let $v$ be a valuation that gives the value $1$ to all three premises.
2. Since $v(\neg r) = 1$, the table of [[negation|029JBBF693]] gives $v(r) = 0$.
3. Since $v(q \to r) = 1$ and $v(r) = 0$, we get $v(q) = 0$, because the table of [[implication|0NMG7W7Q11]] gives $1 \to 0$ the value $0$.
4. Since $v(p \to q) = 1$ and $v(q) = 0$, we get $v(p) = 0$ for the same reason.
5. So $v(\neg p) = 1$.

The steps show that exactly one row makes all three premises true, the row $p = q = r = 0$, and in that row the conclusion $\neg p$ is true.
So the argument is valid by its form alone.

## Remarks

The argument chains two implications and then applies modus tollens.
Its validity has nothing to do with rain, matches or tickets: any three statements in the places of $p$, $q$ and $r$ give a valid argument.

Every premise does work here.
If we drop $\neg r$, the valuation with $p = q = r = 1$ makes $p \to q$ and $q \to r$ true and $\neg p$ false, so $\{ p \to q,\ q \to r \} \not\models \neg p$.
If we change $\neg r$ to $r$, the same valuation makes all premises true and the conclusion false, so the argument becomes invalid.
If we keep the premises and change the conclusion to $\neg q$, the argument stays valid, because step 3 already gives $v(q) = 0$.

Watch out.
A common slip is to check only the row where every variable is true.
The definition asks about every row where the premises are true, and here that is a different row.

## Explanations

### L1 human

The argument says: rain cancels the match, a cancelled match gives a refund, and there was no refund.
So there was no rain.
To check it, we only ask which of the three statements are true or false.
If there was no refund, the match was not cancelled, since a cancellation always gives a refund.
And if the match was not cancelled, it did not rain.
This reasoning works for any three statements with the same pattern.

### L2 human

We check the same form with the full table instead of the shortcut, and we cut the table down one premise at a time.
The premise $\neg r$ is true only in the $4$ rows with $r = 0$.
Among these rows, $q \to r$ is true only in the $2$ rows with $q = 0$.
Among these, $p \to q$ is true only in the row with $p = 0$:
$$\begin{array}{ccc|ccc|c} p & q & r & p \to q & q \to r & \neg r & \neg p \\ \hline 0 & 0 & 0 & 1 & 1 & 1 & 1 \end{array}$$
Check: in this surviving row the conclusion $\neg p$ has the value $1$.

The typical use is to test an everyday argument: write its form, then search for a row with true premises and a false conclusion.
If the search fails, the argument is valid; if it succeeds, the row is a countermodel.
