---
tag: NBZF4B2WJ4
kind: definition
name: f-divergence
msc: [94A17, 62B10, "60E05"]
defines: TC7SQFTN3A
uses: [059TJN0NZ1, P0P21KDV6E, 1NTKG64F7N, 07Q7CNM5WF, DWJF7ABPR1, PQBW43X5RE, 3SZESKX3N5]
sources:
  - url: https://en.wikipedia.org/wiki/F-divergence
---

## Definition

Let $f \colon (0, \infty) \to \R$ be a [[convex function|07Q7CNM5WF]] with $f(1) = 0$, and extend it by $f(0) = \lim_{t \to 0^+} f(t) \in \R \cup \set{+\infty}$.
Let $(\Omega, \mathcal{F})$ be a measurable space, and let $P$ and $Q$ be [[probability measures|059TJN0NZ1]] on it.
Assume that $P$ is [[absolutely continuous|P0P21KDV6E]] with respect to $Q$.
The *$f$-divergence* of $P$ from $Q$ is
$$D_f(P \,\|\, Q) = \int_{\Omega} f\!\left(\frac{dP}{dQ}\right) dQ,$$
where $dP/dQ$ is the [[Radon–Nikodym derivative|1NTKG64F7N]].

## Remarks

The [[integral|DWJF7ABPR1]] is well defined in $[0, +\infty]$.
Indeed, convexity gives a constant $c$ with $f(t) \ge c (t - 1)$, and $\int (dP/dQ - 1) \, dQ = 0$; Jensen's inequality then gives $D_f(P \,\|\, Q) \ge f(1) = 0$.
If $P$ is not absolutely continuous with respect to $Q$, a standard extension adds the term $f'(\infty) \, P_s(\Omega)$, where $P_s$ is the part of $P$ singular to $Q$ and $f'(\infty) = \lim_{t \to \infty} f(t) / t$.

Standard choices of $f$:

1. $f(t) = t \log t$ gives the [[Kullback–Leibler divergence|PQBW43X5RE]] $D(P \,\|\, Q)$.
2. $f(t) = \frac12 \abs{t - 1}$ gives the [[total variation distance|3SZESKX3N5]] $\sup_{A} \abs{P(A) - Q(A)}$.
3. $f(t) = (t - 1)^2$ gives the $\chi^2$-divergence.
4. $f(t) = (\sqrt{t} - 1)^2$ gives the squared Hellinger distance, up to a factor that depends on the convention.

Example: on $\set{0, 1}$, let $P = (\frac12, \frac12)$ and $Q = (\frac14, \frac34)$.
Then $dP/dQ$ takes the values $2$ and $\frac23$, and with $f(t) = \frac12 \abs{t - 1}$ one gets $\frac14 \cdot \frac12 + \frac34 \cdot \frac16 = \frac14$, which is indeed $\abs{P(\set{0}) - Q(\set{0})}$.

Non-example: $f(t) = -t \log t$ satisfies $f(1) = 0$ but is concave, not convex; with the same $P$ and $Q$ it gives $-D(P \,\|\, Q) < 0$, so it is not an $f$-divergence.

Adding $a (t - 1)$ to $f$ does not change $D_f$, so different $f$ can give the same divergence.

## Explanations

### L1 human

An $f$-divergence compares two laws by the ratio of their probabilities at each point, penalized by a convex function and averaged.
