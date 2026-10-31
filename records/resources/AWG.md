---
records:
    - id: AWGYH23JVX
      kind: monograph
      title: A Course in Modern Geometries
      creators:
        - name: Judith N. Cederberg
          role: author
      date: "1989"
      expressions:
        - key: e1
          kind: edition
          date: "1989"
          ids:
            doi:
                - 10.1007/978-1-4757-3490-4
                - 10.1007/978-1-4757-3831-5
          manifestations:
            - key: m1
              kind: print
              publisher: Springer New York
              date: "2001"
              ids:
                isbn:
                    - "9781441931931"
                    - "9781475734904"
            - key: m2
              kind: print
              publisher: Springer New York
              date: "1989"
              ids:
                isbn:
                    - "9781475738339"
                    - "9781475738315"
      relations:
        - kind: part_of
          to: NWQC4TW7S9
          source: cluster/1
      scope:
        value: in
        rule: S4
        by: m2 v0.6.2 scope/1
      catalogue:
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-1-4757-3490-4
          level: work
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-1-4757-3831-5
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
