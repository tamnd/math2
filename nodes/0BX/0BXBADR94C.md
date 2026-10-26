---
tag: 0BXBADR94C
kind: statement
role: theorem
name: Implicit function theorem
aliases: [implicit-function-theorem]
msc: [26B10]
uses: [0TCBZMEYGN, 0YF0VXKXGB, 0K9HSJFCMJ]
sources:
  - url: https://en.wikipedia.org/wiki/Implicit_function_theorem
    locator: Statement of the theorem
  - url: https://en.wikipedia.org/wiki/Implicit_function_theorem
    locator: History
same_as:
  wikidata: Q848375
  wikipedia: Implicit function theorem
---

## Statement

Let $\Omega \subseteq \mathbb{R}^n \times \mathbb{R}^m$ be open, and let $F \colon \Omega \to \mathbb{R}^m$ be of [[class C^1|0TCBZMEYGN]], written $F(x, y)$ with $x \in \mathbb{R}^n$ and $y \in \mathbb{R}^m$.
Let $(a, b) \in \Omega$ with $F(a, b) = 0$.
Suppose that the $m \times m$ matrix $D_y F(a, b) = \left( \partial F_i / \partial y_j (a, b) \right)_{i, j}$ is invertible.
Then there are open sets $U \subseteq \mathbb{R}^n$ and $V \subseteq \mathbb{R}^m$ with $a \in U$ and $b \in V$, and a unique function $g \colon U \to V$ with the following property. For $(x, y) \in U \times V$, $F(x, y) = 0$ if and only if $y = g(x)$.
The function $g$ is of class $C^1$, and $Dg(x) = -\big( D_y F(x, g(x)) \big)^{-1} D_x F(x, g(x))$ for each $x \in U$.

## Remarks

Here $D_x F$ is the $m \times n$ matrix of partial derivatives with respect to $x$. Together, $D_x F$ and $D_y F$ form the [[Jacobian matrix|0YF0VXKXGB]] of $F$.
For $F(x, y) = x^2 + y^2 - 1$ and $(a, b)$ with $b \ne 0$, the solution near $(a, b)$ is $y = \pm \sqrt{1 - x^2}$. At $(\pm 1, 0)$, $\partial F / \partial y = 0$, and no such function exists.
One proof applies the [[inverse function theorem|0K9HSJFCMJ]] to $(x, y) \mapsto (x, F(x, y))$. If $F$ is of class $C^k$, then $g$ is of class $C^k$.
The theorem has a long history. Cauchy gave the first rigorous form, and Dini extended the real version to any number of variables.

## Explanations

### L1 human

An equation $F(x, y) = 0$ often defines $y$ as a function of $x$, even when you cannot solve it with a formula.
The theorem says this works near a solution, provided $F$ really depends on $y$ there, in the sense that $D_y F$ is invertible.
