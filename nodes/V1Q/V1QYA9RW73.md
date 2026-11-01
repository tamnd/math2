---
tag: V1QYA9RW73
kind: statement
role: theorem
name: Schwarz–Pick theorem
msc: [30C80, 51M10]
uses: [0DG0Z72CQD, 0MB48XDBY3, 0B346DDAM5]
about: [8G5ABXRK85, 85MM2EA0TK]
sources:
  - url: https://en.wikipedia.org/wiki/Schwarz_lemma
    locator: Schwarz–Pick theorem
---

## Statement

Let $\mathbb{D} = \set{z \in \C : \abs{z} < 1}$ be the open [[unit disc|8G5ABXRK85]], and let $f \colon \mathbb{D} \to \mathbb{D}$ be [[holomorphic|0DG0Z72CQD]].
Then for all $z, w \in \mathbb{D}$,
$$\abs{\frac{f(z) - f(w)}{1 - \overline{f(w)} f(z)}} \le \abs{\frac{z - w}{1 - \bar w z}},$$
and for all $z \in \mathbb{D}$,
$$\frac{\abs{f'(z)}}{1 - \abs{f(z)}^2} \le \frac{1}{1 - \abs{z}^2}.$$
Assume equality holds in the first inequality for some $z \neq w$, or in the second for some $z$.
Then $f$ is a bijective [[Möbius transformation|0B346DDAM5]] of $\mathbb{D}$ onto itself.

## Remarks

Proof idea: for $a \in \mathbb{D}$ let $\varphi_a(z) = \frac{z - a}{1 - \bar a z}$, a Möbius transformation of $\mathbb{D}$ onto itself with $\varphi_a(a) = 0$.
The map $g = \varphi_{f(w)} \circ f \circ \varphi_w^{-1}$ sends $\mathbb{D}$ into $\mathbb{D}$ and fixes $0$.
The [[Schwarz lemma|0MB48XDBY3]] gives $\abs{g(\zeta)} \le \abs{\zeta}$, which is the first inequality with $\zeta = \varphi_w(z)$; letting $z \to w$ gives the second.
In terms of the hyperbolic metric $\frac{2 \abs{dz}}{1 - \abs{z}^2}$ of the [[Poincaré disk model|85MM2EA0TK]], the theorem says that $f$ does not increase hyperbolic distances.
The Möbius transformations of $\mathbb{D}$ onto itself are exactly the hyperbolic isometries that preserve orientation.
Example: $f(z) = z^2$ gives $\abs{2z}/(1 - \abs{z}^4) \le 1/(1 - \abs{z}^2)$, that is $2\abs{z} \le 1 + \abs{z}^2$, which is $(1 - \abs{z})^2 \ge 0$.

## Explanations

### L1 human

The Schwarz lemma is about maps of the disc into itself that fix the center.
The Schwarz–Pick theorem drops the condition at the center.
It says that such a map can only bring points closer together, when distance is measured in the right way.
That right way is the hyperbolic distance, for which points near the edge of the disc are very far apart.

### L2 human

The theorem shows that the hyperbolic metric is the natural metric for holomorphic maps of the disc.
Every holomorphic self-map is a contraction for it, and the automorphisms are the isometries.
This point of view leads to the Ahlfors–Schwarz lemma for metrics of negative curvature and to the Kobayashi metric in several complex variables.
It also gives quick proofs of distortion estimates, for example $\abs{f'(0)} \le 1 - \abs{f(0)}^2$.
