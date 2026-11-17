---
tag: VA8BKK7M32
kind: example
name: Points at the same distance from the origin
msc: ["00A35", "03E20"]
topics: [MEKKHHQTKB]
audience: ug1
instance_of: [RGNF33GVHX]
uses: [RGNF33GVHX, 0G8VEZ3WTK, 0KT8TGXD8K, 08QMKTWF9T, 0NPPGHQNXQ]
sources:
  - url: https://en.wikipedia.org/wiki/Equivalence_relation
    locator: Definition
  - url: https://en.wikipedia.org/wiki/Kernel_(set_theory)
    locator: lead section
---

## Example

On the plane $\mathbb{R}^2$, define the relation
$$(x_1, y_1) \sim (x_2, y_2) \iff x_1^2 + y_1^2 = x_2^2 + y_2^2.$$
So two points are related when they have the same [[Euclidean distance|0NPPGHQNXQ]] from the origin $(0, 0)$.
We prove that $\sim$ is an [[equivalence relation|0G8VEZ3WTK]] in two ways, as in [[proving a relation is an equivalence relation|RGNF33GVHX]].

First proof, by the three checks.

1. Reflexivity. For each point $p = (x, y)$, the number $x^2 + y^2$ equals itself, so $p \sim p$.
2. Symmetry. If $p_1 \sim p_2$, then $x_1^2 + y_1^2 = x_2^2 + y_2^2$. Equality of real numbers is symmetric, so $x_2^2 + y_2^2 = x_1^2 + y_1^2$, and $p_2 \sim p_1$.
3. Transitivity. If $p_1 \sim p_2$ and $p_2 \sim p_3$, then $x_1^2 + y_1^2 = x_2^2 + y_2^2$ and $x_2^2 + y_2^2 = x_3^2 + y_3^2$. Equality of real numbers is transitive, so $x_1^2 + y_1^2 = x_3^2 + y_3^2$, and $p_1 \sim p_3$.

Second proof, by a function.

4. Define $f \colon \mathbb{R}^2 \to \mathbb{R}$ by $f(x, y) = x^2 + y^2$.
5. By the definition of $\sim$, we have $p_1 \sim p_2$ if and only if $f(p_1) = f(p_2)$.
6. So $\sim$ is the [[equivalence relation induced by a function|0KT8TGXD8K]] $f$, and it is an equivalence relation.

The classes and the [[partition|08QMKTWF9T]]:

7. The class of the origin is $\{(0, 0)\}$, because $x^2 + y^2 = 0$ forces $x = y = 0$.
8. For $p \neq (0, 0)$ with $f(p) = r^2$ and $r > 0$, the class of $p$ is the circle of radius $r$ about the origin.
9. So the classes are the origin and the circles about the origin, and these sets partition the plane.

A check with numbers: $(3, 4) \sim (5, 0)$, because $9 + 16 = 25 = 25 + 0$.
Both points lie on the circle of radius $5$.

## Remarks

1. The first proof only repeats the properties of equality three times. The second proof says this once: a relation of the form "$f(p) = f(q)$" inherits the three properties of equality.
2. The function route also gives the classes at once: they are the non-empty sets $f^{-1}(\{c\})$, the level sets of $f$.
3. If we replace "$=$" by "$\le$", the relation $f(p_1) \le f(p_2)$ is reflexive and transitive but not symmetric: $(0, 0)$ is related to $(1, 0)$, and $(1, 0)$ is not related to $(0, 0)$.
4. The same pattern shows that "has the same determinant", "has the same remainder modulo $n$" and "has the same length" are equivalence relations.

## Explanations

### L1 human

Two points are related when they are equally far from the centre point.
All the points on one circle around the centre are related to each other.
The tests for an equivalence relation hold because "equally far" is a kind of "equal".
So the plane splits into circles around the centre, plus the centre itself.
For example, the point three steps right and four steps up is five steps from the centre, just like the point five steps right.

### L2 human

We use the function route for the relation on $\mathbb{R}$ given by $x \sim y \iff \lfloor x \rfloor = \lfloor y \rfloor$, where $\lfloor x \rfloor$ is the largest integer at most $x$.

1. The function $f(x) = \lfloor x \rfloor$ is defined on all of $\mathbb{R}$.
2. The relation is "$f(x) = f(y)$", so it is an equivalence relation, with no further checks.
3. The class of $x$ is the set of $y$ with $\lfloor y \rfloor = \lfloor x \rfloor$. For $x = 2.5$ it is the interval $[2, 3)$.
4. The classes are the intervals $[k, k + 1)$ for $k \in \mathbb{Z}$, and they partition $\mathbb{R}$.

The typical use of the function route is a relation that compares one quantity, such as a length, a remainder or an invariant, of two objects.
A trap is to apply the route to a relation that compares the quantity only approximately, such as $\lvert f(x) - f(y) \rvert \le 1$, which is not of the form $f(x) = f(y)$.
