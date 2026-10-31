---
records:
    - id: EZ1M0BEEJN
      kind: monograph
      title: Modular Functions and Dirichlet Series in Number Theory
      creators:
        - name: Tom M. Apostol
          role: author
      date: "1976"
      expressions:
        - key: e1
          kind: edition
          date: "1976"
          ids:
            doi:
                - 10.1007/978-1-4612-0999-7
                - 10.1007/978-1-4684-9910-0
          manifestations:
            - key: m1
              kind: print
              publisher: Springer New York
              date: "1990"
              ids:
                isbn:
                    - "9781461269786"
                    - "9781461209997"
            - key: m2
              kind: print
              publisher: Springer New York
              date: "1976"
              ids:
                isbn:
                    - "9781468499124"
                    - "9781468499100"
      relations:
        - kind: part_of
          to: 7ME1ABA6H5
          source: cluster/1
      scope:
        value: in
        rule: S4
        by: m2 v0.6.7 scope/1
      catalogue:
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-1-4612-0999-7
          level: work
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-1-4684-9910-0
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
