---
tag: NZBKMKB8CV
kind: definition
name: Synchronization of chaos
msc: [34D06, 37D45]
defines: YP1PMW0HE3
uses: [0673D85QKZ, DBKXCGDKTD]
sources:
  - url: https://en.wikipedia.org/wiki/Synchronization_of_chaos
---

## Definition

Let $f \colon \R^n \to \R^n$ be a locally Lipschitz vector field whose [[autonomous system|0673D85QKZ]] $x' = f(x)$ has [[chaotic|DBKXCGDKTD]] solutions.
Let $\varepsilon > 0$ and let $\Gamma$ be an $n \times n$ matrix.
Consider the coupled system
$$x' = f(x) + \varepsilon \Gamma (y - x), \qquad y' = f(y) + \varepsilon \Gamma (x - y).$$
The diagonal $\set{(x, y) : x = y}$ is invariant under this system, and on it each component follows the chaotic system $x' = f(x)$.
The coupled system shows *complete synchronization* from a set $U \subseteq \R^n \times \R^n$ of initial states if every solution with $(x(0), y(0)) \in U$ satisfies
$$\lim_{t \to \infty} \norm{x(t) - y(t)} = 0.$$
Synchronization of chaos refers to such behaviour, with $U$ a neighbourhood of a chaotic attractor on the diagonal, and to its weaker forms.

## Remarks

The difference $e = x - y$ satisfies, to first order, $e' = \big(Df(x) - 2 \varepsilon \Gamma\big) e$.
Synchronization is stable when the largest Lyapunov exponent of this linear equation along the synchronized orbit, the transverse Lyapunov exponent, is negative.

Example: let $f(x) = a x$ be scalar with $a > 0$, which is not chaotic but shows the mechanism, and $\Gamma = 1$.
Then $e' = (a - 2\varepsilon) e$ exactly, so $e(t) \to 0$ for every initial state exactly when $\varepsilon > a/2$.

Non-example: for $\varepsilon = 0$ the two copies are uncoupled, and for a chaotic $f$ nearby initial states separate, so $\norm{x(t) - y(t)}$ does not tend to $0$ for most initial states.

Weaker forms are phase synchronization, where only the phases of oscillations lock, and generalized synchronization, where $y(t) - \psi(x(t)) \to 0$ for some function $\psi$.
