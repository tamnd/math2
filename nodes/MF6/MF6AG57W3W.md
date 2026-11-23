---
tag: MF6AG57W3W
kind: example
name: ATR0 proves that the ω-th jump of the empty set exists
msc: ["03B30", "03D55"]
topics: [BY8AAFN7C5]
audience: grad
instance_of: [MKB74TX3Z8]
uses: [TMJJSN9PDP, 60P2XWY5QX, 9KPCZ6NA32, NYJX5QXX1T, PA4PYQ1PZ0, 4A84VHDTHV]
sources:
  - url: https://en.wikipedia.org/wiki/Reverse_mathematics
    locator: Arithmetical transfinite recursion ATR0
---

## Example

Let $\mathrm{TJ}(Y) = \{ (e, x) : \Phi^Y_e(x) \text{ halts} \}$ be the [[Turing jump|60P2XWY5QX]] of $Y$.
The formula "$n \in \mathrm{TJ}(Y)$" is $\Sigma^0_1$ in $Y$, so it is arithmetical.
We check that [[ATR0|TMJJSN9PDP]] proves that there is a set $H$ with $H_j = \mathrm{TJ}(H^j)$ for every $j$, where the columns use the order $(\mathbb{N}, <)$.
Such a set $H$ is, up to [[Turing equivalence|PA4PYQ1PZ0]], the $\omega$-th jump $\emptyset^{(\omega)}$.
Then we check that $\mathsf{ACA}_0$ does not prove that such an $H$ exists.

### The hierarchy exists in ATR0

1. Let $W$ be the usual order on $\mathbb{N}$, coded as the set of pairs $(i, j)$ with $i \le j$.
   This set exists by $\Delta^0_1$ comprehension.
2. $\mathsf{RCA}_0$ proves $\mathrm{WO}(W)$.
   Suppose that $f(k + 1) < f(k)$ for all $k$.
   By $\Sigma^0_1$ induction on $k$, $f(k) + k \le f(0)$ for all $k$, and for $k = f(0) + 1$ this gives $f(0) + 1 \le f(0)$, which is false.
3. Apply arithmetical transfinite recursion with $\theta(n, Y) \equiv n \in \mathrm{TJ}(Y)$ along $W$.
   This gives a set $H$ with $H_j = \mathrm{TJ}(H^j)$ for all $j$.

### The columns are the finite jumps

4. For $j = 0$ we have $H^0 = \emptyset$, so $H_0 = \emptyset'$.
5. $H^{j+1}$ is $H^j$ together with column $j$, so $H^{j+1} \equiv_T H^j \oplus H_j$.
   Since $H^j \le_T \mathrm{TJ}(H^j) = H_j$, this gives $H^{j+1} \equiv_T H_j$.
6. So $H_{j+1} = \mathrm{TJ}(H^{j+1}) \equiv_T (H_j)'$, because the jump respects Turing equivalence.
   By induction on $j$, $H_j \equiv_T \emptyset^{(j+1)}$ for every $j$.
7. So the columns of $H$ are, uniformly in $j$, the finite jumps of $\emptyset$, and $H \equiv_T \emptyset^{(\omega)}$.

### ACA0 does not prove it

8. The family of [[arithmetical sets|9KPCZ6NA32]] is an $\omega$-model of $\mathsf{ACA}_0$.
9. The formula "$H$ is a hierarchy along $W$ for $\theta$" is arithmetical, so it means the same in this $\omega$-model and in the true sets.
10. Suppose that a set $H$ of this kind is arithmetical.
    By [[Post's theorem|NYJX5QXX1T]], $H \le_T \emptyset^{(k)}$ for some $k$.
11. By step 6, $\emptyset^{(k+1)} \equiv_T H_k \le_T H \le_T \emptyset^{(k)}$.
    This is false, because no set computes its own jump.
12. So the model of arithmetical sets has no such $H$.
    By the [[soundness theorem|4A84VHDTHV]], $\mathsf{ACA}_0$ does not prove that $H$ exists.

## Remarks

The same proof, with a parameter $X$ in $\theta$, shows that $\mathsf{ATR}_0$ proves that $X^{(\omega)}$ exists for every $X$.
The system $\mathsf{ACA}_0^+$, which is $\mathsf{ACA}_0$ with the axiom "$X^{(\omega)}$ exists for every $X$", is thus contained in [[ATR0|MKB74TX3Z8]].

Step 2 is the only place where the hypothesis $\mathrm{WO}(W)$ is checked, and for $(\mathbb{N}, <)$ it needs only $\Sigma^0_1$ induction.
For longer well-orderings, such as a computable copy of $\varepsilon_0$, the hypothesis is harder, and $\mathsf{ACA}_0$ cannot prove $\mathrm{WO}(W)$ at all.

Watch out: each column $\emptyset^{(j+1)}$ is arithmetical.
What fails in $\mathsf{ACA}_0$ is the existence of one set that holds all columns at once.

## Explanations

### L1 human

$\mathsf{ACA}_0$ can take the jump of a set any finite number of times, but it cannot collect all these jumps in one set.
$\mathsf{ATR}_0$ can collect them, because it iterates the jump along the well-ordering $\omega$.
The result is a set that decides every question about the natural numbers that uses only number quantifiers.

### L2 human

The set $H$ decides the truth of every arithmetical sentence, uniformly.
A $\Sigma^0_{j+1}$ sentence is decided by column $j$, and $H$ finds the right column from the sentence.
So $\mathsf{ATR}_0$ proves that a truth set for arithmetic exists, and this is how it proves that a countable coded $\omega$-model of $\mathsf{ACA}_0$ exists.
The separation in steps 8 to 12 is the standard method: find a model of the weaker system, and show that the arithmetical statement "$H$ is a hierarchy" has no solution in it.
