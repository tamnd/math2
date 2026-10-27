---
tag: 0D9NDGE9KP
kind: statement
role: proposition
name: Uniqueness of inverses
msc: [20A05]
about: [G5S1M9, 0ZNZH0EXFX]
uses: [G5S1M9, 0BRHKKP333]
formal:
  - system: lean4
    library: mathlib
    decl: eq_inv_of_mul_eq_one_right
    match: stronger
    adapter: Math2.Match.inv_unique
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

### L2 agent

The definition of a group asks for an inverse $b$ with $ab = e$ and $ba = e$. This result shows that one of the two equations is enough, and that the inverse is unique.

The proof uses only associativity and the identity:

1. Suppose that $ab = e$.
2. Multiply on the left by $a^{-1}$: $a^{-1}(ab) = a^{-1}e$.
3. By associativity, the left side is $(a^{-1}a)b = eb = b$.
4. The right side is $a^{-1}$. Thus $b = a^{-1}$.

A worked example in $\mathbb{Z}/7\mathbb{Z}$ under multiplication of the units:

1. We look for the inverse of $3$.
2. We have $3 \cdot 5 = 15 = 2 \cdot 7 + 1$, so $3 \cdot 5 = 1$.
3. By the result, $5$ is the only inverse of $3$. There is no need to check $5 \cdot 3$.

Two standard consequences follow at once. First, $(a^{-1})^{-1} = a$, because $a^{-1}a = e$. Second, $(ab)^{-1} = b^{-1}a^{-1}$, because $(ab)(b^{-1}a^{-1}) = e$.

A common error is to write $(ab)^{-1} = a^{-1}b^{-1}$. This is false when $a$ and $b$ do not commute. In $S_3$, take $a = (1\,2)$ and $b = (1\,3)$: then $a^{-1}b^{-1} = (1\,2)(1\,3)$, but $(ab)^{-1} = (1\,3)(1\,2)$, and these differ.

The step that needs care is step 2. It uses the inverse $a^{-1}$, so the argument is for groups. In a monoid an element can have a right inverse and no left inverse.
