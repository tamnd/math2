---
tag: AATQKCWAAC
kind: statement
role: lemma
name: du Bois-Reymond lemma
msc: [49K05]
uses: [0X3WGX95FE, 0VW90BBSJ4, 0W29TBTY12]
about: [PQ25NHV0KS]
sources:
  - url: https://en.wikipedia.org/wiki/Fundamental_lemma_of_the_calculus_of_variations
---

## Statement

Let $a < b$ and let $f \colon [a, b] \to \R$ be [[continuous|0X3WGX95FE]].
Suppose that
$$\int_a^b f(x) \, \eta'(x) \, dx = 0$$
for every [[continuously differentiable|0VW90BBSJ4]] $\eta \colon [a, b] \to \R$ with $\eta(a) = \eta(b) = 0$.
Then $f$ is constant on $[a, b]$.

## Remarks

Let $c = \frac{1}{b - a} \int_a^b f \, dx$ be the mean of $f$, and set $\eta(x) = \int_a^x (f(s) - c) \, ds$.
Then $\eta$ is $C^1$, $\eta(a) = \eta(b) = 0$ and $\eta' = f - c$.
The hypothesis gives $\int_a^b f (f - c) \, dx = 0$, and $\int_a^b c (f - c) \, dx = 0$ by the choice of $c$.
Subtracting, $\int_a^b (f - c)^2 \, dx = 0$, so $f = c$ by continuity.

A common extension: if $f, g$ are continuous and $\int_a^b (g \eta + f \eta') \, dx = 0$ for all such $\eta$, then $f$ is $C^1$ and $f' = g$.
To see it, apply the lemma to $f - G$, where $G(x) = \int_a^x g(s) \, ds$, after an integration by parts of $\int_a^b g \eta \, dx$.

Example: for $f(x) = x$ on $[0, 1]$ and $\eta(x) = x(1 - x)$, one finds $\int_0^1 x (1 - 2x) \, dx = -1/6 \ne 0$, as the lemma predicts for a non-constant $f$.

## Explanations

### L1 human

If $f$ gives zero against the slope of every function that starts and ends at zero, then $f$ cannot vary.
The reason is that one can build a test function whose slope is exactly $f$ minus its average.

### L2 human

The extension above gives the Euler–Lagrange equation in integrated form, $L_p(x, y, y') = \int_a^x L_z(s, y, y') \, ds + C$, for a $C^1$ minimiser $y$, without assuming that $y$ has a second derivative.
It follows that $x \mapsto L_p(x, y(x), y'(x))$ is $C^1$, which is the start of regularity theory in one variable.
The [[fundamental lemma|JNDZ86CV3Y]] is the version where $\eta$ itself, instead of $\eta'$, appears in the integral.
