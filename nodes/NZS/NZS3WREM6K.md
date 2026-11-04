---
tag: NZS3WREM6K
kind: proof
name: Proof that the rationals are countable
msc: ["03E10"]
proves: 0DS9KWFDK2
uses: [0SEZ3JGZP7, 0NCJ5WXN6Z, 0PVG1CRAJN, 01BX15HSRR, 066RJJVWH9, 01VG2A0BHW, 0ZG61TFBES, 08G4XH86JC, 01FPXMTBX1, 0A9V6RKQG6]
sources:
  - url: https://proofwiki.org/wiki/Rational_Numbers_are_Countably_Infinite
    locator: Proof 2
---

## Proof

We find injections in both directions and apply the Schröder–Bernstein theorem.

1. Let $x \in \Q$ be a [[rational number|0NCJ5WXN6Z]]. Then $x = p/q$ for some $p \in \Z$ and some integer $q \ge 1$.
2. So the set $D_x = \{q \in \N : q \ge 1,\ qx \in \Z\}$ is nonempty. By the [[well-ordering principle|01BX15HSRR]], it has a least element $q_x$.
3. Define $r \colon \Q \to \Z \times \N$ by $r(x) = (q_x x,\ q_x)$. Its first entry is an integer by the choice of $q_x$.
4. The map $r$ is [[injective|0PVG1CRAJN]]. If $r(x) = r(y)$, then $q_x = q_y$ and $q_x x = q_y y$. Dividing by $q_x \ge 1$ gives $x = y$.
5. By [[the integers are countable|066RJJVWH9]], there is a bijection $f \colon \N \to \Z$. Its inverse $f^{-1} \colon \Z \to \N$ is a [[bijection|01VG2A0BHW]], so it is injective. Hence $\Z$ is [[countable|0ZG61TFBES]].
6. The set $\N$ is countable, through the identity map. By the [[product of countable sets is countable|08G4XH86JC]], there is an injection $s \colon \Z \times \N \to \N$.
7. The composite $s \circ r \colon \Q \to \N$ is [[injective|01FPXMTBX1]].
8. The inclusion $\N \to \Q$, $n \mapsto n$, is injective.
9. By the [[Schröder–Bernstein theorem|0A9V6RKQG6]], steps 7 and 8 give a bijection $\N \to \Q$. So $\Q$ is [[countably infinite|0SEZ3JGZP7]].

## Idea

Code each rational by its smallest positive denominator and the matching numerator. This gives an injection into the countable set $\Z \times \N$, so $\Q$ is countable. Since $\Q$ also contains a copy of $\N$, the Schröder–Bernstein theorem upgrades this to a bijection with $\N$.
