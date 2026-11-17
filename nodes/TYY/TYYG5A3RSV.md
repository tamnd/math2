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

We work in [[dependence logic|DNAPTJ98WD]] over a structure whose domain contains $\{0, 1, 2\}$.
Let $X$ be the team over the variables $x, y, z$ with these four assignments.

| assignment | $x$ | $y$ | $z$ |
|---|---|---|---|
| $s_1$ | $0$ | $0$ | $1$ |
| $s_2$ | $0$ | $0$ | $2$ |
| $s_3$ | $1$ | $1$ | $1$ |
| $s_4$ | $1$ | $2$ | $2$ |

The atom $=\!(t_1, \ldots, t_n, t)$ holds in a team when any two assignments that agree on $t_1, \ldots, t_n$ also agree on $t$.
We check six formulas.

1. $=\!(x, y)$ fails in $X$. The assignments $s_3$ and $s_4$ agree on $x = 1$, but $s_3(y) = 1$ and $s_4(y) = 2$.
2. $=\!(x, z, y)$ holds in $X$. The pairs $(x, z)$ are $(0, 1)$, $(0, 2)$, $(1, 1)$ and $(1, 2)$, all different, so no two assignments agree on $x$ and $z$.
3. $=\!(y, x)$ holds in $X$. The value $y = 0$ occurs in $s_1$ and $s_2$, both with $x = 0$; the values $y = 1$ and $y = 2$ occur once each.
4. $=\!(x)$ fails in $X$. The constancy atom asks that all four assignments agree on $x$, and $s_1(x) = 0 \neq 1 = s_3(x)$.
5. $=\!(x, y)$ holds in the subteam $Y = \{ s_1, s_2, s_3 \}$. The only pair that agrees on $x$ is $s_1, s_2$, and both have $y = 0$.
6. $=\!(x, y) \lor =\!(x, y)$ holds in $X$. We split $X = Y \cup \{ s_4 \}$; step 5 gives $Y$, and a team with one assignment satisfies every dependence atom.

## Remarks

Step 1 and step 6 together show that disjunction in team semantics is not idempotent: $=\!(x, y) \lor =\!(x, y)$ is weaker than $=\!(x, y)$.
Step 2 shows that adding a variable to the left side of an atom can only make the atom easier to satisfy.
Steps 3 and 5 are instances of downward closure: every subteam of $X$ satisfies $=\!(y, x)$, and removing $s_4$ repairs $=\!(x, y)$.
If we change $s_4(y)$ from $2$ to $1$, then $=\!(x, y)$ holds in $X$, and $=\!(y, x)$ still holds.
If instead we change $s_2(y)$ from $0$ to $1$, then $=\!(y, x)$ fails, because $s_2$ and $s_3$ agree on $y = 1$ but not on $x$.
The empty subteam satisfies all six formulas, since there is no pair of assignments to compare.

## Explanations

### L1 human

The team is a small table with three columns and four rows.
"$y$ depends on $x$" asks: whenever two rows have the same $x$, do they have the same $y$.
Rows three and four both have $x = 1$ but different $y$, so the answer is no.
If we delete row four, the answer becomes yes.
Deleting rows can only remove counterexamples, which is why a true dependence stays true in a smaller table.

### L2 human

We check one more formula, $\exists w \, =\!(x, w)$, in the team $X$.

1. The clause for $\exists w$ asks for a function $F \colon X \to M$ that gives each assignment a value of $w$.
2. We choose $F(s_1) = F(s_2) = 0$ and $F(s_3) = F(s_4) = 1$, so $w$ copies $x$.
3. In the new team, two assignments that agree on $x$ get the same value of $w$, so $=\!(x, w)$ holds.
4. The choice $F(s_1) = 0$, $F(s_2) = 1$ would fail, because $s_1$ and $s_2$ agree on $x$.

The typical use is to read off functional dependencies of a database table.
A trap is to check the atom row by row: a single row never violates a dependence atom, and only pairs of rows do.
