---
tag: ASBWAKPMFV
kind: proof
name: Proof of the semantic substitution lemma by induction
msc: ["03B10"]
topics: [NJDME6F845]
audience: ug2
proves: A7S460KHBM
uses: [1WTCZB4DVB, FM580NZ9W6, NCDZ969V7X, 6D3WA7N2W4, HYJ10AF6RT]
methods: [12MQ2NJ29A, 0WCP0PVET6]
sources:
  - book: isbn:9780122384523
    locator: Chapter 2
  - url: https://builds.openlogicproject.org/
    locator: Syntax and Semantics
---

## Proof

We prove part 1 by induction on terms and part 2 by induction on formulas, and the only step with real content is the quantifier step.

First we recall the clauses of [[substitution|NCDZ969V7X]] that the proof uses.
For terms, $x[t/x] = t$, $y[t/x] = y$ for a variable $y \neq x$, $c[t/x] = c$, and $f(u_1, \ldots, u_n)[t/x] = f(u_1[t/x], \ldots, u_n[t/x])$.
For formulas, substitution acts on the terms of atomic formulas and commutes with $\neg$, $\wedge$, $\vee$, $\to$ and $\leftrightarrow$.
For a quantifier, $(\forall y \, \psi)[t/x] = \forall y \, \psi$ when $x$ is not free in $\forall y \, \psi$, and $(\forall y \, \psi)[t/x] = \forall y \, (\psi[t/x])$ otherwise, and the same holds for $\exists$.
A syntactic induction from these clauses shows that $\psi[t/x] = \psi$ when $x$ is not free in $\psi$.
Throughout, $a = t^{\mathcal{M}}[s]$, and $\models$ is [[satisfaction|1WTCZB4DVB]].

Part 1, by [[structural induction|12MQ2NJ29A]] on the term $u$, for every assignment $s$.

1. If $u = x$, then $u[t/x] = t$, whose value under $s$ is $a$.
   The variant $s[x \mapsto a]$ also gives $x$ the value $a$, so the two sides agree.
2. If $u = y$ with $y \neq x$, then $u[t/x] = y$, whose value is $s(y)$.
   The variant $s[x \mapsto a]$ also sends $y$ to $s(y)$, because it changes only $x$.
3. If $u = c$, both sides equal $c^{\mathcal{M}}$.
4. If $u = f(u_1, \ldots, u_n)$, the induction hypothesis gives $(u_i[t/x])^{\mathcal{M}}[s] = u_i^{\mathcal{M}}[s[x \mapsto a]]$ for each $i$.
5. Applying $f^{\mathcal{M}}$ to these equal arguments gives equal values, which is the claim for $u$.

Part 2, by induction on $\varphi$.
The claim for $\varphi$ is that the equivalence holds for every assignment $s$ and every term $t$ substitutable for $x$ in $\varphi$.

6. Let $\varphi = R(u_1, \ldots, u_n)$, so that $\varphi[t/x] = R(u_1[t/x], \ldots, u_n[t/x])$.
7. By part 1, the value of each $u_i[t/x]$ under $s$ equals the value of $u_i$ under $s[x \mapsto a]$.
   So one tuple lies in $R^{\mathcal{M}}$ if and only if the other does.
8. The case of an equation $u_1 = u_2$ is the same, with equality of the two values in place of membership in $R^{\mathcal{M}}$.
9. Let $\varphi = \neg \psi$ or $\varphi = \psi \mathbin{\square} \chi$ for a binary connective $\square$.
   If $t$ is substitutable for $x$ in $\varphi$, then it is substitutable in $\psi$ and in $\chi$, since their free occurrences of $x$ are those of $\varphi$.
10. The induction hypothesis gives the equivalence for $\psi$ and $\chi$, and the clause for the connective carries it to $\varphi$.
11. Let $\varphi = \forall y \, \psi$.
    We split into two [[cases|0WCP0PVET6]], according to whether $x$ is free in $\varphi$.
12. Case A: $x$ is not free in $\varphi$.
    Then $\varphi[t/x] = \varphi$, so the left side says $\mathcal{M} \models \varphi[s]$.
13. The assignments $s$ and $s[x \mapsto a]$ differ at most at $x$, which is not free in $\varphi$.
    By the [[coincidence lemma|FM580NZ9W6]], they give $\varphi$ the same value, which proves case A.
14. Case B: $x$ is free in $\varphi$.
    Then $y \neq x$, and $\varphi[t/x] = \forall y \, (\psi[t/x])$.
15. A free occurrence of $x$ in $\varphi$ lies inside $\forall y$, and $t$ is substitutable for $x$ in $\varphi$.
    So $y$ does not occur in $t$, and $t$ is also substitutable for $x$ in $\psi$.
16. Let $b \in M$.
    Since $y$ does not occur in $t$, part 1 of the coincidence lemma gives $t^{\mathcal{M}}[s[y \mapsto b]] = a$.
17. The induction hypothesis for $\psi$, with the assignment $s[y \mapsto b]$, says that $\psi[t/x]$ holds under $s[y \mapsto b]$ if and only if $\psi$ holds under $s[y \mapsto b][x \mapsto a]$.
18. Since $x \neq y$, the two updates act on different variables, so $s[y \mapsto b][x \mapsto a] = s[x \mapsto a][y \mapsto b]$.
19. Hence, for every $b \in M$, we have $\mathcal{M} \models \psi[t/x]\,[s[y \mapsto b]]$ if and only if $\mathcal{M} \models \psi\,[s[x \mapsto a][y \mapsto b]]$.
20. The clause for $\forall y$ on both sides gives $\mathcal{M} \models \varphi[t/x]\,[s]$ if and only if $\mathcal{M} \models \varphi\,[s[x \mapsto a]]$.
21. Let $\varphi = \exists y \, \psi$.
    Steps 12 to 19 apply without change, and the clause for $\exists y$ gives the claim.

This proves the semantic substitution lemma.

## Idea

The term case is a direct check of the definitions, and the connectives pass the claim along.
At a quantifier $\forall y$, the danger is that changing $y$ could change the value of $t$.
Substitutability says that $y$ is not in $t$, so the value $a$ stays fixed while $y$ runs through the domain.
Then the two updates of the assignment, one at $x$ and one at $y$, commute, and the induction hypothesis closes the step.

## Variants

With capture-avoiding substitution, case B first renames $y$ to a fresh variable.
Then the proof also needs the lemma that renaming a bound variable gives an equivalent formula, and after that the lemma holds for every term $t$.
