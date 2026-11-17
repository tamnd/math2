---
tag: JZEBE7HZWQ
kind: example
name: Tseitin transformation against the distributive CNF
msc: ["03B05", "68Q25"]
topics: [JDK63589SA]
audience: ug2
instance_of: [S367PDDP61]
uses: [S367PDDP61, 0B3D4C8YF2, 0JMR2HM2N2]
sources:
  - url: https://en.wikipedia.org/wiki/Tseytin_transformation
    locator: Motivation
  - url: https://en.wikipedia.org/wiki/Conjunctive_normal_form
    locator: lead section
---

## Example

For $n \ge 1$ let $\varphi_n = (x_1 \land y_1) \lor (x_2 \land y_2) \lor \dots \lor (x_n \land y_n)$, bracketed to the left.
We compare an equivalent [[CNF|0B3D4C8YF2]] of $\varphi_n$ with the [[Tseitin transformation|S367PDDP61]] $T(\varphi_n)$.

1. The distributive law gives the CNF whose clauses are $\set{z_1, \dots, z_n}$ with $z_i \in \set{x_i, y_i}$ for each $i$. It has $2^n$ clauses with $n$ literals each.
2. Every CNF $\psi$ that is [[logically equivalent|0JMR2HM2N2]] to $\varphi_n$ has at least $2^n$ clauses. We may drop clauses with a complementary pair, since they are always true.
3. Let $C$ be a clause of $\psi$. If, for some $i$, neither $x_i$ nor $y_i$ is a literal of $C$, then make $x_i = y_i = 1$ and make every literal of $C$ false.
4. This is possible, because $C$ has no complementary pair and its literals on $x_i$, $y_i$ are negative. The assignment makes $\varphi_n$ true and $C$ false, against $\varphi_n \models \psi$.
5. So each clause of $\psi$ contains $x_i$ or $y_i$, for every $i$.
6. Fix a choice $z = (z_1, \dots, z_n)$ with $z_i \in \set{x_i, y_i}$. Let $a_z$ make each $z_i$ false and its partner in $\set{x_i, y_i}$ true.
7. Each term $x_i \land y_i$ has a false variable under $a_z$, so $\varphi_n$ and $\psi$ are false under $a_z$. So some clause $C_z$ of $\psi$ is false under $a_z$.
8. By step 5, $C_z$ contains $x_i$ or $y_i$ for each $i$, and this literal is false under $a_z$. So it is $z_i$, and $C_z$ does not contain the partner of $z_i$.
9. So the set of positive literals of $C_z$ is exactly $\set{z_1, \dots, z_n}$. Different choices $z$ give different clauses $C_z$, and there are $2^n$ choices.
10. The Tseitin transformation names the $n$ conjunctions and the $n - 1$ disjunctions. Each gives 3 clauses, and the root gives 1 more.
11. So $T(\varphi_n)$ has $3 n + 3 (n - 1) + 1 = 6 n - 2$ clauses in $2 n + (2 n - 1) = 4 n - 1$ variables.

For $n = 10$ every equivalent CNF has at least 1024 clauses, while $T(\varphi_{10})$ has 58 clauses.

## Remarks

The exponential growth is not a weakness of the distributive law alone.
Steps 2 to 9 prove it for every equivalent CNF.
The Tseitin transformation avoids the bound because it gives an [[equisatisfiable|B37TYWXS74]] formula with new variables, not an equivalent one.
For $n = 1$ the comparison goes the other way: $\varphi_1 = x_1 \land y_1$ is already a CNF with 2 clauses, and $T(\varphi_1)$ has 4.
The Tseitin form has more clauses up to $n = 4$, with 16 against 22, and fewer from $n = 5$ on, with 32 against 28.

## Explanations

### L1 human

The rule says "at least one of the pairs is complete".
Written as a list of "or" rules, it needs one rule for every way to pick one member from each pair.
With 10 pairs this is 1024 rules.
With helper names for the pairs, about 6 short rules per pair are enough.
So the helpers keep the list short.

### L2 human

The count in step 11 is exact: one new variable and 3 clauses for each of the $2 n - 1$ binary connectives, plus the root clause.
The lower bound in steps 2 to 9 uses the typical argument for CNF size.
A clause that misses a term can be made false while the formula stays true.
A trap is to think that some clever equivalent CNF avoids the blow up.
No equivalent CNF does, so any short CNF must use new variables.
