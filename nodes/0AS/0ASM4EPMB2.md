---
tag: 0ASM4EPMB2
kind: definition
name: Ceiling function
msc: [26A09]
defines: 0EA4XFB0EY
uses: [0YVRNEDSVG, 0C4JS9RF5M]
sources:
  - url: https://en.wikipedia.org/wiki/Floor_and_ceiling_functions
    locator: Definition and properties
---

## Definition

Let $x$ be a real number.
The ceiling of $x$, written $\lceil x \rceil$, is the least [[integer|0C4JS9RF5M]] $n$ with $x \le n$.
The ceiling function is the function $\mathbb{R} \to \mathbb{Z}$, $x \mapsto \lceil x \rceil$.

## Remarks

The ceiling and the [[floor|0YVRNEDSVG]] are related by $\lceil x \rceil = -\lfloor -x \rfloor$.
For each real $x$, $x \le \lceil x \rceil < x + 1$.
If $x$ is not an integer, then $\lceil x \rceil = \lfloor x \rfloor + 1$. If $x$ is an integer, then $\lceil x \rceil = \lfloor x \rfloor = x$.

## Explanations

### L1 human

The ceiling of a number rounds it up to a whole number.
If a trip needs $2.1$ buses, then you must order $\lceil 2.1 \rceil = 3$ buses.
