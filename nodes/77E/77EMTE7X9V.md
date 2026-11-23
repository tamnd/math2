---
tag: 77EMTE7X9V
kind: proof
name: Chaitin's proof of the first incompleteness theorem by Kolmogorov complexity
msc: ["03F40", "68Q30"]
topics: [HXHHWY3328]
audience: grad
proves: X9WYNYE29C
uses: [8PY3K6NCKF, 6M12VR1GT6, TN9G24VABN, 4S29X1GTV4]
methods: [0J0XBKG64S]
sources:
  - url: https://en.wikipedia.org/wiki/Kolmogorov_complexity
    locator: Chaitin's incompleteness theorem
  - book: isbn:9780521701464
---

## Proof

Consider "the least number that cannot be described in fewer than twenty words".
That phrase has fewer than twenty words and describes the number, which is the Berry paradox.
Replace "described" by "printed by a short program" and "the least number" by "the first number $T$ proves complex", and the paradox becomes a proof.
The undecided sentence has the form "$C(\underline{x}) > \underline{c}$".

### Complexity in arithmetic

Fix a universal machine $U$ on binary strings.
The [[Kolmogorov complexity|8PY3K6NCKF]] $C(x)$ is the least length of a program $p$ with $U(p) = x$.

1. The relation "$U$ on input $p$ halts within $s$ steps with output $x$" is decidable.
   Let $\mathrm{Out}(p, s, x)$ represent it in $\mathsf{Q}$.
2. Let $\kappa(x, c) := \neg \exists p \, \exists s \, (\mathrm{lh}(p) \le c \wedge \mathrm{Out}(p, s, x))$.
   This $\Pi_1$ formula says $C(x) > c$, and it defines this relation in $\mathbb{N}$.
3. By the invariance theorem, for every machine $M$ there is a constant $c_M$ with $C(x) \le C_M(x) + c_M$ for all $x$, where $C_M$ is complexity measured with $M$.

### $T$ proves no lower bound $C(\underline{x}) > \underline{c}$

4. Let $M$ be the following machine.
   On input $w$, it reads $w$ as the binary numeral of a number $c$.
   It lists the theorems of $T$, which form a [[computably enumerable|TN9G24VABN]] set, and outputs the first $x$ such that $\kappa(\underline{x}, \underline{c})$ appears.
5. Choose $c$ with $\lfloor \log_2 c \rfloor + 1 + c_M < c$, which exists since $c - \log_2 c$ grows without bound.
6. Assume $T$ is consistent, and suppose $T \vdash \kappa(\underline{x}, \underline{c})$ for some $x$.
   Then $M$ halts on the binary numeral of $c$ with some output $x_0$, and $T \vdash \kappa(\underline{x_0}, \underline{c})$.
7. The binary numeral of $c$ has $\lfloor \log_2 c \rfloor + 1$ digits, so $C_M(x_0) \le \lfloor \log_2 c \rfloor + 1$.
   By steps 3 and 5, $C(x_0) < c$.
8. So the $\Sigma_1$ sentence $\neg \kappa(\underline{x_0}, \underline{c})$ is true in $\mathbb{N}$.
   Every true $\Sigma_1$ sentence is provable in $\mathsf{Q}$, so $T \vdash \neg \kappa(\underline{x_0}, \underline{c})$.
9. Steps 6 and 8 make $T$ inconsistent, so $T$ proves no sentence $\kappa(\underline{x}, \underline{c})$.

### Some lower bound is true

10. There are $2^{c+1} - 1$ binary strings of length at most $c$, so at most $2^{c+1} - 1$ numbers have $C(x) \le c$.
    Among the $2^{c+1}$ numbers $0, \ldots, 2^{c+1} - 1$, some $x_1$ has $C(x_1) > c$.
11. So $\kappa(\underline{x_1}, \underline{c})$ is a true $\Pi_1$ sentence, and $T$ does not prove it, by step 9.
12. If $T$ is $1$-consistent, $T$ does not prove the false $\Sigma_1$ sentence $\neg \kappa(\underline{x_1}, \underline{c})$ either, so $T$ is not negation complete.

## Idea

If $T$ could prove that some $x$ is complex, a short program could search for that proof and print $x$, so $x$ would be simple after all.
For large $c$ the search program is shorter than $c$, and the contradiction shows that $T$ proves no lower bound $C(\underline{x}) > \underline{c}$ at all.
Yet almost every number has complexity above $c$, so the true but unproved sentences are everywhere.

Watch out: $T$ does not fail to prove these bounds because they are hard.
It fails because a proof of any one of them would be a short description, and that description would refute the bound.

## Variants

The constant $c$ in step 5 depends on $T$ through the machine $M$, and it grows roughly with the length of a description of $T$.
It also depends on the choice of universal machine $U$, so no particular value of $c$ has absolute meaning.
Boolos gave a related proof from the Berry paradox, which counts the symbols of a definition in arithmetic instead of using Kolmogorov complexity.
