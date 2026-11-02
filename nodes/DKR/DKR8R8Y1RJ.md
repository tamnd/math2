---
tag: DKR8R8Y1RJ
kind: definition
name: Shooting method
msc: [65L10, 34B15]
defines: ECT6RNF865
uses: [TM8VQJWGHZ, 0FXDW992DS, 07EXVNF9VP]
sources:
  - url: https://en.wikipedia.org/wiki/Shooting_method
---

## Definition

Let $a < b$, let $\alpha, \beta \in \R$, and let $f \colon [a, b] \times \R^2 \to \R$ be continuous and locally Lipschitz in its last two arguments.
Consider the [[boundary value problem|TM8VQJWGHZ]]
$$y'' = f(x, y, y'), \qquad y(a) = \alpha, \qquad y(b) = \beta.$$
For $s \in \R$, let $y(\cdot\,; s)$ be the solution of the [[initial value problem|0FXDW992DS]] $y'' = f(x, y, y')$, $y(a) = \alpha$, $y'(a) = s$.
Let $S$ be the set of $s$ for which this solution exists on all of $[a, b]$, and define $F \colon S \to \R$ by
$$F(s) = y(b; s) - \beta.$$
The shooting method is the procedure that finds a root $s^*$ of $F$ and returns $y(\cdot\,; s^*)$.
The root is found, for example, by bisection, by the secant method or by [[Newton's method|07EXVNF9VP]].

## Remarks

Each root $s^*$ of $F$ gives a solution $y(\cdot\,; s^*)$ of the boundary value problem, and each solution arises this way from $s^* = y'(a)$.
Example: for $y'' = 0$, $y(0) = 0$, $y(1) = 3$, one gets $y(x; s) = s x$ and $F(s) = s - 3$, so $s^* = 3$ and $y = 3x$.
Non-example of success: for $y'' = -y$, $y(0) = 0$, $y(\pi) = 1$, one gets $y(x; s) = s \sin x$ and $F(s) = -1$ for every $s$.
Then $F$ has no root, and indeed the boundary value problem has no solution.
When the solutions of the initial value problems grow fast, small errors in $s$ blow up.
Then one splits $[a, b]$ into pieces and shoots on each piece; this is called multiple shooting.

## Explanations

### L1 human

The method guesses the slope at the left end, solves the equation from there, and looks at where the solution ends up on the right.
The miss distance is a function of the guess.
Making the miss zero is a problem of finding a root of one function of one variable.
