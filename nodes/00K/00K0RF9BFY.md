---
tag: 00K0RF9BFY
kind: definition
name: Multinomial coefficient
msc: [05A10]
defines: 0PCV9EDJM2
sources:
  - url: https://en.wikipedia.org/wiki/Multinomial_theorem
    locator: Multinomial coefficients
inventory: [XM92FVZBV3]
---

## Definition

Let $k_1, \dots, k_m$ be natural numbers and let $n = k_1 + \dots + k_m$.
The multinomial coefficient is the natural number
$$\binom{n}{k_1, k_2, \dots, k_m} = \frac{n!}{k_1!\, k_2! \cdots k_m!}.$$

## Remarks

For $m = 2$ it is the [[binomial coefficient|092GEF38YD]]: $\binom{n}{k, n-k} = \binom{n}{k}$.
It counts the ways to put $n$ distinct objects into $m$ labelled boxes, with $k_i$ objects in box $i$.
It also counts the distinct words that use a letter $a_i$ exactly $k_i$ times. For example, MISSISSIPPI has $\frac{11!}{1!\,4!\,4!\,2!} = 34650$ distinct rearrangements.
It is the coefficient in the [[multinomial theorem|0XFC1VQYEK]].

## Explanations

### L1 human

The multinomial coefficient counts the ways to split $n$ objects into groups of given sizes.
To split 4 people into a group of 2 and two groups of 1, with labelled groups, there are $\frac{4!}{2!\,1!\,1!} = 12$ ways.
