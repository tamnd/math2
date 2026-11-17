---
tag: NCDZ969V7X
kind: concept
name: Substitution
msc: ["03B10", "08B05"]
topics: [PSRDJXRW53]
audience: ug2
uses: [6D3WA7N2W4, HYJ10AF6RT, ~2fd0cd75, 0GHS47PDAQ]
sources:
  - url: https://en.wikipedia.org/wiki/Substitution_(logic)
    locator: lead section
  - url: https://en.wikipedia.org/wiki/First-order_logic
    locator: Free and bound variables
  - book: isbn:9780122384523
    locator: Section 2.4
  - url: https://builds.openlogicproject.org/
    locator: "Chapter: Syntax and Semantics"
same_as:
  wikidata: Q1522579
  wikipedia: Substitution (logic)
---

## Summary

Let $x$ be a variable and let $t$ be a [[term|6D3WA7N2W4]].
In a term $u$, the substitution $u[t/x]$ replaces every occurrence of $x$ by $t$.
In a [[formula|HYJ10AF6RT]] $\varphi$, the substitution $\varphi[t/x]$ replaces every [[free occurrence|~2fd0cd75]] of $x$ by $t$ and leaves bound occurrences alone.
The substitution is *admissible* when $t$ is *substitutable* for $x$ in $\varphi$: no variable of $t$ falls into the scope of a quantifier on that variable.
A *simultaneous* substitution $\theta$ replaces several variables at once, each $x$ by $\theta(x)$.
The [[formal definition|XN8TQE6SRK]] gives all these operations by recursion.
Substitution is the syntactic form of "plug in a value": it drives the quantifier rules of proof systems, the laws of equational logic, unification and term rewriting.

## Motivation

From "every natural number $x$ satisfies $x + 0 = x$" we want to infer "$S(0) + 0 = S(0)$".
The inference replaces $x$ by the term $S(0)$, and the rule behind it is: from $\forall x \, \varphi$ infer $\varphi[t/x]$.
The rule is sound only with two restrictions.
First, bound occurrences must stay: in $P(x) \land \forall x \, Q(x)$ only the first $x$ is a value given from outside.
Second, no variable of $t$ may be captured.
The formula $\forall x \, \exists y \, (x < y)$ is true in $(\mathbb{N}, <)$, but putting $y$ for $x$ in $\exists y \, (x < y)$ gives the false sentence $\exists y \, (y < y)$.
The definition of substitutability states exactly when the rule is safe.

## Notation

1. $t[s/x]$ and $\varphi[t/x]$: the result of replacing $x$ by $s$ or $t$. Enderton writes $\varphi^x_t$. Other notations are $\varphi(t/x)$, $\varphi[x := t]$ and $\varphi\set{x \mapsto t}$.
2. $\varphi[t_1/x_1, \ldots, t_n/x_n]$, for distinct variables $x_i$: simultaneous substitution.
3. $\theta = \set{x_1 \mapsto t_1, \ldots, x_n \mapsto t_n}$ and $t\theta$: a substitution as a map, the usual notation of universal algebra, unification and logic programming.
4. When a formula is written $\varphi(x)$, the notation $\varphi(t)$ means $\varphi[t/x]$, with the tacit assumption that $t$ is substitutable for $x$.

## Remarks

### Examples

1. With $\theta = \set{x \mapsto z \cdot z, \ y \mapsto 1}$ we get $(x + y)\theta = z \cdot z + 1$. Both variables are replaced at once.
2. The swap $\set{x \mapsto y, \ y \mapsto x}$ sends $x + y$ to $y + x$, but two [[successive substitutions|~2501efda]] give $x + x$ or $y + y$.
3. $(P(x) \land \forall x \, Q(x))[c/x] = P(c) \land \forall x \, Q(x)$. Only the free occurrence changes.
4. In $\exists y \, (y + y = x)$, the term $S(0)$ is substitutable for $x$, and the term $S(y)$ is not. A [[renaming|~e2f74c7f]] of the bound $y$ makes the second substitution admissible.
5. The rule "from $\forall x \, \varphi$ infer $\varphi[t/x]$" turns the axiom $\forall x \, (x + 0 = x)$ into $S(0) + 0 = S(0)$.

### Non-examples

1. Putting $y$ for $x$ in $\forall y \, (x < y)$ gives $\forall y \, (y < y)$. The term $y$ is [[captured|~6f9c2060]], so the substitution is not admissible.
2. Replacing only the first $x$ in $x + x$ by $y$ is not a substitution. Every substitution sends $x + x$ to $\theta(x) + \theta(x)$.
3. Replacing the bound $x$ in $\forall x \, P(x)$ by a constant $c$ does not give $\forall c \, P(c)$, which is [[not a formula|~ab247241]]. Substitution leaves $\forall x \, P(x)$ unchanged.

### Basic properties

1. If $x \notin \operatorname{FV}(\varphi)$, then $\varphi[t/x] = \varphi$. The same holds for terms: if $x \notin \operatorname{Var}(u)$, then $u[t/x] = u$.
2. If $t$ is substitutable for $x$ in $\varphi$ and $x \in \operatorname{FV}(\varphi)$, then $\operatorname{FV}(\varphi[t/x]) = (\operatorname{FV}(\varphi) \setminus \set{x}) \cup \operatorname{Var}(t)$.
3. Substitution in terms is compositional: $(t\theta)\eta = t(\theta\eta)$, where $(\theta\eta)(x) = \theta(x)\eta$. The substitutions are the endomorphisms of the [[term algebra|3YYKGWJJND]].
4. Successive substitutions commute in a controlled way: if $x \neq y$ and $x \notin \operatorname{Var}(r)$, then $t[s/x][r/y] = t[r/y][s[r/y]/x]$. This is the [[syntactic substitution lemma|~f943c858]].
5. A term without variables is substitutable for every variable in every formula. For any $t$, $x$ and $\varphi$, renaming the bound variables of $\varphi$ gives an alpha-equivalent formula in which $t$ is substitutable for $x$.
6. If $t$ is substitutable for $x$ in $\varphi$, then the formula $\varphi[t/x]$ says about the value of $t$ what $\varphi$ says about the value of $x$. This is the semantic substitution lemma of [[structures and satisfaction|NJDME6F845]], and it makes $\forall x \, \varphi \to \varphi[t/x]$ valid.

### History

Church's lambda calculus of the 1930s had a rule for renaming bound variables, later called alpha conversion, and its substitution needed such renaming.
In 1965 John Alan Robinson introduced resolution and the unification algorithm, which computes most general substitutions.
In 1972 de Bruijn introduced nameless bound variables, the [[de Bruijn indices|1TC37YHZPE]], so that substitution in his proof checker Automath could not capture variables.

### Common errors

1. Students replace bound occurrences too. $(\forall x \, P(x))[c/x]$ is $\forall x \, P(x)$, not $\forall c \, P(c)$.
2. Students substitute without checking that the term is substitutable, as in the capture of $y$ in $\forall y \, (x < y)$.
3. Students carry out a simultaneous substitution as a sequence of single substitutions. The swap of $x$ and $y$ shows that the results differ.

## Explanations

### L1 human

Substitution is "plugging in".
If "$x$ is even" is the claim, then putting $6$ for $x$ gives "$6$ is even", which is true.
We plug in only where $x$ is an open slot, not where $x$ belongs to a "for all $x$".
We also must not plug in a letter that a "for all" then grabs by mistake.
Putting $y$ in for $x$ in "every $y$ is bigger than $x$" gives "every $y$ is bigger than $y$", which is a different claim.

### L2 human

We compute $\varphi[S(y)/x]$ for $\varphi = \exists y \, (y + y = x)$, which says that $x$ is even.

1. The term $S(y)$ contains $y$, and $x$ is free in the scope of $\exists y$. By the substitutability clause for quantifiers, $S(y)$ is not substitutable for $x$.
2. The blind replacement gives $\exists y \, (y + y = S(y))$. In $\mathbb{N}$ it is a true sentence, because $y = 1$ gives $1 + 1 = 2$.
3. We rename the bound variable: $\varphi$ is alpha-equivalent to $\exists z \, (z + z = x)$, and $S(y)$ is substitutable for $x$ in this formula.
4. The result is $\exists z \, (z + z = S(y))$. It says that $y + 1$ is even, and it is true for $y = 1$ and false for $y = 2$.

The typical use is a step of a formal proof: instantiate $\forall x \, \varphi$ with a term, after renaming the bound variables of $\varphi$ when necessary.
The trap is step 2: the blind replacement is a well-formed formula, so no syntax check catches the error, and only the substitutability condition does.

### L3 human

The terms over a signature form a monad on sets: a set $X$ of variables goes to the set $T(X)$ of terms over $X$.
A substitution $X \to T(Y)$ is an arrow of the Kleisli category of this monad, and composition of substitutions is Kleisli composition.
In a Lawvere theory the same composition is the composition of the category, and the [[syntactic substitution lemma|~f943c858]] follows from associativity and a computation of two composite substitutions.
For formulas the binders break this simple picture, because substitution must respect alpha-equivalence.
Several solutions exist: renaming as part of substitution, [[de Bruijn indices|1TC37YHZPE]], numbered bound variables in a separate type as in Mathlib, and nominal sets.
The [[lambda calculus|BD756KR8FM]] has the same issue, and its beta reduction is a substitution.
In [[unification|RJJ9D0WF53]], substitutions are the solutions of equations between terms, and the most general unifier is the most general substitution that solves them.
In categorical logic, substitution is pullback along a map of contexts, and the quantifiers are adjoints to substitution.
