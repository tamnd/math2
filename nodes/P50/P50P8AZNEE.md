---
tag: P50P8AZNEE
kind: example
name: The successor relation is definable in the integers with order
msc: ["03C07", "06A05"]
topics: [NJDME6F845, AY09KYSW81]
audience: ug2
instance_of: [CY1TXHF6KQ]
uses: [1DQ1M6ZWS4, 0C4JS9RF5M, P33CMYHJW9, NDTJ2E895C]
sources:
  - url: https://en.wikipedia.org/wiki/Definable_set
    locator: lead section
---

## Example

Let $\mathcal{Z} = (\mathbb{Z}, <)$ be the [[integers|0C4JS9RF5M]] with the usual [[strict order|P33CMYHJW9]], and let
$$\varphi(x, y) = x < y \wedge \neg \exists z \, (x < z \wedge z < y).$$
We show that $\varphi$ defines the successor relation $S = \{ (a, a + 1) : a \in \mathbb{Z} \}$.

1. Let $a, b \in \mathbb{Z}$.
   By the clauses for $\wedge$, $\neg$ and $\exists$, we have $\mathcal{Z} \models \varphi[a, b]$ if and only if $a < b$ and no $c \in \mathbb{Z}$ satisfies $a < c < b$.
2. If $b = a + 1$, then $a < b$, and no integer lies strictly between $a$ and $a + 1$.
   So $\varphi[a, b]$ holds.
3. If $a < b$ and $b \ne a + 1$, then $b \ge a + 2$, and $c = a + 1$ satisfies $a < c < b$.
   So $\varphi[a, b]$ fails.
4. If $a < b$ is false, then $\varphi[a, b]$ fails at its first conjunct.

So $S$ is a [[definable relation|1DQ1M6ZWS4]] of $\mathcal{Z}$ without parameters, even though the signature has no function symbol.

## Remarks

The same formula defines the empty relation in $(\mathbb{Q}, <)$, because between two rationals $a < b$ there is always a third one, $(a + b)/2$.
No single integer is $\emptyset$-definable in $\mathcal{Z}$, because the shift $n \mapsto n + 1$ is an automorphism that moves every element; this uses [[isomorphism invariance of truth|NDTJ2E895C]].
With the parameter $0$, every integer becomes definable.
For example, $1$ is the unique $y$ with $\varphi(0, y)$, and $2$ is the unique $y$ with $\exists z \, (\varphi(0, z) \wedge \varphi(z, y))$.

## Explanations

### L1 human

In the integers ordered by size, $b$ comes right after $a$ when $b$ is bigger and nothing fits between them.
That description uses only "is less than", so it is a formula of the language.
For $4$ and $5$ nothing fits between, but for $4$ and $7$ the number $5$ fits.

### L2 human

We check the formula on two pairs.
For $(4, 5)$, we have $4 < 5$, and no integer $c$ has $4 < c < 5$, so $\varphi[4, 5]$ holds.
For $(4, 7)$, the integer $c = 5$ gives
$$4 < 5 < 7,$$
so the second conjunct fails, and $\varphi[4, 7]$ fails.
The typical use is to recover a function, here $n \mapsto n + 1$, from a relation by a formula.
Watch out: the formula defines the successor only in discrete orders like $\mathbb{Z}$; in a dense order such as $\mathbb{Q}$ it defines nothing at all.
