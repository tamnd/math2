---
tag: 20TJDZ5FG2
kind: proof
name: Proof that the ω-models of RCA0 are the Turing ideals
msc: ["03B30", "03D80"]
topics: [BY8AAFN7C5]
audience: grad
proves: Y6D27XJT3H
uses: [DNXCKXZZ08, PA4PYQ1PZ0, TN9G24VABN]
methods: [TFQ1845T84, 41JZ39GE3F]
sources:
  - url: https://en.wikipedia.org/wiki/Reverse_mathematics
    locator: ω-models and β-models
---

## Proof

The plan: in an $\omega$-model, arithmetical formulas mean what they say, so each axiom of $\mathsf{RCA}_0$ becomes a statement about computations.

We use one fact throughout, and call it (A).
In an $\omega$-structure $(\mathbb{N}, \mathcal{S})$, a formula without set quantifiers, with parameters from $\mathbb{N}$ and $\mathcal{S}$, is true exactly when it is true of the actual numbers and sets.

### Models give Turing ideals

1. ($\Rightarrow$) Let $(\mathbb{N}, \mathcal{S})$ be a model of $\mathsf{RCA}_0$, and let $X, Y \in \mathcal{S}$.
2. The formula $\exists m \le n \, \big( (n = 2m \wedge m \in X) \vee (n = 2m + 1 \wedge m \in Y) \big)$ is $\Sigma^0_0$.
   So $\Delta^0_1$ comprehension gives a set $Z \in \mathcal{S}$ that it defines.
3. By (A), $Z = X \oplus Y$, so $\mathcal{S}$ is closed under join.
4. Let $X \in \mathcal{S}$ and $Y \le_T X$, by a program $e$ that computes the characteristic function of $Y$ with oracle $X$.
5. Let $\varphi(n)$ say that some halting computation of $e$ with oracle $X$ on input $n$ has output $1$.
   It is $\Sigma^0_1$, with parameter $X$.
6. Let $\psi(n)$ say that no halting computation of $e$ with oracle $X$ on input $n$ has output $0$.
   It is $\Pi^0_1$.
7. The program halts on every input with output $0$ or $1$.
   So $\varphi(n) \leftrightarrow \psi(n)$ holds for every $n$, and by (A) it holds in $(\mathbb{N}, \mathcal{S})$.
8. $\Delta^0_1$ comprehension gives a set in $\mathcal{S}$ defined by $\varphi$, and by (A) it is $Y$.
   So $\mathcal{S}$ is closed downward under $\le_T$.
9. So $\mathcal{S}$ is a Turing ideal.

### Turing ideals give models

10. ($\Leftarrow$) Let $\mathcal{S}$ be a Turing ideal.
    The basic axioms hold in $(\mathbb{N}, \mathcal{S})$, since the number part is standard.
11. Induction holds for every formula $\varphi(n)$.
    If the set $\{ n : (\mathbb{N}, \mathcal{S}) \models \neg\varphi(n) \}$ were nonempty, its least element $n_0$ would contradict $\varphi(0)$ or $\varphi(n_0 - 1) \to \varphi(n_0)$.
12. Let $\varphi(n)$ be $\Sigma^0_1$ and $\psi(n)$ be $\Pi^0_1$, with set parameters $X_1, \ldots, X_k \in \mathcal{S}$.
    Assume that $\forall n \, (\varphi(n) \leftrightarrow \psi(n))$ holds in $(\mathbb{N}, \mathcal{S})$.
13. Let $X = X_1 \oplus \cdots \oplus X_k$.
    By closure under join, $X \in \mathcal{S}$, and each $X_i \le_T X$.
14. By (A), the set $A = \{ n : \varphi(n) \}$ is [[computably enumerable|TN9G24VABN]] relative to $X$.
    Its complement $\{ n : \neg \psi(n) \}$ is also computably enumerable relative to $X$.
15. To decide whether $n \in A$, run both enumerations until $n$ appears in one of them.
    So $A \le_T X$.
16. By closure downward, $A \in \mathcal{S}$, and $A$ witnesses the instance of $\Delta^0_1$ comprehension.
17. So $(\mathbb{N}, \mathcal{S})$ is a model of $\mathsf{RCA}_0$.

## Idea

Comprehension for $\Delta^0_1$ formulas makes exactly the sets that are computable from finitely many given sets.
In an $\omega$-model, arithmetical formulas mean what they say, so the axioms turn into closure conditions.
The join packs the finitely many parameters into one oracle, and closure downward supplies the defined set.

## Variants

The same method shows that the $\omega$-models of $\mathsf{ACA}_0$ are the Turing ideals closed under the jump.
An arithmetical formula with parameter $X$ defines a set computable from $X^{(n)}$ for some $n$, by Post's theorem.
