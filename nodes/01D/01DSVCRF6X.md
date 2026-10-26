---
tag: 01DSVCRF6X
kind: definition
name: Ramsey number
msc: [05C55, 05D10]
defines: 0K9QVPJYJF
sources:
  - url: https://en.wikipedia.org/wiki/Ramsey's_theorem
    locator: lead section
---

## Definition

Let $r$ and $s$ be positive integers.
The Ramsey number $R(r, s)$ is the least positive integer $n$ with this property.
Colour each edge of the [[complete graph|03WKB2H474]] $K_n$ blue or red, in any way.
Then there is a blue [[clique|0G52BPNPKG]] with $r$ vertices or a red clique with $s$ vertices.

## Remarks

Such an $n$ exists by [[Ramsey's theorem|00TQV3F5S4]].
$R(r, s) = R(s, r)$ and $R(r, 2) = r$. The [[theorem on friends and strangers|0NYM0ZGAK9]] gives $R(3, 3) = 6$.
With more colours there are similar numbers, for example $R(3, 3, 3) = 17$.

## Explanations

### L1 human

The Ramsey number $R(r, s)$ is the size of a party that is large enough for one of two things to happen.
There are $r$ people who all know each other, or $s$ people who are all strangers to each other.
