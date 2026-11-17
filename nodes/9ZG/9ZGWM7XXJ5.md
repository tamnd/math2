---
tag: 9ZGWM7XXJ5
kind: example
name: The positive integers are not definable in the integers with addition
msc: ["03C07", "03C40"]
topics: [NJDME6F845]
audience: ug2
not_instance_of:
  - target: CY1TXHF6KQ
    note: the set of positive integers is not definable without parameters in (Z, +), because the automorphism x to -x moves it
uses: [1DQ1M6ZWS4, NDTJ2E895C, DSQ17TNW1C, 0C4JS9RF5M]
sources:
  - url: https://en.wikipedia.org/wiki/Definable_set
    locator: lead section
---

## Example

Let $\mathcal{Z} = (\Z, +)$ be the [[integers|0C4JS9RF5M]] with addition only, and let $P = \set{1, 2, 3, \ldots}$.
We show that $P$ is not $\emptyset$-definable in $\mathcal{Z}$.

1. Let $h \colon \Z \to \Z$ be $h(a) = -a$. Then $h$ is a bijection, and $h(a + b) = -a - b = h(a) + h(b)$.
2. So $h$ is an [[automorphism|DSQ17TNW1C]] of $\mathcal{Z}$.
3. Suppose $\varphi(x)$ is a formula without parameters that defines $P$.
4. By [[isomorphism invariance of truth|NDTJ2E895C]], $\mathcal{Z} \models \varphi[a]$ if and only if $\mathcal{Z} \models \varphi[h(a)]$, for all $a \in \Z$.
5. Take $a = 1$. Then $\mathcal{Z} \models \varphi[1]$, because $1 \in P$, so $\mathcal{Z} \models \varphi[-1]$.
6. So $-1 \in P$, which is false. Hence no such $\varphi$ exists.

So $P$ is not a [[definable relation|1DQ1M6ZWS4]] of $\mathcal{Z}$ without parameters.
The condition that fails is invariance: every $\emptyset$-definable set is mapped onto itself by every automorphism, and $h(P) \neq P$.

## Remarks

The same argument shows that the order $<$ is not $\emptyset$-definable in $(\Z, +)$, because $h$ reverses it.
In contrast, $P$ is $\emptyset$-definable in $(\Z, +, \cdot)$: by Lagrange's four-square theorem, $a \in P$ if and only if $a \neq 0$ and $a$ is a sum of four squares.
The argument says nothing about definability with parameters, because $h$ moves every nonzero parameter.

## Explanations

### L1 human

With only addition, the integers look the same when you flip the sign of every number.
Any formula that is true of $1$ is then true of $-1$.
So no formula can pick out exactly the positive numbers.

### L2 human

We test the candidate formula $\varphi(x) = \neg (x + x = x)$, which is a natural first try.

1. $\varphi$ holds at $1$, because $1 + 1 \neq 1$.
2. $\varphi$ also holds at $-1$, because $-2 \neq -1$.

So $\varphi$ defines $\Z \setminus \set{0}$, not $P$, as the automorphism argument predicts.
The typical use is to prove non-definability without a list of all formulas.
A trap is to use an automorphism that does not preserve addition, such as a swap of $1$ and $2$ only.
