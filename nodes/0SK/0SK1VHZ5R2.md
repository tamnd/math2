---
tag: 0SK1VHZ5R2
kind: statement
role: theorem
name: Irreducibility of the cyclotomic polynomials over the rationals
msc: [11R18]
uses: [0W0KVBM54S, 00X2A9G9W3]
sources:
  - url: https://en.wikipedia.org/wiki/Cyclotomic_polynomial
    locator: Properties
---

## Statement

For every integer $n \ge 1$, the [[cyclotomic polynomial|0W0KVBM54S]] $\Phi_n$ is [[irreducible|00X2A9G9W3]] in $\mathbb{Q}[x]$.

## Remarks

For $n = p$ prime, [[Eisenstein's criterion|02BPKD7TMD]] applied to $\Phi_p(x + 1)$ with the prime $p$ proves the statement.
The general case is harder. One proof shows that if $\zeta$ is a root of an irreducible factor of $\Phi_n$, then so is $\zeta^p$ for each prime $p \nmid n$.
A consequence: $\Phi_n$ is the [[minimal polynomial|0GK1WB9R98]] over $\mathbb{Q}$ of each primitive $n$-th root of unity. So the degree of $\mathbb{Q}(e^{2\pi i/n})$ over $\mathbb{Q}$ is $\varphi(n)$.

## Explanations

### L1 human

The polynomial $\Phi_n$ cannot be split into smaller polynomials with rational coefficients.
So all the primitive $n$-th roots of unity are conjugate over the rationals: no rational polynomial equation separates them.
