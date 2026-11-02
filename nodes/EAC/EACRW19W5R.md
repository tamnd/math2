---
tag: EACRW19W5R
kind: definition
name: Nontangential limit
msc: [31B25, 31A20, 30H05]
defines: RHDBK62123
uses: [0J8Y1NCY0K, 8G5ABXRK85, Q2N917JQ6A]
sources:
  - url: https://en.wikipedia.org/wiki/Fatou%27s_theorem
---

## Definition

Let $n \ge 2$, let $B = \set{x \in \R^n : \abs{x} < 1}$ and let $S = \partial B$.
For $\zeta \in S$ and $\alpha > 1$, the *nontangential approach region* at $\zeta$ is
$$\Gamma_\alpha(\zeta) = \set{x \in B : \abs{x - \zeta} < \alpha (1 - \abs{x})}.$$
Let $u \colon B \to \C$ and $L \in \C$.
The function $u$ has *nontangential limit* $L$ at $\zeta$ if, for every $\alpha > 1$, $u(x) \to L$ as $x \to \zeta$ with $x \in \Gamma_\alpha(\zeta)$.

## Remarks

The limit along $\Gamma_\alpha(\zeta)$ is a [[limit of a function of several variables|0J8Y1NCY0K]] restricted to that set; $\zeta$ is a limit point of each $\Gamma_\alpha(\zeta)$.
For the [[unit disc|8G5ABXRK85]] the regions $\Gamma_\alpha(\zeta)$ are the Stolz angles, and the same definition works for the upper half-space with cones $\set{(x, t) : \abs{x - x_0} < \alpha t}$.
A nontangential limit implies the radial limit $\lim_{r \to 1} u(r\zeta) = L$.
Example: let $f(z) = \exp\left(-\frac{1 + z}{1 - z}\right)$ on the unit disc and $\zeta = 1$.
Since $\operatorname{Re} \frac{1 + z}{1 - z} = \frac{1 - \abs{z}^2}{\abs{1 - z}^2}$, on $\Gamma_\alpha(1)$ this is at least $\frac{1}{\alpha^2 (1 - \abs{z})}$, which tends to $+\infty$.
So $f$ has nontangential limit $0$ at $1$.
On the circle $\abs{z - 1/2} = 1/2$ the same real part equals $1$, so $\abs{f} = e^{-1}$ there, and $f$ has no unrestricted limit at $1$.
Non-example: the Poisson kernel $u(z) = \frac{1 - \abs{z}^2}{\abs{1 - z}^2}$ has $u(r) = \frac{1 + r}{1 - r} \to +\infty$, so it has no finite nontangential limit at $1$.
By [[Fatou's theorem|Q2N917JQ6A]], the Poisson integral of an integrable function has a nontangential limit at almost every boundary point.
