---
tag: C8S7XX0VZM
kind: statement
role: proposition
name: Bairstow's method
msc: [65H04]
uses: [07EXVNF9VP, D6D0SR1FK3, 047NDTEPCV, 019MA1VTR2]
about: [019MA1VTR2]
sources:
  - url: https://en.wikipedia.org/wiki/Bairstow%27s_method
same_as:
  wikidata: Q384021
  wikipedia: Bairstow's method
---

## Statement

Let $p$ be a polynomial of degree $n \ge 3$ with real coefficients, and let $u, v$ be real numbers.
By [[polynomial long division|D6D0SR1FK3]] by $B(x) = x^2 + ux + v$, write
$$p(x) = B(x) \, q(x) + c x + d, \qquad q(x) = B(x) \, s(x) + g x + h,$$
where $q$ and $s$ are polynomials and $c, d, g, h$ are real numbers that depend on $(u, v)$.
Then $c$ and $d$ are polynomial functions of $(u, v)$ with partial derivatives
$$\frac{\partial c}{\partial u} = ug - h, \quad \frac{\partial c}{\partial v} = -g, \quad \frac{\partial d}{\partial u} = vg, \quad \frac{\partial d}{\partial v} = -h.$$
The step of *Bairstow's method* is
$$\begin{pmatrix} u \\ v \end{pmatrix} \mapsto \begin{pmatrix} u \\ v \end{pmatrix} - \frac{1}{vg^2 + h(h - ug)} \begin{pmatrix} -h & g \\ -vg & ug - h \end{pmatrix} \begin{pmatrix} c \\ d \end{pmatrix}.$$
It is one step of [[Newton's method|07EXVNF9VP]] for the system $c(u, v) = 0$, $d(u, v) = 0$.
The solutions of this system are the pairs $(u, v)$ for which $x^2 + ux + v$ divides $p$.

## Remarks

Differentiate $p = Bq + cx + d$ with respect to $v$: $0 = q + B \, \partial_v q + (\partial_v c) x + \partial_v d$.
So $q$ leaves the remainder $-(\partial_v c) x - \partial_v d$ on division by $B$, which gives $\partial_v c = -g$ and $\partial_v d = -h$.
Differentiating with respect to $u$ gives that $x q(x)$ leaves the remainder $-(\partial_u c) x - \partial_u d$; since $x(gx + h) \equiv (h - ug) x - vg$ modulo $B$, this gives the other two derivatives.
The $2 \times 2$ matrix in the step is the inverse of the [[Jacobian matrix|047NDTEPCV]] of $(c, d)$, times its determinant $vg^2 + h(h - ug)$.
So, when this Jacobian is invertible at a quadratic factor, the method converges quadratically from nearby starting values.
A quadratic factor gives two [[roots|019MA1VTR2]] of $p$ by the quadratic formula, which may be a pair of complex conjugate roots, all in real arithmetic.

## Explanations

### L1 human

A real polynomial can have complex roots, which come in conjugate pairs.
Each pair is the pair of roots of a real quadratic factor $x^2 + ux + v$.
Bairstow's method searches for such a factor directly, by adjusting $u$ and $v$ until the division of $p$ by $x^2 + ux + v$ leaves no remainder.

### L2 human

All the work is two synthetic divisions per step, so it is cheap.
After a factor is found, one divides it out and repeats on the quotient of degree $n - 2$.
Like Newton's method, it needs good starting values and converges only linearly at multiple factors.
