---
tag: 01VG2A0BHW
kind: statement
role: proposition
name: Bijective iff it has a two-sided inverse
msc: ["03E20"]
uses: [0SNQEF7Z53, 02486SD328, 0DDPZAG5ER]
sources:
  - url: https://en.wikipedia.org/wiki/Inverse_function
    locator: Two-sided inverses
---

## Statement

Let $f \colon A \to B$ be a [[function|0XHDTE5YMZ]].
Then $f$ is [[bijective|0SNQEF7Z53]] if and only if there is a function $g \colon B \to A$ with $g \circ f = \mathrm{id}_A$ and $f \circ g = \mathrm{id}_B$.

## Remarks

The function $g$ is then unique. It is the [[inverse function|0W766JAPSN]] $f^{-1}$.
This statement does not need the axiom of choice: for a bijection, $g(b)$ is the unique $a$ with $f(a) = b$.
If $f$ has a [[left inverse|02486SD328]] $g$ and a [[right inverse|0DDPZAG5ER]] $h$, then $g = h$.

## Explanations

### L1 human

A bijection can be undone in both directions.
Going from $A$ to $B$ and back gives the start point, and going from $B$ to $A$ and back gives the start point too.
