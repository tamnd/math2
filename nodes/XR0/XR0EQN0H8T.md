---
tag: XR0EQN0H8T
kind: statement
role: theorem
name: Hyperplanes and linear forms
msc: ["15A03", "15A04"]
topics: [9K7FFF26QR]
audience: ug2
about: [07YQ1C78G0]
uses: [07YQ1C78G0, 0S23E6YE83, 00YC1D652K, 0JMTY8MF54, 03GSZ8RTZJ]
sources:
  - url: https://en.wikipedia.org/wiki/Linear_form
    locator: Hyperplanes and maximal subspaces
  - url: https://en.wikipedia.org/wiki/Hyperplane
    locator: Vector hyperplanes
---

## Statement

The hyperplanes of a vector space are exactly the kernels of the nonzero linear forms, and the kernel fixes the form up to a nonzero scalar.
Let $F$ be a field and let $V$ be a vector space over $F$, of any dimension.
A *hyperplane* of $V$ is a [[subspace|00YC1D652K]] $H \ne V$ such that $V = H + Fv$ for some vector $v \in V$, where $+$ is the [[sum of subspaces|0JMTY8MF54]].
Let $V^*$ be the set of [[linear forms|07YQ1C78G0]] on $V$.

1. If $f \in V^*$ and $f \ne 0$, then the [[kernel|0S23E6YE83]] $\ker f$ is a hyperplane, and $V = \ker f \oplus Fv$ for every $v \in V$ with $f(v) \ne 0$.
2. Every hyperplane $H$ of $V$ equals $\ker f$ for some nonzero $f \in V^*$.
3. If $f, g \in V^*$, $f \ne 0$ and $\ker f \subseteq \ker g$, then $g = cf$ for exactly one $c \in F$.
4. If $f, g \in V^*$ are nonzero and $\ker f = \ker g$, then $g = cf$ for exactly one $c \in F$, and $c \ne 0$.
5. If $\dim V = n$ is finite and $n \ge 1$, then the hyperplanes of $V$ are exactly the subspaces of [[dimension|03GSZ8RTZJ]] $n - 1$.

## Remarks

### A plane in space and its equation

Take the plane $H \subseteq \mathbb{R}^3$ spanned by $u_1 = (1, 0, 1)$ and $u_2 = (0, 1, 2)$.
Part 2 promises a form $f(x, y, z) = ax + by + cz$ with kernel $H$, so we need $f(u_1) = 0$ and $f(u_2) = 0$:
$$a + c = 0, \qquad b + 2c = 0.$$
With $c = 1$ we get $a = -1$ and $b = -2$, so $f(x, y, z) = -x - 2y + z$.
Then $H \subseteq \ker f$, and both are planes of dimension $2$, so $H = \ker f$.
Every solution of the two equations is $t(-1, -2, 1)$, so the forms with kernel $H$ are exactly the multiples $tf$ with $t \ne 0$, as part 4 says.
Check: $f(1, 0, 1) = -1 + 1 = 0$ and $f(0, 1, 2) = -2 + 2 = 0$.

### Why each hypothesis is needed

The condition $f \ne 0$ in part 1 cannot go.
The kernel of the zero form is all of $V$, and $V$ is not a hyperplane.

In part 3 the condition $f \ne 0$ gives uniqueness.
If $f = 0$, then $\ker f = V \subseteq \ker g$ forces $g = 0$, and then $g = cf$ holds for every $c$.

The inclusion of kernels in part 3 is the heart of the matter.
On $\mathbb{R}^2$, the forms $f(x, y) = x$ and $g(x, y) = y$ have different kernels, and $g$ is not a multiple of $f$.

The map $g$ in part 3 must be linear.
The function $g(x, y) = x^2$ vanishes on $\ker f$ for $f(x, y) = x$, but it is not a multiple of $f$.

### What it gives you

In $F^n$, a hyperplane is the solution set of one nonzero linear equation $c_1 x_1 + \dots + c_n x_n = 0$, and that equation is unique up to a nonzero factor.
So the hyperplanes correspond one to one to the nonzero forms up to a nonzero scalar.
An affine hyperplane $\{v : f(v) = a\}$ with $f \ne 0$ is a translate of the hyperplane $\ker f$.

This correspondence lets us count.
Over the finite field $\mathbb{F}_q$, the space $\mathbb{F}_q^n$ has $q^n - 1$ nonzero forms, and each hyperplane is the kernel of exactly $q - 1$ of them, so the number of hyperplanes is
$$\frac{q^n - 1}{q - 1}.$$
For $q = 2$ and $n = 2$ this gives $3$, the three lines through the origin of $\mathbb{F}_2^2$.
For $q = 2$ and $n = 3$ it gives $7$ planes in $\mathbb{F}_2^3$.

### The converse

The converse of part 3 holds.
If $g = cf$ and $f(v) = 0$, then $g(v) = c \cdot 0 = 0$, so $\ker f \subseteq \ker g$.
Part 2 is the converse of part 1.

### Generalizations

The same idea works with several forms.
If $f_1, \dots, f_k, g \in V^*$ and $\ker f_1 \cap \dots \cap \ker f_k \subseteq \ker g$, then $g$ is a linear combination of $f_1, \dots, f_k$.
This follows from the [[kernel and image of the dual map|7FA499AW3T]], applied to the map $v \mapsto (f_1(v), \dots, f_k(v))$ from $V$ to $F^k$.

In any dimension, the hyperplanes are the subspaces of codimension $1$, that is, the subspaces $H$ with $\dim V/H = 1$.
The sub-area on [[direct sums and quotient spaces|QHKTJ89V6S]] studies codimension with quotient spaces.
In a normed space, the kernel of a nonzero linear form is closed exactly when the form is continuous, a fact from functional analysis.

## Explanations

### L1 human

In ordinary space, a plane through the origin is the set of points where one linear expression is zero.
For example, the plane $x + 2y - z = 0$ is the kernel of the form $(x, y, z) \mapsto x + 2y - z$.
The form $(x, y, z) \mapsto 3x + 6y - 3z$ gives the same plane, because it is $3$ times the first form.
The theorem says that this is the only freedom.
The equation of a plane through the origin is fixed up to a nonzero factor.

### L2 human

Here is a typical question: do the equations $2x - 4y + 6z = 0$ and $-x + 2y - 3z = 0$ describe the same plane in $\mathbb{R}^3$?
The first form is $-2$ times the second, since $-2 \cdot (-1, 2, -3) = (2, -4, 6)$.
So the two kernels agree by the converse of part 3, and the planes are the same.
Now compare $x - 2y + 3z = 0$ with $x - 2y + 4z = 0$.
The rows $(1, -2, 3)$ and $(1, -2, 4)$ are not proportional, so by part 4 the kernels differ.
Check: the vector $(3, 0, -1)$ lies on the first plane, since $3 - 0 - 3 = 0$, but not on the second, since $3 - 0 - 4 = -1$.
This is the typical use of the theorem: a question about two planes becomes a question about two rows of numbers.
Watch out: "the" equation of a hyperplane is not unique, so two equations that look different can still give the same hyperplane.

### L3 human

The theorem says that the hyperplanes of $V$ are the points of the projective space $\mathbb{P}(V^*)$.
This is the start of projective duality, in which the points of $\mathbb{P}(V)$ and the hyperplanes of $\mathbb{P}(V)$ exchange roles.
Part 3 is the case $k = 1$ of the statement about several forms above.
That statement is the algebra behind Lagrange multipliers, where the gradient of the objective lies in the span of the gradients of the constraints.
In a normed space the same theorem holds for continuous forms and closed hyperplanes, and the Hahn-Banach theorem supplies enough continuous forms.
