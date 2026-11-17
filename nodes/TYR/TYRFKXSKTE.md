---
tag: TYRFKXSKTE
kind: example
name: Induction on the reals from 0 by adding 1 is not structural induction
msc: ["00A35"]
topics: [EEH2F76CYQ]
audience: ug1
not_instance_of:
  - target: 12MQ2NJ29A
    note: the real numbers are not the least set that contains 0 and is closed under x ↦ x + 1, so the base case and the step do not reach every real number
uses: [12MQ2NJ29A, 08J2M1JYAG, 0ASJVEFA9J]
sources:
  - url: https://en.wikipedia.org/wiki/Structural_induction
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Mathematical_induction
    locator: Description
---

## Example

For a [[real number|08J2M1JYAG]] $x$, let $P(x)$ be the statement "$x$ is an integer".
Consider the following argument for the false claim "$P(x)$ holds for every real number $x$".
Base case: $P(0)$ holds, because $0$ is an integer.
Step: for every real $x$, if $x$ is an integer, then $x + 1$ is an integer.
"Conclusion": every real number is an integer.
We show that this argument is not a [[structural induction|12MQ2NJ29A]] over the reals.

1. The base case and the step are both correct. The base case uses the element $0$, and the step uses the rule $x \mapsto x + 1$.
2. Structural induction with this base element and this rule proves $P$ only on the least set $X$ that contains $0$ and is closed under $x \mapsto x + 1$.
3. Every such set contains $0$, then $1$, then $2$, and so on, so it contains every natural number. The set $\mathbb{N}$ itself contains $0$ and is closed under the rule. So $X = \mathbb{N}$.
4. The set $\mathbb{R}$ is not $X$: the number $\frac{1}{2}$ lies in $\mathbb{R}$ but not in $\mathbb{N}$. The base case and the step give no chain that reaches $\frac{1}{2}$.
5. So the argument proves $P(x)$ for every natural number $x$, which is true, and nothing about the other reals.
6. The claim is false at $\frac{1}{2}$, which is not an integer.

## Remarks

1. The set of $x$ with $P(x)$ is $\mathbb{Z}$. It contains $0$ and is closed under $x \mapsto x + 1$, but it is not all of $\mathbb{R}$. A correct induction principle for a set $S$ must exclude such a proper subset of $S$.
2. The error is the claim that the reals are built from $0$ by the step, not the base case or the step.
3. A second rule $x \mapsto x - 1$ gives the least set $\mathbb{Z}$, which is still not $\mathbb{R}$.
4. No list of finitely many rules of this kind can build all reals from $0$. Each rule builds one new number from given numbers, so the built set is countable, and $\mathbb{R}$ is not countable.
5. Ordinary [[induction|0ASJVEFA9J]] is valid for $\mathbb{N}$ because $\mathbb{N}$ is exactly the least set that contains $0$ and is closed under $n \mapsto n + 1$.

## Explanations

### L1 human

Start at $0$ on the number line and jump to the right by $1$, again and again.
You land on $0, 1, 2, 3$ and so on, and on no other point.
A proof that only starts at $0$ and jumps by $1$ tells us something about these points and no others.
The point $\frac{1}{2}$ is between $0$ and $1$, and no jump lands on it.
So the argument cannot show that $\frac{1}{2}$ is an integer, and in fact it is not.

### L2 human

We check which reals the argument reaches.

1. From $P(0)$, one step gives $P(1)$, two steps give $P(2)$, and $k$ steps give $P(k)$.
2. Each chain of steps from $0$ ends at a natural number.
3. The numbers $\frac{1}{2}$, $-1$ and $\sqrt{2}$ are not natural numbers, so no chain ends at them.
4. Of these, $-1$ is an integer and the other two are not. So the argument is silent on all three, and the claim fails for two of them.

The typical source of this error is a step that is true for every element of a large set, which makes the induction look complete.
A check against it is to ask for one element, such as $\frac{1}{2}$, which chain of steps from the base case reaches it.
