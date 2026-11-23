---
tag: 10NR4PGXHW
kind: example
name: The existence of Turing jumps is equivalent to ACA0 over RCA0
msc: ["03B30", "03D80"]
topics: [BY8AAFN7C5]
audience: grad
instance_of: [7SQS69T17R, NAASTN80QN]
uses: [7SQS69T17R, TQTDKMBJ0F, DNXCKXZZ08, K9XG0Z2N9V, 60P2XWY5QX, S9DK13K5PS, 3MQ39PRCYJ]
sources:
  - url: https://en.wikipedia.org/wiki/Reverse_mathematics
    locator: Arithmetical comprehension ACA0
  - url: https://en.wikipedia.org/wiki/Turing_jump
    locator: lead section
---

## Example

Let $\theta(e, s, X)$ be a $\Sigma^0_0$ formula that says "the oracle program $e$ with oracle $X$ halts on input $e$ within $s$ steps".
It is built from the [[Kleene T predicate|S9DK13K5PS]] relativized to $X$.
Let $\mathrm{TJ}$ be the sentence below, which says that every set $X$ has a [[Turing jump|60P2XWY5QX]] $X'$.
$$\forall X \, \exists Y \, \forall e \, \big( e \in Y \leftrightarrow \exists s \, \theta(e, s, X) \big)$$
We check that $\mathrm{TJ}$ is equivalent to $\mathsf{ACA}_0$ over $\mathsf{RCA}_0$, in the sense of [[reverse mathematics|TQTDKMBJ0F]].

1. $\mathsf{ACA}_0$ proves $\mathrm{TJ}$.
   The formula $\exists s \, \theta(e, s, X)$ has no set quantifiers, so [[arithmetical comprehension|K9XG0Z2N9V]] gives the set $Y$.
2. For the reversal, we work in [[RCA0|DNXCKXZZ08]] plus $\mathrm{TJ}$.
   Let $\varphi(n)$ be a $\Sigma^0_1$ formula, with its set parameters combined into one set $X$.
3. We cite the enumeration theorem, formalized in $\mathsf{RCA}_0$.
   It gives a primitive recursive function $g$ such that $\varphi(n) \leftrightarrow g(n) \in X'$ for all $n$.
   Here $g(n)$ is the index of a program that ignores its input and searches for a witness of $\varphi(n)$.
4. $\mathrm{TJ}$ gives the set $X'$.
   The set $\{ n : g(n) \in X' \}$ is $\Delta^0_1$ in $X'$, so $\Delta^0_1$ comprehension gives it, and it is the set that $\varphi$ defines.
5. So $\mathsf{RCA}_0 + \mathrm{TJ}$ proves $\Sigma^0_1$ comprehension.
6. $\Sigma^0_1$ comprehension proves comprehension for every arithmetical formula.
   The set for $\neg \varphi$ is the complement of the set for $\varphi$, and the set for $\exists m \, \psi(n, m)$ comes from the set for $\psi$ by one more application of step 4.
   This is the argument of the [[range lemma|3MQ39PRCYJ]].

So $\mathsf{RCA}_0 + \mathrm{TJ}$ proves every axiom of $\mathsf{ACA}_0$, and the equivalence holds.

## Remarks

The example shows the computability content of $\mathsf{ACA}_0$.
An $\omega$-model of $\mathsf{RCA}_0$ satisfies $\mathsf{ACA}_0$ exactly when it is closed under the Turing jump.
Step 3 is the formal version of the fact that $X'$ is complete among the sets that are computably enumerable in $X$.

The reversal uses $\mathrm{TJ}$ only for $\Sigma^0_1$ formulas, and then climbs the arithmetical hierarchy one quantifier at a time.
A theorem that implies $\mathrm{TJ}$ therefore implies $\mathsf{ACA}_0$.
This is the usual route of a reversal to $\mathsf{ACA}_0$: show that the theorem computes the jump of each set, or the range of each one-to-one function.

## Explanations

### L1 human

The jump of a set $X$ is the halting problem for programs that may ask questions about $X$.
Arithmetical comprehension proves that the jump exists, because the jump is described without quantifiers over sets.
Conversely, once every jump exists, every set with an arithmetical description is computable from finitely many jumps, so it exists.

### L2 human

Take the formula $\varphi(n) := \exists m \, (m \cdot m = n + 2)$, with no parameters.
The program with index $g(n)$ tries $m = 0, 1, 2, \dots$ and halts when $m^2 = n + 2$.
It halts for $n = 2$ and $n = 7$, since $4 = 2 + 2$ and $9 = 7 + 2$, and it runs forever for $n = 1$.
This particular set is computable, but for a general $\Sigma^0_1$ formula the search may never end, and only $X'$ knows which searches end.

Watch out: applying $\mathrm{TJ}$ $n$ times for a variable $n$ needs more than $\mathsf{ACA}_0$.
The sequence $X, X', X'', \dots$ as one set, the $\omega$-th jump, does not exist in the [[least ω-model of ACA0|9KPCZ6NA32]], and $\mathsf{ATR}_0$ is the system that proves it exists.
