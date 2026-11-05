---
tag: EXAH6KRGF4
kind: statement
role: proposition
name: Approximate Plancherel inequality
sources:
  - wikipedia: en:1967859@r1308193592
    locator: Large sieve, section Development > Approximate Plancherel inequality
    note: adopted
    mention: wikipedia://en/1967859#K0KS
    sections: [Statement]
inventory: [KNZRPKCG3Z]
---

## Statement

If a set $S$ is ill-distributed modulo $p$ (by virtue, for example, of being excluded from the congruence classes $A_p$) then the Fourier coefficients $\widehat{f_p}(a)$ of the characteristic function $f_p$ of the set $S\bmod p$ are in average large. These coefficients can be lifted to values $\widehat{f}(a/p)$ of the Fourier transform $\widehat{f}$ of the characteristic function $f$ of the set $S$, that is,

$$\widehat{f}(a/p)=\widehat{f_p}(a).$$

Bounding derivatives shows see that $\widehat{f}(x)$ must be large, on average, for all $x$ near rational numbers of the form $a/p$. *Large* here means "a relatively large constant times $|S|$". Since

$$|f|_2 = \sqrt{|S|},$$

there is a contradiction with the Plancherel identity

$$|\widehat{f}|_2=|f|_2$$

unless $|S|$ is small. (In practice, to optimise bounds, people nowadays modify the Plancherel identity into an equality rather than bound derivatives as above.)
