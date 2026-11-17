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

Let $K$ be the halting set, and let $\mathcal{S} = \mathrm{REC} \cup \set{K}$, where $\mathrm{REC}$ is the family of [[computable sets|PPGD5KW8JC]].
We check that $(\N, \mathcal{S})$ is not a model of [[RCA0|XQENB067R3]].

1. The formula $\varphi(n) := \neg (n \in K)$, with set parameter $K$, has no quantifiers. So it is both $\Sigma^0_1$ and $\Pi^0_1$.
2. The instance of [[Δ⁰₁ comprehension|DNXCKXZZ08]] with $\varphi$ and $\psi = \varphi$ has a true hypothesis, so it asks for the set $\N \setminus K$.
3. $\N \setminus K$ is not computable, since otherwise $K$ would be computable, against the [[undecidability of the halting problem|Z7TN2B35B0]].
4. $\N \setminus K \ne K$, since $0$ is in exactly one of them. So $\N \setminus K \notin \mathcal{S}$.
5. The instance of $\Delta^0_1$ comprehension fails, and $(\N, \mathcal{S})$ is not a model of $\mathsf{RCA}_0$.

## Remarks

The family $\mathcal{S}$ is not closed downward under Turing reducibility, since $\N \setminus K \le_T K$.
The least $\omega$-model of $\mathsf{RCA}_0$ that contains $K$ is the family of all sets computable from $K$.

## Explanations

### L1 human

If a model has a set, it must also have every set that a computer can decide with that set as oracle.
The complement of the halting set is decided with the halting set as oracle, but it is not in the family.

### L2 human

A family of sets is an $\omega$-model of $\mathsf{RCA}_0$ exactly when it is closed under join and under Turing reducibility.
To show that a family fails, one finds a set computable from members of the family that is missing.
A trap is to check only the axioms without parameters: the failure uses the parameter $K$.
