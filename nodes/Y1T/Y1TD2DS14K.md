---
tag: Y1TD2DS14K
kind: example
name: The Hanf number of first-order logic is aleph-zero
msc: ["03C55", "03C07"]
topics: [W9CHA4PD9H]
audience: research
instance_of: [A9XBRF3A7Z]
uses: [A9XBRF3A7Z, 484M0TZ1S7, DKFGQTRYZE, EY20BF96SJ, 6Q9Z2BM1XR]
sources:
  - url: https://en.wikipedia.org/wiki/Löwenheim–Skolem_theorem
    locator: lead section
  - book: isbn:9780387987606
    locator: Chapter 2
---

## Example

Let $\mathcal{L}$ be first-order logic, with signatures of any size.
We show that its [[Hanf number|A9XBRF3A7Z]] is $\aleph_0$.

1. Upper bound. Let $\varphi$ be a first-order [[sentence|DKFGQTRYZE]] with a model $\mathcal{M}$ of size at least $\aleph_0$. Let $L_0$ be the finite set of symbols that occur in $\varphi$.
2. The [[reduct|EY20BF96SJ]] $\mathcal{M}|L_0$ is an infinite model of $\varphi$. By the upward [[Löwenheim-Skolem theorem|484M0TZ1S7]] for the finite signature $L_0$, $\varphi$ has an $L_0$-model of every infinite size $\kappa$.
3. Interpret the other symbols of the signature in any way on such a model. The result is a model of $\varphi$ of size $\kappa$, since $\varphi$ does not mention them. So $\varphi$ has arbitrarily large models, and $\aleph_0$ has the property.
4. Lower bound. Let $n \ge 1$ be finite, and let $\varepsilon_n$ be $\exists x_1 \dots \exists x_n \, (\bigwedge_{k < l} x_k \ne x_l \wedge \forall y \bigvee_{k} y = x_k)$.
5. A set with $n$ elements is a model of $\varepsilon_n$, and every model of $\varepsilon_n$ has exactly $n$ elements. So $\varepsilon_n$ has a model of size $n$ and no larger model, and $n$ does not have the property.
6. The value $0$ fails for the same reason, with $\varepsilon_1$. So the least cardinal with the property is [[aleph-zero|6Q9Z2BM1XR]].

## Remarks

The example shows that the Hanf number of first-order logic is as small as possible, given that finite sizes can be fixed by single sentences.
The proof uses only the upward Löwenheim-Skolem theorem, which in turn rests on compactness.
For a theory instead of a sentence the same holds: a first-order theory with an infinite model in a signature $L$ has models of every size at least $\abs{L} + \aleph_0$.
In stronger logics compactness fails, and then a sentence can have infinite models of bounded size, as in [[the computation for infinitary logic|QC25K2Y91B]].
The Löwenheim number of first-order logic is also $\aleph_0$, by the downward Löwenheim-Skolem theorem.

## Explanations

### L1 human

The sentence "there are exactly three things" has models with three things and no others.
So the number three cannot be a threshold beyond which models of all sizes exist.
The same holds for every finite number.
But a first-order sentence with infinitely many things in some model has models of every infinite size.
So the threshold for first-order logic is the first infinite size.

### L2 human

We check the upper bound for the sentence $\varphi$ that says that $<$ is a dense linear order without endpoints.

1. The structure $(\Q, <)$ is a model of size $\aleph_0$.
2. Upward Löwenheim-Skolem gives a model of size $\aleph_1$, and of every larger size.
3. The real line $(\R, <)$ is one such model of size $2^{\aleph_0}$, and the lexicographic order on $\kappa \times \Q$ is a model of size $\kappa$ for every infinite $\kappa$.

The typical use is as the base case for comparisons with stronger logics, where the Hanf number is larger.
The trap is to think that the bound also holds for finite models: a sentence with a model of size $5$ may have no larger models.
