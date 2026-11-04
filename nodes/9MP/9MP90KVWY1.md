---
tag: 9MP90KVWY1
kind: proof
name: Proof that the Galois group of a finite Galois extension has order equal to the degree
msc: [12F10]
proves: 0BDJBH8B4Z
uses: [0DS2F7GK05, 0CBRFQ7DVZ, 0N019F6RE9, 03J8BS7FMV, 0GK1WB9R98, 0NFEG48RDR, 06K7SARZKR, 0N5QW9K7MH, 03XVP8Q4GY, 067F8YVYMH, 0KJVQV3E0F, 0ZN39QDTP9, 0GGE0Z0JQ1, 09N7DZ7SDB, 0MA5B744K3, 0A7KJ68XHT, 0912EEEVCT, 0XVR72M51M]
sources:
  - url: https://www.jmilne.org/math/CourseNotes/FT.pdf
---

## Proof

We count the homomorphisms $L \to L$ that fix $K$, adjoining one generator at a time. Homomorphisms are [[ring homomorphisms|0GGE0Z0JQ1]] that send $1$ to $1$.

1. Let $L/K$ be a finite [[Galois extension|0DS2F7GK05]], so $L/K$ is [[normal|0CBRFQ7DVZ]] and [[separable|0N019F6RE9]]. Let $n = [L : K]$.

Lemma. Let $K \subseteq E \subseteq L$ be a field, let $a \in L$ and $E' = E(a)$. Let $\rho \colon E \to L$ be a homomorphism with $\rho(c) = c$ for $c \in K$. Then exactly $[E' : E]$ homomorphisms $\tau \colon E' \to L$ restrict to $\rho$ on $E$.

2. Let $f$ be the [[minimal polynomial|0GK1WB9R98]] of $a$ over $K$, of degree $N$. Let $m$ be the minimal polynomial of $a$ over $E$, of degree $d$. Then $d = [E' : E]$ by the [[degree of a simple extension|0N5QW9K7MH]].
3. Since $f \in E[x]$ and $f(a) = 0$, the polynomial $m$ [[divides|06K7SARZKR]] $f$. Write $f = m h$ with $h \in E[x]$ of degree $N - d$.
4. The polynomial $f$ is [[irreducible|0NFEG48RDR]] over $K$ and has the root $a$ in $L$. As $L/K$ is normal, $f = (x - b_1) \cdots (x - b_N)$ with $b_1, \dots, b_N \in L$.
5. As $a$ is separable over $K$, $f$ is a [[separable polynomial|03J8BS7FMV]]: $u f + v f' = 1$ for some $u, v \in K[x]$.
6. Suppose $b_i = b_j = b$ for some $i \neq j$. Then $(x - b)^2$ divides $f$, so $b$ has [[multiplicity|03XVP8Q4GY]] at least $2$. So [[$f(b) = f'(b) = 0$|067F8YVYMH]], and evaluating step 5 at $b$ gives $1 = 0$. So $b_1, \dots, b_N$ are distinct.
7. For $g \in E[x]$, let $g^\rho \in L[x]$ be obtained by applying $\rho$ to the coefficients. The map $g \mapsto g^\rho$ respects sums and products. Since $\rho$ is [[injective|09N7DZ7SDB]], it preserves degrees.
8. Since $\rho$ fixes the coefficients of $f$, step 3 gives $f = m^\rho h^\rho$ in $L[x]$, with $\deg m^\rho = d$ and $\deg h^\rho = N - d$.
9. Each $b_i$ is a root of $m^\rho$ or of $h^\rho$, since $L$ is a field. The polynomial $h^\rho$ has [[at most $N - d$ roots|0KJVQV3E0F]] in $L$.
10. So at least $d$ of the distinct $b_i$ are roots of $m^\rho$. As $m^\rho$ has at most $d$ roots, it has exactly $d$ roots in $L$.
11. Let $\tau$ extend $\rho$. Applying $\tau$ to $m(a) = 0$ gives $m^\rho(\tau(a)) = 0$. So $\tau(a)$ is one of the $d$ roots of $m^\rho$.
12. By the [[structure of simple extensions|0ZN39QDTP9]], every element of $E'$ is $g(a)$ for some $g \in E[x]$. Then $\tau(g(a)) = g^\rho(\tau(a))$, so $\tau$ is determined by $\tau(a)$.
13. Let $b$ be a root of $m^\rho$ in $L$. Define $\tau(g(a)) = g^\rho(b)$ for $g \in E[x]$. If $g(a) = g_1(a)$, then $m$ divides $g - g_1$, so $m^\rho$ divides $g^\rho - g_1^\rho$, and $g^\rho(b) = g_1^\rho(b)$.
14. So $\tau$ is well defined. It respects sums and products by step 7, it extends $\rho$, and $\tau(a) = b$.
15. By steps 10 to 14, the extensions $\tau$ correspond to the $d$ roots of $m^\rho$. So there are exactly $d = [E' : E]$ of them. This proves the lemma.

Now we count.

16. Let $a_1, \dots, a_s$ be a basis of $L$ over $K$. Then [[$L = K(a_1, \dots, a_s)$|0MA5B744K3]]. Let $E_0 = K$ and $E_j = E_{j-1}(a_j)$, so $E_j = K(a_1, \dots, a_j)$ and $E_s = L$.
17. Claim: exactly $[E_j : K]$ homomorphisms $E_j \to L$ fix $K$. For $j = 0$, the only one is the inclusion of $K$.
18. Let $j \ge 1$. Each such homomorphism on $E_j$ restricts to one on $E_{j-1}$. By the claim for $j - 1$ there are $[E_{j-1} : K]$ restrictions, and each has exactly $[E_j : E_{j-1}]$ extensions by the lemma.
19. So there are $[E_j : E_{j-1}] \cdot [E_{j-1} : K] = [E_j : K]$ of them, by the [[tower law|0A7KJ68XHT]]. With $j = s$, exactly $n$ homomorphisms $\sigma \colon L \to L$ fix $K$.
20. Each such $\sigma$ is injective, and it is $K$-linear because $\sigma(c y) = c \sigma(y)$ for $c \in K$. As $L$ has finite dimension $n$ over $K$, $\sigma$ is [[surjective|0912EEEVCT]].
21. So these $n$ maps are exactly the automorphisms of $L$ that fix $K$, that is, the elements of the [[Galois group|0XVR72M51M]]. Hence $\abs{\operatorname{Gal}(L/K)} = [L : K]$.

## Idea

An automorphism is built by choosing the image of one generator at a time. At each stage the image must be a root of a minimal polynomial. Normality puts all these roots in $L$, and separability makes them distinct, so the number of choices is exactly the degree of that stage. The tower law multiplies these counts into $[L : K]$.
