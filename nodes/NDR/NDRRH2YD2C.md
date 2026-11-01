---
tag: NDRRH2YD2C
kind: conjecture
name: Lehmer's conjecture
msc: [11R06, 11C08]
uses: [QVPYBPRHRC, 08KEYFAH66]
about: [QVPYBPRHRC]
sources:
  - url: https://en.wikipedia.org/wiki/Lehmer%27s_conjecture
same_as:
  wikidata: Q6518929
  wikipedia: Lehmer's conjecture
history:
  posed_by: "Derrick Henry Lehmer"
  first_stated: "1933"
---

## Statement

For a nonzero polynomial $f \in \Z[x]$, let $M(f)$ be its [[Mahler measure|QVPYBPRHRC]].
There is a constant $c > 1$ such that $M(f) \ge c$ for every $f \in \Z[x]$ with $M(f) > 1$.

## Remarks

The condition $M(f) > 1$ excludes exactly the polynomials $\pm x^k \Phi_{n_1} \cdots \Phi_{n_r}$ built from [[cyclotomic polynomials|08KEYFAH66]], which have $M(f) = 1$.
The problem goes back to D. H. Lehmer, who asked it in 1933.
The conjecture is open.
The smallest known value of $M(f) > 1$ is that of Lehmer's polynomial $x^{10} + x^9 - x^7 - x^6 - x^5 - x^4 - x^3 + x + 1$, about $1.17628$.
Smyth proved the conjecture for nonreciprocal polynomials.
If $f \in \Z[x]$ is irreducible of degree $d$, $f \ne \pm x$, and $x^d f(1/x) \ne \pm f(x)$, then $M(f) \ge M(x^3 - x - 1) \approx 1.3247$.
Dobrowolski proved a lower bound of the form $M(f) \ge 1 + c \left( \frac{\log \log d}{\log d} \right)^3$ for an irreducible noncyclotomic $f$ of degree $d$, with an absolute constant $c > 0$.

## Explanations

### L1 human

The Mahler measure of an integer polynomial is at least $1$, and it equals $1$ only for products of cyclotomic polynomials and powers of $x$.
The conjecture says that there is a gap: the next possible values cannot come arbitrarily close to $1$.
The best candidate for the smallest value above $1$ has been known for almost a century.
