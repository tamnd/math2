---
tag: 06XF7BCFFJ
kind: definition
name: Simple continued fraction
aliases: [regular-continued-fraction]
msc: [11A55]
defines: 0XB0J0P64D
uses: [0BK6JBK58W]
sources:
  - url: https://en.wikipedia.org/wiki/Simple_continued_fraction
    locator: Formulation
---

## Definition

A simple continued fraction is a [[continued fraction|0BK6JBK58W]] whose partial numerators are all $1$.
Its first term $a_0$ is an integer, and its later terms $a_1, a_2, \dots$ are positive integers:
$$[a_0; a_1, a_2, \dots] = a_0 + \cfrac{1}{a_1 + \cfrac{1}{a_2 + \cdots}}$$
The sequence of terms can be finite or infinite.

## Remarks

The $a_n$ are called the partial quotients.
For example, $[2; 3, 4] = 2 + \frac{1}{3 + 1/4} = \frac{30}{13}$.
An infinite simple continued fraction always converges, by the [[convergence of the convergents|0E70M92FE3]].
Each real number has a [[continued fraction expansion|0SJ7Z6VKWK]] of this form.

## Explanations

### L1 human

A simple continued fraction is a list of integers $[a_0; a_1, a_2, \dots]$ that encodes a number.
To read it, start at the end, take a reciprocal, add the next term, and repeat.
