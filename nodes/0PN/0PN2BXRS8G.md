---
tag: 0PN2BXRS8G
kind: statement
role: theorem
name: Argument principle
aliases: [cauchys-argument-principle]
msc: [30C15]
uses: [0NSD1TPHR0, 064N002TX4, 0YK27TJ4WF, 0T7ABX4CWE]
sources:
  - url: https://en.wikipedia.org/wiki/Argument_principle
    locator: Formulation
same_as:
  wikidata: Q1370201
  wikipedia: Argument principle
---

## Statement

Let $c \in \mathbb{C}$ and $r > 0$.
Let $f$ be a [[meromorphic function|0NSD1TPHR0]] on an open set that contains the closed disc $\{ z : |z - c| \le r \}$.
Suppose that $f$ has no zeros and no poles on the circle $|z - c| = r$.
Let $Z$ be the number of zeros of $f$ in the open disc $|z - c| < r$, each counted as many times as its [[order|064N002TX4]].
Let $P$ be the number of poles of $f$ in the open disc, each counted as many times as its [[order|0YK27TJ4WF]].
Then
$$\frac{1}{2\pi i} \oint_{|z - c| = r} \frac{f'(z)}{f(z)} \, dz = Z - P,$$
where the [[circle integral|0T7ABX4CWE]] goes once around the circle counterclockwise.

## Remarks

The function $f'/f$ is the logarithmic derivative of $f$.
At a zero of order $m$, it has a simple pole with residue $m$; at a pole of order $m$, it has a simple pole with residue $-m$.
So the theorem follows from the [[residue theorem|032HKYS329]].
The left side is also the [[winding number|0X7SBS8E0F]] around $0$ of the closed curve $\theta \mapsto f(c + r e^{i\theta})$, $\theta \in [0, 2\pi]$.

## Explanations

### L1 human

Walk once around the circle and watch the point $f(z)$.
Each zero inside the circle makes $f(z)$ turn once around $0$ in the positive direction, and each pole makes it turn once in the negative direction.
For example, $f(z) = z^3$ on the unit circle turns three times around $0$, and $f$ has a zero of order $3$ at $0$.
