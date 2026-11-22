---
tag: 43EPSN2NG1
kind: example
name: Bijection between the subsets of even size and of odd size
msc: ["00A35", "05A19"]
topics: [GB14W4SYPK]
audience: ug1
instance_of: [SS07J9ZAQ7]
uses: [SS07J9ZAQ7, 0SNQEF7Z53, 0PQQGFAWSH]
sources:
  - url: https://en.wikipedia.org/wiki/Bijective_proof
    locator: lead section
---

## Example

Let $n \geq 1$.
We prove by a [[bijective proof|SS07J9ZAQ7]] that $[n] = \{1, \dots, n\}$ has as many subsets of even size as subsets of odd size.

1. Let $E$ be the set of subsets of $[n]$ with an even number of elements, and let $O$ be the set of those with an odd number.
2. Define $f(A) = A \setminus \{1\}$ if $1 \in A$, and $f(A) = A \cup \{1\}$ if $1 \notin A$.
   So $f$ removes $1$ if it is there and adds it if it is not, and this uses $n \geq 1$, so that $1 \in [n]$.
3. The map $f$ changes the size of $A$ by exactly $1$, so it sends $E$ into $O$ and $O$ into $E$.
4. Applying $f$ twice gives back $A$, since $1$ is added and then removed, or removed and then added, so $f \circ f$ is the identity.
5. So $f$ restricted to $E$ is a [[bijection|0SNQEF7Z53]] from $E$ to $O$, with inverse $f$ restricted to $O$.
6. Hence $|E| = |O|$, and since $|E| + |O| = 2^n$, each of them equals $2^{n-1}$.
7. Check with $n = 3$: $E = \{\varnothing, \{1,2\}, \{1,3\}, \{2,3\}\}$, and $f$ sends these to $\{1\}$, $\{2\}$, $\{3\}$ and $\{1,2,3\}$, which are exactly the elements of $O$.

## Remarks

The example is a bijective proof of the [[alternating sum of binomial coefficients|0PQQGFAWSH]],
$$\sum_{k=0}^{n} (-1)^k \binom{n}{k} = 0 \qquad (n \geq 1).$$
The positive terms count $E$, the negative terms count $O$, and the bijection matches them.
The algebraic proof puts $x = -1$ and $y = 1$ in the binomial theorem, and it gives the sum but no matching of subsets.

The condition $n \geq 1$ is needed.
For $n = 0$ the only subset is $\varnothing$, so $|E| = 1$ and $|O| = 0$, and the alternating sum is $1$.
The map $f$ is an involution that changes the sign $(-1)^{|A|}$, and this pattern of a sign-reversing involution proves many identities with alternating signs.

## Explanations

### L1 human

Take a set of $n$ things, with $n$ at least $1$, and pick out one thing, called $1$.
For each group of things with an even count, either add $1$ to it or take $1$ out of it.
The count then becomes odd, and doing the same again brings back the first group.
So the even groups and the odd groups pair off exactly, and there are as many of each.

### L2 human

Here is the bijection for $n = 2$, and the alternating sum it gives.
The subsets of $[2]$ of even size are $\varnothing$ and $\{1,2\}$.
The map sends $\varnothing$ to $\{1\}$ and $\{1,2\}$ to $\{2\}$.
The subsets of odd size are exactly $\{1\}$ and $\{2\}$, so the map hits each odd subset once, and $|E| = |O| = 2$.
The alternating sum agrees:
$$\binom{2}{0} - \binom{2}{1} + \binom{2}{2} = 1 - 2 + 1 = 0.$$
The typical use is an alternating sum: find a map that pairs each object of sign $+$ with one of sign $-$.
Watch out for a map that does not apply to every subset, such as "remove the element $1$", which is not defined on the subsets that do not contain $1$.
