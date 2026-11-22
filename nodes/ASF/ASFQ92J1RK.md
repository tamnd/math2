---
tag: ASFQ92J1RK
kind: example
name: Fermat's little theorem as a special case of Lagrange's theorem
msc: ["00A35", "20D60", "11A07"]
topics: [N4P3E53HM0]
audience: ug1
instance_of: [976RZZCT1H]
uses: [976RZZCT1H, 3C53TD, 0ZEPNS9BXK, 0M25PRN3WQ, 0R8YXRC9AJ, 0F8X8ZRQ53, 0WE2NHZJ7B]
sources:
  - url: https://en.wikipedia.org/wiki/Fermat%27s_little_theorem
    locator: Proofs
  - url: https://en.wikipedia.org/wiki/Lagrange%27s_theorem_(group_theory)
    locator: Applications
---

## Example

[[Fermat's little theorem|0M25PRN3WQ]] says that if $p$ is a prime and $p$ does not divide the integer $a$, then $a^{p - 1} \equiv 1 \pmod p$.
We derive it as a special case of a [[general fact about all finite groups|0ZEPNS9BXK]]: every element $g$ of a finite group $G$ satisfies $g^{|G|} = e$, a consequence of [[Lagrange's theorem|3C53TD]].

1. Let $G = (\mathbb{Z}/p\mathbb{Z})^\times = \{\overline{1}, \overline{2}, \ldots, \overline{p - 1}\}$, the nonzero residues modulo $p$ with multiplication.
2. The set $G$ is a group, the [[group of units|0F8X8ZRQ53]] of $\mathbb{Z}/p\mathbb{Z}$, because every nonzero residue has an inverse in the [[field $\mathbb{Z}/p\mathbb{Z}$|0R8YXRC9AJ]].
3. The group $G$ has $p - 1$ elements, so $|G| = p - 1$.
4. Since $p$ does not divide $a$, the residue $\overline{a}$ is not $\overline{0}$, so $\overline{a}$ lies in $G$.
5. The general fact gives $\overline{a}^{\,|G|} = \overline{1}$, that is, $\overline{a}^{\,p - 1} = \overline{1}$.
6. In the language of integers, this says $a^{p - 1} \equiv 1 \pmod p$.

We check the case $p = 7$ and $a = 3$ by multiplying by $3$ and reducing modulo $7$ at each step:
$$3^1 \equiv 3, \quad 3^2 = 9 \equiv 2, \quad 3^3 \equiv 6, \quad 3^4 \equiv 18 \equiv 4, \quad 3^5 \equiv 12 \equiv 5, \quad 3^6 \equiv 15 \equiv 1.$$
So $3^6 \equiv 1 \pmod 7$, as the theorem says.
Here the [[order|0WE2NHZJ7B]] of $\overline{3}$ is $6$, and $6$ divides $|G| = 6$, as Lagrange's theorem requires.

## Remarks

The example shows how a general theorem can make a special proof shorter.
A direct proof of Fermat's little theorem needs an argument special to residues, such as a count of necklaces or the binomial expansion of $(a + 1)^p$.
The group proof needs only two facts: the nonzero residues form a group with $p - 1$ elements, and in a finite group the power $|G|$ of every element is the identity.
The arithmetic of residues enters only in step 2.

The general setting also shows the next generalization.
Replace the prime $p$ by any integer $n \ge 2$, and $G$ by the group of residues coprime to $n$, which has $\varphi(n)$ elements.
The same steps then give Euler's theorem, $a^{\varphi(n)} \equiv 1 \pmod n$ whenever $a$ is coprime to $n$.
For $n = 8$ and $a = 3$, the residues coprime to $8$ are $1, 3, 5, 7$, so $\varphi(8) = 4$, and
$$3^4 = 81 = 10 \cdot 8 + 1 \equiv 1 \pmod 8.$$

## Explanations

### L1 human

Take the numbers $1$ to $6$ and multiply them as on a clock with $7$ hours.
Start with $3$ and keep multiplying by $3$: you get $3, 2, 6, 4, 5, 1$.
After six steps you are back at $1$.
Fermat noticed that this happens for every prime clock: $p - 1$ steps always bring you back to $1$.
Group theory explains it with one fact about all finite groups, so we do not have to check each prime.

### L2 human

We check the theorem for $p = 5$ and every $a$ from $1$ to $4$:
$$1^4 = 1, \qquad 2^4 = 16 = 3 \cdot 5 + 1, \qquad 3^4 = 81 = 16 \cdot 5 + 1, \qquad 4^4 = 256 = 51 \cdot 5 + 1.$$
Each power leaves remainder $1$ on division by $5$, as the theorem says.
The typical use is to reduce large powers, for example $2^{100} = (2^4)^{25} \equiv 1^{25} = 1 \pmod 5$.
Watch out for the hypothesis that $p$ does not divide $a$.
For $a = 5$ and $p = 5$ we get $5^4 \equiv 0 \pmod 5$, because $\overline{5} = \overline{0}$ is not in the group $G$.
