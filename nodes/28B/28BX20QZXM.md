---
tag: 28BX20QZXM
kind: proof
name: Proof of the triangle inequality for the induced norm
msc: ["15A63", "46C05"]
topics: [1D4JTZ9VS3]
audience: ug1
proves: SRN4T2G6AM
methods: [0NTF6DMVAP, 0WCP0PVET6]
uses: [0RFWW56Y22, 0KG4D8AP6G, 08NYZ2FS6B, 063W5JMY85, 0KW2X0TFBX, 0EVHJFTG9Z]
sources:
  - url: https://en.wikipedia.org/wiki/Inner_product_space
    locator: Norm properties
  - book: isbn:9783031410253
    locator: Chapter 6
---

## Proof

We expand $\norm{x + y}^2$, bound the cross term with the Cauchy-Schwarz inequality, and take square roots; then we trace the equality case back through each step.
Let $V$ be an inner product space over $\mathbb{K} = \mathbb{R}$ or $\mathbb{C}$, linear in the first slot and conjugate-linear in the second, and let $x, y \in V$.
For a complex number $z$ we write $\operatorname{Re} z$ for its real part.

*The inequality.*

1. Linearity in the first slot and conjugate-linearity in the second give
$$\norm{x + y}^2 = \ip{x + y}{x + y} = \ip{x}{x} + \ip{x}{y} + \ip{y}{x} + \ip{y}{y}.$$
2. Conjugate symmetry gives $\ip{y}{x} = \overline{\ip{x}{y}}$, and $z + \overline{z} = 2\operatorname{Re} z$ for every complex $z$, so
$$\norm{x + y}^2 = \norm{x}^2 + 2\operatorname{Re}\ip{x}{y} + \norm{y}^2.$$
3. For $z = a + bi$ with $a, b$ real, $\operatorname{Re} z = a \leq \sqrt{a^2 + b^2} = \abs{z}$, where $\abs{z}$ is the [[modulus|0KW2X0TFBX]].
   Equality holds exactly when $b = 0$ and $a \geq 0$, that is, when $z$ is real and $z \geq 0$.
4. The [[Cauchy-Schwarz inequality|0RFWW56Y22]] gives $\abs{\ip{x}{y}} \leq \norm{x}\,\norm{y}$, so step 3 gives
$$\operatorname{Re}\ip{x}{y} \leq \abs{\ip{x}{y}} \leq \norm{x}\,\norm{y}.$$
5. Put step 4 into step 2:
$$\norm{x + y}^2 \leq \norm{x}^2 + 2\norm{x}\,\norm{y} + \norm{y}^2 = \big(\norm{x} + \norm{y}\big)^2.$$
6. Both $\norm{x + y}$ and $\norm{x} + \norm{y}$ are at least $0$, and the square root is increasing on $[0, \infty)$.
   So $\norm{x + y} \leq \norm{x} + \norm{y}$, which is part 1.

*The equality case.*

7. Suppose that $\norm{x + y} = \norm{x} + \norm{y}$.
   Then the squares are equal, and step 2 gives $\operatorname{Re}\ip{x}{y} = \norm{x}\,\norm{y}$.
8. So both inequalities of step 4 are equalities.
   Hence $\abs{\ip{x}{y}} = \norm{x}\,\norm{y}$, and $\ip{x}{y}$ is real and at least $0$ by step 3.
9. The equality case of the Cauchy-Schwarz inequality now says that $x$ and $y$ are [[linearly dependent|0EVHJFTG9Z]].
10. If $y = 0$ we are done.
    If $y \neq 0$, a relation $\alpha x + \beta y = 0$ with $\alpha = 0$ would force $\beta y = 0$ with $\beta \neq 0$, so $\alpha \neq 0$ and $x = cy$ for the scalar $c = -\beta / \alpha$.
11. Then $\ip{x}{y} = c\norm{y}^2$.
    This number is real and at least $0$ by step 8, and $\norm{y}^2 > 0$, so $c$ is real and $c \geq 0$.
12. Conversely, if $y = 0$ both sides equal $\norm{x}$.
    If $x = cy$ with real $c \geq 0$, homogeneity (step 13 below) gives $\norm{x + y} = (c + 1)\norm{y} = c\norm{y} + \norm{y} = \norm{x} + \norm{y}$.
    This proves part 2.

*The norm and the metric.*

13. Homogeneity: for a scalar $a$,
$$\norm{ax}^2 = \ip{ax}{ax} = a\overline{a}\ip{x}{x} = \abs{a}^2\norm{x}^2,$$
    and both $\norm{ax}$ and $\abs{a}\,\norm{x}$ are at least $0$, so $\norm{ax} = \abs{a}\,\norm{x}$.
14. Definiteness: if $\norm{x} = 0$, then $\ip{x}{x} = 0$, so $x = 0$ by positive definiteness.
    With part 1, steps 13 and 14 give every axiom of a [[norm|08NYZ2FS6B]], so the [[induced norm|0KG4D8AP6G]] is a norm.
15. For $d(x, y) = \norm{x - y}$, step 14 gives $d(x, y) = 0$ only for $x = y$, and step 13 with $a = -1$ gives $d(y, x) = d(x, y)$.
16. Part 1 gives $d(x, z) = \norm{(x - y) + (y - z)} \leq d(x, y) + d(y, z)$.
    So $d$ is a [[metric|063W5JMY85]], which proves part 3.

## Idea

The square of $\norm{x + y}$ is $\norm{x}^2 + \norm{y}^2$ plus a cross term $2\operatorname{Re}\ip{x}{y}$.
The Cauchy-Schwarz inequality bounds that cross term by $2\norm{x}\,\norm{y}$, which is exactly the cross term of $(\norm{x} + \norm{y})^2$.
For equality, both bounds in the chain must be tight.
The Cauchy-Schwarz bound is tight only for dependent vectors, and the bound $\operatorname{Re} z \leq \abs{z}$ is tight only for real $z \geq 0$, which forces the factor $c$ to be real and nonnegative.

## Variants

In $\mathbb{R}^2$ and $\mathbb{R}^3$ the inequality is a fact of plane geometry: one side of a triangle is shorter than the sum of the other two.
The proof above does not use the picture, so it works in every inner product space.
For a general norm the triangle inequality is an axiom, so there is nothing to prove, and the page on the [[triangle inequality for norms|0FJZMBX0ZZ]] derives the reverse form from it.
