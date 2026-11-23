---
tag: T72RET4M6A
kind: proof
name: Proof of the coincidence lemma by induction on terms and formulas
msc: ["03B10"]
topics: [NJDME6F845]
audience: ug2
proves: FM580NZ9W6
uses: [1WTCZB4DVB, 6D3WA7N2W4, HYJ10AF6RT]
methods: [12MQ2NJ29A]
sources:
  - book: isbn:9780122384523
    locator: Section 2.2
  - url: https://builds.openlogicproject.org/
    locator: Syntax and Semantics
---

## Proof

We follow the recursive clauses of [[satisfaction|1WTCZB4DVB]] and prove each part by [[structural induction|12MQ2NJ29A]], first on terms and then on formulas.

Part 1, by induction on the term $t$.
Assume that $s_1$ and $s_2$ agree on the variables of $t$.

1. If $t$ is a variable $x$, then $x$ occurs in $t$, so $s_1(x) = s_2(x)$.
   Hence $t^{\mathcal{M}}[s_1] = s_1(x) = s_2(x) = t^{\mathcal{M}}[s_2]$.
2. If $t$ is a constant symbol $c$, then both values equal $c^{\mathcal{M}}$, because the value of a constant does not use the assignment.
3. Let $t = f(t_1, \ldots, t_n)$.
   Every variable of $t_i$ occurs in $t$, so $s_1$ and $s_2$ agree on the variables of each $t_i$.
4. By the induction hypothesis, $t_i^{\mathcal{M}}[s_1] = t_i^{\mathcal{M}}[s_2]$ for each $i$.
5. Both values of $t$ are $f^{\mathcal{M}}$ applied to the same arguments, so they are equal.

Part 2, by induction on $\varphi$.
We prove the following claim for each $\varphi$: for all assignments $s_1, s_2$ that agree on the free variables of $\varphi$, we have $\mathcal{M} \models \varphi[s_1]$ if and only if $\mathcal{M} \models \varphi[s_2]$.

6. Let $\varphi = R(t_1, \ldots, t_n)$.
   Every variable of each $t_i$ is free in $\varphi$, so part 1 gives $t_i^{\mathcal{M}}[s_1] = t_i^{\mathcal{M}}[s_2]$ for each $i$.
7. So the tuple of values is the same under $s_1$ and under $s_2$, and it lies in $R^{\mathcal{M}}$ under both or under neither.
8. Let $\varphi$ be $t_1 = t_2$.
   By part 1, each side has the same value under $s_1$ and under $s_2$, so the equation holds under both or under neither.
9. Let $\varphi = \neg \psi$.
   The free variables of $\psi$ are those of $\varphi$, so the induction hypothesis gives the same truth value for $\psi$ under $s_1$ and $s_2$, and then for $\neg \psi$.
10. Let $\varphi = \psi \mathbin{\square} \chi$ with $\square$ one of $\wedge$, $\vee$, $\to$, $\leftrightarrow$.
    The free variables of $\psi$ and of $\chi$ are free in $\varphi$, so the induction hypothesis applies to both parts.
11. The clause for $\square$ computes the value of $\varphi$ from the values of $\psi$ and $\chi$, and these do not change from $s_1$ to $s_2$.
    So the value of $\varphi$ does not change.
12. Let $\varphi = \forall x \, \psi$, and fix $a \in M$.
    We compare the variants $s_1[x \mapsto a]$ and $s_2[x \mapsto a]$.
13. At $x$, both variants take the value $a$, by the definition of a variant.
14. Let $y \neq x$ be free in $\psi$.
    Then $y$ is free in $\varphi$, so $s_1(y) = s_2(y)$, and both variants take this common value at $y$.
15. So the two variants agree on all free variables of $\psi$.
    The induction hypothesis for $\psi$, applied to these variants, gives $\mathcal{M} \models \psi[s_1[x \mapsto a]]$ if and only if $\mathcal{M} \models \psi[s_2[x \mapsto a]]$.
16. Step 15 holds for every $a \in M$.
    By the clause for $\forall$, we get $\mathcal{M} \models \varphi[s_1]$ if and only if $\mathcal{M} \models \varphi[s_2]$.
17. Let $\varphi = \exists x \, \psi$.
    Steps 12 to 15 apply without change, and the clause for $\exists$ gives the claim.

Part 3, by the same kind of induction, for one fixed assignment $s$.

18. Each $L$-term $t$ has the same value in $\mathcal{M}$ and in $\mathcal{M}'$, because all its symbols are in $L$ and get the same interpretations.
    The induction on $t$ runs as in steps 1 to 5.
19. An atomic $L$-formula holds in $\mathcal{M}$ exactly when it holds in $\mathcal{M}'$, by step 18 and because $R^{\mathcal{M}} = R^{\mathcal{M}'}$ for each relation symbol $R$ of $L$.
20. The steps for $\neg$ and for the binary connectives are as in steps 9 to 11.
21. For $\forall x \, \psi$ and $\exists x \, \psi$, the two structures have the same domain.
    So the variants $s[x \mapsto a]$ range over the same set, and the induction hypothesis gives the claim.

This proves parts 1, 2 and 3 of the coincidence lemma.

## Idea

Satisfaction is defined by recursion on the formula, so we prove the claim by induction along the same recursion.
Terms, atomic formulas and connectives pass the agreement from the parts to the whole with no work.
The only real case is the quantifier: the clause for $\forall x$ overwrites $x$, so the two variants agree at $x$ as well as on the other free variables.
That is why the claim must speak about all pairs of assignments at once, since the quantifier step uses it for the variants, not for $s_1$ and $s_2$.

## Variants

Mathlib avoids the general lemma by a different design.
It interprets a formula with a map on its free variables only and uses de Bruijn indices for bound variables, so part 2 is built into the definition.
The work then moves into lemmas about renaming the free variables.
