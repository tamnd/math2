---
tag: FFTNS66XG6
kind: example
name: Discontinuous additive functions via a Hamel basis
msc: ["39B22", "15A03"]
topics: [MVH97H8B2J]
instance_of: [KF719SZD5T]
uses: [0KCQ9Y3QKA, 0HTGB13FE2, 0X3WGX95FE]
sources:
  - url: https://en.wikipedia.org/wiki/Cauchy%27s_functional_equation
    locator: Existence of nonlinear solutions over the real numbers
---

## Example

View $\mathbb{R}$ as a vector space over the field $\mathbb{Q}$ of rational numbers.
The numbers $1$ and $\sqrt{2}$ are linearly independent over $\mathbb{Q}$, because a relation $a + b\sqrt{2} = 0$ with $b \ne 0$ would make $\sqrt{2} = -a/b$ rational.
With the [[axiom of choice|0HTGB13FE2]], this independent set extends to a [[basis|0KCQ9Y3QKA]] $B$ of $\mathbb{R}$ over $\mathbb{Q}$, a [[Hamel basis|ZCBD0GRGVA]] that contains $1$ and $\sqrt{2}$.
Every real $x$ is then, in exactly one way, a finite sum
$$x = \sum_{b \in B} q_b(x)\, b$$
with rational coefficients $q_b(x)$, all but finitely many equal to $0$.
Define $f \colon \mathbb{R} \to \mathbb{R}$ by $f(x) = q_1(x)$, the coefficient of the basis vector $1$.
We check that $f$ is additive and not continuous.

1. Additivity. Adding the expansions of $x$ and $y$ gives an expansion of $x + y$, and expansions are unique, so $q_b(x + y) = q_b(x) + q_b(y)$ for every $b$. In particular $f(x + y) = f(x) + f(y)$, so $f$ is an [[additive function|KF719SZD5T]].
2. Two values. The expansion of $1$ is $1 \cdot 1$, so $f(1) = 1$. The expansion of $\sqrt{2}$ is $1 \cdot \sqrt{2}$, with coefficient $0$ at the vector $1$, so $f(\sqrt{2}) = 0$.
3. Not linear. If $f(x) = cx$ for a constant $c$, then $f(1) = 1$ forces $c = 1$, and then $f(\sqrt{2})$ would be $\sqrt{2}$, not $0$.
4. Not [[continuous|0X3WGX95FE]]. A continuous additive function on $\mathbb{R}$ has the form $f(x) = cx$, so step 3 rules out continuity.
5. A direct check. The function $f$ takes only rational values. A continuous function on $\mathbb{R}$ with only rational values is constant, by the intermediate value theorem, but $f(0) = 0$ and $f(1) = 1$.

## Remarks

The function $f$ is $\mathbb{Q}$-linear, so $f(qx) = q f(x)$ for every rational $q$, but it is not $\mathbb{R}$-linear.
This is the general picture: the additive functions $\mathbb{R} \to \mathbb{R}$ are exactly the $\mathbb{Q}$-linear maps, and the continuous ones are exactly the $\mathbb{R}$-linear maps $x \mapsto cx$.

Changing the chosen coordinate changes the function but not the conclusion.
Reading off the coefficient of $\sqrt{2}$ instead gives an additive $g$ with $g(1) = 0$ and $g(\sqrt{2}) = 1$, and it fails linearity in the same way.
Any $\mathbb{Q}$-linear map is fixed by its values on $B$, and these values can be chosen freely, so there are many such functions.

The example needs a Hamel basis, and that is not an accident.
In Zermelo-Fraenkel set theory without choice it is consistent that every additive function $\mathbb{R} \to \mathbb{R}$ is continuous, so some form of choice is needed to build $f$.

## Explanations

### L1 human

Imagine writing every real number in a strange coordinate system with rational coordinates.
The function $f$ just reads off one coordinate, the one that belongs to the number $1$.
Reading a coordinate respects addition, so $f(x + y) = f(x) + f(y)$.
But $f(1) = 1$ and $f(\sqrt{2}) = 0$, so $f$ is not a straight line through the origin.
Its graph is so scattered that it cannot be drawn.

### L2 human

Why does additivity force $f(q) = q f(1)$ for rational $q$, but nothing more?
From $f(x + y) = f(x) + f(y)$, induction gives $f(nx) = n f(x)$ for $n \ge 1$.
Since $f(0) = f(0) + f(0)$ gives $f(0) = 0$, and $f(x) + f(-x) = f(0)$, the rule holds for all integers $n$.
Put $x = \tfrac{m}{n}$ to get $n f(\tfrac{m}{n}) = f(m) = m f(1)$, so $f(\tfrac{m}{n}) = \tfrac{m}{n} f(1)$.
For the example, $f(1) = 1$, so $f$ agrees with the identity on every rational number.
To reach irrational numbers you would need a limit, and a limit needs continuity, which $f$ does not have.
Watch out: every additive function is $\mathbb{Q}$-linear, so the step from additive to linear over $\mathbb{R}$ is exactly where an extra hypothesis such as continuity is needed.
