---
tag: 4C3RRDA4WZ
kind: definition
name: Regular semigroup
msc: [20M17]
defines: XGJKF6T7FZ
uses: [0XMEM406JM, 0N5NJZKKN3, 7ZB7MRKPQ9, S7WJW2YES2]
sources:
  - url: https://en.wikipedia.org/wiki/Regular_semigroup
---

## Definition

Let $S$ be a [[semigroup|0XMEM406JM]].
An element $a \in S$ is *regular* if there is $x \in S$ with $axa = a$.
The semigroup $S$ is *regular* if every element of $S$ is regular.

## Remarks

If $axa = a$, then $y = xax$ satisfies $aya = a$ and $yay = y$; such a $y$ is called an inverse of $a$.
So $S$ is regular if and only if every element has at least one inverse in this sense.
If $axa = a$, then $ax$ and $xa$ are [[idempotents|0N5NJZKKN3]].
A semigroup is regular if and only if every $\mathcal{R}$-class, or equivalently every $\mathcal{L}$-class, of [[Green's relations|S7WJW2YES2]] contains an idempotent.

Example: the monoid $T_X$ of all maps $X \to X$ under composition, $(fg)(x) = f(g(x))$.
Given $f$, choose $g$ such that $g(y)$ is a preimage of $y$ under $f$ for each $y$ in the image of $f$, and $g(y)$ is arbitrary otherwise.
Then $f(g(f(x))) = f(x)$ for all $x$, so $fgf = f$.

Non-example: the positive integers under addition.
For $a = 1$, the equation $1 + x + 1 = 1$ has no positive solution $x$, so $1$ is not regular.
