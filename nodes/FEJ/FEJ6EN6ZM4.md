---
tag: FEJ6EN6ZM4
kind: statement
role: lemma
name: Fundamental lemma of the Selberg sieve
sources:
  - wikipedia: en:18826584@r1310515719
    locator: Fundamental lemma of sieve theory, section Fundamental lemma of the Selberg sieve
    note: adopted
    mention: wikipedia://en/18826584#AG2H
    sections: [Statement]
inventory: [MHVDPFN3YV]
---

## Statement

This formulation is from Halberstam & Richert. Another formulation is in Diamond & Halberstam.

We make the assumptions:

- $w(d)$ is a [[multiplicative function|0AP80TT660]].
- The sifting density $\kappa$ satisfies, for some constant $C$ and any real numbers $\eta$ and $\xi$ with $2\leq \eta\leq \xi$:

$$\qquad \sum_{\eta \le p \le \xi} \frac{w(p) \ln p}{p} < \kappa \ln \frac{\xi}{\eta} + C.$$

- *$\frac{w(p)}{p} < 1-c$* for some small fixed *$c$* and all *$p$*.
- *$|R(d)|\leq w(d)$* for all squarefree *$d$* whose prime factors are in *$P$*.

The fundamental lemma has almost the same form as for the combinatorial sieve. Write *$u = \ln{X} /\ln{z}$*. The conclusion is:

$$S(a,P,z) = X \prod_{p \le z,\ p \in P} \left( 1 - \frac{w(p)}{p} \right) \{1 + O(e^{-u/2})\}.$$

Note that *$u$* is no longer an independent parameter at our disposal, but is controlled by the choice of *$z$*.

Note that the error term here is weaker than for the fundamental lemma of the combinatorial sieve. Halberstam & Richert remark: "Thus it is not true to say, as has been asserted from time to time in the literature, that Selberg's sieve is always better than Brun's."
