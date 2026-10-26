---
tag: ~cecaac1c
kind: statement
role: proposition
name: exp z = 1 iff z is an integer multiple of 2πi
aliases: [kernel-of-the-exponential]
msc: [33B10]
uses: [~aa66b863, 04R3CY41VJ, 0C4JS9RF5M]
sources:
  - url: https://en.wikipedia.org/wiki/Exponential_function
    locator: Complex exponential
---

## Statement

Let $z \in \mathbb{C}$.
Then $e^z = 1$ if and only if $z = 2 \pi i k$ for some [[integer|0C4JS9RF5M]] $k$.
Here $e^z$ is the [[complex exponential|~aa66b863]] of $z$.

## Remarks

Proof: write $z = x + iy$ with $x, y$ real. Then $e^z = e^x (\cos y + i \sin y)$. If $e^z = 1$, then $e^x = |e^z| = 1$, so $x = 0$. Then $\cos y = 1$ and $\sin y = 0$, so $y = 2 \pi k$. The converse follows from [[Euler's formula|04R3CY41VJ]].
It follows that $e^z = e^w$ if and only if $z - w = 2 \pi i k$ for some $k \in \mathbb{Z}$.
This is the reason why the [[complex logarithm|~bdd037c1]] has many values.

## Explanations

### L1 human

The value $1$ has size $1$ and direction $0$.
So $e^z = 1$ needs a real part $0$ and an imaginary part that is a whole number of full turns, that is, a multiple of $2\pi$.
