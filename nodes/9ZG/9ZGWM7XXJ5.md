---
tag: 9ZGWM7XXJ5
kind: example
name: The positive integers are not definable in the integers with addition
msc: ["03C07", "03C40"]
topics: [NJDME6F845, AY09KYSW81]
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

Let $\mathcal{Z} = (\mathbb{Z}, +)$ be the [[integers|0C4JS9RF5M]] with addition only, and let $P = \{1, 2, 3, \ldots\}$.
We show that no formula without parameters defines $P$ in $\mathcal{Z}$.

1. Let $h \colon \mathbb{Z} \to \mathbb{Z}$ be $h(a) = -a$.
   It is a bijection, since it is its own inverse, and it preserves addition, since $h(a + b) = -(a + b) = (-a) + (-b) = h(a) + h(b)$.
2. So $h$ is an [[automorphism|DSQ17TNW1C]] of $\mathcal{Z}$.
3. Suppose that a formula $\varphi(x)$ without parameters defines $P$.
4. By [[isomorphism invariance of truth|NDTJ2E895C]], applied to $h$, we have $\mathcal{Z} \models \varphi[a]$ if and only if $\mathcal{Z} \models \varphi[h(a)]$, for every $a \in \mathbb{Z}$.
5. Take $a = 1$.
   Since $1 \in P$, we get $\mathcal{Z} \models \varphi[1]$, and step 4 gives $\mathcal{Z} \models \varphi[-1]$.
6. So $-1 \in P$, which is false.
   Hence no such $\varphi$ exists.

So $P$ is not a [[definable relation|1DQ1M6ZWS4]] of $\mathcal{Z}$ without parameters.
The condition that fails is invariance: every $\emptyset$-definable set is mapped onto itself by every automorphism, and $h(P)$ is the set of negative integers, not $P$.

## Remarks

The same argument shows that the order $<$ is not $\emptyset$-definable in $(\mathbb{Z}, +)$, because $h$ reverses it: $1 < 2$ but $h(1) = -1 > -2 = h(2)$.
Adding multiplication changes the answer.
In $(\mathbb{Z}, +, \cdot)$, Lagrange's four-square theorem gives a definition: $a \in P$ if and only if $a \ne 0$ and $a$ is a sum of four squares.
Here $a \ne 0$ is written $\neg (x + x = x)$, so the whole condition is a formula without parameters.
The argument says nothing about definability with parameters, because $h$ moves every nonzero parameter, and a different method is needed there.

## Explanations

### L1 human

With only addition, the integers look exactly the same when you flip the sign of every number.
Any sentence about $1$ that uses only addition stays true when you replace $1$ by $-1$.
So no description with addition alone can include $1$ and leave out $-1$.
That means no such description picks out exactly the positive numbers.

### L2 human

Here is how a first try fails, exactly as the argument predicts.
Take $\varphi(x) = \neg (x + x = x)$, which looks like it might say "positive".
At $1$ it holds, because $1 + 1 = 2 \ne 1$.
At $-1$ it also holds, because $(-1) + (-1) = -2 \ne -1$.
So $\varphi$ defines $\mathbb{Z} \setminus \{0\}$, not $P$.
Every other attempt meets the same fate, and the automorphism shows this once and for all, without a list of formulas.
Watch out: the method needs a map that preserves addition; a swap of $1$ and $2$ alone is a bijection but not an automorphism.
