---
tag: TCZFSKFQ94
kind: proof
name: Proof of the existence of a vector whose annihilator is the minimal polynomial
msc: ["15A21", "15A04"]
topics: [GEBYZKYV3D]
audience: ug2
proves: QPE5Y86Y8V
methods: [0NTF6DMVAP, 0J0XBKG64S, 0ASJVEFA9J]
uses: [5VYBJYPYMW, 03NDVCSHSB, 03FKX7Z5DC, 055HT85T3S, 0VY3WPP9Y3, 0CHS7RBD39, 0E3MV6E6MG]
sources:
  - url: https://en.wikipedia.org/wiki/Minimal_polynomial_(linear_algebra)
    locator: lead section
  - book: isbn:9780135367971
    locator: Section 7.1
---

## Proof

1. If $V = 0$, then $m_T = 1$ and $v = 0$ has $m_v = 1$. So let $V \ne 0$; then $\deg m_T \ge 1$.
2. Write $m_T = p_1^{e_1} \cdots p_s^{e_s}$ with distinct monic [[irreducible polynomials|03FKX7Z5DC]] $p_j$ and $e_j \ge 1$. This factorization exists because $F[x]$ is a [[Euclidean domain|0CHS7RBD39]] and hence a [[unique factorization domain|055HT85T3S]].
3. Fix $j$. Let $r_j = m_T / p_j^{e_j}$ and $q_j = p_j^{e_j - 1} r_j = m_T / p_j$.
4. The polynomial $q_j$ is monic of degree less than $\deg m_T$. By the [[definition of the minimal polynomial|03NDVCSHSB]], $q_j(T) \ne 0$. Choose $x_j \in V$ with $q_j(T) x_j \ne 0$.
5. Put $u_j = r_j(T) x_j$. Then $p_j^{e_j}(T) u_j = m_T(T) x_j = 0$, using that $(fg)(T) = f(T) g(T)$ for [[polynomials of an endomorphism|0E3MV6E6MG]].
6. By part 2 of the [[lemma on cyclic subspaces|5VYBJYPYMW]], $m_{u_j}$ divides $p_j^{e_j}$. By unique factorization, $m_{u_j} = p_j^{c}$ for some $0 \le c \le e_j$.
7. Assume $c \le e_j - 1$. Then $p_j^{e_j - 1}(T) u_j = 0$ by part 2 of the lemma, that is, $q_j(T) x_j = 0$. This contradicts step 4. So $m_{u_j} = p_j^{e_j}$.
8. Claim: if $m_u = a$ and $m_w = b$ with $\gcd(a, b) = 1$, then $m_{u + w} = ab$.
9. Proof of the claim. $(ab)(T)(u + w) = b(T) a(T) u + a(T) b(T) w = 0$, since polynomials in $T$ commute. So $g = m_{u+w}$ divides $ab$.
10. Apply $b(T)$ to $g(T)(u + w) = 0$. Since $b(T) w = 0$, we get $(gb)(T) u = 0$, so $a \mid gb$ by part 2 of the lemma.
11. By [[Bézout's identity|0VY3WPP9Y3]] in $F[x]$, $1 = sa + tb$ for some $s, t$. So $g = sag + tbg$ is divisible by $a$. In the same way, $b \mid g$.
12. Since $a \mid g$, write $g = a g'$. Then $b \mid a g'$, and $g' = s a g' + t b g'$ shows $b \mid g'$. So $ab \mid g$.
13. By steps 9 and 12, $g$ and $ab$ are monic and divide each other, so $g = ab$. This proves the claim.
14. The polynomials $p_1^{e_1}, \dots, p_s^{e_s}$ are pairwise coprime, since the $p_j$ are distinct monic irreducibles.
15. Let $v = u_1 + \cdots + u_s$. By induction on $s$, using the claim with $a = p_1^{e_1} \cdots p_{t}^{e_{t}}$ and $b = p_{t+1}^{e_{t+1}}$ at each step, $m_v = p_1^{e_1} \cdots p_s^{e_s} = m_T$.

## Idea

The proof works one prime power of $m_T$ at a time.
For each prime power $p^e$, a vector with annihilator exactly $p^e$ exists, since otherwise a proper divisor of $m_T$ would kill $V$.
Annihilators of coprime degrees multiply under addition of vectors, so the sum of these vectors has annihilator $m_T$.

## Variants

The lemma also follows from the [[cyclic decomposition theorem|R3Z20J19BR]]: the generator $v_r$ of the last summand has $m_{v_r} = d_r = m_T$.
Over an infinite field there is a short proof.
For each proper monic divisor $f$ of $m_T$, the kernel of $f(T)$ is a proper subspace, and there are finitely many such $f$.
A vector space over an infinite field is not a finite union of proper subspaces, so some $v$ lies in none of these kernels, and then $m_v = m_T$.
