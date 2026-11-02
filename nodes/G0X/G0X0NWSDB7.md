---
tag: G0X0NWSDB7
kind: concept
name: Dilogarithm
msc: ["33B30", "11G55"]
specializes: [96CHDZKGQ0]
sources:
  - url: https://en.wikipedia.org/wiki/Dilogarithm
same_as:
  wikidata: Q1290753
  wikipedia: Dilogarithm
---

## Summary

The dilogarithm is $\operatorname{Li}_2(z) = \sum_{k \ge 1} \frac{z^k}{k^2}$, the [[polylogarithm|96CHDZKGQ0]] of order $2$.
It equals $-\int_0^z \frac{\ln(1 - u)}{u}\, du$ and continues analytically to $\C \setminus [1, \infty)$.
It satisfies remarkable functional equations, such as Euler's reflection formula and the [[five-term relation|6DHQTFAJ03]].
It appears in hyperbolic geometry, through the [[Bloch–Wigner function|Q8K5MWEXB9]], and in algebraic K-theory.

## Explanations

### L1 human

The dilogarithm is the next function after the logarithm in a natural chain: one divides by $u$ and integrates again.
It is not elementary, but it has many exact values.
For example, $\operatorname{Li}_2(1) = \frac{\pi^2}{6}$ and $\operatorname{Li}_2(-1) = -\frac{\pi^2}{12}$.
Its identities, which relate values at points such as $z$, $1 - z$ and $1/z$, have made it a favourite of number theorists and physicists.
