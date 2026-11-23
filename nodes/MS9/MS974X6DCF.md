---
tag: MS974X6DCF
kind: proof
name: Proof that variable occurrences in atomic formulas are free
msc: ["03B10"]
topics: [PSRDJXRW53]
audience: ug2
proves: D039R5C8TC
uses: [MCZRXR3SVB, 9CNGDRAMGC, Y3FZTH5158, 6D3WA7N2W4, 3QPV4XW8MC, DKFGQTRYZE]
methods: [12MQ2NJ29A, 0NTF6DMVAP]
sources:
  - book: isbn:9780122384523
    locator: Section 2.1
  - url: https://en.wikipedia.org/wiki/Atomic_formula
    locator: Atomic formula in first-order logic
---

## Proof

We show that an atomic formula contains no quantifier, so nothing in it can bind a variable, and then compute its free variables from the base clause.
Let $\varphi$ be $t_1 = t_2$ or $R(t_1, \dots, t_n)$, as in the [[statement|D039R5C8TC]].
We use the [[definition of free and bound variables|Y3FZTH5158]].

1. No [[term|6D3WA7N2W4]] contains the symbol $\forall$ or $\exists$.
   This holds by [[structural induction|12MQ2NJ29A]] on terms, since variables and constant symbols are single symbols, and the clause for $f(t_1, \dots, t_n)$ adds only $f$, brackets and commas.
2. So $\varphi$ contains no $\forall$ and no $\exists$.
   The reason is that $\varphi$ consists of its terms together with $=$ or $R$, brackets and commas.
3. A subformula of the form $\forall x \, \psi$ or $\exists x \, \psi$ would contain $\forall$ or $\exists$.
   By step 2, $\varphi$ has no such subformula, so no position in $\varphi$ lies in the scope of a quantifier.
4. An occurrence is bound only when it lies in the scope of a quantifier on the same variable.
   By step 3, no occurrence in $\varphi$ is bound, so every occurrence is free.
   This is part 1.
5. By the base clause of the definition, $\operatorname{FV}(\varphi) = \operatorname{Var}(t_1) \cup \dots \cup \operatorname{Var}(t_n)$, with $n = 2$ for an equation, and $\operatorname{BV}(\varphi) = \emptyset$.
6. For each term $t$, the set $\operatorname{Var}(t)$ is the set of variables that occur in $t$.
   This holds by structural induction on $t$.
   The clause $\operatorname{Var}(x) = \{ x \}$ covers a variable, the clause $\operatorname{Var}(c) = \emptyset$ covers a constant symbol, and the union clause covers $f(t_1, \dots, t_n)$, whose variables are those of the $t_i$.
7. The variables that occur in $\varphi$ are those that occur in some $t_i$, because $=$, $R$, brackets and commas are not variables.
   With steps 5 and 6 this gives part 2.
8. By definition, $\varphi$ is a [[sentence|DKFGQTRYZE]] when $\operatorname{FV}(\varphi) = \emptyset$.
   By part 2 this means $\operatorname{Var}(t_i) = \emptyset$ for every $i$, that is, every $t_i$ is closed.
   This is part 3.

This proves all three parts.

## Idea

Only quantifiers bind variables, and an atomic formula has no quantifiers.
So every variable in it is free.
The rest is the computation of $\operatorname{FV}$ by its base clause.
For example, in $S(x) < y$ there is no $\forall$ or $\exists$, so the free variables are exactly $x$ and $y$.

## Variants

If $\operatorname{FV}$ is defined only by recursion on formulas, part 2 is its base clause, and parts 1 and 3 follow at once.
With Enderton's definition, "$x$ occurs free in an atomic $\alpha$" means that $x$ occurs in $\alpha$, so part 1 holds by definition.
