---
tag: DNKA4WBKDS
kind: conjecture
name: Generalized Riemann hypothesis
msc: [11M26, 11M06]
uses: [7XB5VJKDPG, 9D2Z543EJQ, 00GC8ZQP4Q, KXS5DQDFYD, MWBDFS2KJ5, 5VBZBXSFDQ]
about: [9D2Z543EJQ, VCGF9YR36X]
sources:
  - url: https://en.wikipedia.org/wiki/Generalized_Riemann_hypothesis
same_as:
  wikidata: Q685140
  wikipedia: Generalized Riemann hypothesis
history:
  posed_by: "Adolf Piltz"
  first_stated: "1884"
---

## Statement

Let $\chi$ be a [[Dirichlet character|7XB5VJKDPG]] and let $L(s, \chi)$ be its [[Dirichlet L-function|9D2Z543EJQ]], continued to all of $\C$.
Then every [[zero|00GC8ZQP4Q]] $s$ of $L(s, \chi)$ with $0 < \operatorname{Re} s < 1$ satisfies $\operatorname{Re} s = 1/2$.

## Remarks

The conjecture is open.
For the principal character modulo $1$, $L(s, \chi)$ is the Riemann zeta function, so the conjecture contains the [[Riemann hypothesis|VCGF9YR36X]].
The extended Riemann hypothesis makes the same claim for the [[Dedekind zeta function|KXS5DQDFYD]] of every [[number field|MWBDFS2KJ5]].
The conjecture implies that there is no [[Siegel zero|5VBZBXSFDQ]].
It also implies $\psi(x; q, a) = x/\varphi(q) + O(x^{1/2} (\log x)^2)$ for all $q \le x$ and all $a$ coprime to $q$, with an absolute implied constant.
Under the conjecture, the Miller test becomes a deterministic primality test: it suffices to test the bases $a < 2(\ln n)^2$, a bound of Bach.
The [[Bombieri–Vinogradov theorem|B3JMY54GJF]] proves an average form of these consequences without any hypothesis.

## Explanations

### L1 human

The Riemann hypothesis says where the zeros of the Riemann zeta function lie: all the nontrivial ones are on one vertical line.
The generalized Riemann hypothesis says the same thing for a whole family of similar functions, the Dirichlet L-functions, one for each way of sorting numbers by residue classes.
If it is true, primes are spread over residue classes as evenly as one could hope, with a small and explicit error.
Many results in number theory and in the analysis of algorithms are first proved under this hypothesis.
