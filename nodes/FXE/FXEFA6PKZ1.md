---
tag: FXEFA6PKZ1
kind: statement
role: lemma
name: Syntactic substitution lemma
msc: ["03B10"]
topics: [PSRDJXRW53]
audience: ug2
about: [NCDZ969V7X]
uses: [XN8TQE6SRK, 6D3WA7N2W4, Y3FZTH5158]
sources:
  - url: https://en.wikipedia.org/wiki/Substitution_(logic)
    locator: lead section
  - book: isbn:9780122384523
    locator: Section 2.4
---

## Statement

Let $\sigma$ be a signature, let $x$ and $y$ be variables, and let $s$ and $r$ be [[terms|6D3WA7N2W4]] over $\sigma$.
Write $u[s/x]$ for the [[substitution|XN8TQE6SRK]] of $s$ for $x$ in $u$, and $\operatorname{Var}(r)$ for the set of variables of $r$.
Assume that $x \neq y$ and $x \notin \operatorname{Var}(r)$.

1. For every term $t$ over $\sigma$,
   $$t[s/x][r/y] = t[r/y]\big[s[r/y]/x\big].$$
2. For every quantifier-free formula $\varphi$ over $\sigma$,
   $$\varphi[s/x][r/y] = \varphi[r/y]\big[s[r/y]/x\big].$$

Both sides are equal as strings, not only logically equivalent.
The [[proof by induction|F8W7W5B97F]] treats terms first and then quantifier-free formulas.

## Remarks

### What the lemma says

The lemma tells us how to swap the order of two substitutions.
Substituting $r$ for $y$ first is allowed, as long as we then put in for $x$ the term $s$ updated by the same substitution, $s[r/y]$.
Check with $t = x + y$, $s = y + 1$ and $r = 2$.
The left side is $(y + 1) + y$ and then $(2 + 1) + 2$.
On the right, $t[2/y] = x + 2$ and $s[2/y] = 2 + 1$, which give $(2 + 1) + 2$ again.

### Why each hypothesis is needed

Without $x \neq y$, take $x = y$, $t = x$, and constant symbols $s = c$ and $r = d$.
The left side is $x[c/x][d/x] = c[d/x] = c$, and the right side is $x[d/x][c/x] = d$.

Without $x \notin \operatorname{Var}(r)$, take $t = y$, $r = x$ and $s = c$.
The left side is $y[c/x][x/y] = x$, and the right side is $y[x/y][c/x] = c$.

Without "quantifier-free", take $\varphi = \forall y \, P(x)$, $s = y$ and $r = c$.
The left side is $(\forall y \, P(y))[c/y] = \forall y \, P(y)$, and the right side is $(\forall y \, P(x))[c/x] = \forall y \, P(c)$.
The failure comes from the capture of $y$ in the first substitution.

### Consequences

If also $y \notin \operatorname{Var}(s)$, then $s[r/y] = s$, and the two substitutions commute: $t[s/x][r/y] = t[r/y][s/x]$.
Both sides of part 1 also equal the single simultaneous substitution $t[s[r/y]/x, \, r/y]$.
By repeated use of this fact, every finite sequence of single substitutions in a term equals one simultaneous substitution.

### Converse and generalizations

The converse is false: the equation can hold for all terms $t$ although the hypotheses fail.
Take $y = x$ and $s = r = x$; both sides equal $t$, because $t[x/x] = t$.

The equation holds for every formula $\varphi$, quantifiers included, when no variable of $s$ or $r$ is bound in $\varphi$.
Then no substitution captures a variable, and the quantifier case of the induction goes through.
The same equation, with $x \neq y$ and $x$ not free in $r$, is the substitution lemma of the [[lambda calculus|BD756KR8FM]], for substitution with renaming of bound variables.
For simultaneous substitutions the general form is the law $(t\theta)\eta = t(\theta\eta)$ of composition.

## History

The lemma belongs to the basic syntax of first-order logic and of the lambda calculus, and textbooks prove it as a routine induction.

## Explanations

### L1 human

Suppose we first put a value in for $x$, and then a value in for $y$.
The lemma says how to do the two steps in the other order.
We first put $r$ in for $y$, and then we put in for $x$ the old value of $x$, updated by the new value of $y$.
For example, in $x + y$ put $y + 1$ for $x$ and then $2$ for $y$: we get $(2 + 1) + 2$.
In the other order, put $2$ for $y$ first, giving $x + 2$, and then $2 + 1$ for $x$: we get $(2 + 1) + 2$ again.

### L2 human

We check the lemma for $t = f(x, y, z)$, $s = g(y)$ and $r = h(z)$, where $x$, $y$, $z$ are distinct.

1. Here $x \neq y$ and $\operatorname{Var}(r) = \{ z \}$ does not contain $x$, so the hypotheses hold.
2. Left side: $t[s/x] = f(g(y), y, z)$, then $[r/y]$ gives $f(g(h(z)), h(z), z)$.
3. Right side: $s[r/y] = g(h(z))$, and $t[r/y] = f(x, h(z), z)$.
4. Then $[g(h(z))/x]$ gives $f(g(h(z)), h(z), z)$, the same term as in step 2.

The typical use is a proof that moves one substitution past another, or merges two substitutions into one.
Watch out for the update $s[r/y]$: without it, $t[r/y][s/x] = f(g(y), h(z), z)$ differs from the left side.

### L3 human

View substitutions as maps.
Both sides apply one substitution $\theta$ with $\theta(x) = s[r/y]$ and $\theta(y) = r$, and the lemma says that two ways of composing single substitutions give the same $\theta$.
From the view of the term monad, this is associativity of Kleisli composition, together with a computation of the composites.
For formulas with binders the clean statement needs capture-free substitution, and this is one reason why proof assistants represent bound variables by numbers or by nominal atoms.
The semantic counterpart, in [[structures and satisfaction|NJDME6F845]], says that substitution of a term corresponds to the update of an assignment by the value of the term.
