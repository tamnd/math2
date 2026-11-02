---
tag: BTM6WJ0A52
kind: statement
role: theorem
name: Implicit function theorem in Banach spaces
msc: [58C15, 47J07, 46G05]
uses: [M218MWZ62X, 06GZ956657, 06EH97V2A7, 0BXBADR94C]
about: [06EH97V2A7, 06GZ956657]
sources:
  - url: https://en.wikipedia.org/wiki/Implicit_function_theorem
---

## Statement

Let $\mathbb{K}$ be $\R$ or $\C$, and let $X$, $Y$ and $Z$ be [[Banach spaces|06GZ956657]] over $\mathbb{K}$.
Let $\Omega \subseteq X \times Y$ be open, and let $F \colon \Omega \to Z$ be of class $C^1$ in the sense of the [[Fréchet derivative|06EH97V2A7]].
Let $D_x F$ and $D_y F$ be the partial derivatives of $F$, with values in the continuous linear maps $X \to Z$ and $Y \to Z$.
Let $(a, b) \in \Omega$ with $F(a, b) = 0$, and suppose that $D_y F(a, b) \colon Y \to Z$ is bijective.
Then there are open sets $U \subseteq X$ and $V \subseteq Y$ with $a \in U$, $b \in V$ and $U \times V \subseteq \Omega$, and a unique map $g \colon U \to V$, such that the following holds.
For $(x, y) \in U \times V$, $F(x, y) = 0$ if and only if $y = g(x)$.
After shrinking $U$ if needed, $g$ is of class $C^1$, $D_y F(x, g(x))$ is bijective for each $x \in U$, and
$$Dg(x) = -D_y F(x, g(x))^{-1}\, D_x F(x, g(x)).$$

## Remarks

Apply the [[inverse function theorem in Banach spaces|M218MWZ62X]] to $\Phi(x, y) = (x, F(x, y))$ from $\Omega$ to $X \times Z$.
Its derivative at $(a, b)$ is bijective because $D_y F(a, b)$ is, and the local inverse of $\Phi$ has the form $(x, z) \mapsto (x, h(x, z))$; then $g(x) = h(x, 0)$.
The formula for $Dg$ comes from differentiating $F(x, g(x)) = 0$ with the chain rule.

Example: let $h \in C([0,1])$ and $F(\lambda, u) = u - h - \lambda \sin \circ u$ on $\R \times C([0,1])$.
Then $F(0, h) = 0$ and $D_u F(0, h) = \id$.
So for $\lambda$ near $0$, the equation $u = h + \lambda \sin(u)$ has exactly one solution $u = g(\lambda)$ near $h$, and $g$ is $C^1$.

For finite-dimensional $X$, $Y$ and $Z$, the theorem is the [[implicit function theorem|0BXBADR94C]] of several-variable calculus.

## Explanations

### L1 human

The theorem says when an equation $F(x, y) = 0$ can be solved for $y$ as a function of $x$ near a known solution.
The test is linear: the derivative in $y$ must be invertible.
It works when $x$ and $y$ are functions themselves, as long as the spaces are complete normed spaces.

### L2 human

The theorem is the basic tool of perturbation theory.
A solution of a problem at one parameter value persists for nearby parameters when the linearized problem is uniquely solvable.
The solution then depends smoothly on the parameter.
Bifurcation theory studies exactly the points where $D_y F$ fails to be invertible.
It is equivalent to the [[inverse function theorem in Banach spaces|M218MWZ62X]], which is the special case $F(x, y) = f(y) - x$.
