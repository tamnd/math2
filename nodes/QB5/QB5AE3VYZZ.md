---
tag: QB5AE3VYZZ
kind: statement
role: theorem
name: Hahn–Banach theorem
msc: [46A22]
uses: [000AYPA9AJ, 00YC1D652K, 07YQ1C78G0, K3356N0SAX]
about: [07YQ1C78G0, K3356N0SAX]
sources:
  - url: https://en.wikipedia.org/wiki/Hahn%E2%80%93Banach_theorem
same_as:
  wikidata: Q866116
  wikipedia: Hahn–Banach theorem
---

## Statement

Let $X$ be a [[vector space|000AYPA9AJ]] over $\R$, and let $p \colon X \to \R$ be a [[sublinear function|K3356N0SAX]].
Let $M$ be a [[linear subspace|00YC1D652K]] of $X$, and let $f \colon M \to \R$ be a [[linear form|07YQ1C78G0]] with $f(m) \le p(m)$ for all $m \in M$.
Then there is a linear form $F \colon X \to \R$ such that $F(m) = f(m)$ for all $m \in M$ and $F(x) \le p(x)$ for all $x \in X$.

## Remarks

The proof first extends $f$ to $M + \R x_0$ for one vector $x_0 \notin M$.
The value $F(x_0)$ must be a number $c$ with $\sup_{m \in M} (f(m) - p(m - x_0)) \le c \le \inf_{m \in M} (p(m + x_0) - f(m))$, and subadditivity of $p$ shows that such a $c$ exists.
[[Zorn's lemma|04RXTQA5ZA]] applied to the partial extensions dominated by $p$ then gives an extension to all of $X$.

The most used case takes $p(x) = \norm{f}\,\norm{x}$ on a real [[normed vector space|03J5RAKB30]].
It shows that every bounded linear functional on a subspace extends to the whole space with the same [[operator norm|06EKW1AKXF]].
The complex case of this norm version follows by applying the real theorem to the real part of $f$.
A consequence is that for each $x \ne 0$ in a normed space there is a functional $F$ of norm $1$ with $F(x) = \norm{x}$, so the [[continuous dual space|4A82S5FVRT]] separates points.

## Explanations

### L1 human

The theorem says that a linear rule defined on part of a space can be extended to the whole space without breaking a given bound.
The bound is a sublinear function, such as a norm.
It is the basic tool that guarantees there are enough continuous linear functionals on a normed space to tell its points apart.

### L2 human

In a course on functional analysis this is the first of the main theorems, next to the [[uniform boundedness principle|YG0042V8CJ]] and the [[bounded inverse theorem|MR5FJXR348]].
Its norm form gives the isometric embedding of a space into its [[bidual|QKR3D65TTH]].
Its geometric form is the [[Hahn–Banach separation theorem|6GWMGFGFJJ]], which separates disjoint convex sets by a closed hyperplane.
The two forms are linked by the [[Minkowski functional|PAX9SHDHDW]] of a convex neighbourhood of $0$.
In a general real vector space the proof needs Zorn's lemma or a weaker choice principle.
