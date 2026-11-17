---
tag: ~fb02fdf0
kind: proof
name: Proof that variable occurrences in atomic formulas are free
msc: ["03B10"]
topics: [PSRDJXRW53]
audience: ug2
proves: D039R5C8TC
uses: [~de213704, ~2fd0cd75, ~e71c5bb3, 6D3WA7N2W4, ~62799b98, DKFGQTRYZE]
methods: [12MQ2NJ29A, 0NTF6DMVAP]
sources:
  - book: isbn:9780122384523
    locator: Section 2.1
  - url: https://en.wikipedia.org/wiki/Atomic_formula
    locator: Atomic formula in first-order logic
---

## Proof

Let $\varphi$ be $t_1 = t_2$ or $R(t_1, \dots, t_n)$, as in the [[statement|D039R5C8TC]].
We use the [[definition of free and bound variables|~e71c5bb3]].

1. No term contains the symbol $\forall$ or $\exists$. Reason: by [[structural induction|12MQ2NJ29A]] on terms, since variables and constant symbols are single symbols, and $f(t_1, \dots, t_n)$ adds only $f$, brackets and commas.
2. So $\varphi$ contains no $\forall$ and no $\exists$. Reason: $\varphi$ consists of its terms, together with $=$, or $R$, brackets and commas.
3. A subformula of the form $\forall x \, \psi$ or $\exists x \, \psi$ would contain $\forall$ or $\exists$. By step 2, $\varphi$ has no such subformula, so no position in $\varphi$ lies in the scope of a quantifier.
4. An occurrence is bound only when it lies in the scope of a quantifier on the same variable. By step 3, no occurrence in $\varphi$ is bound, so every occurrence is free. This is part 1.
5. By the definition, $\operatorname{FV}(\varphi) = \operatorname{Var}(t_1) \cup \dots \cup \operatorname{Var}(t_n)$, with $n = 2$ in the case of an equation, and $\operatorname{BV}(\varphi) = \emptyset$.
6. For each term $t$, $\operatorname{Var}(t)$ is the set of variables that occur in $t$. Reason: by structural induction on $t$. The clause $\operatorname{Var}(x) = \set{x}$ covers a variable, $\operatorname{Var}(c) = \emptyset$ covers a constant symbol, and the union clause covers $f(t_1, \dots, t_n)$, whose variables are those of the $t_i$.
7. The variables that occur in $\varphi$ are those that occur in some $t_i$, because $=$, $R$, brackets and commas are not variables. With step 6 this gives part 2.
8. By definition, $\varphi$ is a [[sentence|DKFGQTRYZE]] when $\operatorname{FV}(\varphi) = \emptyset$. By part 2 this means $\operatorname{Var}(t_i) = \emptyset$ for every $i$, that is, every $t_i$ is closed. This is part 3.

## Idea

Only quantifiers bind variables, and an atomic formula has no quantifiers.
So every variable in it is free.
The rest is the computation of $\operatorname{FV}$ by its base clause.

## Variants

With the recursive definition of $\operatorname{FV}$ alone, part 2 is the base clause, and parts 1 and 3 follow at once.
With Enderton's definition, "$x$ occurs free in an atomic $\varphi$" means "$x$ occurs in $\varphi$", so part 1 holds by definition.
