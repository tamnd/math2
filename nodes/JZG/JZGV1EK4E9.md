---
tag: JZGV1EK4E9
kind: example
name: Sigma_n induction implies Pi_n induction
msc: ["03F30"]
topics: [QHCRN4JVG0]
audience: research
instance_of: [T70PYM1F36]
uses: [T70PYM1F36, 3K1AKGXF8A, GE43CSZTS9, 0J0XBKG64S, GJ9KW45F3C]
sources:
  - book: isbn:9780521857840
---

## Example

Induction for $\Pi_n$ formulas comes for free in $\mathsf{I}\Sigma_n$, by running the induction downward from a failure.
Fix $n \ge 1$.
We show that $\mathsf{I}\Sigma_n$ proves every induction axiom for a $\Pi_n$ formula, so $\mathsf{I}\Pi_n \subseteq \mathsf{I}\Sigma_n$ in the [[hierarchy of fragments|T70PYM1F36]].
Let $\psi(x)$ be a $\Pi_n$ formula; parameters are carried along and do not change the argument.
We work in $\mathsf{I}\Sigma_n$ and argue by [[contradiction|0J0XBKG64S]].
Assume $\psi(0)$ and $\forall x \, (\psi(x) \to \psi(Sx))$, and assume $\neg \psi(a)$ for some $a$.

1. Let $\theta(y)$ be $y \le a \to \exists z \, (z + y = a \land \neg \psi(z))$.
   The formula $\neg \psi$ is equivalent to a $\Sigma_n$ formula, so $\theta$ is equivalent to a $\Sigma_n$ formula.
2. Base: $\theta(0)$ holds with $z = a$, since $a + 0 = a$ by $\mathsf{Q}4$ and $\neg \psi(a)$.
3. Step: assume $\theta(y)$ and $Sy \le a$.
   Then $y \le a$, so some $z$ has $z + y = a$ and $\neg \psi(z)$.
4. $z \ne 0$, because $z = 0$ gives $0 + y = a$, so $y = a$, which contradicts $Sy \le a$.
5. By $\mathsf{Q}3$, $z = Sw$ for some $w$.
   Then $\neg \psi(w)$, since $\psi(w)$ would give $\psi(Sw)$.
6. $w + Sy = S(w + y) = Sw + y = a$, by $\mathsf{Q}5$ and the law $Sw + y = S(w + y)$.
   So $w$ witnesses $\theta(Sy)$.
7. $\Sigma_n$ induction on $\theta$ gives $\theta(a)$, so some $z$ has $z + a = a$ and $\neg \psi(z)$.
8. From $z + a = a$ we get $z = 0$ by cancellation.
   So $\neg \psi(0)$, which contradicts the assumption $\psi(0)$.

So $\psi(0) \land \forall x \, (\psi(x) \to \psi(Sx)) \to \forall x \, \psi(x)$ is a theorem of $\mathsf{I}\Sigma_n$.

## Remarks

The trick is to count the steps downward from $a$: $\theta(y)$ says that $\psi$ fails at the point $y$ steps below $a$.
The formula $\theta$ is $\Sigma_n$ because the bad point $z$ sits under an existential quantifier, which merges with the leading block of $\neg \psi$.
Steps 4, 6 and 8 use the laws $0 + y = y$, $Sw + y = S(w + y)$ and cancellation.
[[Open induction proves them|GJ9KW45F3C]], so $\mathsf{I}\Sigma_n$ proves them too.

The converse also holds: $\mathsf{I}\Pi_n$ proves every $\Sigma_n$ induction axiom.
For $\psi$ in $\Sigma_n$, the downward argument uses the $\Pi_n$ formula $\forall z \, (z + y = a \to \neg \psi(z))$ in place of $\theta(y)$.
So the two theories have the same theorems.

For $n = 0$ the formula $\theta$ has an unbounded $\exists z$.
Adding the bound $z \le a$ keeps it in $\Delta_0$, and then the same argument works.

## Explanations

### L1 human

Suppose a property holds for $0$ and passes from each number to the next, but fails at some number $a$.
Then it also fails at $a - 1$, since otherwise it would pass on to $a$.
Repeating this, it fails at $a - 2$, $a - 3$, and so on down to $0$, which is impossible.
The example turns this walk downward into an upward induction on the number of steps taken.

### L2 human

We trace the argument with $a = 3$, for a property $\psi$ that holds at $0$ and fails at $3$.
At $y = 0$, the point $z = 3$ fails $\psi$, and $3 + 0 = 3$, so $\theta(0)$ holds.
At $y = 1$, the point $z = 2$ fails $\psi$, since $\psi(2)$ would give $\psi(3)$, and $2 + 1 = 3$.
At $y = 2$, the point $z = 1$ fails $\psi$ in the same way, and $1 + 2 = 3$.
At $y = 3$, the point $z = 0$ fails $\psi$, and $0 + 3 = 3$, which contradicts $\psi(0)$.

The typical use is to show that the choice between $\Sigma_n$ and $\Pi_n$ in a fragment does not matter.
Watch out: you cannot use $\neg \psi$ itself as the induction formula.
It is $\Sigma_n$, but it does not hold at $0$, so the base case fails.
