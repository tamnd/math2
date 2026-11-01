---
tag: YD8DB4PMD4
kind: definition
name: Dini derivative
msc: [26A24]
defines: 36DXKAD2RZ
uses: [AZBDB5F4M4, 0P8BA7T7S5, 0H4R3RESGV, 0GSZ7B0CGR, 0F1WR9C83K, 0HXEX0DPRA]
sources:
  - url: https://en.wikipedia.org/wiki/Dini_derivative
---

## Definition

Let $I \subseteq \R$ be an open interval, let $f \colon I \to \R$, and let $x \in I$.
The four *Dini derivatives* of $f$ at $x$ are the following elements of the [[extended real line|0GSZ7B0CGR]].

1. The upper right Dini derivative $D^+ f(x) = \limsup_{h \to 0^+} \frac{f(x + h) - f(x)}{h}$.
2. The lower right Dini derivative $D_+ f(x) = \liminf_{h \to 0^+} \frac{f(x + h) - f(x)}{h}$.
3. The upper left Dini derivative $D^- f(x) = \limsup_{h \to 0^-} \frac{f(x + h) - f(x)}{h}$.
4. The lower left Dini derivative $D_- f(x) = \liminf_{h \to 0^-} \frac{f(x + h) - f(x)}{h}$.

Here the upper and lower limits are the [[limit superior|0P8BA7T7S5]] and [[limit inferior|0H4R3RESGV]] of the quotient.
They are taken over $h$ in the given one-sided range with $x + h \in I$.

## Remarks

Always $D_+ f(x) \le D^+ f(x)$ and $D_- f(x) \le D^- f(x)$.
The [[right derivative|0HXEX0DPRA]] of $f$ at $x$ exists and is finite exactly when $D_+ f(x) = D^+ f(x)$ is finite, and similarly on the left.
So $f$ is differentiable at $x$ exactly when all four Dini derivatives are equal and finite.

Example: let $f(x) = x \sin(1/x)$ for $x \ne 0$ and $f(0) = 0$.
For $h \ne 0$, the [[difference quotient|AZBDB5F4M4]] at $0$ is $\frac{h \sin(1/h)}{h} = \sin(1/h)$.
For $h > 0$ and for $h < 0$ alike, it takes every value in $[-1, 1]$ for arbitrarily small $\abs{h}$.
So $D^+ f(0) = D^- f(0) = 1$ and $D_+ f(0) = D_- f(0) = -1$, and $f$ is not differentiable at $0$.

Non-example of finiteness: for $f(x) = \sqrt{\abs{x}}$ at $0$, the quotient for $h > 0$ is $h^{-1/2}$, so $D^+ f(0) = D_+ f(0) = +\infty$.
The Dini derivatives exist but are not real numbers.
