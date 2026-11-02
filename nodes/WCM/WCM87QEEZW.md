---
tag: WCM87QEEZW
kind: statement
role: theorem
name: Wielandt's theorem
msc: [33B15, 30D30]
uses: [0V3FZMVB4K, 0NAHXR1FRH]
about: [0H5SYBSED9]
sources:
  - url: https://en.wikipedia.org/wiki/Wielandt_theorem
same_as:
  wikidata: Q3527182
  wikipedia: Wielandt theorem
---

## Statement

Let $H = \set{z \in \C : \operatorname{Re} z > 0}$ and let $F \colon H \to \C$ be a [[holomorphic function|0NAHXR1FRH]] such that:

1. $F(z + 1) = z F(z)$ for every $z \in H$;
2. $F$ is bounded on the strip $\set{z \in \C : 1 \le \operatorname{Re} z \le 2}$.

Then $F(z) = F(1)\,\Gamma(z)$ for every $z \in H$, where $\Gamma$ is the [[gamma function|0V3FZMVB4K]].

## Remarks

The gamma function satisfies both conditions: the functional equation, and $\abs{\Gamma(z)} \le \Gamma(\operatorname{Re} z) \le 1$ on the strip, by Euler's integral.
For the proof, put $v = F - F(1)\Gamma$; it satisfies condition 1 and $v(1) = 0$.
The equation $v(z) = v(z + 1)/z$ extends $v$ to a meromorphic function on $\C$, and the possible poles at $0, -1, -2, \ldots$ are removable because $v(1) = 0$, so $v$ is entire and bounded on $0 \le \operatorname{Re} z \le 1$.
Then $u(z) = v(z) v(1 - z)$ is entire, satisfies $u(z + 1) = -u(z)$, and is bounded on that strip, so it is bounded on $\C$ and constant by [[Liouville's theorem|0EHKVRF4J6]]; since $u(1) = 0$, $u = 0$ and hence $v = 0$.
Condition 2 cannot be dropped: $F(z) = \Gamma(z)\big(1 + \sin(2\pi z)\big)$ satisfies condition 1 but is not a multiple of $\Gamma$, and it is unbounded on the strip.

## Explanations

### L1 human

Wielandt's theorem says that the gamma function is the only holomorphic solution of $F(z + 1) = z F(z)$ on the right half-plane that stays bounded on a vertical strip, up to a constant factor.
It is a complex analogue of the Bohr–Mollerup theorem, with boundedness in place of log-convexity.

### L2 human

The theorem is a quick tool for proving identities: to show that a function $F$ equals $\Gamma$, check the functional equation, boundedness on the strip $1 \le \operatorname{Re} z \le 2$, and $F(1) = 1$.
For example, the [[Euler–Gauss limit formula|SKRP9NDXR4]] and the [[Legendre duplication formula|CND4E1PY9V]] can be proved this way.
Compare with the [[Bohr–Mollerup theorem|QFF87AXWN2]], which works on the real line.
