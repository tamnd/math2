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

Let $F$ be a field and let $V$ be a vector space over $F$, of any dimension.
A *hyperplane* of $V$ is a [[subspace|00YC1D652K]] $H \ne V$ such that $V = H + Fv$ for some vector $v \in V$, where $+$ is the [[sum of subspaces|0JMTY8MF54]].
Let $V^*$ be the set of [[linear forms|07YQ1C78G0]] on $V$.

1. If $f \in V^*$ and $f \ne 0$, then the [[kernel|0S23E6YE83]] $\ker f$ is a hyperplane. In fact, $V = \ker f \oplus Fv$ for every $v \in V$ with $f(v) \ne 0$.
2. Every hyperplane $H$ of $V$ is $\ker f$ for some nonzero $f \in V^*$.
3. Let $f, g \in V^*$ with $f \ne 0$ and $\ker f \subseteq \ker g$. Then $g = cf$ for exactly one $c \in F$.
4. In particular, two nonzero linear forms with the same kernel are proportional: $g = cf$ with $c \ne 0$.
5. If $\dim V = n$ is finite and $n \ge 1$, then the hyperplanes of $V$ are exactly the subspaces of [[dimension|03GSZ8RTZJ]] $n - 1$.

## Remarks

### Why each hypothesis is needed

- In part 1, $f \ne 0$ is needed: the kernel of the zero form is $V$, and $V$ is not a hyperplane.
- In part 3, $f \ne 0$ is needed for uniqueness. If $f = 0$, then $\ker f = V \subseteq \ker g$ forces $g = 0$, and $g = cf$ for every $c$.
- In part 3, the inclusion of kernels is needed. On $\R^2$, the forms $f(x, y) = x$ and $g(x, y) = y$ have different kernels, and $g$ is not a multiple of $f$.
- In part 3, $g$ must be linear. The map $g(x, y) = x^2$ vanishes on $\ker f$ for $f(x, y) = x$, but it is not a multiple of $f$.

### Consequences

- In $F^n$, a hyperplane is the solution set of one nonzero linear equation $c_1 x_1 + \dots + c_n x_n = 0$. The equation is unique up to a nonzero factor.
- Call two nonzero forms equivalent when one is a nonzero multiple of the other. Then $f \mapsto \ker f$ gives a bijection from the equivalence classes onto the hyperplanes.
- Over the finite field $\F_q$, the space $\F_q^n$ has $q^n - 1$ nonzero forms, and each hyperplane is the kernel of exactly $q - 1$ of them. So $\F_q^n$ has $(q^n - 1)/(q - 1)$ hyperplanes. For $q = 2$ and $n = 2$, this gives the $3$ lines through the origin of $\F_2^2$.
- An affine hyperplane $\set{v : f(v) = a}$ with $f \ne 0$ is a translate of the hyperplane $\ker f$.

### Converse

The converse of part 3 holds: if $g = cf$, then $f(v) = 0$ gives $g(v) = c \cdot 0 = 0$, so $\ker f \subseteq \ker g$.
The converse of part 1 is part 2.

### Generalizations

- If $f_1, \dots, f_k, g \in V^*$ and $\ker f_1 \cap \dots \cap \ker f_k \subseteq \ker g$, then $g$ is a linear combination of $f_1, \dots, f_k$. This follows from the [[kernel and image of the dual map|7FA499AW3T]] applied to $v \mapsto (f_1(v), \dots, f_k(v))$.
- In any dimension, the hyperplanes are the subspaces of codimension $1$, that is, the subspaces $H$ with $\dim V/H = 1$. The codimension is studied with quotient spaces in the sub-area on [[direct sums and quotient spaces|QHKTJ89V6S]].
- In a normed space, the kernel of a nonzero linear form is closed exactly when the form is continuous. This belongs to functional analysis.

## Explanations

### L1 human

In ordinary space, a plane through the origin is the set of points where one linear expression is zero.
For example, the plane $x + 2y - z = 0$ is the kernel of the form $(x, y, z) \mapsto x + 2y - z$.
The form $(x, y, z) \mapsto 3x + 6y - 3z$ gives the same plane, because it is $3$ times the first form.
The theorem says that this is the only freedom: the equation of a plane through the origin is fixed up to a nonzero factor.

### L2 human

We find the form of a hyperplane and check the uniqueness on an example.

1. Let $H \subseteq \R^3$ be spanned by $u_1 = (1, 0, 1)$ and $u_2 = (0, 1, 2)$.
2. We look for $f(x, y, z) = ax + by + cz$ with $f(u_1) = a + c = 0$ and $f(u_2) = b + 2c = 0$.
3. With $c = 1$, we get $a = -1$ and $b = -2$. So $f(x, y, z) = -x - 2y + z$, and $H \subseteq \ker f$.
4. Both $H$ and $\ker f$ have dimension $2$, so $H = \ker f$.
5. Every other solution of step 2 is $(a, b, c) = t(-1, -2, 1)$, so every form with kernel $H$ is $t f$ with $t \ne 0$.

The typical use is to pass between a geometric object, the hyperplane, and an algebraic one, the form up to a scalar.
A trap: "the" equation of a hyperplane is not unique, so two equations that look different can give the same hyperplane.

### L3 human

The theorem says that the hyperplanes of $V$ are the points of the projective space $\mathbb{P}(V^*)$.
This is the start of projective duality, where points of $\mathbb{P}(V)$ and hyperplanes of $\mathbb{P}(V)$ exchange roles.
Part 3 is the case $k = 1$ of a general fact: a form that vanishes on the common kernel of $f_1, \dots, f_k$ lies in their span.
This fact is the algebraic core of the method of Lagrange multipliers, where the gradient of the objective lies in the span of the gradients of the constraints.
In a normed space, the same theorem holds for continuous forms and closed hyperplanes, and the Hahn-Banach theorem gives enough of them.
