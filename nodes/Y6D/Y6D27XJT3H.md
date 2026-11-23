---
tag: Y6D27XJT3H
kind: statement
role: theorem
name: The ω-models of RCA0 are exactly the Turing ideals
msc: ["03B30", "03D80"]
topics: [BY8AAFN7C5]
audience: grad
about: [XQENB067R3]
uses: [XQENB067R3, DNXCKXZZ08, PA4PYQ1PZ0, TN9G24VABN]
sources:
  - url: https://en.wikipedia.org/wiki/Reverse_mathematics
    locator: ω-models and β-models
---

## Statement

The computable sets satisfy every axiom of $\mathsf{RCA}_0$, and so do the sets computable from the halting set.
The theorem says exactly which families of sets of standard numbers do, by two closure conditions from computability theory.

A *Turing ideal* is a nonempty family $\mathcal{S} \subseteq \mathcal{P}(\mathbb{N})$ with these two properties.

1. If $X, Y \in \mathcal{S}$, then the join $X \oplus Y = \{ 2n : n \in X \} \cup \{ 2n + 1 : n \in Y \}$ is in $\mathcal{S}$.
2. If $X \in \mathcal{S}$ and $Y$ is [[Turing reducible|PA4PYQ1PZ0]] to $X$, then $Y \in \mathcal{S}$.

**Theorem.** For every nonempty family $\mathcal{S} \subseteq \mathcal{P}(\mathbb{N})$, the $\omega$-structure $(\mathbb{N}, \mathcal{S})$ is a model of [[RCA0|XQENB067R3]] if and only if $\mathcal{S}$ is a Turing ideal.

## Remarks

### Why each hypothesis is needed

The number part must be standard.
A model of $\mathsf{RCA}_0$ with non-standard numbers has sets that are not subsets of $\mathbb{N}$, and Turing reducibility does not apply to them.
Such models are the main tool for questions about induction, and they need other methods.

Closure under join cannot be dropped.
Take sets $A$ and $B$ of incomparable Turing degrees, and let $\mathcal{S}$ be the family of sets computable from $A$ or from $B$.
This family is closed downward under $\le_T$, but it does not contain $A \oplus B$.
If $A \oplus B \le_T A$, then $B \le_T A$, and if $A \oplus B \le_T B$, then $A \le_T B$, and both are excluded.
Comprehension with the two parameters $A$ and $B$ asks for $A \oplus B$, so $(\mathbb{N}, \mathcal{S})$ is not a model.

Closure downward cannot be dropped either.
The family of all sets that compute the halting set $K$ is closed under join, since $X \oplus Y$ computes $X$.
It does not contain $\emptyset$, which comprehension without parameters asks for.
The [[computable sets together with the halting set|ZMVX86T0XK]] fail in a similar way: they miss the complement of $K$.

### What it gives you

The computable sets form the [[least ω-model of RCA0|F5T3F7E0H1]], since every Turing ideal contains them.
For each set $X$, the sets computable from $X$ form an $\omega$-model, for example the [[sets computable from the halting set|7KCGVY6XJM]].
A sentence of $L_2$ that fails in some Turing ideal is not provable in $\mathsf{RCA}_0$.
This is the main way to show that a theorem is not provable in the base system.
The intersection of a nonempty collection of Turing ideals is again a Turing ideal, since both closure conditions pass to intersections.

### The converse

The statement is an equivalence, and the [[proof|20TJDZ5FG2]] proves both directions.

### Generalizations

The same method shows that the $\omega$-models of $\mathsf{ACA}_0$ are the Turing ideals closed under the Turing jump.
The $\omega$-models of $\mathsf{WKL}_0$ are the Turing ideals in which every infinite binary tree has a path, often called Scott ideals.

## History

The correspondence between $\omega$-models of the base system and Turing ideals was part of the program from its start in the 1970s, and Simpson's book of 1999 states it in this form.

## Explanations

### L1 human

A family of sets satisfies the axioms of computable mathematics exactly when two things hold.
It can combine two of its sets into one, by putting one on the even numbers and the other on the odd numbers.
It contains every set that a computer can decide with one of its sets as a helper.

### L2 human

We check the join condition with numbers.
Let $X = \{1, 2\}$ and $Y = \{0\}$.
The join puts $2n$ for $n \in X$ and $2n + 1$ for $n \in Y$:
$$X \oplus Y = \{2, 4\} \cup \{1\} = \{1, 2, 4\}.$$
Check: $4 = 2 \cdot 2$ comes from $2 \in X$, and $1 = 2 \cdot 0 + 1$ comes from $0 \in Y$.

The theorem turns questions about $\omega$-models into questions of computability theory.
To show that a principle is not provable in $\mathsf{RCA}_0$, find a Turing ideal where it fails, often the computable sets.
The trap is to forget the parameters: comprehension may use any finite list of sets from $\mathcal{S}$, and the join reduces the list to one set.

### L3 human

The theorem is the first entry of a dictionary between subsystems and classes of Turing ideals.
$\mathsf{WKL}_0$ matches the Scott ideals and $\mathsf{ACA}_0$ the jump ideals.
For [[β-models|J0Z2GNJZ2W]], $\Pi^1_1\text{-}\mathsf{CA}_0$ matches closure under the hyperjump.
Through this dictionary, theorems such as the low basis theorem become independence results: they produce Turing ideals in which some principle holds and another fails.
