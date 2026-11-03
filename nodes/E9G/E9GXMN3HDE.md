---
tag: E9GXMN3HDE
kind: conjecture
name: Monodromy conjecture
msc: ["14E18", 11S40, 32S40]
uses: [07GNX8GCYP, VY0HXD3GC4, V6TJAFZ4MD, WGN82TCEF2, KTFG1S2SMG, C8HD62AB6Q, 0BQAA2BK3Q, 7M5P2A0BZ6]
about: [C8HD62AB6Q, 7M5P2A0BZ6]
sources:
  - url: https://en.wikipedia.org/wiki/Bernstein%E2%80%93Sato_polynomial
history:
  posed_by: "Jun-Ichi Igusa"
---

## Statement

Let $f \in \Z[x_1, \dots, x_n]$ be a nonconstant [[polynomial|07GNX8GCYP]].
Let $p$ be a prime and let $\Z_p$ be the ring of [[p-adic integers|V6TJAFZ4MD]].
Let $\abs{\cdot}_p$ be the [[p-adic absolute value|WGN82TCEF2]].
Let $dx$ be the [[Haar measure|VY0HXD3GC4]] on $\Z_p^n$ of total mass $1$.
Igusa's local zeta function of $f$ at $p$ is
$$Z_p(s) = \int_{\Z_p^n} \abs{f(x)}_p^{s} \, dx \quad \text{for } s \in \C, \ \operatorname{Re} s > 0.$$
It is a rational function of $p^{-s}$, so it extends to a meromorphic function of $s$ on $\C$.
Let $a \in \C^n$ with $f(a) = 0$, and let $F_a$ be the Milnor fibre of $f$ at $a$.
The [[Milnor fibration|KTFG1S2SMG]] induces an automorphism of $H^i(F_a, \C)$, the local [[monodromy|C8HD62AB6Q]] at $a$.
The conjecture: for all but finitely many primes $p$, the following holds.
If $s_0$ is a pole of $Z_p(s)$, then $e^{2\pi i \operatorname{Re} s_0}$ is an [[eigenvalue|0BQAA2BK3Q]] of the local monodromy on $H^i(F_a, \C)$.
Here $a$ is some zero of $f$ in $\C^n$ and $i \ge 0$ is some integer.

## Remarks

A stronger form of the conjecture says that $\operatorname{Re} s_0$ is a root of the [[Bernstein–Sato polynomial|7M5P2A0BZ6]] $b_f(s)$.
By a theorem of Malgrange and Kashiwara, $e^{2\pi i \alpha}$ is a monodromy eigenvalue for every root $\alpha$ of $b_f$, so the strong form implies the original one.
Both forms hold for $n = 2$, by work of Loeser.
Denef and Loeser stated an analogous conjecture for the topological zeta function, which is a limit of the $p$-adic zeta functions.
The conjecture is open in general, already for $n = 3$.
Example: for $f = x_1$, a direct computation gives $Z_p(s) = (1 - p^{-1}) / (1 - p^{-1-s})$, with poles of real part $-1$.
Every point of $f = 0$ is smooth, so each Milnor fibre is contractible, and the monodromy on $H^0$ is the identity, with eigenvalue $1 = e^{-2\pi i}$.
Also $b_f(s) = s + 1$ has root $-1$.

## Explanations

### L1 human

Igusa's zeta function counts, in a $p$-adic way, how often the values of $f$ are divisible by high powers of $p$.
Its candidate poles can be read off from an embedded resolution of singularities of the hypersurface $f = 0$.
A resolution produces many candidate poles, and most of them cancel.
The conjecture says that the poles that survive are always seen by the topology of the complex hypersurface, through the monodromy of its Milnor fibres.
It is a bridge between arithmetic and the topology of complex singularities.
