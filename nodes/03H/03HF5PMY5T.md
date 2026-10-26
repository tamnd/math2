---
tag: 03HF5PMY5T
kind: statement
role: theorem
name: Triangle inequality
msc: [26A03]
uses: [00S7C68D51]
sources:
  - url: https://en.wikipedia.org/wiki/Triangle_inequality
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Absolute_value
    locator: Real numbers
same_as:
  wikidata: Q208216
  wikipedia: Triangle inequality
---

## Statement

For all real numbers $a$ and $b$,
$$|a + b| \le |a| + |b|,$$
where $|\cdot|$ is the [[absolute value|00S7C68D51]].

## Remarks

Proof: $-|a| \le a \le |a|$ and $-|b| \le b \le |b|$. Add these inequalities to get $-(|a| + |b|) \le a + b \le |a| + |b|$.
Equality holds exactly when $a b \ge 0$.
For distances, it gives $|x - z| \le |x - y| + |y - z|$. The [[reverse triangle inequality|0C9S13WKMF]] is a consequence.

## Explanations

### L1 human

The name comes from geometry: one side of a triangle is never longer than the other two sides together.
For numbers, $|a + b|$ can be smaller than $|a| + |b|$ when $a$ and $b$ have opposite signs, for example $|5 + (-3)| = 2 < 8$.
