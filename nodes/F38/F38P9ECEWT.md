---
tag: F38P9ECEWT
kind: example
name: Computing the truth value of a formula
msc: ["03B05"]
topics: [JDK63589SA]
audience: ug1
instance_of: [H31CS3HK5P]
uses: [P0S056MDS7, TT7WT5HPN9]
sources:
  - url: https://en.wikipedia.org/wiki/Interpretation_(logic)
    locator: Interpretations for propositional logic
  - book: isbn:9781482237726
    locator: Chapter 1
---

## Example

A [[truth valuation|H31CS3HK5P]] computes the value of a formula from the inside out, one connective at a time.
Let
$$\varphi = (p \to (q \land \neg r)) \leftrightarrow (\neg p \lor q),$$
and let $v$ be the assignment with $v(p) = v(q) = v(r) = 1$.
We apply the clauses of the [[definition|P0S056MDS7]] from the variables up to the main connective $\leftrightarrow$.

1. $\bar v(\neg r) = 1 - 1 = 0$.
2. $\bar v(q \land \neg r) = \min(1, 0) = 0$.
3. $\bar v(p \to (q \land \neg r)) = \max(1 - 1, 0) = 0$.
4. $\bar v(\neg p) = 1 - 1 = 0$, and $\bar v(\neg p \lor q) = \max(0, 1) = 1$.
5. The two sides of $\leftrightarrow$ have the values $0$ and $1$, which differ, so $\bar v(\varphi) = 0$.

Now change only $r$: let $w(p) = w(q) = 1$ and $w(r) = 0$.

6. $\bar w(\neg r) = 1$, so $\bar w(q \land \neg r) = \min(1, 1) = 1$ and $\bar w(p \to (q \land \neg r)) = \max(0, 1) = 1$.
7. $\bar w(\neg p \lor q) = 1$, as in step 4.
8. Both sides have the value $1$, so $\bar w(\varphi) = 1$.

## Remarks

The computation follows the parse tree from the leaves to the root, with one clause at each node.
Since $v$ and $w$ differ only at $r$ and give $\varphi$ different values, the value of $\varphi$ really depends on $r$.
A variable that does not occur in $\varphi$, such as $s$, has no effect at all on its value.

The first assignment shows that $\varphi$ is not a [[tautology|05006AJ7DZ]], and the second shows that it is satisfiable.
In fact $v$ gives the only false row, as the L2 explanation shows.

Watch out.
One true row shows that a formula is satisfiable, but a tautology needs every row.
Stopping at the first true row is a common slip.

## Explanations

### L1 human

We have a formula with three letters, and all three letters are true.
We work from the inside out.
"Not $r$" is false, so "$q$ and not $r$" is false.
"If $p$ then ($q$ and not $r$)" is then false, since $p$ is true.
On the other side, "not $p$ or $q$" is true, since $q$ is true.
The two sides differ, so the "if and only if" is false.

### L2 human

We find the whole truth table of $\varphi$ without writing $8$ rows.
Write $A = p \to (q \land \neg r)$ and $B = \neg p \lor q$.
If $p = 0$, then $A = 1$ and $B = 1$, so $\varphi = 1$ in these $4$ rows.
If $p = 1$, then the clauses give
$$A = \min(q, 1 - r), \qquad B = q .$$
For $p = 1$ and $q = 0$, both $A$ and $B$ are $0$, so $\varphi = 1$ in these $2$ rows.
For $p = 1$ and $q = 1$, we get $A = 1 - r$ and $B = 1$, so $\varphi = 1$ exactly when $r = 0$.
So $\varphi$ is false in exactly one of the $8$ rows, $p = q = r = 1$.
Splitting on one variable first is the typical way to shorten a table by hand.
