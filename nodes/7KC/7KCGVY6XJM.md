---
tag: 7KCGVY6XJM
kind: example
name: The sets computable from the halting set form an ω-model of RCA0 but not of ACA0
msc: ["03B30", "03D80"]
topics: [BY8AAFN7C5]
audience: grad
instance_of: [XQENB067R3]
not_instance_of:
  - target: NAASTN80QN
    note: the jump of the halting set is not computable from the halting set
uses: [XQENB067R3, Y6D27XJT3H, 10NR4PGXHW, PA4PYQ1PZ0, 60P2XWY5QX]
sources:
  - url: https://en.wikipedia.org/wiki/Reverse_mathematics
    locator: ω-models and β-models
  - url: https://en.wikipedia.org/wiki/Turing_jump
    locator: Properties
---

## Example

Let $K = \emptyset'$ be the halting set, and let $\mathcal{S} = \set{X \subseteq \N : X \le_T K}$, where $\le_T$ is [[Turing reducibility|PA4PYQ1PZ0]].
We check that $(\N, \mathcal{S})$ is an $\omega$-model of [[RCA0|XQENB067R3]] and not of [[ACA0|NAASTN80QN]].

1. $\mathcal{S}$ is not empty, since $\emptyset \le_T K$.
2. If $X, Y \le_T K$, then $X \oplus Y \le_T K$: to decide $2n \in X \oplus Y$ run the reduction of $X$, and for $2n + 1$ run the reduction of $Y$.
3. If $Y \le_T X$ and $X \le_T K$, then $Y \le_T K$, by composition of reductions.
4. So $\mathcal{S}$ is a Turing ideal, and $(\N, \mathcal{S})$ is an $\omega$-model of $\mathsf{RCA}_0$ by the [[characterization of ω-models|Y6D27XJT3H]].
5. $K \in \mathcal{S}$. Its [[Turing jump|60P2XWY5QX]] $K' = \emptyset''$ satisfies $K <_T K'$, since every set is strictly below its jump.
6. So $K' \notin \mathcal{S}$. The sentence "every set has a Turing jump" fails in $(\N, \mathcal{S})$.
7. That sentence is [[provable in ACA0|10NR4PGXHW]], so $(\N, \mathcal{S})$ is not a model of $\mathsf{ACA}_0$.

## Remarks

The model contains non-computable sets, so it is not the least $\omega$-model of $\mathsf{RCA}_0$.
In $\omega$-models of $\mathsf{RCA}_0$, the instance of arithmetical comprehension that fails is always a jump: the model is closed under computability, but not under the jump.
The model is not a model of $\mathsf{WKL}_0$ either: the Kleene tree construction relativized to $K$ gives a tree in $\mathcal{S}$ with no path in $\mathcal{S}$.

## Explanations

### L1 human

Here the sets are those that a computer can decide when it may ask an oracle about the halting problem.
These sets satisfy the axioms of computable mathematics.
The halting problem for oracle computers with this oracle is missing, so arithmetical comprehension fails.

### L2 human

The check of $\mathsf{RCA}_0$ reduces to closure properties, by the characterization of $\omega$-models.
The check that $\mathsf{ACA}_0$ fails reduces to one missing jump.
A trap is to think that every arithmetical set is in $\mathcal{S}$, since $K$ is: $\emptyset''$ is arithmetical and not in $\mathcal{S}$.
