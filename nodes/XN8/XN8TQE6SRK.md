---
tag: XN8TQE6SRK
kind: definition
name: Substitution
msc: ["03B10", "08B05"]
topics: [PSRDJXRW53]
audience: ug2
defines: NCDZ969V7X
uses: [6D3WA7N2W4, WDVVEYD6AT, HYJ10AF6RT, Y3FZTH5158]
sources:
  - url: https://en.wikipedia.org/wiki/Substitution_(logic)
    locator: lead section
  - url: https://en.wikipedia.org/wiki/First-order_logic
    locator: Free and bound variables
  - book: isbn:9780122384523
    locator: Section 2.4
---

## Definition

Let $T$ be the set of [[terms|6D3WA7N2W4]] over a [[signature|WDVVEYD6AT]] $\sigma$, with variables from $\mathrm{Var}$.

*Substitution in terms.*
A *substitution* is a map $\theta \colon \mathrm{Var} \to T$.
Its *application* to a term $t$, written $t\theta$, is defined by recursion on $t$:

1. $x\theta = \theta(x)$ for each variable $x$;
2. $c\theta = c$ for each constant symbol $c$;
3. $f(t_1, \ldots, t_n)\theta = f(t_1\theta, \ldots, t_n\theta)$ for each function symbol $f$ of arity $n \ge 1$.

*Substitution in formulas.*
For a substitution $\theta$ and a variable $y$, let $\theta_y$ be the substitution with $\theta_y(y) = y$ and $\theta_y(z) = \theta(z)$ for $z \neq y$.
The application $\varphi\theta$ to a [[formula|HYJ10AF6RT]] $\varphi$ is defined by recursion on $\varphi$:

4. $(t_1 = t_2)\theta$ is $t_1\theta = t_2\theta$, and $R(t_1, \ldots, t_n)\theta$ is $R(t_1\theta, \ldots, t_n\theta)$;
5. $(\neg \varphi)\theta = \neg (\varphi\theta)$, and $(\varphi \ast \psi)\theta = (\varphi\theta \ast \psi\theta)$ for each binary connective $\ast$;
6. $(\forall y \, \varphi)\theta = \forall y \, (\varphi\theta_y)$ and $(\exists y \, \varphi)\theta = \exists y \, (\varphi\theta_y)$.

*Substitutability.*
A term $t$ is *substitutable* (or *free*) for $x$ in $\varphi$ when the following recursion says so:

7. $t$ is substitutable for $x$ in every atomic formula;
8. $t$ is substitutable for $x$ in $\neg \varphi$ when it is substitutable in $\varphi$, and in $(\varphi \ast \psi)$ when it is substitutable in $\varphi$ and in $\psi$;
9. $t$ is substitutable for $x$ in $\forall y \, \varphi$ and in $\exists y \, \varphi$ when $x \notin \operatorname{FV}(\forall y \, \varphi)$, or when $y \notin \operatorname{Var}(t)$ and $t$ is substitutable for $x$ in $\varphi$.

A substitution $\varphi[t_1/x_1, \ldots, t_n/x_n]$ is *admissible* when each $t_i$ is substitutable for $x_i$ in $\varphi$.

## Notation

1. For distinct variables $x_1, \ldots, x_n$, the substitution $\set{x_1 \mapsto s_1, \ldots, x_n \mapsto s_n}$ sends $x_i$ to $s_i$ and every other variable to itself. Its application to $t$ or $\varphi$ is written $t[s_1/x_1, \ldots, s_n/x_n]$ or $\varphi[s_1/x_1, \ldots, s_n/x_n]$, and $t[s/x]$ or $\varphi[s/x]$ when $n = 1$.
2. Enderton writes $\varphi^x_t$ for $\varphi[t/x]$. Other books write $\varphi(t/x)$, $\varphi[x := t]$ or $\varphi\set{x \mapsto t}$.
3. When $\varphi$ is written $\varphi(x)$, many books write $\varphi(t)$ for $\varphi[t/x]$, with the tacit assumption that $t$ is substitutable for $x$.
4. In universal algebra and in unification, $\theta$ is usually the identity on all but finitely many variables, and the notation $t\theta$ is standard.
5. Some books define $\varphi[t/x]$ with automatic renaming of bound variables, so that it is always admissible. Then $\varphi[t/x]$ is defined only up to [[alpha-equivalence|Y3FZTH5158]].

## Remarks

By clauses 4 to 6, $\varphi\theta$ replaces each free occurrence of each variable $z$ by $\theta(z)$, and leaves the bound occurrences alone.
When $t$ is not substitutable for $x$ in $\varphi$, the formula $\varphi[t/x]$ *captures* a variable of $t$.
This means that some free occurrence of $x$ lies in the scope of a quantifier on a variable of $t$.

Example: with $\theta = \set{x \mapsto z \cdot z, \ y \mapsto 1}$, clauses 3 and 1 give $(x + y)\theta = (z \cdot z) + 1$.

Example: $(\forall x \, P(x) \land Q(x))[c/x] = (\forall x \, P(x) \land Q(c))$ for a constant symbol $c$.
By clause 6 with $\theta_x = \mathrm{id}$, the bound $x$ stays, and by clause 4 the free $x$ in $Q(x)$ becomes $c$.

Non-example: replacing only the first occurrence of $x$ in $x + x$ by $y$ is not a substitution.
By clauses 1 and 3, every substitution sends $x + x$ to $\theta(x) + \theta(x)$, which never equals $y + x$.

Non-example: $y$ is not substitutable for $x$ in $\forall y \, (x < y)$.
Clause 9 fails, because $x$ is free in $\forall y \, (x < y)$ and $y \in \operatorname{Var}(y)$.
The string $(\forall y \, (x < y))[y/x] = \forall y \, (y < y)$ shows the [[capture|WW01WZR9MF]].

A term $s$ is an *instance* of $t$ if $s = t\theta$ for some substitution $\theta$.
The substitutions are exactly the endomorphisms of the term algebra, restricted to the variables, and $(t\theta)\eta = t(\theta\eta)$, where $(\theta\eta)(x) = (\theta(x))\eta$.
For an identity $s \approx t$, the identity $s\theta \approx t\theta$ holds in every algebra in which $s \approx t$ holds.
A term without variables is substitutable for every variable in every formula, by clauses 7 to 9.

## Explanations

### L1 human

To substitute $5$ for $x$ in "$x$ is even" means to write "$5$ is even".
We replace every $x$ that stands for a value given from outside.
We do not touch an $x$ that belongs to a "for all $x$" or a "there is an $x$".
The substitution is legal only when the new term does not get caught by a quantifier.
For example, putting $y$ for $x$ in "every $y$ is larger than $x$" would give "every $y$ is larger than $y$", which is a different claim.

### L2 human

We compute $\varphi[S(z)/x]$ for $\varphi = \exists y \, (x = y + y) \land \forall x \, (x = x)$.

1. In the left conjunct, $x$ is free. The term $S(z)$ does not contain $y$, so it is substitutable, by clauses 9 and 7.
2. By clauses 6 and 4, the left conjunct becomes $\exists y \, (S(z) = y + y)$.
3. In the right conjunct, $x$ is not free, so by clause 6 with $\theta_x = \mathrm{id}$ it stays $\forall x \, (x = x)$.
4. So $\varphi[S(z)/x] = \exists y \, (S(z) = y + y) \land \forall x \, (x = x)$.

The typical use is the quantifier rule: from $\forall x \, \varphi$ infer $\varphi[t/x]$ when $t$ is substitutable for $x$ in $\varphi$.
The trap is the term $S(y)$ in place of $S(z)$: step 1 then fails, and the bound $y$ must be renamed first.
