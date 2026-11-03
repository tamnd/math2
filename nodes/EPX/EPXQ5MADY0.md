---
tag: EPXQ5MADY0
kind: definition
name: Linear program in standard form
msc: [90C05]
defines: T7Y2GVS1FQ
uses: [VNMXB0J2KA, 0VD9ZSWWJG, 5VE5GVSNHK]
sources:
  - url: https://en.wikipedia.org/wiki/Linear_programming
    locator: Standard form
---

## Definition

Let $m, n \ge 1$, let $A$ be a real $m \times n$ [[matrix|0VD9ZSWWJG]], let $b \in \R^m$ and let $c \in \R^n$.
For vectors $u, w$ of the same size, $u \le w$ means $u_i \le w_i$ for every $i$.
The *linear program in standard form* given by $(A, b, c)$ is the problem
$$\text{maximize } c^T x \quad \text{subject to} \quad A x \le b, \quad x \ge 0,$$
over $x \in \R^n$.

## Remarks

It is the [[linear program|VNMXB0J2KA]] with constraint matrix $\begin{pmatrix} A \\ -I \end{pmatrix}$ and right-hand side $\begin{pmatrix} b \\ 0 \end{pmatrix}$.
Conversely, every linear program can be put in standard form by these steps.

1. Replace "minimize $c^T x$" by "maximize $-c^T x$".
2. Replace a constraint $a^T x \ge \beta$ by $-a^T x \le -\beta$, and $a^T x = \beta$ by the two inequalities $a^T x \le \beta$ and $-a^T x \le -\beta$.
3. Replace a free variable $x_j$ by $x_j^+ - x_j^-$ with $x_j^+, x_j^- \ge 0$.

Adding [[slack variables|5VE5GVSNHK]] $s = b - A x$ gives the *equational form* $A x + s = b$, $x \ge 0$, $s \ge 0$.
Many texts, in particular those on the simplex method, call this equational form the standard form.

Example: "maximize $x_1 + x_2$ subject to $x_1 + 2 x_2 \le 4$, $3 x_1 + x_2 \le 6$, $x_1, x_2 \ge 0$" is in standard form, with $A = \begin{pmatrix} 1 & 2 \\ 3 & 1 \end{pmatrix}$, $b = (4, 6)^T$ and $c = (1, 1)^T$.

Non-example: "maximize $x_1$ subject to $x_1 + x_2 \le 1$" is not in standard form, because there is no sign condition on $x_1$ and $x_2$.
