---
tag: BZP11VY05S
kind: example
name: The formation tree of a ring term
msc: ["03B10"]
topics: [PSRDJXRW53]
audience: ug2
instance_of: [6D3WA7N2W4]
uses: [6D3WA7N2W4, BQQ0FPFZ67, 3QPV4XW8MC, 0B1261B5ED]
sources:
  - url: https://en.wikipedia.org/wiki/Term_(logic)
    locator: lead section
  - book: isbn:9780122384523
    locator: Section 2.1
---

## Example

Every term carries a tree that records how it was built, and the tree is what gives the term its value.
Let $\sigma = \{ +, \cdot, -, 0, 1 \}$ be the signature of [[rings|0B1261B5ED]], with arities $2, 2, 1, 0, 0$.
Consider the string $t = \cdot(x, +(y, 1))$, usually written $x \cdot (y + 1)$.
We check that $t$ is a [[term|6D3WA7N2W4]], draw its formation tree, and compute its value.

1. The strings $x$ and $y$ are terms by the variable clause of the [[definition|BQQ0FPFZ67]], and $1$ is a term by the constant clause.
2. The string $+(y, 1)$ is a term by the function clause, since $+$ has arity $2$ and gets two terms.
3. The string $\cdot(x, +(y, 1))$ is a term by the function clause, since $\cdot$ has arity $2$ and gets two terms.
4. The formation tree has the root $\cdot$ with two children, the leaf $x$ and a node $+$.
   The node $+$ has the two leaves $y$ and $1$.
5. By [[unique readability|3QPV4XW8MC]], this is the only formation tree of $t$.
6. The leaves that are variables are $x$ and $y$, so $\operatorname{Var}(t) = \{ x, y \}$ and $t$ is not closed.
7. In the ring $\mathbb{Z}$ with $x = 3$ and $y = 4$, we compute from the leaves up:
   $$y + 1 = 4 + 1 = 5, \qquad x \cdot (y + 1) = 3 \cdot 5 = 15.$$

So the term $t$ has one tree, and its value comes from that tree.

## Remarks

Without brackets, the infix string $x \cdot y + 1$ has two readings, $(x \cdot y) + 1$ and $x \cdot (y + 1)$.
Everyday practice picks the first, by the rule that $\cdot$ binds more strongly than $+$.
The prefix form $\cdot(x, +(y, 1))$ needs no such rule, since its brackets and the arities fix the tree.

If we change one value, the computation changes only along one path of the tree.
With $x = 3$ and $y = -1$, the node $+$ gets $0$ and the root gets $3 \cdot 0 = 0$.
The value at the root is defined by recursion on the tree, and unique readability is what makes that recursion well defined.

## Explanations

### L1 human

The term $x \cdot (y + 1)$ is built in steps: first $y + 1$, then $x$ times that.
These steps form a tree with $\cdot$ at the top.
To compute the value, start at the bottom of the tree and work up.
With $x = 3$ and $y = 4$, first $y + 1 = 5$, then $3 \cdot 5 = 15$.

### L2 human

We compare $t$ with the term $s = +(\cdot(x, y), 1)$, usually written $x \cdot y + 1$.
The root of $s$ is $+$, while the root of $t$ is $\cdot$.
At $x = 3$ and $y = 4$ the two values are
$$s = 3 \cdot 4 + 1 = 13, \qquad t = 3 \cdot (4 + 1) = 15.$$
So $s$ and $t$ are different terms: the same symbols sit in a different tree.
The typical use of the tree is to define functions on terms by recursion, such as the value, the set of variables, and substitution.
Watch out: two terms can have the same value for all inputs and still be different terms, such as $x \cdot (y + 1)$ and $x \cdot y + x$.
