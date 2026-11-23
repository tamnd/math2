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

The semantic substitution lemma says that writing a term $t$ in place of $x$ has the same effect as giving $x$ the value of $t$, provided that no quantifier captures a variable of $t$.

Let $\mathcal{M}$ be an $L$-structure, let $s$ be an assignment in $\mathcal{M}$, let $x$ be a variable and let $t$ be an $L$-[[term|6D3WA7N2W4]].
Write $a = t^{\mathcal{M}}[s]$ for the value of $t$ under $s$.

1. For every $L$-term $u$, we have $\bigl(u[t/x]\bigr)^{\mathcal{M}}[s] = u^{\mathcal{M}}[s[x \mapsto a]]$.
2. For every $L$-[[formula|HYJ10AF6RT]] $\varphi$ such that $t$ is substitutable for $x$ in $\varphi$,
$$\mathcal{M} \models \varphi[t/x]\,[s] \quad \text{if and only if} \quad \mathcal{M} \models \varphi\,[s[x \mapsto a]].$$

Here $\varphi[t/x]$ is the result of the [[substitution|NCDZ969V7X]] of $t$ for the free occurrences of $x$ in $\varphi$.
The term $t$ is substitutable for $x$ in $\varphi$ when no free occurrence of $x$ in $\varphi$ lies inside a quantifier $\forall y$ or $\exists y$ for a variable $y$ of $t$.
The symbol $\models$ is [[satisfaction|1WTCZB4DVB]].

## Remarks

### A first check

Work in $(\mathbb{N}, +, <, 0, 1)$ with $\varphi = \exists z \, (x + z = y)$, which says that $x$ is at most $y$.
Take the term $t = w + 1$ and an assignment $s$ with $s(w) = 2$ and $s(y) = 5$.
The value of the term is
$$a = t^{\mathcal{M}}[s] = 2 + 1 = 3.$$
The variable $z$ does not occur in $t$, so $t$ is substitutable, and $\varphi[t/x] = \exists z \, ((w + 1) + z = y)$.

On the left side, $s$ satisfies $\varphi[t/x]$ when some $c$ gives $(2 + 1) + c = 5$, and $c = 2$ works.
On the right side, $s[x \mapsto 3]$ satisfies $\varphi$ when some $c$ gives $3 + c = 5$, and again $c = 2$ works.
Both sides hold, as the lemma predicts.
Check: with $s(y) = 2$ instead, both sides fail, since no natural number $c$ gives $3 + c = 2$.

### Why the hypothesis is needed

Substitutability cannot be dropped.
Let $\varphi = \exists y \, \neg (x = y)$, let $t = y$, and let $\mathcal{M}$ have domain $\{0, 1\}$.
The free $x$ lies inside $\exists y$, and $y$ occurs in $t$, so $t$ is not substitutable for $x$.
Blind replacement gives $\exists y \, \neg (y = y)$, which no assignment satisfies.
But $\varphi$ under $s[x \mapsto s(y)]$ is satisfied, with the witness $1 - s(y)$ for $y$.
So the two sides of the lemma differ.

### What it gives you

The lemma is the semantic fact behind the quantifier rules of every proof system.
If $t$ is substitutable for $x$ in $\varphi$, then $\forall x \, \varphi \to \varphi[t/x]$ is [[valid|5SDS9T8E7J]].
The reason is that if every variant $s[x \mapsto b]$ satisfies $\varphi$, then so does $s[x \mapsto a]$, and the lemma turns this into "$s$ satisfies $\varphi[t/x]$".
In the same way $\varphi[t/x] \to \exists x \, \varphi$ is valid, with the value $a$ as the witness.

These two facts give the [[soundness|4A84VHDTHV]] of $\forall$-elimination and $\exists$-introduction in natural deduction, and of the quantifier axioms of Hilbert systems.
The equality axioms $t_1 = t_2 \to (\varphi[t_1/x] \to \varphi[t_2/x])$ are valid for the same reason, when $t_1$ and $t_2$ are substitutable for $x$ in $\varphi$.
If $t_1$ and $t_2$ have the same value $a$, both substituted formulas reduce to $\varphi$ under $s[x \mapsto a]$.

### The converse

The lemma is already an equivalence for each $\varphi$, so the real question is whether the hypothesis is necessary.
It is not necessary for every formula.
For $\varphi = \forall y \, (x = x)$ and $t = y$, the term is not substitutable, yet both sides are satisfied by every assignment.

### Generalizations

The lemma holds for the simultaneous substitution $\varphi[t_1/x_1, \ldots, t_n/x_n]$, with the variant $s[x_1 \mapsto a_1, \ldots, x_n \mapsto a_n]$.
If substitution renames bound variables to avoid capture, then the lemma holds for every term $t$, with no hypothesis.

### Watch out

The trap is variable capture, and it hides well.
In $\varphi = \exists z \, (x + z = y)$ over $\mathbb{N}$, substitute $t = z + 1$ for $x$ without care.
You get $\exists z \, ((z + 1) + z = y)$, which says that $y$ is odd.
The right side of the lemma says something else: there is $c$ with $(s(z) + 1) + c = s(y)$, that is, $s(z) + 1 \le s(y)$.
With $s(z) = 0$ and $s(y) = 4$, the right side holds and the left side fails, since $4$ is even.
The correct move is to rename the bound $z$ first, for example to $\exists v \, ((z + 1) + v = y)$.

### Try it

In $(\mathbb{Z}, +, 0)$, let $\varphi = x + x = 0$ and $t = y + y$, with $s(y) = 0$.
Do both sides hold?
Yes: $t$ has value $0$, the right side asks whether $0 + 0 = 0$, and the left side asks whether $(0 + 0) + (0 + 0) = 0$.

Is $y$ substitutable for $x$ in $\forall y \, (y < x) \vee x = y$?
No, because the first free occurrence of $x$ sits inside $\forall y$; the occurrence in $x = y$ is fine, but one bad occurrence is enough.

## History

The lemma belongs to the standard development of Tarski's semantics.
Enderton's textbook, first published in 1972, proves it and uses it in the proof of the soundness theorem.

## Explanations

### L1 human

Suppose a rule says "$x + 1 > 3$" and you are told that $x$ is "twice $y$".
You can either write $2 \cdot y + 1 > 3$, or first work out the number $2 \cdot y$ and then put that number in for $x$.
Both ways give the same answer, which is what the lemma says.
The one danger is a letter in the inserted expression that is already used inside the rule for something else.
Then the inserted letter gets confused with the old one, and the meaning changes.

### L2 human

Here is a typical use: we check that $\forall x \, \varphi \to \varphi[t/x]$ cannot fail.
Take $\mathcal{M} = (\mathbb{N}, +)$, $\varphi = \exists z \, (x + z = x)$ and $t = w + w$, with $s(w) = 4$.
First, $\forall x \, \varphi$ is true, since $z = 0$ works for every $x$.
The value of $t$ is $a = 8$, and the right side of the lemma asks for $c$ with
$$8 + c = 8,$$
which $c = 0$ gives.
So the lemma says that $s$ satisfies $\varphi[t/x] = \exists z \, ((w + w) + z = w + w)$, and a direct check with $c = 0$ agrees.
A proof of [[soundness|4A84VHDTHV]] makes this argument once for all $\varphi$ and $t$, instead of for one example.

### L3 human

The lemma says that syntactic substitution is the counterpart of the semantic operation of updating an assignment.
In categorical logic, it becomes the statement that the interpretation of formulas commutes with pullback along the interpretation of terms.
In Mathlib, bound variables are de Bruijn indices, so variable capture cannot occur, and the lemma becomes a statement about composing the map that interprets the variables.
The proof uses the [[coincidence lemma|FM580NZ9W6]] in the quantifier step, and the [[soundness theorem|4A84VHDTHV]] for first-order logic uses this lemma for its quantifier rules.
