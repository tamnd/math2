---
tag: VGV9FAPCHN
kind: statement
role: theorem
name: Jury stability criterion
msc: [93D20, 39A30, 26C10]
uses: [X11Q0G8PNA, 0D430QR02W]
about: [X11Q0G8PNA]
sources:
  - url: https://en.wikipedia.org/wiki/Jury_stability_criterion
same_as:
  wikidata: Q3697760
  wikipedia: Jury stability criterion
---

## Statement

Let $P(z) = a_n z^n + \cdots + a_1 z + a_0$ be a polynomial of degree $n \ge 1$ with real coefficients and $a_n > 0$.
Build rows of numbers as follows.
The first row is $(a_0, a_1, \dots, a_n)$.
If a row $(x_0, x_1, \dots, x_m)$ has $m \ge 3$, the next row is $(y_0, \dots, y_{m-1})$ with
$$y_k = x_0 x_k - x_m x_{m-k}, \qquad k = 0, 1, \dots, m-1.$$
Stop at the first row that has exactly $3$ entries; for $n \le 2$ only the first row is built.
Then $P$ is [[Schur stable|X11Q0G8PNA]] if and only if all of the following hold.

1. $P(1) > 0$.
2. $(-1)^n P(-1) > 0$.
3. $\abs{a_0} < a_n$.
4. Every row $(y_0, \dots, y_{m-1})$ built after the first satisfies $\abs{y_0} > \abs{y_{m-1}}$.

## Remarks

The proof rests on the Schur–Cohn reduction.
Write $P^*(z) = z^n P(1/z)$, so that $\abs{P^*(z)} = \abs{P(z)}$ on the unit circle because the coefficients are real.
When $\abs{a_0} < a_n$, [[Rouché's theorem|0D430QR02W]] shows that $P$ is Schur stable if and only if the polynomial $(a_n P(z) - a_0 P^*(z))/z$ of degree $n - 1$ is Schur stable.
The next row of the table lists the coefficients of this reduced polynomial in reverse order and with the opposite sign, so the table repeats the reduction until degree $2$.
The conditions 1 and 2 are necessary, since a real polynomial with $a_n > 0$ and no roots in $[1, \infty)$ or $(-\infty, -1]$ has the stated signs at $\pm 1$.
For $n = 2$ the criterion reads $\abs{a_0} < a_2$ and $\abs{a_1} < a_0 + a_2$.
For instance $z^2 - z + \tfrac{1}{2}$ passes: $\tfrac{1}{2} < 1$ and $1 < \tfrac{3}{2}$.
The polynomial $z^2 - \tfrac{5}{2} z + 1 = (z - 2)(z - \tfrac{1}{2})$ fails condition 1, since $P(1) = -\tfrac{1}{2}$.

## Explanations

### L1 human

The criterion decides whether all roots of a real polynomial lie inside the unit circle without finding the roots.
It checks a few signs and inequalities that come from simple products of the coefficients.
Engineers use it to see whether a digital filter or a sampled control loop is stable.

### L2 human

The criterion is the discrete-time analogue of the [[Routh–Hurwitz stability criterion|KJF8Y19BNV]], which tests whether roots lie in the left half-plane.
Combined with the stability theorem for linear recurrences, it decides from the coefficients whether every solution of a linear recurrence tends to zero.
A degree $n$ polynomial needs $n + 1$ conditions in total: three simple ones and $n - 2$ from the table.
When a parameter enters the coefficients, the conditions give the region of parameters where the system is stable.
