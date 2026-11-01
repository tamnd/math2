---
tag: XPBQEJNYJ6
kind: statement
role: proposition
name: Nesbitt's inequality
msc: [26D20]
uses: [0RFWW56Y22, 0DRF0F3XC9]
about: []
sources:
  - url: https://en.wikipedia.org/wiki/Nesbitt%27s_inequality
same_as:
  wikidata: Q370642
  wikipedia: Nesbitt's inequality
---

## Statement

Let $a, b, c$ be positive real numbers.
Then
$$\frac{a}{b + c} + \frac{b}{c + a} + \frac{c}{a + b} \ge \frac{3}{2},$$
with equality if and only if $a = b = c$.

## Remarks

Proof idea: let $s = a + b + c$.
Adding $1$ to each fraction gives $\frac{a}{b+c} + 1 = \frac{s}{b+c}$, so the left side equals $s \big( \frac{1}{b+c} + \frac{1}{c+a} + \frac{1}{a+b} \big) - 3$.
By the [[Cauchy–Schwarz inequality|0RFWW56Y22]], or the inequality between arithmetic and harmonic means, $\big((b+c) + (c+a) + (a+b)\big)\big(\frac{1}{b+c} + \frac{1}{c+a} + \frac{1}{a+b}\big) \ge 9$.
Since the first factor is $2s$, the left side is at least $\frac{9}{2} - 3 = \frac{3}{2}$.

Example: $a = b = 1$, $c = 2$ gives $\frac{1}{3} + \frac{1}{3} + 1 = \frac{5}{3} \ge \frac{3}{2}$.

There is no upper bound: for $a = b = 1$ and $c \to \infty$ the left side tends to $\infty$.

## Explanations

### L1 human

Divide each of three positive numbers by the sum of the other two and add the results.
You always get at least $\frac{3}{2}$, and you get exactly $\frac{3}{2}$ only when the three numbers are equal.

### L2 human

Nesbitt's inequality is a standard first example of a symmetric inequality in three variables.
It has many proofs: by the means inequalities, by the [[rearrangement inequality|6E9TAF8HCY]], or by clearing denominators and using [[Muirhead's inequality|PBPFVY20WT]].
Comparing the proofs is a good way to learn the toolbox of elementary inequalities.
