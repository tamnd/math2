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
Here is an argument for the false claim that $P(x)$ holds for every real number $x$.
The base case says that $P(0)$ holds, because $0$ is an integer.
The step says that for every real $x$, if $x$ is an integer, then $x + 1$ is an integer.
The "conclusion" is that every real number is an integer.
We show that this argument is not a [[structural induction|12MQ2NJ29A]] over the reals.

1. The base case and the step are both true.
   The base case uses the element $0$, and the step uses the rule $x \mapsto x + 1$.
2. Structural induction with this base element and this rule proves $P$ only on the least set $X$ that contains $0$ and is closed under $x \mapsto x + 1$.
3. Every set that contains $0$ and is closed under the rule contains $1$, then $2$, and so on, so it contains every natural number.
   The set $\mathbb{N}$ itself contains $0$ and is closed under the rule, so $X = \mathbb{N}$.
4. The set $\mathbb{R}$ is not $X$, because $\tfrac{1}{2}$ lies in $\mathbb{R}$ but not in $\mathbb{N}$.
   No chain of steps from $0$ reaches $\tfrac{1}{2}$.
5. So the argument proves $P(x)$ for every natural number $x$, which is true, and nothing about the other reals.
6. The claim is false at $\tfrac{1}{2}$, which is not an integer.

## Remarks

The base case and the step are not the problem.
The error is the hidden claim that the reals are built from $0$ by adding $1$.
A quick test exposes it: the set of reals $x$ with $P(x)$ is $\mathbb{Z}$, which contains $0$ and is closed under $x \mapsto x + 1$, and yet it is not all of $\mathbb{R}$.
A valid induction principle for a set $S$ must rule out every proper subset of $S$ that passes the base case and the step.

Adding a second rule $x \mapsto x - 1$ gives the least set $\mathbb{Z}$, which is still not $\mathbb{R}$.
In fact no finite list of rules of this kind can build all reals from $0$.
Each rule builds one number from finitely many given numbers, so the numbers that the rules build form a [[countable set|01TQB88H4C]], and $\mathbb{R}$ is not countable.
Ordinary [[induction|0ASJVEFA9J]] is valid on $\mathbb{N}$ for exactly the reason that fails here: $\mathbb{N}$ is the least set that contains $0$ and is closed under $n \mapsto n + 1$.

## Explanations

### L1 human

Start at $0$ on the number line and jump to the right by $1$, again and again.
You land on $0, 1, 2, 3$ and so on, and on no other point.
A proof that starts at $0$ and jumps by $1$ tells you about these points and no others.
The point $\tfrac{1}{2}$ is between $0$ and $1$, and no jump lands on it.
So the argument cannot show that $\tfrac{1}{2}$ is an integer, and in fact it is not.

### L2 human

Let us check which reals the argument reaches.
From $P(0)$, one step gives $P(1)$, two steps give $P(2)$, and $k$ steps give $P(k)$.
So each chain of steps from $0$ ends at a natural number.
The numbers $\tfrac{1}{2}$, $-1$ and $\sqrt{2}$ are not natural numbers, so no chain ends at them.
Of these, $-1$ is an integer and the other two are not.
The argument is silent on all three, and the claim fails for two of them.
This error usually comes from a step that is true on a large set, which makes the induction look complete.
The check against it is to pick one element, such as $\tfrac{1}{2}$, and ask which chain of steps from the base case reaches it.
