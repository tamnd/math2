---
tag: DFXSJH9TY4
kind: definition
name: Critical point theory
msc: ["58E05", 47J30, 57R70]
defines: 9ZQC7ARWTT
uses: [9K15AMGBV9, 06EH97V2A7, 0YTCMFB4HC]
sources:
  - url: https://en.wikipedia.org/wiki/Critical_point_(mathematics)
---

## Definition

Let $M$ be a $C^1$ [[Banach manifold|9K15AMGBV9]], for example a finite-dimensional smooth manifold.
Let $f \colon M \to \R$ be a $C^1$ function, with differential $df_p$ at $p \in M$ in the sense of the [[Fréchet derivative|06EH97V2A7]].

1. A [[critical point|0YTCMFB4HC]] of $f$ is a point $p \in M$ with $df_p = 0$.
2. A *critical value* of $f$ is a number $c = f(p)$ with $p$ a critical point; other real numbers are *regular values*.
3. For $c \in \R$ the *sublevel set* is $M^c = \set{p \in M : f(p) \le c}$.

*Critical point theory* studies the critical points and critical values of such $f$ through the topology of $M$ and of the sublevel sets $M^c$.
A central topic is the change of $M^c$ as $c$ passes a critical value.

## Remarks

The basic mechanism is a deformation along a gradient flow.
If $[a, b]$ contains no critical value and a compactness condition holds, it shows that $M^a$ is a deformation retract of $M^b$.
So the topology of the sublevel sets changes only at critical values.

Example: let $M = S^1 \subset \R^2$ and $f(x, y) = y$.
The critical points are $(0, 1)$ and $(0, -1)$, with critical values $1$ and $-1$.
The sublevel set $M^c$ is empty for $c < -1$, a point for $c = -1$, an arc for $-1 < c < 1$, and the whole circle for $c \ge 1$.
So its topology changes exactly at the two critical values.

Non-example: for $f(x) = e^x$ on $\R$, every real number is a regular value and $f$ has no critical point.
The sublevel set $M^c$ is empty for $c \le 0$ and is the half-line $(-\infty, \log c]$ for $c > 0$.
So its topology changes at $c = 0$, although $0$ is not a critical value, and $f$ has no minimum.
This is possible because the compactness condition, the [[Palais–Smale condition|4724KRNHAT]], fails.
Along $x_n = -n$ the values $f(x_n)$ are bounded and $f'(x_n) \to 0$, but $(x_n)$ has no convergent subsequence.

The two classical frameworks are Morse theory, through [[Morse functions|KPQ96640ZJ]], and [[Lusternik–Schnirelmann theory|QARH15D2PN]].
