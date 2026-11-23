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

Let $\sigma = \{ 0, S, +, \cdot \}$ be the signature of arithmetic: a constant symbol $0$, a unary function symbol $S$ and binary function symbols $+$ and $\cdot$.
Consider the string
$$\varphi = \forall x \, (\neg x = 0 \to \exists y \, x = S(y)).$$
We check that $\varphi$ is a [[well-formed formula|HYJ10AF6RT]] by the clauses of the [[definition|2CHENV4DCC]], and we draw its parse tree.

1. The strings $x$, $y$ and $0$ are [[terms|6D3WA7N2W4]], two variables and a constant symbol.
   Then $S(y)$ is a term, because $S$ has arity $1$.
2. The strings $x = 0$ and $x = S(y)$ are [[atomic formulas|MCZRXR3SVB]], by clause 1.
3. The string $\neg x = 0$ is a formula, by clause 3 applied to $x = 0$.
4. The string $\exists y \, x = S(y)$ is a formula, by clause 5 applied to $x = S(y)$ with the variable $y$.
5. The string $(\neg x = 0 \to \exists y \, x = S(y))$ is a formula, by clause 4 applied to steps 3 and 4.
6. The string $\varphi$ is a formula, by clause 5 applied to step 5 with the variable $x$.

The parse tree records these steps upside down.
Its root is $\forall x$, with one child $\to$.
The node $\to$ has the left child $\neg$ and the right child $\exists y$.
Below $\neg$ hangs the leaf $x = 0$, and below $\exists y$ hangs the leaf $x = S(y)$.
If we also draw terms, the leaf $x = 0$ has the children $x$ and $0$, and the leaf $x = S(y)$ has the children $x$ and $S(y)$, with $y$ below $S(y)$.

## Remarks

The tree shows the main symbol of each subformula at a glance: $\forall x$ for $\varphi$, $\to$ for step 5, and $\neg$ and $\exists y$ below it.
The complexity of $\varphi$ is the number of connective and quantifier nodes, here $4$: $\forall x$, $\to$, $\neg$ and $\exists y$.

The tree also gives the free variables, computed from the leaves up.
The leaf $x = 0$ has the variable $x$, and the leaf $x = S(y)$ has $x$ and $y$.
The node $\exists y$ removes $y$, so both children of $\to$ have the free variable set $\{ x \}$.
The root $\forall x$ removes $x$, so $\varphi$ has no free variables and is a [[sentence|DKFGQTRYZE]].
Check: every $x$ sits under $\forall x$ and every $y$ sits under $\exists y$.

In the natural numbers, $\varphi$ says that every nonzero number is a successor, which is true.
If we replace $S(y)$ by $y + y$, the tree keeps its shape, but the new sentence says that every nonzero number is even, which is false.
So the tree fixes the grammar, and the meaning depends on the symbols at the leaves.

Watch out for missing brackets.
Without the brackets of step 5, the string $\forall x \, \neg x = 0 \to \exists y \, x = S(y)$ has the root $\to$, because $\forall x$ binds more strongly than $\to$.
Its first part $\forall x \, \neg x = 0$ is a different formula, so the two strings have different trees.

## Explanations

### L1 human

A parse tree is a family tree for a formula.
At the top sits the last rule used, here "for every $x$".
Below it sit the parts that the rule joined, down to the simple claims "$x = 0$" and "$x = S(y)$".
The tree tells you how to read the formula aloud: "for every $x$, if $x$ is not $0$, then $x$ is the successor of some $y$".
For example, $x = 5$ is the successor of $y = 4$.

### L2 human

Here is how a computer would evaluate $\varphi$ in the natural numbers using the tree, from the leaves up.
For a fixed value of $x \ge 1$, the leaf $x = S(y)$ is true at $y = x - 1$, and for $x = 0$ it is false at every $y$.
So the node $\exists y$ is true exactly when $x \ge 1$.
The node $\neg$ is true exactly when $x \neq 0$, which is the same condition.
So the node $\to$ is true for every value of $x$, and the root $\forall x$ is true.
Every recursive definition on formulas, such as truth, free variables or complexity, follows the tree in this way.
