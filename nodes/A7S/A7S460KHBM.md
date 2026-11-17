---
tag: A7S460KHBM
kind: statement
role: lemma
name: Substitution lemma (semantic)
aliases: [semantic-substitution-lemma]
msc: ["03B10"]
topics: [NJDME6F845]
audience: ug2
about: [2RBQPV02AS, NCDZ969V7X]
uses: [1WTCZB4DVB, FM580NZ9W6, NCDZ969V7X, 6D3WA7N2W4, HYJ10AF6RT]
sources:
  - book: isbn:9780122384523
    locator: Chapter 2
  - book: isbn:9781447145578
    locator: Chapter 3
  - url: https://builds.openlogicproject.org/
    locator: Syntax and Semantics
---

## Statement

Let $\mathcal{M}$ be an $L$-structure, let $s$ be an assignment in $\mathcal{M}$, let $x$ be a variable and let $t$ be an $L$-[[term|6D3WA7N2W4]].
Write $a = t^{\mathcal{M}}[s]$ for the value of $t$ under $s$.

1. For every $L$-term $u$, $\bigl(u[t/x]\bigr)^{\mathcal{M}}[s] = u^{\mathcal{M}}[s[x \mapsto a]]$.
2. For every $L$-[[formula|HYJ10AF6RT]] $\varphi$ such that $t$ is substitutable for $x$ in $\varphi$,
$$\mathcal{M} \models \varphi[t/x]\,[s] \quad \text{if and only if} \quad \mathcal{M} \models \varphi\,[s[x \mapsto a]].$$

Here $\varphi[t/x]$ is the result of the [[substitution|NCDZ969V7X]] of $t$ for the free occurrences of $x$ in $\varphi$.
The term $t$ is substitutable for $x$ in $\varphi$ when no free occurrence of $x$ in $\varphi$ lies inside a quantifier $\forall y$ or $\exists y$ for a variable $y$ of $t$.
The symbol $\models$ is [[satisfaction|1WTCZB4DVB]].

## Remarks

### Why each hypothesis is needed

The substitutability of $t$ is needed.
Let $\varphi = \exists y \, \neg (x = y)$ and $t = y$, and let $\mathcal{M}$ have domain $\set{0, 1}$.
Here $t$ is not substitutable for $x$, because the free $x$ lies inside $\exists y$.
Blind replacement gives $\exists y \, \neg (y = y)$, which no assignment satisfies.
But $\varphi$ under $s[x \mapsto s(y)]$ is satisfied, with the witness $y \mapsto 1 - s(y)$.
So the two sides of the lemma differ.

### Consequences

1. The formula $\forall x \, \varphi \to \varphi[t/x]$ is [[valid|5SDS9T8E7J]] when $t$ is substitutable for $x$ in $\varphi$: if every variant satisfies $\varphi$, then so does $s[x \mapsto a]$.
2. In the same way, $\varphi[t/x] \to \exists x \, \varphi$ is valid, with the witness $a$.
3. These two facts give the [[soundness|4A84VHDTHV]] of the quantifier rules: $\forall$-elimination and $\exists$-introduction in natural deduction, and the quantifier axioms of Hilbert systems.
4. The equality axioms $t_1 = t_2 \to (\varphi[t_1/x] \to \varphi[t_2/x])$ are valid when $t_1$ and $t_2$ are substitutable for $x$ in $\varphi$, because both sides reduce to $\varphi$ under the same variant.

### Converse

The lemma is an equivalence for each $\varphi$, so the question is whether the hypothesis is necessary.
It is not: for $\varphi = \forall y \, (x = x)$ and $t = y$, the term is not substitutable, yet both sides are always satisfied.

### Generalizations

The lemma holds for the simultaneous substitution $\varphi[t_1/x_1, \ldots, t_n/x_n]$, with the variant $s[x_1 \mapsto a_1, \ldots, x_n \mapsto a_n]$.
If substitution renames bound variables to avoid capture, then the lemma holds for every term $t$, without a hypothesis.

## History

The lemma belongs to the standard development of Tarski's semantics.
Enderton's textbook, first published in 1972, proves it and uses it in the proof of the soundness theorem.

## Explanations

### L1 human

Putting the expression $t$ in place of $x$ has the same effect as giving $x$ the value of $t$.
For example, "$x + 1 > 3$ with $x$ replaced by $2 \cdot y$" means the same as "$x + 1 > 3$ where $x$ is the number $2 \cdot y$".
The one danger is that a quantifier in the formula might capture a letter of $t$; the lemma excludes that case.

### L2 human

We check part 2 in $(\N, +, <, 0, 1)$ with $\varphi = \exists z \, (x + z = y)$, $t = w + 1$ and $s(w) = 2$, $s(y) = 5$.

1. The value of $t$ is $a = 2 + 1 = 3$.
2. The term $t$ is substitutable, because $z$ does not occur in $t$. So $\varphi[t/x] = \exists z \, ((w + 1) + z = y)$.
3. Left side: $s$ satisfies $\varphi[t/x]$ if some $c$ gives $(2 + 1) + c = 5$; the witness is $c = 2$.
4. Right side: $s[x \mapsto 3]$ satisfies $\varphi$ if some $c$ gives $3 + c = 5$; the witness is $c = 2$.
5. Both sides hold, as the lemma predicts.

The typical use is to show that a quantifier rule of a proof system is sound.
A trap is to forget the hypothesis: with $t = z + 1$, the substitution would read $\exists z \, ((z + 1) + z = y)$, which says that $y$ is odd.

### L3 human

The lemma says that syntactic substitution is the syntactic counterpart of the semantic operation of updating an assignment.
In categorical logic, it becomes the statement that the interpretation of formulas commutes with pullback along the interpretation of terms.
In Mathlib, bound variables are de Bruijn indices, so variable capture cannot occur.
