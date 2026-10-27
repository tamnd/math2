---
tag: 0YVRNEDSVG
kind: definition
name: Floor function
msc: [26A09]
defines: 08GR54CKEA
uses: [0A3GWZ86AY, 0C4JS9RF5M]
sources:
  - url: https://en.wikipedia.org/wiki/Floor_and_ceiling_functions
    locator: Definition and properties
inventory: [BEWT00TARS]
---

## Definition

Let $x$ be a real number.
The floor of $x$, written $\lfloor x \rfloor$, is the greatest [[integer|0C4JS9RF5M]] $n$ with $n \le x$.
The floor function is the function $\mathbb{R} \to \mathbb{Z}$, $x \mapsto \lfloor x \rfloor$.

## Remarks

The greatest such integer exists because the [[reals are Archimedean|0A3GWZ86AY]] and because of the [[well-ordering principle|01BX15HSRR]].
For each integer $n$, $\lfloor n \rfloor = n$. For example, $\lfloor \pi \rfloor = 3$ and $\lfloor -0.5 \rfloor = -1$.
The [[characterization of the floor|0R9B0B5458]] gives an equivalent definition.

## Explanations

### L1 human

The floor of a number rounds it down to a whole number.
On the number line, it is the nearest integer at the number or to its left.
For negative numbers, take care: the floor of $-1.2$ is $-2$, not $-1$.
