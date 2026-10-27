---
tag: 0G01TS1RRP
kind: definition
name: Deficient number
msc: [11A25]
defines: 0MXFJ0J00R
uses: [009QCP5T3Z]
sources:
  - url: https://en.wikipedia.org/wiki/Deficient_number
    locator: lead section
inventory: [11EPCM4WQC]
---

## Definition

A positive integer $n$ is deficient if the sum of its positive divisors other than $n$ is less than $n$.
Equivalently, $\sigma(n) < 2n$, where $\sigma$ is the [[sum of divisors|009QCP5T3Z]].

## Remarks

Each prime $p$ is deficient, since its only smaller divisor is $1$.
More generally, each prime power is deficient. For example, $1 + 2 + 4 = 7 < 8$.
Each divisor of a deficient number or of a [[perfect number|0SB7Q8SYSF]], other than the number itself, is deficient.

## Explanations

### L1 human

A deficient number has "too few" divisors: its smaller divisors add up to less than the number.
Most small numbers are deficient, for example $1, 2, 3, 4, 5, 7, 8, 9, 10$.
