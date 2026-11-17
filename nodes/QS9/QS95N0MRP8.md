---
tag: QS95N0MRP8
kind: example
name: The parse tree of a formula of arithmetic
msc: ["03B10"]
topics: [PSRDJXRW53]
audience: ug2
instance_of: [HYJ10AF6RT]
uses: [HYJ10AF6RT, 2CHENV4DCC, 6D3WA7N2W4, MCZRXR3SVB]
sources:
  - url: https://en.wikipedia.org/wiki/Well-formed_formula
    locator: lead section
  - url: https://builds.openlogicproject.org/
    locator: "Chapter: Syntax and Semantics"
---

## Example

Let $\sigma = \set{0, S, +, \cdot}$ be the signature of arithmetic: a constant symbol $0$, a unary function symbol $S$ and binary function symbols $+$ and $\cdot$.
Consider the string
$$\varphi = \forall x \, (\neg x = 0 \to \exists y \, x = S(y)).$$
We check that $\varphi$ is a [[well-formed formula|HYJ10AF6RT]] and find its parse tree, by the clauses of the [[definition|2CHENV4DCC]].

1. The strings $x$, $0$ and $y$ are [[terms|6D3WA7N2W4]]: two variables and a constant symbol. Then $S(y)$ is a term, because $S$ has arity $1$.
2. The strings $x = 0$ and $x = S(y)$ are [[atomic formulas|MCZRXR3SVB]], by clause 1.
3. The string $\neg x = 0$ is a formula, by clause 3 applied to $x = 0$.
4. The string $\exists y \, x = S(y)$ is a formula, by clause 5 applied to $x = S(y)$.
5. The string $(\neg x = 0 \to \exists y \, x = S(y))$ is a formula, by clause 4 applied to steps 3 and 4.
6. The string $\varphi$ is a formula, by clause 5 applied to step 5 with the variable $x$.

The parse tree has the root $\forall x$, with one child $\to$.
The node $\to$ has the left child $\neg$ and the right child $\exists y$.
The node $\neg$ has the leaf $x = 0$, and the node $\exists y$ has the leaf $x = S(y)$.
Below each leaf hang the parse trees of its terms: $x$ and $0$ for the first leaf, and $x$ and $S(y)$, with the child $y$, for the second leaf.

## Remarks

The parse tree shows the main symbol of each subformula: $\forall x$ for $\varphi$, $\to$ for the formula of step 5, $\neg$ and $\exists y$ below it.
The complexity of $\varphi$ is $4$, the number of inner nodes of the tree above the leaves: $\forall x$, $\to$, $\neg$ and $\exists y$.
The formula $\varphi$ is a [[sentence|DKFGQTRYZE]], since each occurrence of $x$ and of $y$ lies under a quantifier on that variable.
In the natural numbers it says that every number other than $0$ is a successor, which is true.
If we replace $S(y)$ by $y + y$, we get a formula that says that every nonzero number is even, which is false in the natural numbers, although the parse tree has the same shape.

## Explanations

### L1 human

A parse tree is like a family tree for a formula.
At the top sits the last rule that was used, here "for every $x$".
Below it sit the parts that the rule combined, down to the simple claims "$x = 0$" and "$x = S(y)$".
The tree shows how to read the formula: "for every $x$, if $x$ is not $0$, then $x$ is the successor of some $y$".
For example, $x = 5$ is the successor of $y = 4$.

### L2 human

We use the tree to compute the variables that each subformula leaves free.

1. The leaf $x = 0$ has the variable $x$, and the leaf $x = S(y)$ has the variables $x$ and $y$.
2. The node $\neg$ keeps $\set{x}$, and the node $\exists y$ removes $y$ from $\set{x, y}$ and keeps $\set{x}$.
3. The node $\to$ takes the union $\set{x}$.
4. The root $\forall x$ removes $x$, so $\varphi$ has no free variables.

The typical use of a parse tree is any computation by recursion on formulas: free variables, complexity or truth.
The trap is a tree drawn from a string with missing brackets: without the brackets of step 5, the root could also be read as an implication.
