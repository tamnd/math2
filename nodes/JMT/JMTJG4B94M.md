---
tag: JMTJG4B94M
kind: definition
name: Kloosterman sum
msc: [11L05]
defines: E1SQWQ2PAV
uses: [97PBMQCPPM, 03VFZ2WETT, 07GJV36896]
sources:
  - url: https://en.wikipedia.org/wiki/Kloosterman_sum
---

## Definition

Let $m \ge 1$ be an integer, and let $a, b \in \Z$.
For a real $t$, write $e(t) = e^{2\pi i t}$.
For an integer $x$ coprime to $m$, let $\bar{x}$ be an integer with $x \bar{x} \equiv 1 \pmod{m}$.
The *Kloosterman sum* is
$$K(a, b; m) = \sum_{\substack{x \bmod m \\ \gcd(x, m) = 1}} e\!\left(\frac{a x + b \bar{x}}{m}\right),$$
where $x$ runs over a set of representatives of the invertible classes of the [[integers modulo m|03VFZ2WETT]].

## Remarks

The value does not depend on the choice of representatives or of $\bar{x}$, since the phase is defined modulo $1$.
Example: $m = 5$, $a = b = 1$.
The pairs $(x, \bar{x})$ are $(1, 1), (2, 3), (3, 2), (4, 4)$, so the phases are $2/5, 1, 1, 8/5$ and
$$K(1, 1; 5) = e(2/5) + 2 + e(3/5) = 2 + 2\cos(4\pi/5) \approx 0.382.$$
Non-example: the sum $\sum_{x = 0}^{m-1} e((a x + b \bar{x})/m)$ over all residues is not defined, since $\bar{x}$ does not exist when $\gcd(x, m) > 1$.
The sum is real, because replacing $x$ by $-x$ conjugates each term.
If $\gcd(a, m) = 1$, then $K(a, b; m) = K(1, ab; m)$.
For $b = 0$, the sum $K(a, 0; m)$ is the Ramanujan sum $c_m(a)$.
It is an [[exponential sum|97PBMQCPPM]] in which the phase function is $x \mapsto (ax + b\bar{x})/m$.
