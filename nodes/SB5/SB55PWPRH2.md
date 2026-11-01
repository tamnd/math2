---
tag: SB55PWPRH2
kind: statement
role: theorem
name: Denjoy–Carleman–Ahlfors theorem
msc: ["30D20", "30D15"]
uses: [0419794R0T, SHF8Z7GMFX, 0JDE56HWQ8]
about: [0419794R0T, SHF8Z7GMFX]
sources:
  - url: https://en.wikipedia.org/wiki/Denjoy%E2%80%93Carleman%E2%80%93Ahlfors_theorem
same_as:
  wikidata: Q17097849
  wikipedia: Denjoy–Carleman–Ahlfors theorem
---

## Statement

Let $f$ be an [[entire function|0419794R0T]] of [[order|SHF8Z7GMFX]] $\rho$.
Call $a \in \C$ a finite asymptotic value of $f$ if there is a continuous curve $\gamma \colon [0, 1) \to \C$ with $\gamma(t) \to \infty$ and $f(\gamma(t)) \to a$ as $t \to 1$.
If $f$ has $n \ge 1$ distinct finite asymptotic values, then $n \le 2\rho$.

## Remarks

Between two curves along which $f$ tends to different finite limits, $f$ must be unbounded, so $f$ has at least $n$ separate regions near $\infty$ where $\abs{f}$ is large.
Ahlfors's proof bounds the growth of $f$ in such regions with an estimate for conformal maps of strip-like domains.
This estimate is now called the Ahlfors distortion theorem.
It is proved by the length–area method, which later grew into the theory of [[extremal length|HX72KT9D0G]].
For example, $e^z$ has order $1$ and the single finite asymptotic value $0$, reached along the negative real axis, so $1 \le 2$.
For $n = 1$ the theorem says that an entire function of order less than $1/2$ has no finite asymptotic value.

## Explanations

### L1 human

An asymptotic value is a limit that the function approaches along some road to infinity.
The theorem says that an entire function cannot have many different such limits unless it grows fast.
Each extra finite limit costs half a unit of order.

### L2 human

The order is defined by $\rho = \limsup_{r \to \infty} \log \log M(r)/\log r$, where $M(r)$ is the maximum of $\abs{f}$ on $\abs{z} = r$.
The case $n = 1$ is consistent with the $\cos \pi\rho$ theorem, which shows that functions of order less than $1/2$ are large on a sequence of whole circles.
The method of the proof, through extremal length and conformal invariants, became a central tool of geometric function theory.
