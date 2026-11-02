---
tag: PDXR52YGPD
kind: definition
name: Gateaux derivative
msc: [46G05, 58C20]
defines: EAZF9NJW12
uses: [03J5RAKB30, 03TM135G0N, 06KWGHDN2J, 06EH97V2A7]
sources:
  - url: https://en.wikipedia.org/wiki/Gateaux_derivative
---

## Definition

Let $\mathbb{K}$ be $\R$ or $\C$, and let $X$ and $Y$ be [[normed vector spaces|03J5RAKB30]] over $\mathbb{K}$.
Let $U \subseteq X$ be open, let $f \colon U \to Y$, let $x \in U$ and let $h \in X$.
The *Gateaux differential* of $f$ at $x$ in the direction $h$ is the limit
$$df(x; h) = \lim_{t \to 0} \frac{f(x + t h) - f(x)}{t},$$
taken over $t \in \mathbb{K} \setminus \set{0}$, when this limit exists in $Y$.
The map $f$ is *Gateaux differentiable* at $x$ if $df(x; h)$ exists for every $h \in X$ and $h \mapsto df(x; h)$ is a [[continuous linear map|03TM135G0N]] $X \to Y$.
This map is the *Gateaux derivative* of $f$ at $x$.

## Remarks

For $X = \R^n$ and $Y = \R$, $df(x; h)$ is the [[directional derivative|06KWGHDN2J]] of $f$ along $h$.
Some authors do not ask $h \mapsto df(x; h)$ to be linear or continuous.
The definition works without change for locally convex spaces.
If $f$ has a [[Fréchet derivative|06EH97V2A7]] $Df(x)$, then $f$ is Gateaux differentiable at $x$ with $df(x; h) = Df(x) h$.

Example: let $H$ be a real Hilbert space and $f(x) = \norm{x}^2$.
Then $f(x + t h) = \norm{x}^2 + 2t \ip{x}{h} + t^2 \norm{h}^2$, so $df(x; h) = 2\ip{x}{h}$, which is continuous and linear in $h$.

Non-example: on $\R^2$, let $f(x, y) = x^3 / (x^2 + y^2)$ and $f(0, 0) = 0$.
For $h = (a, b) \neq 0$, $f(t a, t b) / t = a^3 / (a^2 + b^2)$, so $df(0; h)$ exists for every $h$.
But $h \mapsto a^3 / (a^2 + b^2)$ is not linear, so $f$ is not Gateaux differentiable at $0$.

A Gateaux differentiable map need not be Fréchet differentiable.
On $\R^2$, let $g(x, y) = 1$ when $y = x^2$ and $(x, y) \neq 0$, and $g = 0$ elsewhere.
Each line through $0$ meets the parabola in at most one point other than $0$, so $dg(0; h) = 0$ for all $h$.
But $g$ is not continuous at $0$.
