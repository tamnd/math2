---
tag: C2F2D75YSA
kind: example
name: Goodstein's theorem is a sentence of true arithmetic not provable in PA
msc: ["03F30", "03F40"]
topics: [QHCRN4JVG0]
audience: grad
instance_of: [DX0KPMH4QZ]
uses: [DX0KPMH4QZ, XQMNJF241J, HACXBCM7SS, 5NVA2JRHPV, 0ZHQMQ2C1N]
sources:
  - url: https://en.wikipedia.org/wiki/Goodstein%27s_theorem
    locator: lead section
  - url: https://en.wikipedia.org/wiki/True_arithmetic
    locator: Definition
---

## Example

[[Goodstein's theorem|XQMNJF241J]] says that every Goodstein sequence reaches $0$.
The Goodstein sequence of $m$ starts with $G_1(m) = m$.
To get $G_{k+1}(m)$, write $G_k(m)$ in hereditary base $k + 1$, replace every $k + 1$ by $k + 2$, and subtract $1$.
We show that the theorem is a sentence of [[true arithmetic|DX0KPMH4QZ]] that [[Peano arithmetic|HACXBCM7SS]] does not prove.

1. The function $g(m, k) = G_k(m)$ is [[primitive recursive|5NVA2JRHPV]], so a $\Sigma_1$ formula $\gamma(m, k, v)$ defines its graph in $\mathfrak{N}$.
2. The theorem is the sentence $\forall m \, \exists k \, \exists v \, (\gamma(m, k, v) \land v = 0)$ of $L_A$, a $\Pi_2$ sentence.
3. The sentence is true in $\mathfrak{N}$. Goodstein's proof replaces each base by $\omega$ and gets a strictly decreasing sequence of ordinals below $\varepsilon_0$. Such a sequence is finite, by the well-ordering of the ordinals.
4. By step 3, the sentence belongs to $\mathrm{TA}$.
5. Kirby and Paris proved in 1982 that $\mathsf{PA}$ does not prove the sentence. We cite this.

So $\mathrm{TA}$ contains a natural combinatorial $\Pi_2$ sentence that $\mathsf{PA}$ does not prove.

## Remarks

Step 3 uses [[transfinite induction|0ZHQMQ2C1N]] up to $\varepsilon_0$, which $\mathsf{PA}$ cannot carry out in full.
Each single instance, "the sequence of $\overline{m}$ reaches $0$", is a true $\Sigma_1$ sentence, so $\mathsf{PA}$ proves it, even $\mathsf{Q}$ does.
What $\mathsf{PA}$ misses is the uniform statement over all $m$.
The function $m \mapsto$ (least $k$ with $G_k(m) = 0$) grows too fast to be provably total in $\mathsf{PA}$.
Unlike $\mathrm{Con}(\mathsf{PA})$, Goodstein's theorem does not mention proofs or codes of formulas.

## Explanations

### L1 human

Start with a number, write it in base $2$, replace each $2$ by $3$, and subtract $1$.
Then write the result in base $3$, replace each $3$ by $4$, subtract $1$, and so on.
The numbers often grow enormous at first, but Goodstein proved that they always come back down to $0$.
This is a true statement about whole numbers, so it is part of true arithmetic, yet Peano arithmetic cannot prove it.

### L2 human

We compute the Goodstein sequence of $3$.

1. $G_1 = 3 = 2^1 + 1$ in base $2$. Replace $2$ by $3$: $3^1 + 1 = 4$. Subtract $1$: $G_2 = 3$.
2. $G_2 = 3 = 3^1$ in base $3$. Replace $3$ by $4$: $4$. Subtract $1$: $G_3 = 3$.
3. $G_3 = 3$ is a single digit in base $4$, so the base change leaves it at $3$. Subtract $1$: $G_4 = 2$.
4. In the same way $G_5 = 1$ and $G_6 = 0$.

The typical use is as the standard example of a true arithmetical sentence, unprovable in $\mathsf{PA}$, with no reference to logic.
A trap is to start with $m = 4$ and expect a short computation: the sequence of $4$ reaches $0$ only after more than $10^{100}$ steps.
