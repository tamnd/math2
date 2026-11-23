---
tag: TYYG5A3RSV
kind: example
name: Dependence atoms on a four-row team
msc: ["03B60"]
topics: [MDHDYV8QZW]
audience: research
uses: [DNAPTJ98WD]
instance_of: [DNAPTJ98WD]
sources:
  - url: https://en.wikipedia.org/wiki/Dependence_logic
    locator: Semantics
  - url: https://en.wikipedia.org/wiki/Dependence_logic
    locator: Properties
---

## Example

A dependence atom is a statement about a whole table of assignments, not about one row.
We test six formulas on one small table to see how the atoms behave.
We work in [[dependence logic|DNAPTJ98WD]] over a structure whose domain contains $\{0, 1, 2\}$.
Let $X$ be the team over the variables $x, y, z$ with these four assignments.

| assignment | $x$ | $y$ | $z$ |
|---|---|---|---|
| $s_1$ | $0$ | $0$ | $1$ |
| $s_2$ | $0$ | $0$ | $2$ |
| $s_3$ | $1$ | $1$ | $1$ |
| $s_4$ | $1$ | $2$ | $2$ |

The atom $=\!(t_1, \ldots, t_n, t)$ holds in a team when any two assignments that agree on $t_1, \ldots, t_n$ also agree on $t$.

1. $=\!(x, y)$ fails in $X$.
   The assignments $s_3$ and $s_4$ agree on $x = 1$, but $s_3(y) = 1$ and $s_4(y) = 2$.
2. $=\!(x, z, y)$ holds in $X$.
   The pairs $(x, z)$ are $(0, 1)$, $(0, 2)$, $(1, 1)$ and $(1, 2)$.
   They are all different, so no two assignments agree on $x$ and $z$.
3. $=\!(y, x)$ holds in $X$.
   The value $y = 0$ occurs in $s_1$ and $s_2$, and both have $x = 0$.
   The values $y = 1$ and $y = 2$ occur once each.
4. $=\!(x)$ fails in $X$.
   This constancy atom asks that all four assignments agree on $x$, but $s_1(x) = 0$ and $s_3(x) = 1$.
5. $=\!(x, y)$ holds in the subteam $Y = \{ s_1, s_2, s_3 \}$.
   The only two assignments that agree on $x$ are $s_1$ and $s_2$, and both have $y = 0$.
6. $=\!(x, y) \lor =\!(x, y)$ holds in $X$.
   A disjunction holds in a team when the team splits into two parts, one for each disjunct.
   We split $X = Y \cup \{ s_4 \}$.
   Step 5 gives $Y$, and a team with one assignment satisfies every dependence atom.

## Remarks

Steps 1 and 6 show that disjunction in team semantics is not idempotent.
The formula $=\!(x, y) \lor =\!(x, y)$ is weaker than $=\!(x, y)$.

Step 2 is an instance of a general fact: if we add a variable to the left side of an atom, the atom can only get easier to satisfy.
Fewer pairs of assignments agree on more variables, so there are fewer pairs to check.

Steps 1 and 5 agree with downward closure.
A subteam has fewer pairs of assignments, so it can only lose counterexamples.
Here, removing $s_4$ removes the only counterexample to $=\!(x, y)$.
In the same way, every subteam of $X$ satisfies $=\!(y, x)$, since $X$ does.

Small changes to the table move the answers.
If we change $s_4(y)$ from $2$ to $1$, then $=\!(x, y)$ holds in $X$, and $=\!(y, x)$ still holds.
If instead we change $s_2(y)$ from $0$ to $1$, then $=\!(y, x)$ fails, because $s_2$ and $s_3$ agree on $y = 1$ but not on $x$.
The empty subteam satisfies all six formulas, since it has no pair of assignments to compare.

## Explanations

### L1 human

The team is a small table with three columns and four rows.
"$y$ depends on $x$" asks this: whenever two rows have the same $x$, do they have the same $y$?
Rows three and four both have $x = 1$ but different values of $y$, so the answer is no.
If we delete row four, the answer becomes yes.
Deleting rows can only remove counterexamples, so a true dependence stays true in a smaller table.

### L2 human

We check one more formula, $\exists w \, =\!(x, w)$, in the team $X$.

1. The clause for $\exists w$ asks for a function $F \colon X \to M$ that gives each assignment a value of $w$.
2. We choose $F(s_1) = F(s_2) = 0$ and $F(s_3) = F(s_4) = 1$, so $w$ copies $x$.
3. In the new team, two assignments that agree on $x$ get the same value of $w$, so $=\!(x, w)$ holds.
   Check: the rows with $x = 0$ have $w = 0$, and the rows with $x = 1$ have $w = 1$.
4. The choice $F(s_1) = 0$ and $F(s_2) = 1$ would fail, because $s_1$ and $s_2$ agree on $x$.

The typical use of these checks is to read off the functional dependencies of a database table.
Watch out: do not check the atom row by row.
A single row never violates a dependence atom, and only pairs of rows do.
