---
tag: KT50SMH3EC
kind: object
name: Epsilon nought
msc: ["03E10", "03F15"]
instance_of: [0YSCSX5YZC]
uses: [0RDJK7EQYY, 01TQB88H4C]
sources:
  - url: https://en.wikipedia.org/wiki/Epsilon_number
---

## Description

Ordinal exponentiation is defined by $\omega^0 = 1$, $\omega^{\alpha + 1} = \omega^\alpha \cdot \omega$, and $\omega^\lambda = \sup_{\alpha < \lambda} \omega^\alpha$ for a limit ordinal $\lambda$.
An *epsilon number* is an [[ordinal|0RDJK7EQYY]] $\varepsilon$ with $\omega^\varepsilon = \varepsilon$.
The ordinal $\varepsilon_0$, read "epsilon nought", is the least epsilon number.
It is the limit of the sequence
$$\omega, \quad \omega^\omega, \quad \omega^{\omega^\omega}, \quad \dots,$$
that is, $\varepsilon_0 = \sup \set{\omega_n : n \in \N}$ with $\omega_0 = \omega$ and $\omega_{n+1} = \omega^{\omega_n}$.

Check: let $\varepsilon = \sup_n \omega_n$.
The map $\alpha \mapsto \omega^\alpha$ is continuous at limits, so $\omega^\varepsilon = \sup_n \omega^{\omega_n} = \sup_n \omega_{n+1} = \varepsilon$.
If $\beta$ is an epsilon number, then $\omega \le \beta$, and induction on $n$ gives $\omega_n \le \beta$, so $\varepsilon \le \beta$.
Since each $\omega_n$ is a [[countable|01TQB88H4C]] ordinal, $\varepsilon_0$ is a countable union of countable sets, hence countable.

## Remarks

Every ordinal $\alpha$ with $0 < \alpha < \varepsilon_0$ has a Cantor normal form $\omega^{\beta_1} c_1 + \dots + \omega^{\beta_k} c_k$ with $\alpha > \beta_1 > \dots > \beta_k$ and positive integers $c_i$.
Since each exponent is smaller than $\alpha$, the exponents can be written in the same form again, and the process ends.
This gives a finite notation for each ordinal below $\varepsilon_0$.
The ordinal $\varepsilon_0$ is the proof-theoretic ordinal of Peano arithmetic.

## Explanations

### L1 human

Start with $\omega$, the first infinite ordinal, and keep raising $\omega$ to the power of what you have.
The tower $\omega^{\omega^{\omega^{\cdots}}}$ never ends, and $\varepsilon_0$ is the first ordinal past all of its stages.
It is the first ordinal that does not change when you raise $\omega$ to it.
Every smaller ordinal can be written as a finite expression built from $\omega$, sums and powers.
