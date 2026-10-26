---
tag: ~2bdf37ac
kind: statement
role: corollary
name: Implicit function theorem for a surjective derivative
aliases: [regular-value-theorem-euclidean]
msc: [26B10]
uses: [~c4a20657, ~454e4d78, ~896c035b]
sources:
  - url: https://en.wikipedia.org/wiki/Inverse_function_theorem
    locator: Several variables
  - url: https://en.wikipedia.org/wiki/Implicit_function_theorem
    locator: Statement of the theorem
---

## Statement

Let $U \subseteq \mathbb{R}^n$ be open, let $m \le n$, and let $F \colon U \to \mathbb{R}^m$ be of class $C^1$.
Let $p \in U$ with $F(p) = 0$, and suppose that $DF(p) \colon \mathbb{R}^n \to \mathbb{R}^m$ is surjective.
Then there are $m$ coordinates $x_{i_1}, \dots, x_{i_m}$ and an open neighbourhood $W$ of $p$ with this property. The set $\{x \in W : F(x) = 0\}$ is the graph of a $C^1$ function of the other $n - m$ coordinates.

## Remarks

The derivative is surjective if and only if the [[Jacobian matrix|~896c035b]] $J_F(p)$ has rank $m$. Then some $m$ columns of $J_F(p)$ are linearly independent, and these columns choose the coordinates.
After a renumbering of coordinates, the statement is the [[implicit function theorem|~c4a20657]] with $y = (x_{i_1}, \dots, x_{i_m})$.
If $DF(x)$ is surjective at each point of the [[level set|~454e4d78]] $F^{-1}(0)$, this set is locally a graph near each of its points. So it is a $C^1$ submanifold of dimension $n - m$.
Example: for $F(x, y, z) = x^2 + y^2 + z^2 - 1$, $DF$ is surjective on the unit sphere. So the sphere is locally the graph of a function of two coordinates.

## Explanations

### L1 human

The condition that the derivative is onto means the $m$ equations are independent at the point.
Then $m$ of the variables are determined by the others, and the solution set has $n - m$ free directions.
