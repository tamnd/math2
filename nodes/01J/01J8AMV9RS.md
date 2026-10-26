---
tag: 01J8AMV9RS
kind: definition
name: Legendre symbol
msc: [11A15]
defines: 0JTC045NNZ
uses: [0SQDB87Z3T, 0SN0MAEKYX]
sources:
  - url: https://en.wikipedia.org/wiki/Legendre_symbol
    locator: Definition
---

## Definition

Let $p$ be an odd [[prime number|0SN0MAEKYX]] and let $a$ be an integer.
The Legendre symbol $\left(\frac{a}{p}\right)$ is the number
$$\left(\frac{a}{p}\right) = \begin{cases} 0 & \text{if } p \mid a, \\ 1 & \text{if } p \nmid a \text{ and } a \text{ is a quadratic residue modulo } p, \\ -1 & \text{if } a \text{ is a quadratic nonresidue modulo } p. \end{cases}$$
Here quadratic residue has the meaning of the [[definition of a quadratic residue|0SQDB87Z3T]].

## Remarks

The value depends only on the class of $a$ modulo $p$.
For example, $\left(\frac{2}{7}\right) = 1$ because $3^2 \equiv 2 \pmod 7$, and $\left(\frac{3}{7}\right) = -1$.
[[Euler's criterion|0M7DEDKSYB]] gives the value as $a^{(p-1)/2}$ modulo $p$.
The [[law of quadratic reciprocity|085MJS6907]] helps to compute the symbol quickly.

## Explanations

### L1 human

The Legendre symbol is a short way to say whether $a$ is a square modulo $p$.
The value $1$ means yes, the value $-1$ means no, and the value $0$ means that $a$ is $0$ modulo $p$.
