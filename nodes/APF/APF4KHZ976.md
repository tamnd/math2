---
tag: APF4KHZ976
kind: example
name: Torsion-free groups need infinitely many axioms
msc: ["20A15", "03C60"]
topics: [BAZT8JJ70S]
audience: research
instance_of: [RX9MB386C5]
uses: [RX9MB386C5, PEMNN32A43, 1NR3HAWG9D, 3C53TD, 03VFZ2WETT]
sources:
  - url: https://en.wikipedia.org/wiki/Compactness_theorem
    locator: lead section
---

## Example

We work in the first-order language of groups with the signature $\{\cdot, {}^{-1}, e\}$, as in the [[elementary theory of groups|RX9MB386C5]].
Let $T_{\mathrm{grp}}$ be the set of the three group axioms.
For each integer $n \ge 2$, let $\tau_n$ be the sentence $\forall x \, (x^n = e \to x = e)$.
We show that the [[torsion-free groups|PEMNN32A43]] are the models of $T_{\mathrm{grp}} \cup \{\tau_n : n \ge 2\}$, and that no finite set of sentences is enough.

1. A group $G$ is torsion-free when $x^n = e$ with $n \ge 1$ implies $x = e$. For $n = 1$ the implication is always true, so $G$ is torsion-free if and only if $G \models \tau_n$ for all $n \ge 2$.
2. Suppose, for a contradiction, that a finite set $\Phi$ of sentences has the property: a group satisfies $\Phi$ if and only if it is torsion-free. Let $\psi$ be the conjunction of the sentences of $\Phi$.
3. The set $\Gamma = T_{\mathrm{grp}} \cup \{\tau_n : n \ge 2\} \cup \{\neg \psi\}$ has no model. A model would be a torsion-free group by step 1, and it would not be torsion-free by step 2.
4. By the [[compactness theorem|1NR3HAWG9D]], some finite subset of $\Gamma$ has no model. So there is an integer $N \ge 2$ such that $T_{\mathrm{grp}} \cup \{\tau_2, \ldots, \tau_N\} \cup \{\neg \psi\}$ has no model.
5. Let $p$ be a prime with $p > N$, and let $G = \mathbb{Z}/p\mathbb{Z}$ with addition. Let $2 \le n \le N$ and $x \in G$ with $nx = 0$. By [[Lagrange's theorem|3C53TD]] the order of $x$ divides $p$, and it also divides $n$.
6. Since $p$ is prime and $p > n$, the only common divisor of $p$ and $n$ is $1$. So $x$ has order $1$, that is, $x = 0$. Thus $G \models \tau_n$ for $2 \le n \le N$.
7. The element $1 \in G$ satisfies $p \cdot 1 = 0$ and $1 \ne 0$, so $G$ is not torsion-free. By step 2, $G \models \neg \psi$.
8. By steps 6 and 7, $G$ is a model of the set in step 4. This contradicts step 4, so no such finite set $\Phi$ exists.

## Remarks

The class of torsion-free groups is an [[elementary class|MEC3ZMC4F1]], because the infinite set in step 1 axiomatizes it.
It is not a finitely axiomatizable class.
The proof uses only that each finite part of the axioms is true in a group that is not torsion-free.
The same proof works for the [[divisible groups|ZXVBEPMTCN]], with the sentences $\forall x \exists y \, (y^n = x)$ for $n \ge 2$.
In $\mathbb{Z}/p\mathbb{Z}$ each $n$ with $2 \le n < p$ is invertible modulo $p$, so these sentences hold for $n < p$, but the sentence for $n = p$ fails at $x = 1$.
In contrast, the property "$x^2 = e$ implies $x = e$" alone is one sentence, so the groups without elements of order $2$ form a finitely axiomatizable class.

## Explanations

### L1 human

A group is torsion-free when no element other than the identity comes back to the identity after a number of steps.
The integers with addition are torsion-free: if we add a nonzero number to itself again and again, we never get $0$.
To say this with sentences, we need one sentence for $2$ steps, one for $3$ steps, one for $4$ steps, and so on.
The example shows that this endless list cannot be replaced by a short list.
The reason is that the clock group with $p$ hours, for a large prime $p$, passes every check up to $p - 1$ steps, but it fails the check for $p$ steps.

### L2 human

We test the first sentences $\tau_2, \tau_3, \tau_4$ on the group $\mathbb{Z}/5\mathbb{Z}$.

1. The multiples of $2$ modulo $5$: $2x = 0$ gives $x = 0$, because $2 \cdot 1 = 2$, $2 \cdot 2 = 4$, $2 \cdot 3 = 1$ and $2 \cdot 4 = 3$ are nonzero.
2. In the same way $3x = 0$ and $4x = 0$ give $x = 0$, because $3$ and $4$ are invertible modulo $5$.
3. So $\mathbb{Z}/5\mathbb{Z}$ satisfies $\tau_2$, $\tau_3$ and $\tau_4$.
4. But $5 \cdot 1 = 0$ and $1 \ne 0$, so $\tau_5$ fails.

This is step 5 of the proof with $N = 4$ and $p = 5$.
The typical use of the compactness theorem is this pattern: a property that holds in arbitrarily good finite approximations, but not exactly, cannot be finitely axiomatized.
A trap is to think that the proof shows that torsion-freeness is not first-order at all.
It is first-order, because the infinite set $\{\tau_n\}$ expresses it; only a finite set is impossible.
