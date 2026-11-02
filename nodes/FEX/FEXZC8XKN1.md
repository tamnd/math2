---
tag: FEXZC8XKN1
kind: statement
role: theorem
name: M. Riesz extension theorem
msc: [46A22, 46A40, 44A60]
uses: [000AYPA9AJ, 00YC1D652K, 6VE4KA12VD, 07YQ1C78G0]
about: [07YQ1C78G0, 6VE4KA12VD]
sources:
  - url: https://en.wikipedia.org/wiki/M._Riesz_extension_theorem
same_as:
  wikidata: Q3527217
  wikipedia: M. Riesz extension theorem
---

## Statement

Let $E$ be a real [[vector space|000AYPA9AJ]], let $F \subseteq E$ be a [[linear subspace|00YC1D652K]], and let $K \subseteq E$ be a [[convex cone|6VE4KA12VD]].
Let $\varphi \colon F \to \R$ be a [[linear form|07YQ1C78G0]] such that $\varphi(x) \ge 0$ for every $x \in F \cap K$.
Assume that for every $y \in E$ there is $x \in F$ with $y - x \in K$.
Then there is a linear form $\psi \colon E \to \R$ such that $\psi(x) = \varphi(x)$ for all $x \in F$ and $\psi(y) \ge 0$ for all $y \in K$.

## Remarks

The proof extends $\varphi$ one dimension at a time, as in the proof of the [[Hahn–Banach theorem|QB5AE3VYZZ]].
To add a vector $y \notin F$, one needs a value $c = \psi(y)$ with $\sup \varphi(x) \le c \le \inf \varphi(x')$, where $x$ runs over $F$ with $y - x \in K$ and $x'$ runs over $F$ with $x' - y \in K$.
The hypothesis on $F$ makes both sets nonempty, and positivity of $\varphi$ on $F \cap K$ makes the supremum at most the infimum.
Zorn's lemma then gives an extension to all of $E$.
In the moment problem, $E$ is a space of functions containing the polynomials and $K$ is the cone of nonnegative functions in $E$.
There $F$ is the space of polynomials and $\varphi$ is the moment functional $x^n \mapsto m_n$.
The positive extension $\psi$ is then turned into a measure by a representation theorem, which solves the [[Hamburger moment problem|TBNCFXTMMW]] for a positive moment functional.
Without the assumption that $y - x \in K$ for some $x \in F$, an extension may fail to exist.
For example, take $E = \R^2$, $K = \set{(s, t) : t > 0} \cup \set{(s, 0) : s \ge 0}$, $F = \R \times \set{0}$ and $\varphi(s, 0) = s$; then $\varphi \ge 0$ on $F \cap K$, but a positive extension $\psi(s, t) = s + ct$ would need $s + c \ge 0$ for all $s$, which is impossible.

## Explanations

### L1 human

A linear rule that gives nonnegative values on the "positive" vectors of a subspace can be extended to the whole space without losing this property.
The only condition is that the subspace is large enough: every vector must lie above some vector of the subspace.
It is the order version of the Hahn–Banach theorem.

### L2 human

The theorem is the abstract tool behind the existence parts of moment problems.
A sequence $(m_n)$ defines a linear form $L$ on polynomials by $L(x^n) = m_n$.
Suppose that $L(p) \ge 0$ for every polynomial $p \ge 0$.
Then the theorem extends $L$ to a positive linear form on a larger space of functions, such as the continuous functions bounded by a polynomial.
The [[Riesz representation theorem|TTC40N49M6]] then gives a measure with moments $m_n$.
The same argument, with polynomials in several variables and nonnegativity on a closed set, gives the multivariate form of this existence result.
