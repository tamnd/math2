---
tag: 5A6KND2VR5
kind: statement
role: lemma
name: Fundamental lemma of the combinatorial sieve
sources:
  - wikipedia: en:18826584@r1310515719
    locator: Fundamental lemma of sieve theory, section Fundamental lemma of the combinatorial sieve
    note: adopted
    mention: wikipedia://en/18826584#XYK6
    sections: [Statement]
inventory: [RD75CH431S]
---

## Statement

This formulation is from Tenenbaum. Other formulations are in Halberstam & Richert, in Greaves, and in Friedlander & Iwaniec. We make the assumptions:

- $w(d)$ is a [[multiplicative function|0AP80TT660]].
- The sifting density $\kappa$ satisfies, for some constant $C$ and any real numbers $\eta$ and $\xi$ with $2\leq \eta\leq \xi$:

$$\prod_{\eta \le p \le \xi} \left( 1 - \frac{w(p)}{p} \right) ^{-1} < \left( \frac{\ln \xi}{\ln \eta} \right) ^\kappa \left( 1 + \frac{C}{\ln \eta} \right).$$

There is a parameter $u\geq 1$ that is at our disposal. We have uniformly in $A$, *$X$*, *$z$*, and $u$ that

$$S(a,P,z) = X \prod_{p \le z, p \in P} \left( 1 - \frac{w(p)}{p} \right) \{1 + O(u^{-u/2})\} + O\left(\sum_{d \le z^u, d|P(z)} |R_d| \right).$$

In applications we pick *$u$* to get the best error term. In the sieve it is related to the number of levels of the [[inclusion–exclusion principle|0FF7726C7P]].
