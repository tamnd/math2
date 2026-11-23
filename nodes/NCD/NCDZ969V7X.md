---
tag: NCDZ969V7X
kind: concept
name: Substitution
msc: ["03B10", "08B05"]
topics: [PSRDJXRW53]
audience: ug2
uses: [6D3WA7N2W4, HYJ10AF6RT, 9CNGDRAMGC, 0GHS47PDAQ]
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

Substitution is "plug in a term for a variable", done on strings.
It looks harmless, but it has one trap.
The formula $\forall y \, (x < y)$ says that $x$ is below every element.
If we write $y$ in place of $x$, we get $\forall y \, (y < y)$, which says that every element is below itself; the $y$ we put in has been *captured* by $\forall y$.
If we first rename the bound variable, $\forall z \, (x < z)$, and then put $y$ for $x$, we get $\forall z \, (y < z)$, which says correctly that $y$ is below every element.

Let $x$ be a variable and $t$ a [[term|6D3WA7N2W4]].
In a term $u$, the term $u[t/x]$ replaces every occurrence of $x$ by $t$.
In a [[formula|HYJ10AF6RT]] $\varphi$, the formula $\varphi[t/x]$ replaces every [[free occurrence|9CNGDRAMGC]] of $x$ by $t$ and leaves the bound occurrences alone.
The term $t$ is *free for* $x$ in $\varphi$, or *substitutable* for $x$ in $\varphi$, when no free occurrence of $x$ in $\varphi$ lies within the scope of a quantifier $\forall y$ or $\exists y$ with $y$ a variable of $t$.
The substitution $\varphi[t/x]$ is *admissible* when $t$ is free for $x$ in $\varphi$, and the [[formal definition|XN8TQE6SRK]] gives all of this by recursion.

## Motivation

From "every natural number $x$ satisfies $x + 0 = x$" we want to infer "$S(0) + 0 = S(0)$".
The step replaces $x$ by the term $S(0)$, and the rule behind it is: from $\forall x \, \varphi$ infer $\varphi[t/x]$.
This rule appears in every proof system for first-order logic, and it is sound only with two restrictions.
Bound occurrences must stay, since in $P(x) \land \forall x \, Q(x)$ only the first $x$ is an input.
And no variable of $t$ may be captured: $\forall x \, \exists y \, (x < y)$ is true in $(\mathbb{N}, <)$, but blind replacement of $x$ by $y$ in $\exists y \, (x < y)$ gives the false sentence $\exists y \, (y < y)$.

Substitution also drives the equational logic of algebra, unification in logic programming, term rewriting and beta reduction in the [[lambda calculus|BD756KR8FM]].

## Notation

We write $\varphi[t/x]$, read "$\varphi$ with $t$ for $x$".
Enderton writes $\varphi^x_t$, and other books write $\varphi(t/x)$, $\varphi[x := t]$ or $\varphi\{ x \mapsto t \}$.
For distinct variables $x_1, \ldots, x_n$, the simultaneous substitution $\varphi[t_1/x_1, \ldots, t_n/x_n]$ replaces all of them at once.
In algebra and unification a substitution is a map $\theta$ from variables to terms, written $\{ x_1 \mapsto t_1, \ldots \}$, and its result on $t$ is written $t\theta$.
When a formula is written $\varphi(x)$, the notation $\varphi(t)$ means $\varphi[t/x]$, with the tacit assumption that $t$ is free for $x$.

## Remarks

### A first computation

Let $\varphi = \exists y \, (y + y = x)$, which says in $\mathbb{N}$ that $x$ is even.
The term $S(0)$ has no variables, so it is free for $x$, and
$$\varphi[S(0)/x] = \exists y \, (y + y = S(0)),$$
which says that $1$ is even, and is false, as it should be.
The term $S(y)$ is not free for $x$, because the free $x$ lies in the scope of $\exists y$ and $y$ occurs in $S(y)$.
A [[renaming of the bound variable|XX4DS8DGN3]] gives $\exists z \, (z + z = x)$, and then
$$\exists z \, (z + z = x)[S(y)/x] = \exists z \, (z + z = S(y)),$$
which says that $y + 1$ is even.
Check: for $y = 1$ the witness $z = 1$ gives $1 + 1 = 2$, and for $y = 2$ no $z$ gives $z + z = 3$.

### Bound occurrences stay

Substitution acts only on free occurrences:
$$(P(x) \land \forall x \, Q(x))[c/x] = P(c) \land \forall x \, Q(x).$$
Replacing the bound $x$ too would give $\forall c \, Q(c)$, which is [[not even a formula|4SV9Q67884]].
If $x$ is not free in $\varphi$ at all, then $\varphi[t/x] = \varphi$.

### Several variables at once

The simultaneous swap $\{ x \mapsto y, y \mapsto x \}$ sends $x + y$ to $y + x$.
Two [[successive substitutions|VS6SNA8Z23]] give something else: $(x + y)[y/x] = y + y$, and then $(y + y)[x/y] = x + x$.
A substitution must also treat all occurrences of a variable alike, so it sends $x + x$ to $\theta(x) + \theta(x)$, never to $y + x$.

### The rules you can use

If $t$ is free for $x$ in $\varphi$ and $x \in \operatorname{FV}(\varphi)$, then $\operatorname{FV}(\varphi[t/x]) = (\operatorname{FV}(\varphi) \setminus \{ x \}) \cup \operatorname{Var}(t)$.
A term with no variables is free for every variable in every formula.
For any $t$, $x$ and $\varphi$, renaming the bound variables of $\varphi$ to fresh names gives an alpha-equivalent formula in which $t$ is free for $x$.
In terms, two single substitutions can be reordered: if $x \neq y$ and $x \notin \operatorname{Var}(r)$, then $u[s/x][r/y] = u[r/y][s[r/y]/x]$, the [[syntactic substitution lemma|FXEFA6PKZ1]].
If $t$ is free for $x$ in $\varphi$, then $\varphi[t/x]$ says about the value of $t$ what $\varphi$ says about the value of $x$; this semantic substitution lemma of [[structures and satisfaction|NJDME6F845]] makes $\forall x \, \varphi \to \varphi[t/x]$ valid.

### Watch out

The captured result is still a well-formed formula.
No grammar check catches the error in $\forall y \, (y < y)$; only the test "is $t$ free for $x$?" does.
So run that test before every instantiation, and rename bound variables when it fails.

Do not carry out a simultaneous substitution one variable at a time, since the swap above gives $x + x$ instead of $y + x$.

When you rename, pick a name that occurs nowhere in the scope and not in $t$.
Renaming the bound $y$ of $\exists y \, (y + y = x)$ back to $y$ itself, or to a variable of $t$, brings the capture back.

### History

Church's lambda calculus of the 1930s needed a rule for renaming bound variables, later called alpha conversion, so that substitution would avoid capture.
In 1965 John Alan Robinson introduced resolution together with a unification algorithm, which finds most general substitutions.
In 1972 de Bruijn introduced nameless bound variables, now called [[de Bruijn indices|1TC37YHZPE]], so that substitution in his Automath proof checker could not capture variables.

### Try it

Compute $(\forall y \, R(x, y) \land Q(x))[f(z)/x]$.
The term $f(z)$ contains no $y$, so it is free for $x$, and the result is $\forall y \, R(f(z), y) \land Q(f(z))$.

Is $g(y)$ free for $x$ in $\forall y \, P(y) \lor P(x)$?
Yes: the only free $x$ is in $P(x)$, which lies outside the scope of $\forall y$, so the result $\forall y \, P(y) \lor P(g(y))$ captures nothing.

## Explanations

### L1 human

Substitution is "plugging in".
If the claim is "$x$ is even", putting $6$ for $x$ gives "$6$ is even", which is true.
We plug in only where $x$ is an open slot, not where $x$ belongs to a "for all $x$".
We also must not plug in a letter that a "for all" then grabs by mistake.
Putting $y$ in for $x$ in "every $y$ is bigger than $x$" gives "every $y$ is bigger than $y$", which is a different claim.

### L2 human

Here is a typical step of a formal proof.
From the axiom $\forall x \, \exists y \, \neg (x = y)$, which holds in every structure with at least two elements, we want an instance for the term $y$.
The blind replacement in $\exists y \, \neg (x = y)$ gives $\exists y \, \neg (y = y)$, which is false in every structure.
The test fails: $y$ is not free for $x$, because the free $x$ lies in the scope of $\exists y$.
So we rename first, to $\exists z \, \neg (x = z)$, and then substitute:
$$\exists z \, \neg (x = z)[y/x] = \exists z \, \neg (y = z).$$
This says that some element differs from $y$, which is true whenever the structure has two elements.
The lesson: instantiate only after the test, and rename when the test fails.

### L3 human

The terms over a signature form a monad on sets: a set $X$ of variables goes to the set $T(X)$ of terms over $X$.
A substitution $X \to T(Y)$ is an arrow of the Kleisli category of this monad, and composing substitutions is Kleisli composition.
For formulas the binders spoil this simple picture, because substitution must respect alpha-equivalence.
The usual solutions are renaming built into substitution, [[de Bruijn indices|1TC37YHZPE]], numbered bound variables in a separate type as in Mathlib, and nominal sets.
In [[unification|RJJ9D0WF53]], substitutions are the solutions of equations between terms, and the most general unifier is the most general such solution.
In categorical logic, substitution is pullback along a map of contexts, and the quantifiers are adjoints to it.
