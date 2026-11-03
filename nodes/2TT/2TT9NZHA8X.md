---
tag: 2TT9NZHA8X
kind: definition
name: Slack variable
msc: [90C05]
defines: 5VE5GVSNHK
uses: [X3663P90AE, VNMXB0J2KA]
sources:
  - url: https://en.wikipedia.org/wiki/Slack_variable
---

## Definition

Let $a \in \R^n$ and $\beta \in \R$, and consider the inequality [[constraint|X3663P90AE]] $a^T x \le \beta$ on $x \in \R^n$.
A *slack variable* for it is a new real variable $s$ together with the replacement of the constraint by the two constraints
$$a^T x + s = \beta, \qquad s \ge 0.$$
A point $x$ satisfies $a^T x \le \beta$ if and only if $(x, s)$ satisfies the new constraints with $s = \beta - a^T x$.

## Remarks

For a constraint $a^T x \ge \beta$, the variable $s$ in $a^T x - s = \beta$, $s \ge 0$, is called a *surplus variable*.
For a system $A x \le b$ of $m$ constraints, one adds a vector $s \in \R^m$ of slack variables and gets $A x + s = b$, $s \ge 0$.
The constraint $a^T x \le \beta$ is active at $x$ exactly when its slack is $0$.

Example: for $x_1 + 2 x_2 \le 4$ the slack form is $x_1 + 2 x_2 + s = 4$, $s \ge 0$.
At $x = (1, 1)$ the slack is $s = 4 - 3 = 1 \ge 0$, so $x$ satisfies the constraint and it is inactive.

Non-example: at $x = (2, 2)$ the equation forces $s = 4 - 6 = -2$, which violates $s \ge 0$; accordingly $x$ violates $x_1 + 2 x_2 \le 4$.

In a [[linear program|VNMXB0J2KA]], slack variables carry objective coefficient $0$, so the optimal value is unchanged.
