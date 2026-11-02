---
tag: 5NPVX29Y0C
kind: concept
name: Rounding
msc: [65G50, 65Y04]
sources:
  - url: https://en.wikipedia.org/wiki/Rounding
same_as:
  wikidata: Q663208
  wikipedia: Rounding
---

## Summary

Rounding replaces a number by a nearby number from a fixed set, such as the integers, the numbers with two decimals, or the [[floating-point numbers|RTKRSC3KPH]].
Rounding to nearest picks the closest element and needs a rule for ties, such as rounding half to even.
Directed rounding always goes down, up or toward zero; the [[floor function|08GR54CKEA]] is rounding down to an integer.
In a computer every arithmetic result is rounded, and the difference is the [[round-off error|CPN6SD3BTV]].

## Explanations

### L1 human

Rounding makes a number shorter and simpler, at the price of a small error.
A price of $3.47$ euros rounded to whole euros is $3$; rounded to one decimal it is $3.5$.
The number $2.5$ is exactly halfway between $2$ and $3$, so one needs a tie rule: "half up" gives $3$, "half to even" gives $2$.
Rounding half to even avoids a systematic upward drift when many rounded numbers are added.
