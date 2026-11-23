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

Let $K = \emptyset'$ be the halting set, and let $\mathcal{S} = \{ X \subseteq \mathbb{N} : X \le_T K \}$, where $\le_T$ is [[Turing reducibility|PA4PYQ1PZ0]].
We check that $(\mathbb{N}, \mathcal{S})$ is an $\omega$-model of [[RCA0|XQENB067R3]] and not of [[ACA0|NAASTN80QN]].

1. $\mathcal{S}$ is not empty, since $\emptyset \le_T K$.
2. If $X, Y \le_T K$, then $X \oplus Y \le_T K$.
   To decide whether $2n \in X \oplus Y$, run the reduction of $X$ on $n$, and for $2n + 1$ run the reduction of $Y$ on $n$.
3. If $Y \le_T X$ and $X \le_T K$, then $Y \le_T K$, because two reductions compose into one.
4. So $\mathcal{S}$ is a Turing ideal, and $(\mathbb{N}, \mathcal{S})$ is an $\omega$-model of $\mathsf{RCA}_0$ by the [[characterization of ω-models|Y6D27XJT3H]].
5. $K$ is in $\mathcal{S}$, and its [[Turing jump|60P2XWY5QX]] $K' = \emptyset''$ satisfies $K <_T K'$, since every set is strictly below its jump.
   So $K' \notin \mathcal{S}$, and the sentence "every set has a Turing jump" fails in $(\mathbb{N}, \mathcal{S})$.
6. That sentence is [[equivalent to ACA0|10NR4PGXHW]] over $\mathsf{RCA}_0$, and in particular $\mathsf{ACA}_0$ proves it.

So $(\mathbb{N}, \mathcal{S})$ is not a model of $\mathsf{ACA}_0$.

## Remarks

The model contains a non-computable set, $K$, so it is larger than the least $\omega$-model of $\mathsf{RCA}_0$.
The failure of $\mathsf{ACA}_0$ has a general form.
An $\omega$-model of $\mathsf{RCA}_0$ is a model of $\mathsf{ACA}_0$ exactly when it is closed under the jump, so a model of $\mathsf{RCA}_0$ that fails $\mathsf{ACA}_0$ always misses the jump of one of its sets.

The model fails $\mathsf{WKL}_0$ as well.
The Kleene tree of the [[computable sets example|F5T3F7E0H1]], relativized to $K$, is a tree in $\mathcal{S}$ with no path in $\mathcal{S}$.
What changes with a different set in place of $K$?
For every set $X$, the sets computable from $X$ form an $\omega$-model of $\mathsf{RCA}_0$ that fails both $\mathsf{WKL}_0$ and $\mathsf{ACA}_0$, by the same two arguments.

## Explanations

### L1 human

Here the sets are those that a computer can decide when it may ask an oracle about the halting problem.
These sets satisfy the axioms of computable mathematics.
The halting problem for computers with this oracle is a new set, and it is missing, so arithmetical comprehension fails.

### L2 human

The check of $\mathsf{RCA}_0$ reduces to closure properties, by the characterization of $\omega$-models.
The check that $\mathsf{ACA}_0$ fails reduces to one missing jump.

Watch out: the model contains $K$, and $K$ is the most complex $\Sigma^0_1$ set, but the model does not contain every arithmetical set.
The set $\emptyset''$ is $\Sigma^0_2$, so it is arithmetical, and it is not in $\mathcal{S}$.
