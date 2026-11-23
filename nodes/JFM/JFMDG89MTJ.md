---
tag: JFMDG89MTJ
kind: example
name: Strings that are not propositional formulas
msc: ["03B05"]
topics: [JDK63589SA]
audience: ug1
not_instance_of:
  - target: TT7WT5HPN9
    note: each string fails a property that every formula has, proved by induction on formulas
uses: [TFDYXS3K1N, EDRV3N0SA3]
sources:
  - url: https://en.wikipedia.org/wiki/Well-formed_formula
    locator: Propositional calculus
  - book: isbn:9780122384523
    locator: Chapter 1
---

## Example

To prove that a string is not a formula, we need a property that every formula has and the string lacks.
A failed search for a formation sequence proves nothing, because the next search might succeed.
We show that the strings $(p \land \land q)$, $(p \land q$ and $)p \land q($ are not [[propositional formulas|TT7WT5HPN9]].

First we prove two properties by [[induction on formulas|EDRV3N0SA3]].

1. Property B: a formula has as many left brackets as right brackets, and twice as many brackets as connectives.
   A variable has $0$ brackets and $0$ connectives.
   The rules $(\neg \varphi)$ and $(\varphi \circ \psi)$ each add one left bracket, one right bracket and one connective, so they keep B.
2. Property F: the first symbol of a formula is a variable or a left bracket.
   A variable starts with itself, and $(\neg \varphi)$ and $(\varphi \circ \psi)$ start with a left bracket.

Now we test the three strings.

3. The string $(p \land \land q)$ has $2$ brackets and $2$ connectives, and $2 \neq 2 \cdot 2$, so it fails B.
4. The string $(p \land q$ has $1$ left bracket and $0$ right brackets, so it fails B.
5. The string $)p \land q($ starts with a right bracket, so it fails F.

So none of the three strings is a formula.

## Remarks

The third string passes B: it has $1$ left bracket, $1$ right bracket and $1$ connective.
So B alone does not decide whether a string is a formula.
Each property of this kind gives only a necessary condition.
A full test is the parsing algorithm that the [[unique readability theorem|6KBJX91N7G]] supports: find the main connective by the bracket count, then test the two parts.

Small changes move a string across the line.
The string $(p)$ fails B, since it has $2$ brackets and $0$ connectives.
Remove one $\land$ from the first string and you get $(p \land q)$, which is a formula.

## Explanations

### L1 human

Not every string of logic symbols is a formula.
In "$(p$ and and $q)$" the word "and" appears twice in a row, with nothing between the two.
In "$(p$ and $q$" a bracket is opened and never closed.
To prove that such a string is not a formula, we find a rule that every formula obeys, for example "brackets come in pairs", and we show that the string breaks the rule.

### L2 human

Is $((p \to q)(\neg r))$ a formula?
Count the symbols: $3$ left brackets, $3$ right brackets and $2$ connectives.
Property B asks for
$$2 \cdot 2 = 4$$
brackets, but the string has $6$, so it is not a formula.
The reason is a missing binary connective between $(p \to q)$ and $(\neg r)$.
An invariant like B is the typical quick check before a full parse.

Watch out.
A string that passes B need not be a formula, as $)p \land q($ shows.
