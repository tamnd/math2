---
tag: RY425WPK6N
kind: statement
role: theorem
name: Fenchel's duality theorem
msc: [90C46, 49N15, 52A41]
uses: [T7V2VPY61S, 07Q7CNM5WF, 0RZH6W98HK]
about: [T7V2VPY61S]
sources:
  - url: https://en.wikipedia.org/wiki/Fenchel%27s_duality_theorem
same_as:
  wikidata: Q5443003
  wikipedia: Fenchel's duality theorem
---

## Statement

Let $f \colon \R^n \to (-\infty, +\infty]$ and $g \colon \R^m \to (-\infty, +\infty]$ be [[convex functions|07Q7CNM5WF]], and let $A$ be a real $m \times n$ matrix.
Write $\operatorname{dom} f = \set{x : f(x) < \infty}$, and let $f^*$ and $g^*$ be the [[Fenchel conjugates|T7V2VPY61S]] of $f$ and $g$.
Let
$$p = \inf_{x \in \R^n} \big( f(x) + g(Ax) \big), \qquad d = \sup_{y \in \R^m} \big( -f^*(A^{T} y) - g^*(-y) \big).$$
Then $d \le p$.
If moreover $0$ lies in the [[interior|0RZH6W98HK]] of the set $\operatorname{dom} g - A \operatorname{dom} f = \set{z - Ax : z \in \operatorname{dom} g,\ x \in \operatorname{dom} f}$, then $p = d$, and the supremum is attained when it is finite.

## Remarks

The inequality $d \le p$ follows from the [[Fenchel–Young inequality|NSTD00PJPE]]: $f(x) + f^*(A^{T}y) \ge \ip{A^{T}y}{x}$ and $g(Ax) + g^*(-y) \ge -\ip{y}{Ax}$, and the two right sides cancel.
Equality comes from separating a convex set by a hyperplane, or from the convexity of the value function $v(u) = \inf_x (f(x) + g(Ax + u))$; the interior condition makes $v$ continuous at $0$.
The theorem is a form of Lagrangian duality for the problem $\min f(x) + g(z)$ subject to $z = Ax$.
With $A = I$ and under the interior condition, a common form says $\inf (f + g) = \max_y \big( -f^*(y) - g^*(-y) \big)$.

Example: $n = m = 1$, $A = 1$, $f(x) = x^2/2$, $g(x) = (x - 1)^2/2$.
Then $p = 1/4$, attained at $x = 1/2$.
One computes $f^*(y) = y^2/2$ and $g^*(z) = z + z^2/2$, so $d = \sup_y (y - y^2) = 1/4$.

Without the interior condition the dual supremum can fail to be attained.
Take $n = m = 1$, $A = 1$, $f(x) = -\sqrt{x}$ for $x \ge 0$ and $f(x) = +\infty$ for $x < 0$, and $g$ equal to $0$ at $0$ and $+\infty$ elsewhere.
Then $\operatorname{dom} g - \operatorname{dom} f = (-\infty, 0]$, which does not contain $0$ in its interior, and $p = f(0) = 0$.
One finds $g^* = 0$, $f^*(y) = -1/(4y)$ for $y < 0$ and $f^*(y) = +\infty$ for $y \ge 0$.
So $d = \sup_{y < 0} 1/(4y) = 0$, but no $y$ attains it.

## Explanations

### L1 human

The theorem gives a second way to compute the minimum of a sum of two convex functions.
Instead of the functions, one uses their conjugates, which describe them by their supporting lines.
Under a mild overlap condition the two ways give the same number.

### L2 human

Fenchel duality is the convex-analysis form of linear programming duality and contains it as a special case.
It is the basis of many first-order algorithms, which work on the dual problem when the conjugates are simpler.
It connects to the [[Fenchel–Moreau theorem|XZFYB2PBPD]], which says that a closed convex function is its own biconjugate.
