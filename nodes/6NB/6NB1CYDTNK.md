---
tag: 6NB1CYDTNK
kind: proof
name: Proof of the Cauchy–Schwarz inequality
msc: [15A63, 46C05]
proves: 0RFWW56Y22
uses: [0QVNCJXRY3, 0NB0AWGJBW, 0MFJJV97RJ, 0BJV24C4SY, 0ZB7J071WQ, 0GMV7GP8W0, 0EVHJFTG9Z]
sources:
  - url: https://en.wikipedia.org/wiki/Cauchy–Schwarz_inequality
    locator: Proof via the orthogonal projection
---

## Proof

Let $\mathbb{K}$ be the scalar field, $\R$ or $\C$. Over $\R$, the [[complex conjugate|0BJV24C4SY]] $\bar a$ of a scalar $a$ is $a$ itself.

1. By axiom 1 of the [[inner product|0NB0AWGJBW]], $\langle 0, v \rangle = \langle 0 \cdot 0, v \rangle = 0 \langle 0, v \rangle = 0$ for every $v \in V$.
2. By axioms 1 and 2, for $u, v, w \in V$ and $a, b \in \mathbb{K}$, we get $\langle w, a u + b v \rangle = \overline{a \langle u, w \rangle + b \langle v, w \rangle}$. This equals $\bar a \langle w, u \rangle + \bar b \langle w, v \rangle$.
3. By axiom 2, $\langle v, v \rangle$ equals its own conjugate, so it is real. By axiom 3 and step 1, $\langle v, v \rangle \ge 0$, with equality only for $v = 0$.
4. So the [[induced norm|0MFJJV97RJ]] $\norm{v} = \sqrt{\langle v, v \rangle}$ is a real number $\ge 0$. Also $\norm{v} = 0$ holds if and only if $v = 0$.
5. Suppose first that $y = 0$. By steps 1 and 2, $\langle x, 0 \rangle = \overline{\langle 0, x \rangle} = 0$, and $\norm{y} = 0$. So both sides are $0$ and equality holds.
6. In this case $x$ and $y$ are also linearly dependent, since $0 \cdot x + 1 \cdot y = 0$. So the whole claim holds when $y = 0$.
7. Now suppose that $y \ne 0$. Then $\langle y, y \rangle > 0$ by axiom 3. Put $c = \langle x, y \rangle / \langle y, y \rangle$ and $z = x - c y$.
8. By axiom 1, $\langle z, y \rangle = \langle x, y \rangle - c \langle y, y \rangle = 0$. By axiom 2, also $\langle y, z \rangle = \overline{0} = 0$.
9. Since $x = z + c y$, axiom 1 and step 2 give $\langle x, x \rangle = \langle z, z \rangle + \bar c \langle z, y \rangle + c \langle y, z \rangle + c \bar c \langle y, y \rangle$.
10. By step 8 the middle terms vanish. A [[complex number times its conjugate|0ZB7J071WQ]] is $c \bar c = \abs{c}^2$. So $\norm{x}^2 = \norm{z}^2 + \abs{c}^2 \norm{y}^2$.
11. The [[absolute value is multiplicative|0GMV7GP8W0]], so $\abs{c}^2 = \abs{\langle x, y \rangle}^2 / \norm{y}^4$. Hence $\abs{c}^2 \norm{y}^2 = \abs{\langle x, y \rangle}^2 / \norm{y}^2$.
12. Since $\norm{z}^2 \ge 0$, steps 10 and 11 give $\abs{\langle x, y \rangle}^2 \le \norm{x}^2 \norm{y}^2$. Equality holds exactly when $\norm{z} = 0$, that is, when $z = 0$.
13. Both $\abs{\langle x, y \rangle}$ and $\norm{x} \norm{y}$ are $\ge 0$. Taking square roots in step 12 gives $\abs{\langle x, y \rangle} \le \norm{x} \norm{y}$, with equality exactly when $z = 0$.
14. If $z = 0$, then $1 \cdot x - c y = 0$. So $x$ and $y$ are [[linearly dependent|0EVHJFTG9Z]].
15. Conversely, let $a x + b y = 0$ with $a, b \in \mathbb{K}$ not both $0$. If $a = 0$, then $b \ne 0$ and $y = 0$, which is excluded. So $a \ne 0$ and $x = d y$ with $d = -b / a$.
16. Then $z = (d - c) y$, and step 8 gives $(d - c) \langle y, y \rangle = \langle z, y \rangle = 0$. Since $\langle y, y \rangle \ne 0$, we get $d = c$ and $z = 0$.
17. By steps 13 to 16, when $y \ne 0$, equality holds if and only if $x$ and $y$ are linearly dependent. With step 6, this proves the theorem.

## Idea

Subtract from $x$ its projection $c y$ onto the line through $y$. The remainder $z$ is orthogonal to $y$, so a Pythagoras identity gives $\norm{x}^2 = \norm{z}^2 + \abs{c}^2 \norm{y}^2$. Dropping $\norm{z}^2$ gives the inequality, and equality means $z = 0$.
