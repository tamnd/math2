---
tag: VCGF9YR36X
kind: conjecture
name: Riemann hypothesis
msc: [11M26]
uses: [1XWBY4N0VT, NFXKNDJX9C]
about: [1XWBY4N0VT]
sources:
  - url: https://en.wikipedia.org/wiki/Riemann_hypothesis
same_as:
  wikidata: Q205966
  wikipedia: Riemann hypothesis
history:
  posed_by: "Bernhard Riemann"
  first_stated: "1859"
---

## Statement

Let $\zeta$ be the [[Riemann zeta function|1XWBY4N0VT]].
Every zero $s$ of $\zeta$ with $0 < \operatorname{Re} s < 1$ satisfies $\operatorname{Re} s = \frac{1}{2}$.

## Remarks

The zeros of $\zeta$ are the trivial zeros $-2, -4, -6, \dots$ and the nontrivial zeros, which lie in the strip $0 < \operatorname{Re} s < 1$.
This follows from the [[functional equation|NFXKNDJX9C]] and the [[non-vanishing on the line Re s = 1|CXES7915R7]].
So the conjecture says that every nontrivial zero lies on the critical line $\operatorname{Re} s = 1/2$.
The first nontrivial zeros are at about $\frac{1}{2} \pm 14.1347 i$.
The conjecture is open.
Riemann stated it in his 1859 paper on the number of primes below a given size.
It is one of Hilbert's problems of 1900 and one of the Clay Millennium Prize Problems.
Known partial results: Hardy proved that infinitely many zeros lie on the critical line, and Selberg proved that a positive proportion of them do.
An equivalent form: $\pi(x) = \operatorname{li}(x) + O(\sqrt{x} \log x)$, where $\pi$ is the [[prime-counting function|0RQSNVTFVZ]] and $\operatorname{li}(x) = \int_2^x dt / \log t$.
The [[generalized Riemann hypothesis|DNKA4WBKDS]] states the same for [[Dirichlet L-functions|9D2Z543EJQ]] and other L-functions.

## Explanations

### L1 human

The zeta function has infinitely many zeros in a vertical strip of the complex plane.
Riemann guessed that all of them lie exactly on the middle line of this strip.
If true, the primes are distributed as regularly as possible: the number of primes up to $x$ differs from its smooth approximation by roughly $\sqrt{x}$ only.
