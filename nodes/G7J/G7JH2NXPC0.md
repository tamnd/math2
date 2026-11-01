---
tag: G7JH2NXPC0
kind: conjecture
name: abc conjecture
msc: [11D75, 11D41]
uses: [0VZ48N083F, 01826KMG2H, ZWPWF6NJC3]
about: [G7JH2NXPC0]
sources:
  - url: https://en.wikipedia.org/wiki/Abc_conjecture
same_as:
  wikidata: Q306393
  wikipedia: Abc conjecture
history:
  posed_by: "Joseph Oesterlé and David Masser"
  first_stated: "1985"
---

## Statement

For a positive integer $n$, let $\operatorname{rad}(n)$ be the product of the distinct [[primes|01826KMG2H]] that divide $n$.
For every real number $\varepsilon > 0$, there are only finitely many triples $(a, b, c)$ of [[coprime|0VZ48N083F]] positive integers with $a + b = c$ and
$$c > \operatorname{rad}(abc)^{1 + \varepsilon}.$$

## Remarks

The conjecture was formulated by Joseph Oesterlé and David Masser in 1985.
Shinichi Mochizuki announced a proof in 2012; it is not accepted by most experts, and the conjecture is generally treated as open.
The analogue for polynomials is a theorem, the [[Mason–Stothers theorem|ZWPWF6NJC3]].
The $\varepsilon$ cannot be removed.
For each $k \ge 1$, take $a = 1$, $c = 2^{6k}$ and $b = c - 1$; since $2^6 = 64 \equiv 1 \pmod 9$, the number $9$ divides $b$, so $\operatorname{rad}(abc) \le 2 \cdot b/3 < c$.
For example, $1 + 8 = 9$ has $\operatorname{rad}(1 \cdot 8 \cdot 9) = 6 < 9$, and $5 + 27 = 32$ has radical $30 < 32$.
The conjecture would imply many results, for instance that the Fermat equation $x^n + y^n = z^n$ has no solutions in positive integers for all large $n$.

## Explanations

### L1 human

The radical of a number keeps each prime factor only once, so $\operatorname{rad}(72) = \operatorname{rad}(2^3 \cdot 3^2) = 6$.
If $a + b = c$ and the three numbers share no factor, then usually $c$ is smaller than the radical of $abc$.
The conjecture says that $c$ can exceed the radical only by a little, and even this happens only rarely in a precise sense.
It expresses a tension between adding numbers and multiplying primes, and it has a remarkable list of consequences.
