---
tag: WZ0QZBR9ST
kind: example
name: A map on formulas that extends an assignment but is not a truth valuation
msc: ["03B05"]
topics: [JDK63589SA]
audience: ug1
not_instance_of:
  - target: H31CS3HK5P
    note: the map agrees with the assignment on variables, but it breaks the clauses for conjunction and negation
uses: [P0S056MDS7, TT7WT5HPN9]
sources:
  - url: https://en.wikipedia.org/wiki/Valuation_(logic)
    locator: Mathematical logic
  - book: isbn:9780122384523
    locator: Chapter 1
---

## Example

Here is a tempting but wrong rule for truth: "a formula is true when at least one of its letters is true".
Fix a truth assignment $v$, and define $f \colon \mathrm{Form} \to \{ 0, 1 \}$ by
$$f(\varphi) = \begin{cases} 1 & \text{if some variable that occurs in } \varphi \text{ has } v\text{-value } 1, \\ 0 & \text{otherwise.} \end{cases}$$
Take $v(p) = 1$ and $v(q) = 0$.
We show that $f$ agrees with $v$ on variables but is not a [[truth valuation|H31CS3HK5P]].

1. For a variable $s$, the only variable that occurs in $s$ is $s$ itself, so $f(s) = v(s)$.
2. The formula $p \land q$ contains $p$, and $v(p) = 1$, so $f(p \land q) = 1$.
3. The clause for $\land$ in the [[definition|P0S056MDS7]] asks for
   $$f(p \land q) = \min(f(p), f(q)) = \min(1, 0) = 0 .$$
   Steps 2 and 3 disagree, so $f$ breaks the clause for $\land$.
4. Also $f(\neg p) = 1$, since $p$ occurs in $\neg p$, but the clause for $\neg$ asks for $1 - f(p) = 0$.

So $f$ is not a truth valuation, and in particular $f \neq \bar v$.

## Remarks

The example shows that agreeing with $v$ on the variables is not enough.
A valuation must follow the clauses at every connective, and by the extension theorem $\bar v$ is the only map that does so; here $\bar v(p \land q) = 0$.

The map $f$ is not wrong everywhere.
It obeys the clause for $\lor$, because $\varphi \lor \psi$ contains a true variable exactly when $\varphi$ or $\psi$ does.
So $f$ and $\bar v$ agree on every formula built from variables with $\lor$ alone.
If $v$ gives $1$ to every variable, then $f$ is constant $1$, and it breaks the clause for $\neg$ at every formula $\neg \varphi$.

## Explanations

### L1 human

The wrong rule says "a formula is true when at least one of its letters is true".
With $p$ true and $q$ false, the rule calls "$p$ and $q$" true.
But "$p$ and $q$" is false, since $q$ is false.
The rule also calls "not $p$" true, but it is false.
So the rule does not follow the tables of the connectives.

### L2 human

To test a proposed map $g$ on formulas, check the clauses on small compound formulas first, such as $\neg p$, $p \land q$, $p \lor q$ and $p \to q$, in each row.
One failure, as in step 3, shows that $g$ is not a valuation.
To show that $g$ is a valuation, you need an argument for all formulas, not a list of cases.

Watch out.
Testing the clauses only on variables proves nothing, because the clauses are about compound formulas.
The map $f$ above passes every test on variables and still fails.
