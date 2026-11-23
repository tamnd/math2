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

On the plane $\mathbb{R}^2$, define
$$(x_1, y_1) \sim (x_2, y_2) \iff x_1^2 + y_1^2 = x_2^2 + y_2^2,$$
so two points are related when they have the same [[Euclidean distance|0NPPGHQNXQ]] from the origin.
We prove that $\sim$ is an [[equivalence relation|0G8VEZ3WTK]] in two ways, as in [[proving a relation is an equivalence relation|RGNF33GVHX]], and then find its classes.

1. Reflexivity: for $p = (x, y)$, the number $x^2 + y^2$ equals itself, so $p \sim p$.
2. Symmetry: if $x_1^2 + y_1^2 = x_2^2 + y_2^2$, then $x_2^2 + y_2^2 = x_1^2 + y_1^2$, because equality of numbers is symmetric.
3. Transitivity: if $x_1^2 + y_1^2 = x_2^2 + y_2^2$ and $x_2^2 + y_2^2 = x_3^2 + y_3^2$, then $x_1^2 + y_1^2 = x_3^2 + y_3^2$, because equality of numbers is transitive.
4. The function route: put $f(x, y) = x^2 + y^2$.
   Then $p \sim q$ exactly when $f(p) = f(q)$, so $\sim$ is the [[equivalence relation induced by a function|0KT8TGXD8K]] and needs no further checks.
5. The class of the origin is $\{(0, 0)\}$, because $x^2 + y^2 = 0$ forces $x = y = 0$.
6. For $p \ne (0, 0)$ with $f(p) = r^2$ and $r > 0$, the class of $p$ is the circle of radius $r$ about the origin.
   So the origin and these circles form a [[partition|08QMKTWF9T]] of the plane.

Check: $(3, 4) \sim (5, 0)$, because $9 + 16 = 25 = 25 + 0$, and both points lie on the circle of radius $5$.

## Remarks

Steps 1 to 3 repeat the properties of equality three times.
Step 4 says it once: a relation of the form $f(p) = f(q)$ inherits all three properties from equality, and its classes are the non-empty level sets $f^{-1}(\{c\})$.
The same route shows at once that "has the same determinant", "has the same remainder modulo $n$" and "has the same length" are equivalence relations.

Replace "$=$" by "$\le$" and symmetry breaks.
The relation $f(p) \le f(q)$ is reflexive and transitive, but $(0, 0)$ is related to $(1, 0)$ while $(1, 0)$ is not related to $(0, 0)$.

## Explanations

### L1 human

Two points are related when they are equally far from the center.
All the points on one circle around the center are related to each other.
The tests for an equivalence relation pass because "equally far" is a kind of "equal".
So the plane splits into circles around the center, plus the center itself.
The point three steps right and four steps up is five steps from the center, just like the point five steps right.

### L2 human

We use the function route for $x \sim y \iff \lfloor x \rfloor = \lfloor y \rfloor$ on $\mathbb{R}$, where $\lfloor x \rfloor$ is the largest integer at most $x$.

1. The relation reads "$f(x) = f(y)$" with $f(x) = \lfloor x \rfloor$, so it is an equivalence relation with no further checks.
2. The class of $2.5$ is the set of $y$ with $\lfloor y \rfloor = 2$, the interval $[2, 3)$.
3. In general the classes are the intervals $[k, k + 1)$ for $k \in \mathbb{Z}$, and they partition $\mathbb{R}$.

The route fits relations that compare one quantity of two objects, such as a length, a remainder or an invariant.
Watch out: a relation that compares the quantity only approximately, such as $\lvert f(x) - f(y) \rvert \le 1$, is not of the form $f(x) = f(y)$, and it can fail transitivity.
