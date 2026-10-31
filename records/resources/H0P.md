---
records:
    - id: H0P70MGPF0
      kind: monograph
      title: A First Course in Discrete Dynamical Systems
      creators:
        - name: Richard A. Holmgren
          role: author
      date: "1994"
      expressions:
        - key: e1
          kind: edition
          date: "1994"
          ids:
            doi:
                - 10.1007/978-1-4419-8732-7
                - 10.1007/978-1-4684-0222-3
          manifestations:
            - key: m1
              kind: print
              publisher: Springer New York
              date: "1996"
              ids:
                isbn:
                    - "9780387947808"
                    - "9781441987327"
            - key: m2
              kind: print
              publisher: Springer US
              date: "1994"
              ids:
                isbn:
                    - "9780387942087"
                    - "9781468402223"
      relations:
        - kind: part_of
          to: W0CC03QJC7
          source: cluster/1
      scope:
        value: in
        rule: S4
        by: m2 v0.6.7 scope/1
      catalogue:
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-1-4419-8732-7
          level: work
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-1-4684-0222-3
          level: work
      history:
        - op: add
          at: "2026-10-31"
          by: m2 v0.6.2 cluster/1
        - op: scope
          at: "2026-10-31"
          by: m2 v0.6.2 scope/1
          note: to in
---
