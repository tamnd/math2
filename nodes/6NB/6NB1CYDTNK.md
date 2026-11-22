---
tag: 6NB1CYDTNK
kind: proof
name: Proof of the Cauchy-Schwarz inequality by orthogonal projection
msc: ["15A63", "46C05"]
topics: [1D4JTZ9VS3]
audience: ug1
proves: 0RFWW56Y22
methods: [0NTF6DMVAP, 0WCP0PVET6]
uses: [01EK923SKP, 0VGSYBWHV2, 0KG4D8AP6G, 0BJV24C4SY, 0ZB7J071WQ, 0GMV7GP8W0, 0EVHJFTG9Z]
sources:
  - url: https://en.wikipedia.org/wiki/Cauchy–Schwarz_inequality
    locator: Proof via the orthogonal projection
  - book: isbn:9783031410253
    locator: Chapter 6
---

## Proof

We split $x$ into a multiple of $y$ and a part orthogonal to $y$, and we compare lengths with a Pythagoras identity.
Let $V$ be an [[inner product space|01EK923SKP]] over $\mathbb{K} = \mathbb{R}$ or $\mathbb{C}$, and let $x, y \in V$.
Over $\mathbb{R}$ the [[complex conjugate|0BJV24C4SY]] $\overline{a}$ of a scalar $a$ is $a$ itself, so the proof covers both cases.
We use the axioms of the [[inner product|0VGSYBWHV2]]: (1) linearity in the first slot, (2) conjugate symmetry, (3) positive definiteness.

1. For every $v \in V$, axiom 1 gives $\ip{0}{v} = \ip{0 \cdot 0}{v} = 0 \cdot \ip{0}{v} = 0$.
2. Axioms 1 and 2 give conjugate-linearity in the second slot: for $u, v, w \in V$ and $a, b \in \mathbb{K}$,
$$\ip{w}{au + bv} = \overline{a\ip{u}{w} + b\ip{v}{w}} = \overline{a}\ip{w}{u} + \overline{b}\ip{w}{v}.$$
3. By axiom 2, $\ip{v}{v}$ equals its own conjugate, so it is real.
By axiom 3 and step 1, $\ip{v}{v} \geq 0$, with equality only for $v = 0$.
4. So the [[induced norm|0KG4D8AP6G]] $\norm{v} = \sqrt{\ip{v}{v}}$ is a real number $\geq 0$, and $\norm{v} = 0$ if and only if $v = 0$.
5. Suppose first that $y = 0$.
By steps 1 and 2, $\ip{x}{0} = \overline{\ip{0}{x}} = 0$, and $\norm{y} = 0$, so both sides are $0$ and equality holds.
6. In this case $x$ and $y$ are also linearly dependent, since $0 \cdot x + 1 \cdot y = 0$.
So the whole claim holds when $y = 0$.
7. Now suppose that $y \neq 0$, so that $\ip{y}{y} > 0$ by axiom 3.
Put
$$c = \frac{\ip{x}{y}}{\ip{y}{y}}, \qquad z = x - c y.$$
8. The vector $z$ is orthogonal to $y$, since axiom 1 gives $\ip{z}{y} = \ip{x}{y} - c\ip{y}{y} = 0$.
By axiom 2, also $\ip{y}{z} = \overline{0} = 0$.
9. Since $x = z + c y$, axiom 1 and step 2 give
$$\ip{x}{x} = \ip{z}{z} + \overline{c}\ip{z}{y} + c\ip{y}{z} + c\overline{c}\ip{y}{y}.$$
10. By step 8 the two middle terms vanish, and a [[complex number times its conjugate|0ZB7J071WQ]] is $c\overline{c} = \abs{c}^2$.
So $\norm{x}^2 = \norm{z}^2 + \abs{c}^2 \norm{y}^2$.
11. The [[absolute value is multiplicative|0GMV7GP8W0]], so $\abs{c}^2 = \abs{\ip{x}{y}}^2 / \norm{y}^4$.
Hence $\abs{c}^2 \norm{y}^2 = \abs{\ip{x}{y}}^2 / \norm{y}^2$.
12. Since $\norm{z}^2 \geq 0$, steps 10 and 11 give $\abs{\ip{x}{y}}^2 \leq \norm{x}^2 \norm{y}^2$.
Equality holds exactly when $\norm{z} = 0$, that is, when $z = 0$ by step 4.
13. Both $\abs{\ip{x}{y}}$ and $\norm{x}\,\norm{y}$ are $\geq 0$, so taking square roots in step 12 gives $\abs{\ip{x}{y}} \leq \norm{x}\,\norm{y}$, with equality exactly when $z = 0$.
14. If $z = 0$, then $1 \cdot x - c y = 0$, so $x$ and $y$ are [[linearly dependent|0EVHJFTG9Z]].
15. Conversely, let $ax + by = 0$ with $a, b \in \mathbb{K}$ not both $0$.
If $a = 0$, then $b \neq 0$ and $y = 0$, which is excluded.
So $a \neq 0$, and $x = dy$ with $d = -b/a$.
16. Then $z = (d - c) y$, and step 8 gives $(d - c)\ip{y}{y} = \ip{z}{y} = 0$.
Since $\ip{y}{y} \neq 0$, we get $d = c$ and so $z = 0$.
17. By steps 13 to 16, when $y \neq 0$, equality holds if and only if $x$ and $y$ are linearly dependent.
Together with step 6, this proves the theorem.

## Idea

Drop a perpendicular from $x$ to the line through $y$.
The foot of the perpendicular is $cy$, and the remainder $z = x - cy$ is orthogonal to $y$.
Then the theorem of Pythagoras gives $\norm{x}^2 = \norm{z}^2 + \abs{c}^2 \norm{y}^2$, so the projection is never longer than $x$, and that is the inequality.
Equality means that nothing is left over, $z = 0$, so $x$ lies on the line of $y$.
The choice of $c$ with $\ip{x}{y}$ in the numerator, and not $\ip{y}{x}$, is what makes $\ip{z}{y} = 0$ under our convention.

## Variants

The [[proof by the discriminant|7SW8PQYAEH]] studies the real quadratic $t \mapsto \norm{x - t\lambda y}^2$ and uses that its discriminant is not positive.
Another proof first reduces to unit vectors and then expands $\norm{x \pm y}^2 \geq 0$; the [[example of this reduction|N8Z4J61ZHV]] does it in $\mathbb{R}^n$, and over $\mathbb{C}$ one first multiplies $y$ by a scalar of modulus $1$ that makes $\ip{x}{y}$ real.
A third proof uses the [[Gram matrix|00SPJSDT3Z]]: the inequality says that the Gram determinant of $x, y$ is $\geq 0$, and that determinant equals $\norm{u_1}^2 \norm{u_2}^2$ for the orthogonal vectors $u_1, u_2$ of the Gram-Schmidt process.
