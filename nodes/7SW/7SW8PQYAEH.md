---
tag: 7SW8PQYAEH
kind: proof
name: Proof of the Cauchy-Schwarz inequality by the discriminant of a quadratic
msc: ["15A63", "46C05"]
topics: [1D4JTZ9VS3]
audience: ug1
proves: 0RFWW56Y22
methods: [0NTF6DMVAP, 0WCP0PVET6]
uses: [01EK923SKP, 0VGSYBWHV2, 0KG4D8AP6G, XNCV97HTZ8, 0VVK64Q4JK, 0KW2X0TFBX, 0GMV7GP8W0, 0EVHJFTG9Z]
sources:
  - url: https://en.wikipedia.org/wiki/Cauchy–Schwarz_inequality
    locator: Proof by analyzing a quadratic
  - book: isbn:9780134860244
    locator: Chapter 6
---

## Proof

We rotate $y$ so that its inner product with $x$ becomes a nonnegative real number, and then we use that a real quadratic which is never negative has a discriminant that is not positive.
Let $V$ be an [[inner product space|01EK923SKP]] over $\mathbb{K} = \mathbb{R}$ or $\mathbb{C}$, and let $x, y \in V$.
Over $\mathbb{R}$ every conjugate below does nothing, so the proof covers both cases.

1. First let $y = 0$.
Conjugate-linearity in the second slot gives $\ip{x}{0} = \ip{x}{0 \cdot 0} = 0 \cdot \ip{x}{0} = 0$, and $\norm{0} = 0$.
So both sides are $0$, and equality holds.
2. In this case $x$ and $y$ are [[linearly dependent|0EVHJFTG9Z]], because $0 \cdot x + 1 \cdot y = 0$.
So the theorem holds when $y = 0$.
3. From now on let $y \neq 0$.
Then $\norm{y}^2 = \ip{y}{y} > 0$, by positive definiteness of the [[inner product|0VGSYBWHV2]].
4. Choose a scalar $\lambda$ as follows: $\lambda = \ip{x}{y} / \abs{\ip{x}{y}}$ if $\ip{x}{y} \neq 0$, and $\lambda = 1$ otherwise.
Over $\mathbb{R}$ this $\lambda$ is $1$ or $-1$.
5. In both cases $\abs{\lambda} = 1$ and $\overline{\lambda}\ip{x}{y} = \abs{\ip{x}{y}}$, because $\overline{\ip{x}{y}}\,\ip{x}{y} = \abs{\ip{x}{y}}^2$ by the rules of the [[modulus|0KW2X0TFBX]].
6. Put $w = \lambda y$ and $m = \abs{\ip{x}{y}}$.
Conjugate-linearity in the second slot and step 5 give $\ip{x}{w} = \overline{\lambda}\ip{x}{y} = m$.
By conjugate symmetry $\ip{w}{x} = \overline{m} = m$, since $m$ is real.
7. The length of $w$ is the length of $y$, because
$$\norm{w}^2 = \ip{\lambda y}{\lambda y} = \lambda\overline{\lambda}\norm{y}^2 = \abs{\lambda}^2 \norm{y}^2 = \norm{y}^2.$$
8. For a real number $t$ let $f(t) = \norm{x - tw}^2$.
Expand with linearity in the first slot and conjugate-linearity in the second, using $\overline{t} = t$:
$$f(t) = \norm{x}^2 - t\ip{w}{x} - t\ip{x}{w} + t^2\norm{w}^2.$$
9. By steps 6 and 7 this is the real quadratic
$$f(t) = a t^2 - 2 m t + c, \qquad a = \norm{y}^2 > 0, \quad c = \norm{x}^2.$$
10. By positive definiteness, $f(t) \geq 0$ for every real $t$.
11. [[Completing the square|XNCV97HTZ8]] gives, as one checks by expanding the right side,
$$f(t) = a\left(t - \frac{m}{a}\right)^2 + \frac{ac - m^2}{a}.$$
12. Put $t_0 = m/a$.
Then $f(t_0) = (ac - m^2)/a$, and step 10 gives $ac - m^2 \geq 0$, since $a > 0$.
In the language of the [[discriminant|0VVK64Q4JK]], this says $(2m)^2 - 4ac \leq 0$.
13. So $\abs{\ip{x}{y}}^2 = m^2 \leq ac = \norm{x}^2\norm{y}^2$.
Both $\abs{\ip{x}{y}}$ and $\norm{x}\,\norm{y}$ are nonnegative, so taking square roots gives $\abs{\ip{x}{y}} \leq \norm{x}\,\norm{y}$.
14. For the first direction of the equality case, suppose $\abs{\ip{x}{y}} = \norm{x}\,\norm{y}$.
Then $m^2 = ac$, so $f(t_0) = 0$ by step 12.
15. By the definition of $f$ this means $\norm{x - t_0 w} = 0$, so $x = t_0 w = t_0\lambda y$ by positive definiteness.
Hence $x$ and $y$ are linearly dependent.
16. For the second direction, suppose $\alpha x + \beta y = 0$ with $\alpha, \beta$ not both $0$.
If $\alpha = 0$, then $\beta y = 0$ with $\beta \neq 0$, so $y = 0$, which is excluded.
So $\alpha \neq 0$, and $x = d y$ with $d = -\beta/\alpha$.
17. Then $\ip{x}{y} = d\norm{y}^2$, so $\abs{\ip{x}{y}} = \abs{d}\,\norm{y}^2$ by the [[multiplicativity of the absolute value|0GMV7GP8W0]].
18. The computation of step 7 with $d$ in place of $\lambda$ gives $\norm{x} = \abs{d}\,\norm{y}$.
So $\norm{x}\,\norm{y} = \abs{d}\,\norm{y}^2 = \abs{\ip{x}{y}}$, and equality holds.
19. Steps 2, 13, 15 and 18 prove the inequality, and they show that equality holds exactly when $x$ and $y$ are dependent.

## Idea

The whole proof is the fact that a quadratic $at^2 - 2mt + c$ with $a > 0$ which never goes below zero must have $m^2 \leq ac$.
To get such a quadratic, we look at the squared length $\norm{x - tw}^2$ as $t$ runs over the reals.
Over $\mathbb{C}$ one extra move is needed first: we multiply $y$ by a number of modulus $1$, so that the middle coefficient $m$ is the full size of $\ip{x}{y}$ and not only its real part.
Equality means that the quadratic touches zero at $t_0$, and then $x = t_0 w$ lies on the line of $y$.

## Variants

Over $\mathbb{R}$ we can take $w = y$ at once and use $\norm{x - ty}^2 = \norm{x}^2 - 2t\ip{x}{y} + t^2\norm{y}^2$, whose discriminant gives $\ip{x}{y}^2 \leq \norm{x}^2\norm{y}^2$.
Over $\mathbb{C}$ one can instead use a complex parameter and the single value $s = \ip{x}{y}/\norm{y}^2$ in $\norm{x - sy}^2 \geq 0$, which is the [[proof by orthogonal projection|6NB1CYDTNK]].
If you skip the rotation by $\lambda$ over $\mathbb{C}$, the middle term is $-2t\operatorname{Re}\ip{x}{y}$, and the discriminant gives only the weaker bound $(\operatorname{Re}\ip{x}{y})^2 \leq \norm{x}^2\norm{y}^2$.
