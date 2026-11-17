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

Let $\sigma = \set{+, \cdot, -, 0, 1}$ be the signature of [[rings|0B1261B5ED]], with arities $2, 2, 1, 0, 0$.
Consider the string $t = \cdot(x, +(y, 1))$, usually written $x \cdot (y + 1)$.
We check that $t$ is a [[term|6D3WA7N2W4]] and compute its formation tree and its value.

1. The strings $x$ and $y$ are terms by the variable clause, and $1$ is a term by the constant clause.
2. The string $+(y, 1)$ is a term by the function clause, since $+$ has arity $2$.
3. The string $\cdot(x, +(y, 1))$ is a term by the function clause, since $\cdot$ has arity $2$.
4. The formation tree has root $\cdot$ with two children: the leaf $x$, and the node $+$. The node $+$ has the two leaves $y$ and $1$.
5. By [[unique readability|3QPV4XW8MC]], this is the only formation tree of $t$.
6. The variables of $t$ are $x$ and $y$, so $\operatorname{Var}(t) = \set{x, y}$, and $t$ is not closed.
7. In the ring $\mathbb{Z}$ with $x = 3$ and $y = 4$, the value is computed from the leaves up: $y + 1$ has value $5$, and then $x \cdot (y + 1)$ has value $15$.

So the term $t$ has one tree, and its value comes from that tree.

## Remarks

The string $x \cdot y + 1$ without brackets has two readings in infix notation, $(x \cdot y) + 1$ and $x \cdot (y + 1)$.
Usual practice fixes the first by the rule that $\cdot$ binds more strongly than $+$.
The formal notation $\cdot(x, +(y, 1))$ needs no such rule.
The value in step 7 is defined by recursion on the tree, and unique readability makes this recursion well defined.

## Explanations

### L1 human

The term $x \cdot (y + 1)$ is built in steps: first $y + 1$, then $x$ times that.
These steps form a tree with $\cdot$ at the top.
To compute the value, start at the bottom of the tree and work up.
With $x = 3$ and $y = 4$, first $y + 1 = 5$, then $3 \cdot 5 = 15$.

### L2 human

We compare with the term $s = +(\cdot(x, y), 1)$, usually written $x \cdot y + 1$.

1. The root of $s$ is $+$, and the root of $t$ is $\cdot$.
2. With $x = 3$ and $y = 4$, the value of $s$ is $3 \cdot 4 + 1 = 13$, and the value of $t$ is $15$.
3. So $s$ and $t$ are different terms, with the same symbols in a different tree.

The typical use of the tree is to define functions on terms by recursion: the value, the set of variables, and substitution.
A trap: two terms can have the same value for all inputs and still be different, such as $x \cdot (y + 1)$ and $x \cdot y + x$.
