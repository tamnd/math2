---
tag: ZMVX86T0XK
kind: example
name: The computable sets together with the halting set do not form a model of RCA0
msc: ["03B30", "03D80"]
topics: [BY8AAFN7C5]
audience: grad
not_instance_of:
  - target: XQENB067R3
    note: the complement of the halting set is computable from a member of the family, but it is not in the family
uses: [XQENB067R3, DNXCKXZZ08, PPGD5KW8JC, Z7TN2B35B0]
sources:
  - url: https://en.wikipedia.org/wiki/Reverse_mathematics
    locator: Base system RCA0
---

## Example

Let $K$ be the halting set, and let $\mathcal{S} = \mathrm{REC} \cup \{K\}$, where $\mathrm{REC}$ is the family of [[computable sets|PPGD5KW8JC]].
We check that $(\mathbb{N}, \mathcal{S})$ is not a model of [[RCA0|XQENB067R3]], by finding one instance of comprehension that fails.

1. The formula $\varphi(n) := \neg (n \in K)$, with the set parameter $K$, has no quantifiers.
   So it is both $\Sigma^0_1$ and $\Pi^0_1$.
2. The instance of [[Δ⁰₁ comprehension|DNXCKXZZ08]] with $\varphi$ and $\psi = \varphi$ has a true hypothesis, so it asks for the set $\mathbb{N} \setminus K$.
3. $\mathbb{N} \setminus K$ is not computable, since otherwise $K$ would be computable, against the [[undecidability of the halting problem|Z7TN2B35B0]].
4. $\mathbb{N} \setminus K$ is not $K$ either, since a set is never equal to its complement.
   So $\mathbb{N} \setminus K \notin \mathcal{S}$.

The instance of $\Delta^0_1$ comprehension fails, and $(\mathbb{N}, \mathcal{S})$ is not a model of $\mathsf{RCA}_0$.

## Remarks

The family $\mathcal{S}$ is not closed downward under Turing reducibility, since $\mathbb{N} \setminus K \le_T K$.
It is not closed under join either, since $K \oplus \emptyset$ is computable from $K$ but is neither computable nor equal to $K$.

What is the smallest repair?
The least $\omega$-model of $\mathsf{RCA}_0$ that contains $K$ is the family of all sets computable from $K$.
That family is a model of $\mathsf{RCA}_0$, as the [[sets computable from the halting set|7KCGVY6XJM]] show, but it still fails $\mathsf{ACA}_0$.
So adding one set to a model of $\mathsf{RCA}_0$ always drags in everything computable from it.

## Explanations

### L1 human

If a model has a set, it must also have every set that a computer can decide with that set as a helper.
The complement of the halting set is decided with the halting set as a helper: answer "yes" exactly when the helper says "no".
That complement is not in the family, so the family is not a model.

### L2 human

A family of sets is an $\omega$-model of $\mathsf{RCA}_0$ exactly when it is nonempty and closed under join and under Turing reducibility.
To show that a family fails, find a set computable from members of the family that is missing from it.

Watch out: it is not enough to check the axioms without parameters.
Every instance without set parameters defines a computable set, and those are all in $\mathcal{S}$.
The failure needs the parameter $K$.
