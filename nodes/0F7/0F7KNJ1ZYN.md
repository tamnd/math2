---
tag: 0F7KNJ1ZYN
kind: definition
name: Greatest common divisor in an integral domain
msc: [13A05]
defines: 0ZAF9KHDDF
uses: [04GNK7K4VP, 053E86NWVK, 09S3PFBEPM]
sources:
  - url: https://en.wikipedia.org/wiki/GCD_domain
    locator: lead section
---

## Definition

Let $R$ be an [[integral domain|09S3PFBEPM]] and let $a, b \in R$.
An element $d \in R$ is a greatest common divisor of $a$ and $b$ if it has these two properties.

1. $d \mid a$ and $d \mid b$.
2. For every $c \in R$ with $c \mid a$ and $c \mid b$, $c \mid d$.

## Remarks

If $d$ and $d'$ are two greatest common divisors of $a$ and $b$, then $d$ and $d'$ are [[associates|053E86NWVK]].
In $\mathbb{Z}$, the greatest common divisors of $12$ and $18$ are $6$ and $-6$.
A greatest common divisor need not exist. A GCD domain is an integral domain in which every pair of elements has one.
In a [[principal ideal domain|0RZYDVZ475]], $d$ is a greatest common divisor of $a$ and $b$ if and only if $(a, b) = (d)$.

## Explanations

### L1 human

In a general ring, "greatest" does not refer to size.
It means the largest for divisibility: every other common divisor divides it.
For the integers, this gives the usual gcd, up to the sign.
