---
tag: 0CBRFQ7DVZ
kind: definition
name: Normal extension
msc: [12F10]
defines: 08S0NW8SES
uses: [09EYMKMSB9, 00X2A9G9W3, 0SHMC00RJV]
sources:
  - url: https://en.wikipedia.org/wiki/Normal_extension
    locator: Definition
---

## Definition

Let $L/K$ be an [[algebraic extension|09EYMKMSB9]].
The extension $L/K$ is normal if every [[irreducible polynomial|00X2A9G9W3]] $f \in K[x]$ that has a root in $L$ [[splits|0SHMC00RJV]] over $L$.

## Remarks

A finite extension $L/K$ is normal if and only if $L$ is the [[splitting field|02NZZ1J0FH]] of some polynomial over $K$.
Every extension of degree $2$ is normal. For example, $\mathbb{Q}(\sqrt{2})/\mathbb{Q}$ is normal.
The extension $\mathbb{Q}(\sqrt[3]{2})/\mathbb{Q}$ is not normal: $x^3 - 2$ has a root in it, but its other two roots are not real.
Normality is not transitive: $\mathbb{Q}(\sqrt[4]{2})/\mathbb{Q}(\sqrt{2})$ and $\mathbb{Q}(\sqrt{2})/\mathbb{Q}$ are normal, but $\mathbb{Q}(\sqrt[4]{2})/\mathbb{Q}$ is not.

## Explanations

### L1 human

A normal extension contains all the roots of a polynomial as soon as it contains one of them.
It has no lopsided gaps, like a field that contains one cube root of $2$ but not the others.
