---
tag: 0P7CH1CND5
kind: definition
name: Characteristic of a ring
msc: [13A99]
defines: 0F6ES3BRYP
uses: [0894J980RK]
sources:
  - url: https://en.wikipedia.org/wiki/Characteristic_(algebra)
    locator: lead section
---

## Definition

Let $R$ be a [[ring|0894J980RK]].
For a positive integer $n$, write $n \cdot 1 = 1 + 1 + \dots + 1$, with $n$ terms.
If there is a positive integer $n$ with $n \cdot 1 = 0$ in $R$, then the characteristic of $R$ is the least such $n$.
If there is no such $n$, then the characteristic of $R$ is $0$.

## Remarks

The rings $\mathbb{Z}$, $\mathbb{Q}$, $\mathbb{R}$ and $\mathbb{C}$ have characteristic $0$.
For $n \ge 1$, the ring $\mathbb{Z}/n\mathbb{Z}$ has characteristic $n$.
The characteristic of $R$ is the nonnegative generator of the kernel of the unique ring homomorphism $\mathbb{Z} \to R$.
The [[characteristic of an integral domain is zero or prime|00758QM6JJ]].

## Explanations

### L1 human

Start with $1$ and keep adding $1$.
In the integers you never come back to $0$, so the characteristic is $0$.
Modulo $5$, you get $0$ after five steps, so the characteristic is $5$.
