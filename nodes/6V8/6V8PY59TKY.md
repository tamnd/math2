---
tag: 6V8PY59TKY
kind: proof
name: Proof that there is a natural number n with 1/n below any positive epsilon
msc: [26A03]
proves: 0WH916TJNY
uses: [0A3GWZ86AY, 0QSPNASE50, 010JCV9J4E]
sources:
  - url: https://en.wikipedia.org/wiki/Archimedean_property
    locator: Ordered fields
---

## Proof

1. Let $\varepsilon$ be a real number with $\varepsilon > 0$.
2. Since the [[reals are Archimedean|0A3GWZ86AY]], applied with $x = 1$ and $y = \varepsilon$, there is a natural number $n$ with $n \varepsilon > 1$.
3. We have $n \ge 1$. Indeed, for $n = 0$ we would get $0 \cdot \varepsilon = 0 > 1$, but $0 < 1$ in each [[ordered field|010JCV9J4E]].
4. In the [[ordered field|0QSPNASE50]] $\R$, if $a < b$ and $c > 0$, then $a c < b c$. Indeed, $(b - a) c \ge 0$ by the product axiom, and $(b - a) c \ne 0$ because both factors are nonzero.
5. Since $0 < 1$ and $n \ge 1$, adding $1$ repeatedly gives $0 < n$. The number $1/n$ is positive. It is nonzero. If $1/n < 0$, then $-1/n > 0$, and step 4 with $0 < n$ gives $0 < n \cdot (-1/n) = -1$, which is false.
6. Multiply $1 < n \varepsilon$ by $1/n > 0$, using step 4. This gives $1/n < \varepsilon$.

## Idea

The Archimedean property says that enough copies of $\varepsilon$ exceed $1$. Dividing $n \varepsilon > 1$ by $n$ gives $1/n < \varepsilon$.
