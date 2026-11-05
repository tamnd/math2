---
tag: 9CN2PJWMPW
kind: statement
role: proposition
name: Menon's identity
msc: [11A25]
sources:
  - wikipedia: en:3170@r1363074436
    locator: Arithmetic function, section Relations among the functions > Menon's identity
    note: adopted
    mention: wikipedia://en/3170#3CO8
    sections: [Statement]
inventory: [25BM4KP0BF]
---

## Statement

In 1965 P Kesava Menon proved

$$\sum_{\stackrel{1\le k\le n}{ \gcd(k,n)=1}} \gcd(k-1,n)=\varphi(n)d(n).$$

This has been generalized by a number of mathematicians. For example,

- B. Sury $$\sum_{\stackrel{1\le k_1, k_2, \dots, k_s\le n}{ \gcd(k_1,n)=1}} \gcd(k_1-1,k_2,\dots,k_s,n) = \varphi(n)\sigma_{s-1}(n).$$
- N. Rao $$\sum_{\stackrel{1\le k_1, k_2, \dots, k_s\le n}{ \gcd(k_1,k_2,\dots,k_s,n)=1}} \gcd(k_1-a_1,k_2-a_2,\dots,k_s-a_s,n)^s =J_s(n)d(n),$$ where *a*<sub>1</sub>, *a*<sub>2</sub>, ..., *a*<sub>*s*</sub> are integers, gcd(*a*<sub>1</sub>, *a*<sub>2</sub>, ..., *a*<sub>*s*</sub>, *n*) = 1.
- László Fejes Tóth $$\sum_{\stackrel{1\le k\le m}{ \gcd(k,m)=1}} \gcd(k^2-1,m_1)\gcd(k^2-1,m_2) =\varphi(n)\sum_{\stackrel{d_1\mid m_1} {d_2\mid m_2}} \varphi(\gcd(d_1, d_2))2^{\omega(\operatorname{lcm}(d_1, d_2))},$$ where *m*<sub>1</sub> and *m*<sub>2</sub> are odd, *m* = lcm(*m*<sub>1</sub>, *m*<sub>2</sub>).

In fact, if *f* is any arithmetical function

$$\sum_{\stackrel{1\le k\le n}{ \gcd(k,n)=1}} f(\gcd(k-1,n)) =\varphi(n)\sum_{d\mid n}\frac{(\mu*f)(d)}{\varphi(d)},$$

where $*$ stands for Dirichlet convolution.
