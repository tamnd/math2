---
tag: 0D9NDGE9KP
kind: statement
role: proposition
name: Uniqueness of inverses
msc: [20A05]
uses: [G5S1M9, 0BRHKKP333]
sources:
  - url: https://en.wikipedia.org/wiki/Inverse_element
    locator: Definitions and basic properties
---

## Statement

Let $G$ be a [[group|G5S1M9]] with identity element $e$, and let $a, b \in G$.
If $ab = e$, then $b = a^{-1}$.

## Remarks

In particular, each element of a group has exactly one [[inverse|0ZNZH0EXFX]].
The same argument works in a [[monoid|0N6R902FG1]]: if $ba = e$ and $ac = e$, then $b = b(ac) = (ba)c = c$.
Two consequences are $(a^{-1})^{-1} = a$ and $(ab)^{-1} = b^{-1} a^{-1}$.

## Explanations

### L1 human

In a group, you only need to check one equation to know that $b$ is the inverse of $a$.
Multiply $ab = e$ on the left by $a^{-1}$, and you get $b = a^{-1}$.
Thus the notation $a^{-1}$ makes sense: there is only one inverse.
