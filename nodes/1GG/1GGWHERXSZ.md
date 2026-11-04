---
tag: 1GGWHERXSZ
kind: proof
name: Proof of the impossibility of doubling the cube
msc: [12F05]
proves: 0CQ357M0QS
uses: [0FMN2MN7TM, 04SD3F4FCR, 02BPKD7TMD, 0GK1WB9R98, 06K7SARZKR, 0N5QW9K7MH, 0SSSM1D475, 0PN9WMRWT7, 0BJV24C4SY, 0KW2X0TFBX, 0ZB7J071WQ]
sources:
  - url: https://en.wikipedia.org/wiki/Doubling_the_cube
    locator: Proof of impossibility
---

## Proof

Let $c = \sqrt[3]{2}$, the real cube root of $2$, and let $\mathcal{C}$ be the set of the [[constructible numbers|0FMN2MN7TM]].

1. The polynomial $f = x^3 - 2$ satisfies [[Eisenstein's criterion|02BPKD7TMD]] with $p = 2$: $2$ divides $0, 0, -2$, $2$ does not divide $1$, and $4$ does not divide $-2$. So $f$ is irreducible in $\Q[x]$.
2. The [[minimal polynomial|0GK1WB9R98]] of $c$ over $\Q$ [[divides|06K7SARZKR]] $f$, since $f(c) = 0$. As $f$ is irreducible and both are monic, the minimal polynomial is $f$.
3. By the [[degree of a simple extension|0N5QW9K7MH]], $[\Q(c) : \Q] = 3$.
4. If $c$ were constructible, then $[\Q(c) : \Q]$ would be a [[power of $2$|0SSSM1D475]]. But $3$ is not a power of $2$. So $c \notin \mathcal{C}$.

Now we turn to the construction problem. Take the edge of the given cube as the segment from $0$ to $1$. A [[doubling of the cube|04SD3F4FCR]] would construct two points $P, Q$ with $\abs{P - Q} = c$, since the doubled cube has volume $2 = c^3$.

5. By the [[field theorem|0PN9WMRWT7]], $\mathcal{C}$ is a subfield of $\C$ closed under square roots, and it is the smallest such subfield.
6. Let $\overline{\mathcal{C}} = \set{\bar z : z \in \mathcal{C}}$, using the [[complex conjugate|0BJV24C4SY]]. Conjugation preserves sums, products and inverses, so $\overline{\mathcal{C}}$ is a subfield of $\C$.
7. If $w = \bar z$ with $z \in \mathcal{C}$, and $s^2 = w$, then $\bar s^2 = z$. So $\bar s \in \mathcal{C}$ and $s \in \overline{\mathcal{C}}$. Thus $\overline{\mathcal{C}}$ is closed under square roots.
8. By minimality, $\mathcal{C} \subseteq \overline{\mathcal{C}}$. So for $z \in \mathcal{C}$ we have $z = \bar u$ with $u \in \mathcal{C}$, and $\bar z = u \in \mathcal{C}$.
9. Let $w = P - Q$. Then $w \in \mathcal{C}$, so $\bar w \in \mathcal{C}$ by step 8, and [[$w \bar w = \abs{w}^2$|0ZB7J071WQ]] lies in $\mathcal{C}$.
10. The [[modulus|0KW2X0TFBX]] $\abs{w} = c$ is a square root of $\abs{w}^2$, so $c \in \mathcal{C}$ by step 5. This contradicts step 4.
11. So $\sqrt[3]{2}$ is not constructible, and the cube cannot be doubled with straightedge and compass.

## Idea

The number $\sqrt[3]{2}$ has degree $3$ over $\Q$, while constructible numbers have degree a power of $2$. A construction of the doubled edge would make its length constructible, because the constructible numbers are closed under conjugation, products and square roots.
