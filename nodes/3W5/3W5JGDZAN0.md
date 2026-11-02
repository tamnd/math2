---
tag: 3W5JGDZAN0
kind: statement
role: theorem
name: Tarski–Seidenberg theorem
msc: [14P10, 03C10, 12D15]
uses: [DDY3Q3PJ6W, FSJ9NGRRPA, 07GNX8GCYP]
about: [DDY3Q3PJ6W]
sources:
  - url: https://en.wikipedia.org/wiki/Tarski–Seidenberg_theorem
same_as:
  wikidata: Q16705451
  wikipedia: Tarski–Seidenberg theorem
---

## Statement

Let $R$ be a [[real closed field|DDY3Q3PJ6W]], for example $\R$.
A subset of $R^m$ is *semialgebraic* if it is a finite union of sets of the following form.
$$\set{x \in R^m : f(x) = 0, \ g_1(x) > 0, \dots, g_k(x) > 0}$$
Here $k \ge 0$, and $f, g_1, \dots, g_k$ are [[polynomials|07GNX8GCYP]] in $m$ variables with coefficients in $R$.
Let $n \ge 1$, let $\pi \colon R^{n+1} \to R^n$ be the projection $\pi(x_1, \dots, x_{n+1}) = (x_1, \dots, x_n)$, and let $S \subseteq R^{n+1}$ be semialgebraic.
Then $\pi(S)$ is a semialgebraic subset of $R^n$.

## Remarks

The theorem is the geometric form of [[quantifier elimination for real closed fields|FSJ9NGRRPA]].
The set $\pi(S)$ is defined by the formula $\exists x_{n+1} \, \varphi(x_1, \dots, x_{n+1})$, where $\varphi$ is a quantifier-free formula that defines $S$.
Quantifier elimination replaces it by a quantifier-free formula with parameters in $R$, and the set defined by such a formula is semialgebraic.

Example: let $S = \set{(a, x) \in \R^2 : x^2 - a = 0}$, which is semialgebraic.
Its projection to the first coordinate is $\set{a : a \ge 0}$, which is semialgebraic as the union of $\set{a : a = 0}$ and $\set{a : a > 0}$.

The analogous statement fails for algebraic sets.
The projection of the algebraic set $S$ above is $[0, \infty)$, which is not the zero set of any family of polynomials in one variable.
This is why inequalities are part of the definition.

## Explanations

### L1 human

Semialgebraic sets are the sets cut out by polynomial equations and inequalities, such as discs, half-planes and parabolic regions.
The theorem says that the shadow of such a set on a lower-dimensional space is again of this kind.
So the class of semialgebraic sets is stable under the operations that geometric constructions use.

### L2 human

By induction on $n$, the image of a semialgebraic set under any polynomial map is semialgebraic, and so are closures, interiors and sets defined with quantifiers over $R$.
This makes semialgebraic sets the natural setting of real algebraic geometry, in contrast with real algebraic sets, which lack this closure property.
It also shows that every subset of $R$ definable with $+$, $\cdot$ and $<$ is semialgebraic, hence a finite union of points and open intervals.
This is the starting point of o-minimality.
Algorithms for quantifier elimination over $\R$, such as cylindrical algebraic decomposition, make the projection effective.
