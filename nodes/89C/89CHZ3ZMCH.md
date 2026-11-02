---
tag: 89CHZ3ZMCH
kind: statement
role: proposition
name: Mutual absolute continuity of harmonic measures
msc: [31B15, 31A15]
uses: [CFD7BPM51W, YNH832D50W, P0P21KDV6E, R12KQGVGN6]
about: [CFD7BPM51W]
sources:
  - url: https://en.wikipedia.org/wiki/Harmonic_measure
---

## Statement

Let $n \ge 2$, let $\Omega \subseteq \R^n$ be a bounded domain, and for $x \in \Omega$ let $\omega^x$ be the [[harmonic measure|CFD7BPM51W]] of $\Omega$ at $x$.
Let $x, y \in \Omega$.
Then there is a constant $C \ge 1$, depending only on $x$, $y$ and $\Omega$, such that
$$C^{-1}\, \omega^y(E) \le \omega^x(E) \le C\, \omega^y(E) \qquad \text{for every Borel set } E \subseteq \partial\Omega.$$
In particular $\omega^x$ and $\omega^y$ are mutually [[absolutely continuous|P0P21KDV6E]].

## Remarks

Here $\omega^x(E)$ is the value at $x$ of the [[Perron–Wiener–Brelot solution|R12KQGVGN6]] of the Dirichlet problem with boundary data the indicator function of $E$.
Idea of the proof: for a fixed Borel set $E$, the function $z \mapsto \omega^z(E)$ is harmonic on $\Omega$ with values in $[0, 1]$.
Join $x$ to $y$ by a path in $\Omega$ and cover it by finitely many balls whose doubles lie in $\Omega$.
[[Harnack's inequality|YNH832D50W]] on each ball compares the values of a nonnegative harmonic function at nearby points.
The chain of balls then gives a constant $C$ that does not depend on $E$.
Example: for the unit disc, $d\omega^z = \frac{1 - \abs{z}^2}{\abs{e^{i\theta} - z}^2} \frac{d\theta}{2\pi}$.
With $y = 0$ and $\abs{x} = r$, the density lies between $\frac{1 - r}{1 + r}$ and $\frac{1 + r}{1 - r}$, so one can take $C = \frac{1 + r}{1 - r}$.
Connectedness is needed: on a disjoint union of two discs, the harmonic measures at points of different discs are carried by disjoint circles.

## Explanations

### L1 human

Harmonic measure at $x$ records where a random path from $x$ leaves the domain.
Starting from a different point changes the probabilities, but only by a bounded factor.
So the sets that are never hit are the same for every starting point.

### L2 human

Because of this result one speaks of sets of harmonic measure zero without naming the starting point.
This is how the class of null sets of harmonic measure enters statements such as Fatou-type theorems, Dahlberg's theorem and Makarov's theorem.
The constant $C$ blows up as $x$ or $y$ approaches the boundary, which is why boundary estimates need finer tools such as the boundary Harnack principle.
