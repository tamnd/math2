---
tag: KCK4AQ469Q
kind: concept
name: Stronger and weaker statements
aliases: [stronger-statement, weaker-statement, strengthening, weakening]
msc: ["00A35"]
topics: [Z2WNQ1DNTX]
audience: ug1
uses: [0NMG7W7Q11, 0JMR2HM2N2, 09A3N7ZN5G, 09BJQQB3VS, 0BJR9QR08E]
sources:
  - url: https://en.wikipedia.org/wiki/Glossary_of_mathematical_jargon
    locator: Descriptive informalities
  - url: https://en.wikipedia.org/wiki/Inventor%27s_paradox
    locator: History
  - book: isbn:9780691164076
---

## Summary

"Euler's theorem is stronger than Fermat's little theorem" means that Fermat's theorem follows from Euler's, and not the other way around.
A stronger statement says more, so it rules out more possibilities, and everything a weaker statement says can be read off from it.

Let $A$ and $B$ be statements.
$A$ is *stronger* than $B$, and $B$ is *weaker* than $A$, when $A$ [[implies|0NMG7W7Q11]] $B$.
$A$ is *strictly stronger* than $B$ when $A$ implies $B$ but $B$ does not imply $A$.
When each implies the other, they are [[logically equivalent|0JMR2HM2N2]].
When neither implies the other, they are *incomparable*.
For a theorem "if $H$, then $C$", a weaker hypothesis $H$ or a stronger conclusion $C$ gives a stronger theorem.
For properties of objects, a stronger property defines a smaller class.

## Motivation

A theorem with a stronger conclusion tells you more, and a theorem with a weaker hypothesis applies to more objects.
So mathematicians compare results by strength, and much of research consists of strengthening known results.
Fermat's little theorem is about a prime modulus, and Euler's theorem gives the same kind of statement for every modulus.
Euler's theorem is stronger, because Fermat's theorem is its [[special case|FWG3D8760C]] for a prime modulus.

Strength is also a tool inside proofs.
To prove $B$, it is enough to prove a stronger statement $A$, and sometimes the stronger statement is easier to prove.
To disprove $A$, it is enough to disprove a weaker consequence $B$.
The words return in [[sharp and best possible results|KWQV0G0VJ3]], where a sharp bound is the strongest bound of its form.

## Notation

There is no special symbol: "$A$ is stronger than $B$" is written $A \Rightarrow B$.
"$A$ strengthens $B$", "$A$ is a strengthening of $B$", "$A$ refines $B$" and "$A$ improves $B$" mean the same.
"$B$ weakens $A$", "$B$ is a weakening of $A$" and "$B$ is a consequence of $A$" describe the other direction.
In "$A$ is a [[necessary condition|09BJQQB3VS]] for $B$", the condition $A$ is the weaker statement, and in "$A$ is a sufficient condition for $B$", it is the stronger one.

Many technical terms contain "strong" or "weak": strong induction, the strong law of large numbers, weak convergence, strongly regular graphs.
In these terms the word is part of a fixed name, and it need not mean "implies".
The page of each term gives its exact meaning.

## Remarks

### Reading a comparison

Take $x$ a real number and compare "$x > 2$" with "$x^2 > 4$".
If $x > 2$, then
$$x^2 = x \cdot x > 2x > 4,$$
so the first statement implies the second.
The number $x = -3$ has $x^2 = 9 > 4$ but not $x > 2$, so the converse fails.
So "$x > 2$" is strictly stronger.
The method is always the same: a proof in one direction and a counterexample in the other.

The same holds for properties of functions.
"$f$ is [[differentiable|0K57YG3BB8]] at $a$" is strictly stronger than "$f$ is [[continuous|0X3WGX95FE]] at $a$".
Every function differentiable at $a$ is continuous there, and the [[absolute value|0FFXKTKKQC]] $|x|$ is continuous at $0$ but not differentiable there.
So the [[converse|09A3N7ZN5G]] fails.

### Comparing named theorems

[[The strong Goldbach conjecture implies the weak one|R42W0Q4S4B]].
If every even integer greater than $2$ is a sum of two primes, then every odd $n > 5$ is a sum of three: write $n - 3$ as a sum of two primes and add $3$.
For example, $15 - 3 = 12 = 5 + 7$, so $15 = 3 + 5 + 7$.

[[Euler's theorem is stronger than Fermat's little theorem|9XRWP7QCP8]].
For a prime $p$ we have $\varphi(p) = p - 1$, so Euler's $a^{\varphi(n)} \equiv 1 \pmod{n}$ becomes Fermat's $a^{p-1} \equiv 1 \pmod{p}$.
Lagrange's theorem on groups is stronger still, since it gives Euler's theorem when applied to the group of units modulo $n$.

### Incomparable statements

Two statements can fail to compare.
[[Divisibility by 4 and by 6 are incomparable|DZSC3MRGFF]]: $4$ is divisible by $4$ but not by $6$, and $6$ is divisible by $6$ but not by $4$.
In the same way, for an integer $n$, "$n$ is prime" and "$n$ is odd" are incomparable, because $2$ is prime and even and $9$ is odd and not prime.
Strength is a partial comparison, not a ranking of every pair.

### The rules you can use

Implications chain, so "stronger than" is transitive.
"$A$ and $B$" is stronger than $A$, and $A$ is stronger than "$A$ or $B$".

For theorems, let $T$ be "$H \Rightarrow C$" and $T'$ be "$H' \Rightarrow C'$", with $H \Rightarrow H'$ and $C' \Rightarrow C$.
Then $T'$ implies $T$: from $H$ we get $H'$, then $C'$ by $T'$, then $C$.
So weakening the hypothesis and strengthening the conclusion both strengthen a theorem.

For quantifiers, let $S \subseteq S'$.
"$P(x)$ for all $x \in S'$" is stronger than "$P(x)$ for all $x \in S$", and "$P(x)$ for some $x \in S$" is stronger than "$P(x)$ for some $x \in S'$".
"There is $y$ with $P(x, y)$ for all $x$" is stronger than "for every $x$ there is $y$ with $P(x, y)$", and the [[order of quantifiers|0FYQMKFE77]] shows that the converse fails.

Negation reverses strength: if $A$ is stronger than $B$, then "not $B$" is stronger than "not $A$", by the [[contrapositive|04T1CT7212]].
For properties, $A$ is stronger than $B$ exactly when the class of objects with $A$ is a [[subset|0BJR9QR08E]] of the class with $B$.

### Two readings of "stronger" for theorems

For statements that might be false, "stronger" has its exact meaning: $A \Rightarrow B$.
For two proved theorems this meaning is empty.
Every true statement is implied by every statement, so two theorems formally imply each other.
Between theorems, authors mean an informal relation: the weaker one follows from the stronger by a short argument, and not conversely.
To tell which reading is meant, ask whether both statements are known to be true; if they are, the comparison is about how directly one gives the other.

### Watch out

The first trap is the direction.
"$A$ is stronger than $B$" means $A \Rightarrow B$, so a theorem with a stronger hypothesis is a weaker theorem.

The second trap is a name.
"Strong induction" is not stronger than ordinary induction as a principle: each one proves the other, so they are equivalent.
The word "strong" names the larger induction hypothesis, not a stronger theorem.

The third trap is to think that a stronger statement is always harder to prove.
In an induction, a stronger statement gives a stronger induction hypothesis, and this can make the step work, as the L2 explanation shows.

### History

Christian Goldbach stated his conjecture in a letter to Leonhard Euler in 1742.
Harald Helfgott announced a proof of the weak form in 2013, and the strong form is still open.
George Pólya, in "How to Solve It", described the inventor's paradox: the more ambitious plan may have more chance of success.

### Try it

First, which is stronger: "$n$ is divisible by $6$" or "$n$ is even"?
Divisibility by $6$ is strictly stronger: $6k = 2 \cdot 3k$ is even, and $2$ is even but not divisible by $6$.

Second, a theorem says "every continuous function on $[0, 1]$ is bounded".
Is "every differentiable function on $[0, 1]$ is bounded" stronger or weaker?
It is weaker, because its hypothesis is stronger and its conclusion is the same.

## Explanations

### L1 human

A stronger statement says more.
"I live in Paris" is stronger than "I live in France": if the first is true, then the second is true, but not the other way round.
In mathematics, "$x > 2$" is stronger than "$x^2 > 4$", because $x = -3$ makes the second true and the first false.
A stronger theorem is better: it needs less to start with, or it tells you more at the end.

### L2 human

Here is the classic case where the stronger statement is easier to prove: show $\sum_{k=1}^{n} 1/k^2 < 2$ for all $n \ge 1$.
Write $S_n = \sum_{k=1}^{n} 1/k^2$.
A direct [[induction|0ASJVEFA9J]] fails, because from $S_n < 2$ we only get
$$S_{n+1} = S_n + \frac{1}{(n+1)^2} < 2 + \frac{1}{(n+1)^2},$$
and that bound is above $2$.
So strengthen the claim to $S_n \le 2 - 1/n$.
For $n = 1$, $S_1 = 1 = 2 - 1$.
For the step, use $(n+1)^2 > n(n+1)$:
$$\frac{1}{(n+1)^2} < \frac{1}{n(n+1)} = \frac{1}{n} - \frac{1}{n+1}.$$
Then
$$S_{n+1} < \left( 2 - \frac{1}{n} \right) + \left( \frac{1}{n} - \frac{1}{n+1} \right) = 2 - \frac{1}{n+1}.$$
By induction $S_n \le 2 - 1/n < 2$ for every $n \ge 1$.
Check: $S_2 = 1.25 \le 1.5$ and $S_3 = 1.36\ldots \le 1.66\ldots$.

The stronger claim carries more information through the step, and that is why it works.
Pólya calls this effect the inventor's paradox.
Watch out: the strengthened statement must still be true, so test small cases before you try to prove it.

### L3 human

Implication is a preorder on statements: it is reflexive and transitive.
If we identify logically equivalent statements, it becomes a partial order, and for propositional logic the result is the [[Lindenbaum-Tarski algebra|QC9M3Q8B8Q]], a Boolean algebra.
In it, conjunction is the greatest lower bound and disjunction is the least upper bound.
For properties of the elements of a set $X$, the order corresponds to inclusion of subsets of $X$, so a stronger property has a smaller extension.

For proved theorems the order collapses, as the reading above explains.
[[Reverse mathematics|7SQS69T17R]] gives an exact substitute: over a weak base theory, it compares theorems by the axioms needed to prove them.
The other informal words of mathematics are in [[mathematical jargon|4M1FGQ0HNZ]].
