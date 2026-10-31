---
records:
    - id: DGBGBY4FKY
      kind: monograph
      title: Algebra
      creators:
        - name: L. E. Sigler
          role: author
      date: "1976"
      expressions:
        - key: e1
          kind: edition
          date: "1976"
          ids:
            doi:
                - 10.1007/978-1-4613-9410-5
                - 10.1007/978-3-662-26738-7
          manifestations:
            - key: m1
              kind: print
              publisher: Springer New York
              date: "1976"
              ids:
                isbn:
                    - "9781461394129"
                    - "9781461394105"
            - key: m2
              kind: print
              publisher: Springer Berlin Heidelberg
              date: "1976"
              ids:
                isbn:
                    - "9783540901952"
                    - "9783662267387"
      relations:
        - kind: part_of
          to: NWQC4TW7S9
          source: cluster/1
      scope:
        value: in
        rule: S4
        by: m2 v0.6.4 scope/1
      catalogue:
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-1-4613-9410-5
          level: work
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-3-662-26738-7
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
