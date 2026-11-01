---
tag: 97DDM0ZBYG
kind: definition
name: Difference quotient
msc: [26A24, 26A06]
defines: AZBDB5F4M4
uses: [0XHDTE5YMZ, 0F1WR9C83K, 0TXTSEMHR5, 0BARQY52N5]
sources:
  - url: https://en.wikipedia.org/wiki/Difference_quotient
---

## Definition

Let $D \subseteq \R$ and let $f \colon D \to \R$ be a [[function|0XHDTE5YMZ]].
Let $x \in D$ and let $h \ne 0$ be a real number with $x + h \in D$.
The *difference quotient* of $f$ at $x$ with increment $h$ is
$$\frac{f(x + h) - f(x)}{h}.$$
Equivalently, for $a \ne b$ in $D$, the difference quotient of $f$ between $a$ and $b$ is $\dfrac{f(b) - f(a)}{b - a}$.

## Remarks

The function $f$ has [[derivative|0F1WR9C83K]] $f'(x)$ at an interior point $x$ of $D$ exactly when the difference quotient has the [[limit|0TXTSEMHR5]] $f'(x)$ as $h \to 0$.
The [[mean value theorem|0BARQY52N5]] says that, for $f$ continuous on $[a, b]$ and differentiable on $(a, b)$, the difference quotient between $a$ and $b$ equals $f'(c)$ for some $c \in (a, b)$.

Example: for $f(x) = x^2$, the difference quotient is $\frac{(x + h)^2 - x^2}{h} = \frac{2xh + h^2}{h} = 2x + h$.
It tends to $2x$ as $h \to 0$, which is $f'(x)$.

Non-example: the increment $h = 0$ is not allowed, since the expression $\frac{f(x) - f(x)}{0}$ has no meaning.
This is why the derivative is a limit and not a value of the quotient.

In numerical analysis, the quotient is also called the forward difference quotient, and $\frac{f(x + h) - f(x - h)}{2h}$ is the central difference quotient.
The symbol $\frac{\Delta y}{\Delta x}$ is common notation for it.
