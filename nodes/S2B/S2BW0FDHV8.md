---
tag: S2BW0FDHV8
kind: concept
name: Mathematical fallacies
aliases: [mathematical-fallacy, invalid-proof, false-proof, howler]
msc: ["00A35", "97E50"]
topics: [T6QQ749DM5]
audience: school
uses: [0B94TKFQJX, 5V35SGEN1T]
sources:
  - url: https://en.wikipedia.org/wiki/Mathematical_fallacy
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Mathematical_fallacy
    locator: Howlers
  - book: isbn:9781108439534
---

## Summary

A mathematical fallacy is an argument that looks like a proof but hides one bad step.
Here is a short one, a false proof that $2 = 1$; try to find the bad step before you read on.

1. Let $x = 1$, so $x^2 = x$.
2. Subtract $1$ from both sides: $x^2 - 1 = x - 1$.
3. Factor the left side: $(x - 1)(x + 1) = x - 1$.
4. Divide both sides by $x - 1$: $x + 1 = 1$.
5. Put $x = 1$: $2 = 1$.

The bad step is step 4, because $x - 1 = 0$ and nobody may divide by $0$.
The correct move reads step 3 as $(x - 1)\big((x + 1) - 1\big) = 0$, so $x - 1 = 0$ or $x + 1 = 1$, and the first case is true and tells us nothing new.

In general, a mathematical fallacy is an argument in the form of a [[mathematical proof|0B94TKFQJX]] in which at least one step is invalid, and the invalid step looks like a correct rule.
The conclusion can be false, as in $2 = 1$, or it can be true.
A fallacy with a true conclusion is a howler: a wrong method that gives the right answer by luck.

## Motivation

Every rule of algebra and analysis comes with conditions.
You may cancel a factor only when it is not zero, split a square root of a product only when both factors are non-negative, and reorder a series only when it converges absolutely.
In daily work these conditions hold so often that we stop seeing them.
A fallacy is a short argument in which one condition fails at exactly one step.
When the conclusion is absurd, you know that some step is wrong, and the hunt for that step trains the habit of checking each condition.

The same habit protects real proofs.
A research argument rarely ends in $1 = 2$, so its errors are harder to see, and the [[famous incorrect proofs|1CV4HTA6C8]] show how long a bad step can survive.
Logical errors have their own pages: [[circular reasoning|JPHE53PABT]], [[affirming the consequent|J7KFCFQRBT]], [[proof by example|ZX6ERT3SW7]] and the [[quantifier shift fallacy|CRW82NARQV]].

## Notation

Books use several words for the same idea: fallacy, false proof, invalid proof and bogus proof.
Some authors keep the word "fallacy" for an error that the author hides on purpose, as in a puzzle.
"Howler" is the word of E. A. Maxwell for a wrong argument with a right result.
A paradox is a different thing: an argument that seems valid, from premises that seem true, to a conclusion that seems false.
Some paradoxes contain a fallacy, and others show that a premise was false after all.

## Remarks

### A gallery of hidden conditions

Most classical fallacies break one rule at one place, and the rule is always one with a condition that is easy to forget.
The [[division by zero fallacies|V7601AG5G3]] cancel a factor $a - b$ that equals $0$, so they use "$xc = yc$ gives $x = y$" without $c \neq 0$.
The [[fallacies with roots and powers|75ZEQ21AG2]] use $\sqrt{ab} = \sqrt{a}\sqrt{b}$ with $a = b = -1$, although the rule needs $a, b \ge 0$.
The [[fallacies with infinite series and integrals|KDXKVT5K1E]] compute with the divergent series $1 - 1 + 1 - \cdots$ as if it were a number, or cancel two indefinite integrals that differ by a constant.
The [[geometric fallacies|5CJ4KD4D96]] read from a wrong figure that a point lies inside a triangle.
The [[proof that all horses are the same color|AJ2FDJJGTH]] is an induction whose step fails in the passage from $1$ to $2$.
The [[non-reversible steps in solving equations|641ZP4RA5S]] add false solutions, because squaring both sides is not an equivalence.

### A howler: the right answer by a wrong rule

A student simplifies $\frac{16}{64}$ by crossing out the two digits $6$ and gets $\frac{1}{4}$.
The answer is right, since $16 \cdot 4 = 64$.
The method is wrong, because a digit is not a factor: the same move turns $\frac{12}{24}$ into $\frac{1}{4}$, while $\frac{12}{24} = \frac{1}{2}$.
The [[anomalous cancellation of digits|AAS5V2CKBG]] finds all the two-digit fractions where the trick happens to work.
So a true conclusion never shows that an argument is valid.

### What a fallacy is not

The proof that [[$0.999\ldots = 1$|AY76QGXZZ2]] surprises many readers, but each of its steps is valid.
A surprising result is not a fallacy.
A false [[conjecture|WMEMMHZ3BH]] stated without an argument is not a fallacy either, because a fallacy is a property of an argument, not of a statement.
A copying error such as $7 \cdot 8 = 54$ is a slip: it is an error, but it does not apply a wrong rule that looks right.

### Why one bad step is enough

If every step of an argument is valid and the premises are true, then the conclusion is true.
So an argument from true premises to a false conclusion must contain an invalid step, even when you cannot yet see it.
One false equation also gives every other false equation.
From $2 = 1$ subtract $1$ to get $1 = 0$, then multiply by any number $c$:
$$c = 0 \quad \text{for every } c.$$
This is why a single fallacy in a long computation can make the result say anything.

### Watch out

The bad step is often a dull one early in the argument, not the line that looks strange.
In the false proof of the Summary, steps 1 to 3 are correct and step 4 looks like routine cancelling.
To find the error, name the exact rule that each step uses, write its conditions, and check them for the numbers in front of you.
"It feels wrong" is not a diagnosis; "step 4 divides by $x - 1$, which is $0$" is.

### History

The ancient book *Pseudaria*, a collection of false proofs in geometry, is attributed to Euclid, and it is lost.
The false proof that every triangle is isosceles was known to Lewis Carroll, and it was published in 1899.
E. A. Maxwell collected many fallacies in his book *Fallacies in Mathematics* (1959), where he used the word "howler" for a wrong method with a right answer.

### Try it

Find the bad step: "$(-2)^2 = 2^2$, so $-2 = 2$."
The step uses "$x^2 = y^2$ gives $x = y$", which is false; the correct rule gives $x = y$ or $x = -y$, and here $x = -y$.

Find the bad step: "$\frac{1}{2} + \frac{1}{3} = \frac{1 + 1}{2 + 3} = \frac{2}{5}$."
The rule "add the tops and add the bottoms" is false; the correct sum is $\frac{3}{6} + \frac{2}{6} = \frac{5}{6}$, and $\frac{2}{5}$ is even smaller than $\frac{1}{2}$ alone.

## Explanations

### L1 human

A fallacy is a trick argument that seems to prove something impossible, such as $2 = 1$.
Each line looks fine, so the trick hides in one line.
Often that line divides both sides by a number that is secretly $0$.
For example, $2 \times 0 = 1 \times 0$ is true, because both sides are $0$.
If you "cancel the $0$", you get $2 = 1$, which is false.
Finding the bad line is a good game, because it shows you which rules have small print.

### L2 human

Here is a howler to examine: a student writes
$$\log(1 + 2 + 3) = \log 1 + \log 2 + \log 3.$$
Both sides are equal, since the left side is $\log 6$ and the right side is $\log(1 \cdot 2 \cdot 3) = \log 6$.
The rule behind the step, $\log(a + b + c) = \log a + \log b + \log c$, is false: with $a = b = c = 1$ it would give $\log 3 = 0$.
The step worked only because $1 + 2 + 3 = 1 \cdot 2 \cdot 3$.

How rare is this luck?
Suppose that positive integers $a \le b \le c$ satisfy $a + b + c = abc$.
Then $abc \le 3c$, so $ab \le 3$, and the only cases are $(a, b) = (1, 1), (1, 2), (1, 3)$.
The first gives $2 + c = c$, which is impossible.
The second gives $3 + c = 2c$, so $c = 3$.
The third gives $4 + c = 3c$, so $c = 2$, which is smaller than $b = 3$ and breaks the order.
So $\{1, 2, 3\}$ is the only triple where the wrong rule gives the right answer.
The problem shows the typical use of a howler: a correct answer is a reason to check the method, not a proof that the method is right.

### L3 human

In logic, a fallacy is an argument in which some inference is not an instance of a valid rule of the system in use.
In algebra and analysis the invalid inferences usually drop a side condition: a nonzero divisor, a non-negative radicand, a branch of a multivalued function, or absolute convergence.
Each condition marks a place where a structure lacks a property.
The field $\mathbb{R}$ has no inverse of $0$, no square root on $\mathbb{C}$ is multiplicative, and conditionally convergent series are not commutative.
Proof assistants reject all such steps, because a rule is applied only after its conditions are proved.
The larger errors of research work, such as a lemma used outside its range, appear in [[famous incorrect proofs|1CV4HTA6C8]], and the informal names for gaps hidden by words appear in [[proof by intimidation and handwaving|D8A1K052XV]].
